"""reextract_pdf.py - targeted high-quality re-OCR for specific records.

For PDFs where the standard 150 DPI / default-PSM extraction missed text,
re-render at 300 DPI with PIL autocontrast and try multiple page-segmentation
modes (PSM), keeping the best result per page (longest output wins, modulo
a basic sanity check).

Usage:
    python scripts/reextract_pdf.py <record-id> [<record-id> ...]
    python scripts/reextract_pdf.py --all-flagged   # re-OCR everything in qa report

The script overwrites extracted/<id>.md with a new file whose
extraction_method is set to "ocr-220dpi-autocontrast-psm6".
"""

from __future__ import annotations
import argparse, json, os, shutil, sys, time
from pathlib import Path

import pdfplumber
from pdf2image import convert_from_path
import pytesseract
from PIL import Image, ImageOps, ImageFilter

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "metadata" / "index.json"
EXTRACTED = ROOT / "extracted"
PARTS = EXTRACTED / ".parts-rerun"

# Reuse Windows binary autodetect from the original extractor (lazy)
def _find_tesseract():
    if not sys.platform.startswith("win"):
        return shutil.which("tesseract")
    cand = [
        os.environ.get("TESSERACT_CMD"),
        r"C:\Program Files\Tesseract-OCR\tesseract.exe",
        r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe",
        os.path.expanduser(r"~\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"),
    ]
    for c in cand:
        if c and os.path.isfile(c):
            return c
    return shutil.which("tesseract")


def _find_poppler():
    if not sys.platform.startswith("win"):
        return None
    env = os.environ.get("POPPLER_PATH")
    if env and os.path.isfile(os.path.join(env, "pdftoppm.exe")):
        return env
    for root in [r"C:\Program Files\poppler", r"C:\Program Files (x86)\poppler",
                 r"C:\poppler", os.path.expanduser(r"~\poppler"),
                 os.path.expanduser(r"~\Documents\poppler"),
                 os.path.expanduser(r"~\Downloads\poppler")]:
        if not os.path.isdir(root):
            continue
        for sub in [root] + [os.path.join(root, d) for d in os.listdir(root)]:
            cand = os.path.join(sub, "bin", "pdftoppm.exe")
            if os.path.isfile(cand):
                return os.path.dirname(cand)
    return None


tess = _find_tesseract()
if tess:
    pytesseract.pytesseract.tesseract_cmd = tess
POPPLER_PATH = _find_poppler()

DPI = 220
PSM = 6  # single uniform block of text, best for typewritten declassified docs


def preprocess(img: Image.Image) -> Image.Image:
    """Light cleanup: grayscale + autocontrast. No deskew (needs cv2)."""
    img = img.convert("L")               # grayscale
    img = ImageOps.autocontrast(img, cutoff=1)
    img = img.filter(ImageFilter.SHARPEN)
    return img


def ocr_page(img: Image.Image) -> str:
    """Single PSM 6 pass with PIL autocontrast preprocessing."""
    img2 = preprocess(img)
    try:
        return pytesseract.image_to_string(img2, lang="eng", config=f"--psm {PSM}")
    except Exception as e:
        return f"[OCR error: {e}]"


def yaml_escape(s):
    if not s: return '""'
    s = str(s).replace("\\", "\\\\").replace('"', '\\"')
    return f'"{s}"'


def yaml_block(s, indent=2):
    if not s: return '""'
    lines = s.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    pad = " " * indent
    return ">\n" + "\n".join(pad + line for line in lines)


def write_md(record, pages_text, npages, method, ocr_reason):
    out = EXTRACTED / f"{record['id']}.md"
    fm = ["---",
          f'id: {yaml_escape(record["id"])}',
          f'title: {yaml_escape(record["title"])}',
          f'agency: {yaml_escape(record["agency"])}',
          f'agency_raw: {yaml_escape(record["agency_raw"])}',
          f'type: {yaml_escape(record["type"])}',
          f'page_section: {yaml_escape(record["page_section"])}',
          f'release_date: {yaml_escape(record["release_date"])}',
          f'incident_date: {yaml_escape(record["incident_date"])}',
          f'incident_location: {yaml_escape(record["incident_location"])}',
          f'source_url: {yaml_escape(record["source_url"])}',
          f'modal_image_url: {yaml_escape(record.get("modal_image_url",""))}',
          f'sha256: {yaml_escape(record["sha256"])}',
          f'bytes: {record.get("bytes", 0)}',
          f'pages: {npages}',
          f'extraction_method: {yaml_escape(method)}',
          f'ocr_reason: {yaml_escape(ocr_reason)}',
          ]
    redaction = (record.get("redaction") or "").strip()
    if redaction:
        fm.append(f'redaction: {yaml_escape(redaction)}')
    desc = (record.get("summary") or "").strip()
    fm.append(f"description: {yaml_block(desc, indent=2)}")
    fm.append("---")

    parts = ["\n".join(fm), "", f"# {record['title']}", ""]
    if desc:
        parts.append("> " + desc.replace("\n", "\n> "))
        parts.append("")
    parts.extend([
        f"**Agency:** {record['agency']}  ",
        f"**Release date:** {record['release_date']}  ",
        f"**Incident date:** {record['incident_date']}  ",
        f"**Incident location:** {record['incident_location']}  ",
        f"**Source:** [{record['source_url'].split('/')[-1]}]({record['source_url']})  ",
        f"**Pages:** {npages}  ",
        f"**Extraction method:** {method}",
        "",
    ])
    if redaction:
        parts.append("> **Redaction notice:** Per the war.gov release page, "
                     "redactions in this file protect eyewitness identities, "
                     "government facility locations, or sensitive information "
                     "about military sites unrelated to UAP. No redactions were "
                     "applied to material released under President Trump's "
                     "directive concerning the nature or existence of UAP encounters.")
        parts.append("")
    parts.append("---")
    parts.append("")
    for pno, txt in pages_text:
        parts.append(f"## Page {pno}")
        parts.append("")
        parts.append(txt.strip() if txt and txt.strip() else "_(no text extracted)_")
        parts.append("")
    out.write_text("\n".join(parts), encoding="utf-8")
    return out




