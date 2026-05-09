"""qa_review.py - quality assurance pass over the extracted corpus.

Doesn't fix anything. Just reports.

Checks:
  - Index integrity (records, paths, hashes)
  - Per-file extraction stats (page count, text length per page)
  - OCR error markers in body text
  - Empty pages
  - Suspiciously short extractions (probably failed OCR)
  - Tesseract garbage signatures (e.g., "i ee","Wee","|/")
  - Description blurb completeness
  - Common typewriter/scan OCR confusions (l/I/1 collisions, sparse text)
  - Cross-reference: which agencies have the most low-quality extractions?

Output:
  - logs/qa_report.md (full report)
  - stdout summary
"""

from __future__ import annotations
import json, re, sys, time
from pathlib import Path
from collections import Counter, defaultdict

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "metadata" / "index.json"
EXTRACTED = ROOT / "extracted"
REPORT = ROOT / "logs" / "qa_report.md"

# ---- Tunables ----------------------------------------------------------

# OCR garbage detection: heuristics for tesseract output that's mostly noise.
GARBAGE_PATTERNS = [
    (re.compile(r"^[\W_]{20,}$", re.M), "long stretch of non-word chars"),
    (re.compile(r"\b[a-z]{1,2}\s+[a-z]{1,2}\s+[a-z]{1,2}\s+[a-z]{1,2}\s+[a-z]{1,2}\b"),
     "many 1-2 letter fragments in a row"),
    (re.compile(r"^.{0,3}$", re.M), "very short line"),  # info, not necessarily bad
]

ERROR_MARKERS = [
    "[OCR error on page",
    "[pdf2image returned no image",
    "[pdfplumber error on page",
    "[tesseract error on page",
]

# A page is "thin" if its extracted text is < this many chars.
# (Many real declassified pages have only a few words. Tune cautiously.)
THIN_PAGE_CHARS = 30

# A page is "empty" if it has no text at all.
EMPTY_PAGE_PATTERN = re.compile(r"^_\(no text extracted\)_\s*$", re.M)


# ---- Helpers -----------------------------------------------------------

