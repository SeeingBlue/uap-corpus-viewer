"""extract_pdfs.py - extract text from every PDF in the archive.

Modes:
  --text-only   Only extract PDFs with a text layer; skip ones that need OCR.
  --max-time S  Stop after S seconds (default: no limit).
  --max-pdfs N  Stop after N PDFs in this run.

Resumability:
  - At the file level: existing extracted/<id>.md is skipped.
  - At the page level: OCR writes per-page checkpoints to
    extracted/.parts/<id>/page_NNNN.txt as it goes, so a long-PDF OCR
    interrupted mid-way picks up where it left off on the next run.

PII / names: extracts verbatim, no filtering.
"""

from __future__ import annotations

import argparse
import json
import shutil
import sys
import time
import traceback
from pathlib import Path

import pdfplumber
from pdf2image import convert_from_path
import pytesseract

# ---- Windows binary auto-detect ------------------------------------------
# pdf2image and pytesseract shell out to external programs (pdftoppm and
# tesseract) that don't ship with Python or Windows. On Windows we look for
# them in common install locations and wire them up automatically. On Linux
# they're typically already on PATH.
import os, shutil, sys

def _find_windows_tesseract():
    candidates = [
        os.environ.get("TESSERACT_CMD"),
        r"C:\Program Files\Tesseract-OCR\tesseract.exe",
        r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe",
        os.path.expanduser(r"~\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"),
    ]
    for c in candidates:
        if c and os.path.isfile(c):
            return c
    return shutil.which("tesseract")


def _find_windows_poppler():
    """Return the directory containing pdftoppm.exe, or None."""
    env = os.environ.get("POPPLER_PATH")
    if env and os.path.isfile(os.path.join(env, "pdftoppm.exe")):
        return env
    common_roots = [
        r"C:\Program Files\poppler",
        r"C:\Program Files (x86)\poppler",
        r"C:\poppler",
        os.path.expanduser(r"~\poppler"),
        os.path.expanduser(r"~\Documents\poppler"),
        os.path.expanduser(r"~\Downloads\poppler"),
    ]
    for root in common_roots:
        if not os.path.isdir(root):
            continue
        # Look for bin/ subdir directly or in versioned subfolders
        for sub in [root] + [os.path.join(root, d) for d in os.listdir(root)]:
            cand = os.path.join(sub, "bin", "pdftoppm.exe")
            if os.path.isfile(cand):
                return os.path.dirname(cand)
    via_path = shutil.which("pdftoppm.exe") or shutil.which("pdftoppm")
    if via_path:
        return os.path.dirname(via_path)
    return None


POPPLER_PATH = None
if sys.platform.startswith("win"):
    tess = _find_windows_tesseract()
    if tess:
        pytesseract.pytesseract.tesseract_cmd = tess
    else:
        print("[setup] Tesseract not found. Install:", file=sys.stderr)
        print("        winget install --id UB-Mannheim.TesseractOCR", file=sys.stderr)
        print("        or download: https://github.com/UB-Mannheim/tesseract/wiki", file=sys.stderr)
        sys.exit(3)
    POPPLER_PATH = _find_windows_poppler()
    if not POPPLER_PATH:
        print("[setup] Poppler (pdftoppm.exe) not found. Install:", file=sys.stderr)
        print("        1. Download poppler-windows-25.x.zip from", file=sys.stderr)
        print("           https://github.com/oschwartz10612/poppler-windows/releases", file=sys.stderr)
        print("        2. Extract to C:\\poppler  (so C:\\poppler\\Library\\bin\\pdftoppm.exe exists)", file=sys.stderr)
        print("        3. Or set POPPLER_PATH env var to the directory containing pdftoppm.exe", file=sys.stderr)
        sys.exit(3)
    PDFTOTEXT_CMD = os.path.join(POPPLER_PATH, "pdftotext.exe")
    if not os.path.isfile(PDFTOTEXT_CMD):
        print(f"[setup] pdftotext.exe not found at {PDFTOTEXT_CMD}", file=sys.stderr)
        sys.exit(3)
    print(f"[setup] tesseract: {tess}")
    print(f"[setup] poppler:   {POPPLER_PATH}")
    print(f"[setup] pdftotext: {PDFTOTEXT_CMD}")
else:
    PDFTOTEXT_CMD = "pdftotext"  # Linux/Mac: assume on PATH

PROJECT_ROOT = Path(__file__).resolve().parent.parent
INDEX_PATH   = PROJECT_ROOT / "metadata" / "index.json"
EXTRACTED    = PROJECT_ROOT / "extracted"
PARTS_DIR    = EXTRACTED / ".parts"
LOGS_DIR     = PROJECT_ROOT / "logs"
EXTRACT_LOG  = LOGS_DIR / "extract.log"

OCR_THRESHOLD_CHARS_PER_PAGE = 50
OCR_DPI = 150
OCR_LANG = "eng"


def load_index():
    return json.loads(INDEX_PATH.read_text(encoding="utf-8-sig"))