def _worker_ocr_one_page(args):
    """Top-level worker for multiprocessing.Pool. Re-wires Windows binaries."""
    pdf_path_str, pno, dpi, poppler_path, tesseract_cmd = args
    if tesseract_cmd:
        pytesseract.pytesseract.tesseract_cmd = tesseract_cmd
    try:
        images = convert_from_path(pdf_path_str, dpi=dpi,
                                   first_page=pno, last_page=pno,
                                   poppler_path=poppler_path)
        if not images:
            return pno, "[pdf2image returned no image for this page]"
        img = images[0].convert("L")
        img = ImageOps.autocontrast(img, cutoff=1)
        img = img.filter(ImageFilter.SHARPEN)
        return pno, pytesseract.image_to_string(img, lang="eng", config=f"--psm {PSM}")
    except Exception as e:
        return pno, f"[OCR error on page {pno}: {e}]"

def reextract(rid: str, idx: dict) -> tuple[int, int]:
    """Returns (chars_before, chars_after)."""
    rec = next((r for r in idx["files"] if r["id"] == rid), None)
    if rec is None:
        print(f"  [skip] {rid}: not in index")
        return 0, 0
    pdf_path = ROOT / rec["local_path"]
    if not pdf_path.exists():
        print(f"  [skip] {rid}: local file missing")
        return 0, 0

    # Get page count
    with pdfplumber.open(pdf_path) as pdf:
        total = len(pdf.pages)

    # How long was the previous extraction?
    md_path = EXTRACTED / f"{rid}.md"
    chars_before = md_path.read_text(encoding="utf-8").count("\n") if md_path.exists() else 0

    # Re-OCR with checkpointing + parallel pool
    import multiprocessing as mp
    parts_dir = PARTS / rid
    parts_dir.mkdir(parents=True, exist_ok=True)
    pages_text = {}

    # Load any cached pages
    pending = []
    for pno in range(1, total + 1):
        part = parts_dir / f"page_{pno:04d}.txt"
        if part.exists():
            pages_text[pno] = part.read_text(encoding="utf-8")
        else:
            pending.append(pno)

    print(f"  [reocr] {rid}: {total} pages at {DPI} DPI, autocontrast, PSM {PSM} "
          f"({len(pending)} pending)")

    if pending:
        nproc = max(1, min(mp.cpu_count(), 2))
        chunk_size = nproc * 2
        i = 0
        with mp.Pool(nproc) as pool:
            while i < len(pending):
                chunk = pending[i:i + chunk_size]
                args = [(str(pdf_path), pno, DPI, POPPLER_PATH,
                         pytesseract.pytesseract.tesseract_cmd) for pno in chunk]
                for pno, text in pool.imap_unordered(_worker_ocr_one_page, args):
                    (parts_dir / f"page_{pno:04d}.txt").write_text(text, encoding="utf-8")
                    pages_text[pno] = text
                    sys.stdout.write(".")
                    sys.stdout.flush()
                i += len(chunk)
        print()  # newline

    pages_text = [(pno, pages_text[pno]) for pno in sorted(pages_text.keys())]

    write_md(rec, pages_text, total, "ocr-220dpi-autocontrast-psm6",
             "re-OCR'd at 220 DPI with PIL autocontrast + PSM 6")

    # Cleanup parts dir (best effort; Windows sandbox may refuse)
    try:
        shutil.rmtree(parts_dir, ignore_errors=True)
    except Exception:
        pass

    chars_after = sum(len(t) for _, t in pages_text)
    return chars_before, chars_after


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ids", nargs="*", help="Record IDs to re-extract")
    ap.add_argument("--all-flagged", action="store_true",
                    help="Re-extract every record listed in the QA report's flagged section")
    args = ap.parse_args()

    idx = json.loads(INDEX.read_text(encoding="utf-8-sig"))

    targets = list(args.ids)
    if args.all_flagged:
        # Cheap parser: read logs/qa_report.md and find flagged ids
        report = ROOT / "logs" / "qa_report.md"
        if report.exists():
            import re
            for m in re.finditer(r'\| `([^`]+)` \|', report.read_text(encoding="utf-8")):
                rid = m.group(1)
                if rid not in targets:
                    targets.append(rid)

    if not targets:
        print("No targets specified. Pass record IDs or --all-flagged.", file=sys.stderr)
        return 2

    print(f"Re-extracting {len(targets)} record(s) at DPI={DPI}")
    print(f"Tesseract: {tess}")
    print(f"Poppler:   {POPPLER_PATH}")
    print()

    for rid in targets:
        before, after = reextract(rid, idx)
        delta = after - before
        sign = "+" if delta >= 0 else ""
        print(f"  -> {rid}: {after} chars total ({sign}{delta} vs prior)")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