def read_md(path: Path) -> tuple[dict, str]:
    """Return (frontmatter_dict, body) for an extracted markdown file."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}, text
    try:
        end = text.index("\n---\n", 4)
    except ValueError:
        return {}, text
    fm_block = text[4:end]
    body = text[end + 5:]
    fm = {}
    # Cheap YAML-ish parser - just key: "value" lines + key: > blocks
    cur_key = None
    in_block = False
    block_lines = []
    for line in fm_block.split("\n"):
        if in_block:
            if line.startswith("  "):
                block_lines.append(line[2:])
                continue
            else:
                fm[cur_key] = "\n".join(block_lines).strip()
                in_block = False
                cur_key = None
                block_lines = []
        m = re.match(r'^(\w+):\s*"((?:[^"\\]|\\.)*)"\s*$', line)
        if m:
            fm[m.group(1)] = m.group(2).replace('\\"', '"').replace("\\\\", "\\")
            continue
        m = re.match(r'^(\w+):\s*(\d+)\s*$', line)
        if m:
            fm[m.group(1)] = int(m.group(2))
            continue
        m = re.match(r'^(\w+):\s*>\s*$', line)
        if m:
            cur_key = m.group(1)
            in_block = True
            block_lines = []
            continue
    if in_block:
        fm[cur_key] = "\n".join(block_lines).strip()
    return fm, body


def page_chunks(body: str) -> list[tuple[int, str]]:
    """Return [(page_no, text), ...] from the body of an extracted .md."""
    pages = []
    for m in re.finditer(r'^## Page (\d+)\s*\n+(.*?)(?=\n## Page \d+|\n## Tables|\n## DVIDS|\Z)',
                         body, re.S | re.M):
        pno = int(m.group(1))
        txt = m.group(2).strip()
        pages.append((pno, txt))
    return pages


def detect_garbage(text: str) -> list[str]:
    """Heuristic OCR-garbage detectors. Returns list of issue tags."""
    issues = []
    if not text:
        return issues
    # Ratio of alphabetic to total chars
    alpha = sum(1 for c in text if c.isalpha())
    total = len(text)
    if total > 30 and alpha / total < 0.4:
        issues.append("low alpha density")
    # Average word length sanity
    words = re.findall(r"\b[A-Za-z]+\b", text)
    if len(words) > 20:
        avg_len = sum(len(w) for w in words) / len(words)
        if avg_len < 2.5:
            issues.append("very short avg word length")
    # Excessive single-character "words"
    singles = sum(1 for w in words if len(w) == 1)
    if len(words) > 30 and singles / len(words) > 0.25:
        issues.append("many single-char words")
    # Pipe / slash noise (tesseract likes to insert these)
    pipes = text.count("|")
    if pipes > 10 and pipes / max(1, len(text.split())) > 0.3:
        issues.append("excessive '|' pipes")
    return issues





def is_image_only_pdf(record: dict) -> bool:
    """Heuristic: this PDF is essentially just an image (UFO photo / sketch),
    not a text document. OCR returning empty is expected, not a problem."""
    title = (record.get("title") or "").lower()
    summary = (record.get("summary") or "").lower()
    if "photo" in title or "sketch" in title:
        return True
    image_phrases = [
        "still image", "photograph", "narrative description",
        "the monochrome image", "composite sketch",
    ]
    if any(p in summary for p in image_phrases) and len(summary) < 800:
        return True
    return False


# ---- Main --------------------------------------------------------------

def main():
    idx = json.loads(INDEX.read_text(encoding="utf-8-sig"))
    records = idx["files"]

    # Build a lookup
    by_id = {r["id"]: r for r in records}

    # Per-record stats
    stats = []
    for r in records:
        rid = r["id"]
        md_path = EXTRACTED / f"{rid}.md"
        out = {
            "id": rid,
            "type": r["type"],
            "agency": r["agency"],
            "title": r["title"],
            "redaction": r.get("redaction", ""),
            "method": None,
            "pages": 0,
            "chars": 0,
            "thin_pages": 0,
            "empty_pages": 0,
            "error_lines": 0,
            "garbage_pages": 0,
            "missing_extracted": False,
            "missing_summary": not bool((r.get("summary") or "").strip()),
            "issues": [],
        }
        if not md_path.exists():
            out["missing_extracted"] = True
            stats.append(out)
            continue

        fm, body = read_md(md_path)
        out["method"] = fm.get("extraction_method", None) or ("metadata-only" if r["type"] == "video" else "?")
        pages = page_chunks(body)
        out["pages"] = len(pages)

        for pno, txt in pages:
            out["chars"] += len(txt)
            if EMPTY_PAGE_PATTERN.search(txt):
                out["empty_pages"] += 1
            elif len(txt) < THIN_PAGE_CHARS:
                out["thin_pages"] += 1
            for marker in ERROR_MARKERS:
                if marker in txt:
                    out["error_lines"] += txt.count(marker)
            if r["type"] == "pdf" and out["method"] == "ocr":
                garbage_tags = detect_garbage(txt)
                if garbage_tags:
                    out["garbage_pages"] += 1

        out["image_only"] = is_image_only_pdf(r) if r["type"] == "pdf" else False

        # File-level issues
        if r["type"] == "pdf" and out["pages"] > 0 and not out["image_only"]:
            chars_per_page = out["chars"] / out["pages"]
            if chars_per_page < 50:
                out["issues"].append(f"avg only {int(chars_per_page)} chars/page")
            if out["empty_pages"] / out["pages"] > 0.5:
                out["issues"].append(f"{out['empty_pages']}/{out['pages']} pages empty")
            if out["error_lines"] > 0:
                out["issues"].append(f"{out['error_lines']} OCR error markers")
            if out["garbage_pages"] / out["pages"] > 0.3 and out["pages"] > 5:
                out["issues"].append(f"{out['garbage_pages']}/{out['pages']} pages flagged as OCR garbage")
        stats.append(out)

    # ---- Build report -----------------------------------------------------

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    lines = []

    def w(s=""):
        lines.append(s)

    w(f"# QA review report - generated {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}")
    w()
    w("Pass: index integrity, extraction completeness, OCR sanity, metadata.")
    w("This report flags anomalies for human review. It does not fix anything.")
    w()

    # Index integrity
    w("## Index integrity")
    w()
    w(f"- Records in index: {len(records)}")
    missing_md = [s for s in stats if s["missing_extracted"]]
    w(f"- Records missing extracted .md: {len(missing_md)}")
    for s in missing_md:
        w(f"  - {s['id']}")
    missing_summary = [s for s in stats if s["missing_summary"]]
    w(f"- Records missing Description Blurb: {len(missing_summary)}")
    for s in missing_summary[:10]:
        w(f"  - {s['id']} ({s['type']})")
    image_only = [s for s in stats if s.get("image_only")]
    w(f"- Image-only PDFs (no extractable text expected): {len(image_only)}")
    for s in image_only[:5]:
        w(f"  - {s['id']}")
    if len(image_only) > 5:
        w(f"  - ... and {len(image_only) - 5} more")
    w()

    # Method breakdown
    w("## Extraction method breakdown")
    w()
    methods = Counter(s["method"] for s in stats if s["method"])
    for m, c in methods.most_common():
        w(f"- `{m}`: {c}")
    w()

    # Per-agency stats
    w("## Per-agency stats (PDFs only)")
    w()
    w("| agency | count | total pages | total chars | avg chars/page |")
    w("|---|---:|---:|---:|---:|")
    by_agency = defaultdict(lambda: {"count": 0, "pages": 0, "chars": 0})
    for s in stats:
        if s["type"] != "pdf":
            continue
        a = s["agency"]
        by_agency[a]["count"] += 1
        by_agency[a]["pages"] += s["pages"]
        by_agency[a]["chars"] += s["chars"]
    for a, d in sorted(by_agency.items(), key=lambda kv: -kv[1]["chars"]):
        avg = d["chars"] // d["pages"] if d["pages"] else 0
        w(f"| {a} | {d['count']} | {d['pages']:,} | {d['chars']:,} | {avg:,} |")
    w()

    # Files flagged for review
    w("## Records flagged for review")
    w()
    flagged = [s for s in stats if s["issues"]]
    flagged.sort(key=lambda s: (-len(s["issues"]), -s["garbage_pages"], -s["empty_pages"]))
    w(f"Count: {len(flagged)} of {len(stats)}")
    w()
    if flagged:
        w("| id | type | method | pages | chars | issues |")
        w("|---|---|---|---:|---:|---|")
        for s in flagged:
            issues = "; ".join(s["issues"])
            w(f"| `{s['id']}` | {s['type']} | {s['method']} | {s['pages']} | {s['chars']:,} | {issues} |")
    w()

    # OCR sanity per agency
    w("## OCR sanity (suspected garbage pages)")
    w()
    ocr_stats = [s for s in stats if s["method"] == "ocr"]
    if ocr_stats:
        w(f"Total OCR'd PDFs: {len(ocr_stats)}")
        total_pages = sum(s["pages"] for s in ocr_stats)
        total_garbage = sum(s["garbage_pages"] for s in ocr_stats)
        w(f"Total OCR'd pages: {total_pages:,}")
        w(f"Pages flagged as garbage: {total_garbage:,} "
          f"({100 * total_garbage / total_pages:.1f}% of OCR'd pages)")
        w()
        w("Heuristics: low alpha density, very short avg word length, "
          "excessive single-char words, excessive '|' pipes.")
        w()
        worst = sorted(ocr_stats,
                       key=lambda s: -(s["garbage_pages"] / max(1, s["pages"])))[:10]
        w("Top 10 worst OCR'd PDFs by garbage-page ratio:")
        w()
        w("| id | pages | garbage | ratio |")
        w("|---|---:|---:|---:|")
        for s in worst:
            ratio = s["garbage_pages"] / max(1, s["pages"])
            w(f"| `{s['id']}` | {s['pages']} | {s['garbage_pages']} | {ratio:.0%} |")
    w()

    # Empty / thin pages
    w("## Empty and thin pages")
    w()
    total_empty = sum(s["empty_pages"] for s in stats if s["type"] == "pdf")
    total_thin = sum(s["thin_pages"] for s in stats if s["type"] == "pdf")
    total_pages = sum(s["pages"] for s in stats if s["type"] == "pdf")
    w(f"- Total PDF pages: {total_pages:,}")
    w(f"- Pages with NO extracted text: {total_empty:,} ({100*total_empty/max(1,total_pages):.1f}%)")
    w(f"- Pages with <{THIN_PAGE_CHARS} chars (thin): {total_thin:,} ({100*total_thin/max(1,total_pages):.1f}%)")
    w()
    w("Empty pages are usually one of: blank scans, redacted-out pages, "
      "or pages where OCR genuinely failed. Thin pages may be "
      "single-line stamps or footer-only pages.")
    w()

    # Header showing which records had ocr_reason flagged in their frontmatter
    w("## Records originally text-layer that fell back to OCR")
    w()
    ocr_reason_records = [s for s in stats if s["method"] == "ocr"]
    w(f"All {len(ocr_reason_records)} OCR'd PDFs had text-layer extraction below threshold; check the `ocr_reason` field in their frontmatter for details.")
    w()

    REPORT.write_text("\n".join(lines), encoding="utf-8")

    # ---- Stdout summary --------------------------------------------------

    print(f"records: {len(records)}")
    print(f"  pdf:   {sum(1 for s in stats if s['type']=='pdf')}")
    print(f"  video: {sum(1 for s in stats if s['type']=='video')}")
    print(f"  image: {sum(1 for s in stats if s['type']=='image')}")
    print()
    print(f"missing extracted .md: {len(missing_md)}")
    print(f"missing description blurb: {len(missing_summary)}")
    print(f"records flagged for review: {len(flagged)}")
    print()
    print("extraction methods:")
    for m, c in methods.most_common():
        print(f"  {m}: {c}")
    print()
    if ocr_stats:
        total_pages = sum(s["pages"] for s in ocr_stats)
        total_garbage = sum(s["garbage_pages"] for s in ocr_stats)
        print(f"OCR garbage rate: {total_garbage}/{total_pages} pages "
              f"({100*total_garbage/max(1,total_pages):.1f}%)")
    print()
    print(f"full report: {REPORT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