def save_index(idx):
    INDEX_PATH.write_text(
        json.dumps(idx, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def log(line: str):
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    ts = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    with EXTRACT_LOG.open("a", encoding="utf-8") as f:
        f.write(f"{ts}\t{line}\n")


def yaml_escape(s):
    if not s:
        return '""'
    s = str(s).replace("\\", "\\\\").replace('"', '\\"')
    return f'"{s}"'


def yaml_block(s, indent=2):
    if not s:
        return '""'
    lines = s.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    pad = " " * indent
    return ">\n" + "\n".join(pad + line for line in lines)


# ---- Extraction ----

def extract_text_layer(pdf_path: Path):
    """Use pdftotext (poppler) - 15x faster than pdfplumber.

    Returns (pages_text, [], npages, avg_chars_per_page).
    Tables are not extracted in this pass (separate concern).
    """
    import subprocess
    out = subprocess.run(
        [PDFTOTEXT_CMD, "-layout", str(pdf_path), "-"],
        capture_output=True, text=True, timeout=60,
    )
    raw = out.stdout
    # pdftotext separates pages with form-feed (\f)
    pages = raw.split("\f")
    # The last entry after the final page is usually empty; trim it.
    if pages and not pages[-1].strip():
        pages.pop()
    pages_text = [(i, t) for i, t in enumerate(pages, 1)]
    npages = len(pages_text)
    total_chars = sum(len(t) for _, t in pages_text)
    avg = total_chars // npages if npages else 0
    return pages_text, [], npages, avg


class PartialOCR(Exception):
    """Raised when OCR runs out of time before finishing all pages."""
    def __init__(self, done, total):
        self.done = done
        self.total = total
        super().__init__(f"OCR partial: {done}/{total} pages done")


def get_total_pages(pdf_path: Path):
    """Cheap page count via pdfplumber metadata."""
    with pdfplumber.open(pdf_path) as pdf:
        return len(pdf.pages)


def _ocr_one_page(args):
    """Worker for the multiprocessing pool: OCR a single page.

    On Windows with spawn-based multiprocessing, the child process re-imports
    the module but module-level globals set by setup may not stick. So we
    pass the binary paths explicitly via args and re-wire pytesseract here.
    """
    pdf_path_str, pno, dpi, lang, tesseract_cmd, poppler_path = args
    if tesseract_cmd:
        pytesseract.pytesseract.tesseract_cmd = tesseract_cmd
    try:
        images = convert_from_path(pdf_path_str, dpi=dpi,
                                   first_page=pno, last_page=pno,
                                   poppler_path=poppler_path)
        if not images:
            return pno, "[pdf2image returned no image for this page]"
        return pno, pytesseract.image_to_string(images[0], lang=lang)
    except Exception as e:
        return pno, f"[OCR error on page {pno}: {e}]"


def extract_ocr_resumable(pdf_path: Path, parts_dir: Path, deadline):
    """OCR page-by-page with per-page checkpoints, parallel across cores."""
    import multiprocessing as mp
    parts_dir.mkdir(parents=True, exist_ok=True)
    total = get_total_pages(pdf_path)

    # Figure out which pages still need OCR
    pending = []
    cached = {}
    for pno in range(1, total + 1):
        part = parts_dir / f"page_{pno:04d}.txt"
        if part.exists():
            cached[pno] = part.read_text(encoding="utf-8")
        else:
            pending.append(pno)

    if pending:
        # Parallel OCR. Process pages in chunks so we can check deadline.
        nproc = max(1, min(mp.cpu_count(), 2))
        chunk_size = nproc * 2  # 2 batches of work per loop iteration
        i = 0
        with mp.Pool(nproc) as pool:
            while i < len(pending):
                if deadline is not None and time.monotonic() >= deadline:
                    break
                chunk = pending[i:i + chunk_size]
                _tess = pytesseract.pytesseract.tesseract_cmd
                args = [(str(pdf_path), pno, OCR_DPI, OCR_LANG, _tess, POPPLER_PATH) for pno in chunk]
                for pno, text in pool.imap_unordered(_ocr_one_page, args):
                    (parts_dir / f"page_{pno:04d}.txt").write_text(text, encoding="utf-8")
                    cached[pno] = text
                i += len(chunk)

    if len(cached) < total:
        raise PartialOCR(len(cached), total)

    pages_text = [(pno, cached[pno]) for pno in sorted(cached.keys())]
    return pages_text, total


def render_markdown_table(rows):
    if not rows or not rows[0]:
        return ""
    norm = [[("" if c is None else str(c)).replace("\n", " ").replace("|", "\\|").strip()
             for c in row] for row in rows]
    width = max(len(r) for r in norm)
    norm = [r + [""] * (width - len(r)) for r in norm]
    header = norm[0]
    body = norm[1:] if len(norm) > 1 else []
    sep = ["---"] * width
    lines = ["| " + " | ".join(header) + " |",
             "| " + " | ".join(sep) + " |"]
    for row in body:
        lines.append("| " + " | ".join(row) + " |")
    return "\n".join(lines)


def write_md(record, pages_text, tables, npages, method, ocr_reason=""):
    out = EXTRACTED / f"{record['id']}.md"
    out.parent.mkdir(parents=True, exist_ok=True)

    fm_lines = ["---",
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
                ]
    if ocr_reason:
        fm_lines.append(f'ocr_reason: {yaml_escape(ocr_reason)}')
    redaction_marker = (record.get("redaction") or "").strip()
    if redaction_marker:
        fm_lines.append(f'redaction: {yaml_escape(redaction_marker)}')
    desc = (record.get("summary") or "").strip()
    fm_lines.append(f"description: {yaml_block(desc, indent=2)}")
    fm_lines.append("---")
    fm = "\n".join(fm_lines)

    parts = [fm, "", f"# {record['title']}", ""]
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
    if redaction_marker:
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

    if tables:
        parts.append("---")
        parts.append("")
        parts.append("## Tables")
        parts.append("")
        for pno, tbl in tables:
            parts.append(f"### Page {pno}")
            parts.append("")
            md = render_markdown_table(tbl)
            if md:
                parts.append(md)
            parts.append("")

    out.write_text("\n".join(parts), encoding="utf-8")
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--text-only", action="store_true",
                    help="Skip OCR-needed PDFs (only process those with text layer)")
    ap.add_argument("--max-time", type=int, default=0,
                    help="Stop after N seconds (0 = no limit)")
    ap.add_argument("--max-pdfs", type=int, default=0,
                    help="Stop after N PDFs in this run (0 = no limit)")
    args = ap.parse_args()

    deadline = (time.monotonic() + args.max_time) if args.max_time > 0 else None

    idx = load_index()
    pdf_records = [r for r in idx["files"] if r.get("type") == "pdf"]
    # Sort small-first so quick wins come first; tie-break by id for stability.
    def _est_pages(rec):
        return rec.get("bytes", 0) or 0  # crude proxy: file size correlates with pages
    pdf_records.sort(key=lambda r: (_est_pages(r), r["id"]))
    total = len(pdf_records)

    EXTRACTED.mkdir(parents=True, exist_ok=True)

    by_id = {r["id"]: r for r in idx["files"]}
    n_text = n_ocr = n_skip = n_partial = n_fail = 0
    n_processed = 0

    for i, record in enumerate(pdf_records, 1):
        rid = record["id"]
        out = EXTRACTED / f"{rid}.md"
        if out.exists() and out.stat().st_size > 0:
            n_skip += 1
            continue

        if deadline is not None and time.monotonic() >= deadline:
            print(f"[time] stopping early ({args.max_time}s budget exhausted)")
            break
        if args.max_pdfs and n_processed >= args.max_pdfs:
            print(f"[count] stopping early ({args.max_pdfs} PDFs done this run)")
            break

        local = record.get("local_path")
        if not local:
            log(f"SKIP\t{rid}\tno local_path")
            continue
        pdf_path = PROJECT_ROOT / local
        if not pdf_path.exists():
            log(f"SKIP\t{rid}\tnot on disk: {pdf_path}")
            continue

        print(f"[{i:>3}/{total}] {rid}", flush=True)
        try:
            pages_text, tables, npages, avg = extract_text_layer(pdf_path)
            method = "text-layer"
            ocr_reason = ""

            if avg < OCR_THRESHOLD_CHARS_PER_PAGE:
                if args.text_only:
                    print(f"      [skip-ocr] text layer avg {avg} c/p")
                    continue
                ocr_reason = f"text layer avg only {avg} chars/page"
                print(f"      [ocr] {ocr_reason}", flush=True)
                parts_dir = PARTS_DIR / rid
                pages_text, npages = extract_ocr_resumable(pdf_path, parts_dir, deadline)
                tables = []
                method = "ocr"
                n_ocr += 1
            else:
                n_text += 1

            write_md(record, pages_text, tables, npages, method, ocr_reason)
            by_id[rid]["extracted_text_path"] = f"extracted/{rid}.md"
            log(f"OK\t{rid}\t{method}\tpages={npages}\tchars_avg={avg}")

            # Clean up parts dir on full success
            parts_dir = PARTS_DIR / rid
            if parts_dir.exists():
                shutil.rmtree(parts_dir, ignore_errors=True)

            n_processed += 1
        except PartialOCR as e:
            print(f"      [partial] {e.done}/{e.total} pages OCR'd, will resume next run")
            log(f"PARTIAL\t{rid}\tpages={e.done}/{e.total}")
            n_partial += 1
            break  # bail out so caller can re-invoke
        except Exception as e:
            tb = traceback.format_exc(limit=2)
            log(f"FAIL\t{rid}\t{e!r}\t{tb}")
            print(f"      FAIL: {e}")
            n_fail += 1

    # Save index
    idx["files"] = list(by_id.values())
    idx["last_updated"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    save_index(idx)

    print(f"\n[run] processed={n_processed} text-layer={n_text} ocr={n_ocr} "
          f"skipped={n_skip} partial={n_partial} failed={n_fail} "
          f"total-extracted={len(list(EXTRACTED.glob('*.md')))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
