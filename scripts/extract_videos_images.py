"""Generate extracted/<id>.md for video and image records.

Videos: write metadata-only stubs from CSV (Description Blurb is rich).
        DVIDS captions are fetched separately via PowerShell on the host.
Images: run OCR via tesseract; many will yield nothing but we try anyway.
"""

from __future__ import annotations
import json, sys, time, traceback
from pathlib import Path

import pytesseract
from PIL import Image

PROJECT_ROOT = Path(__file__).resolve().parent.parent
INDEX_PATH   = PROJECT_ROOT / "metadata" / "index.json"
EXTRACTED    = PROJECT_ROOT / "extracted"
LOGS_DIR     = PROJECT_ROOT / "logs"
EXTRACT_LOG  = LOGS_DIR / "extract.log"


def load_index():
    return json.loads(INDEX_PATH.read_text(encoding="utf-8-sig"))


def save_index(idx):
    INDEX_PATH.write_text(
        json.dumps(idx, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def log(line):
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    ts = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    EXTRACT_LOG.open("a", encoding="utf-8").write(f"{ts}\t{line}\n")


def yaml_escape(s):
    if not s: return '""'
    s = str(s).replace("\\", "\\\\").replace('"', '\\"')
    return f'"{s}"'


def yaml_block(s, indent=2):
    if not s: return '""'
    lines = s.replace("\r\n","\n").replace("\r","\n").split("\n")
    pad = " " * indent
    return ">\n" + "\n".join(pad + line for line in lines)


def write_video_md(record):
    """Video records get metadata-only .md; transcripts come later via host."""
    out = EXTRACTED / f"{record['id']}.md"
    fm_lines = ["---",
                f'id: {yaml_escape(record["id"])}',
                f'title: {yaml_escape(record["title"])}',
                f'agency: {yaml_escape(record["agency"])}',
                f'agency_raw: {yaml_escape(record["agency_raw"])}',
                f'type: {yaml_escape(record["type"])}',
                f'type_code: {yaml_escape(record.get("type_code",""))}',
                f'page_section: {yaml_escape(record["page_section"])}',
                f'release_date: {yaml_escape(record["release_date"])}',
                f'incident_date: {yaml_escape(record["incident_date"])}',
                f'incident_location: {yaml_escape(record["incident_location"])}',
                f'video_title: {yaml_escape(record.get("video_title",""))}',
                f'dvids_video_id: {yaml_escape(record.get("dvids_video_id",""))}',
                f'source_url: {yaml_escape(record["source_url"])}',
                f'modal_image_url: {yaml_escape(record.get("modal_image_url",""))}',
                f'sha256: {yaml_escape(record["sha256"])}',
                f'bytes: {record.get("bytes", 0)}',
                f'extraction_method: "metadata-only"',
                ]
    redaction = (record.get("redaction") or "").strip()
    if redaction:
        fm_lines.append(f'redaction: {yaml_escape(redaction)}')
    desc = (record.get("summary") or "").strip()
    fm_lines.append(f"description: {yaml_block(desc, indent=2)}")
    fm_lines.append("---")

    parts = ["\n".join(fm_lines), "", f"# {record['title']}", ""]
    if record.get("video_title"):
        parts.append(f"_DVIDS title: {record['video_title']}_")
        parts.append("")
    if desc:
        parts.append("> " + desc.replace("\n", "\n> "))
        parts.append("")

    parts.extend([
        f"**Agency:** {record['agency']}  ",
        f"**Release date:** {record['release_date']}  ",
        f"**Incident date:** {record['incident_date']}  ",
        f"**Incident location:** {record['incident_location']}  ",
        f"**DVIDS video ID:** {record.get('dvids_video_id','')}  ",
        f"**Source:** [{record['source_url'].split('/')[-1]}]({record['source_url']})  ",
        f"**Local path:** `{record['local_path']}`  ",
        f"**SHA-256:** `{record['sha256']}`",
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
    parts.append("## DVIDS metadata")
    parts.append("")
    parts.append("_Captions, transcripts, and full DVIDS metadata are fetched "
                 "separately by `scripts/fetch-dvids-captions.ps1` on the host "
                 "(api.dvidshub.net is not reachable from the sandbox). Once "
                 "that runs, this section will be populated automatically._")
    parts.append("")

    out.write_text("\n".join(parts), encoding="utf-8")
    return out


def write_image_md(record):
    out = EXTRACTED / f"{record['id']}.md"
    pdf_path = PROJECT_ROOT / record["local_path"]

    # OCR the image
    try:
        with Image.open(pdf_path) as img:
            ocr_text = pytesseract.image_to_string(img, lang="eng")
            width, height = img.size
            mode = img.mode
    except Exception as e:
        ocr_text = f"[OCR error: {e}]"
        width = height = 0
        mode = "?"

    fm_lines = ["---",
                f'id: {yaml_escape(record["id"])}',
                f'title: {yaml_escape(record["title"])}',
                f'agency: {yaml_escape(record["agency"])}',
                f'agency_raw: {yaml_escape(record["agency_raw"])}',
                f'type: {yaml_escape(record["type"])}',
                f'type_code: {yaml_escape(record.get("type_code",""))}',
                f'page_section: {yaml_escape(record["page_section"])}',
                f'release_date: {yaml_escape(record["release_date"])}',
                f'incident_date: {yaml_escape(record["incident_date"])}',
                f'incident_location: {yaml_escape(record["incident_location"])}',
                f'source_url: {yaml_escape(record["source_url"])}',
                f'modal_image_url: {yaml_escape(record.get("modal_image_url",""))}',
                f'sha256: {yaml_escape(record["sha256"])}',
                f'bytes: {record.get("bytes", 0)}',
                f'image_size: "{width}x{height}"',
                f'image_mode: {yaml_escape(mode)}',
                f'extraction_method: "tesseract-ocr"',
                ]
    redaction = (record.get("redaction") or "").strip()
    if redaction:
        fm_lines.append(f'redaction: {yaml_escape(redaction)}')
    desc = (record.get("summary") or "").strip()
    fm_lines.append(f"description: {yaml_block(desc, indent=2)}")
    fm_lines.append("---")

    parts = ["\n".join(fm_lines), "", f"# {record['title']}", ""]
    if desc:
        parts.append("> " + desc.replace("\n", "\n> "))
        parts.append("")

    parts.extend([
        f"**Agency:** {record['agency']}  ",
        f"**Release date:** {record['release_date']}  ",
        f"**Incident date:** {record['incident_date']}  ",
        f"**Incident location:** {record['incident_location']}  ",
        f"**Source:** [{record['source_url'].split('/')[-1]}]({record['source_url']})  ",
        f"**Image size:** {width}x{height} ({mode})  ",
        f"**SHA-256:** `{record['sha256']}`",
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
    parts.append("## OCR text")
    parts.append("")
    if ocr_text and ocr_text.strip():
        parts.append(ocr_text.strip())
    else:
        parts.append("_(no text extracted by OCR — image is likely diagrammatic / no readable text)_")
    parts.append("")

    out.write_text("\n".join(parts), encoding="utf-8")
    return out


def main():
    idx = load_index()
    by_id = {r["id"]: r for r in idx["files"]}
    EXTRACTED.mkdir(parents=True, exist_ok=True)

    n_video = n_image = n_skip = n_fail = 0

    # Videos
    for record in [r for r in idx["files"] if r["type"] == "video"]:
        out = EXTRACTED / f"{record['id']}.md"
        if out.exists() and out.stat().st_size > 0:
            n_skip += 1
            continue
        try:
            write_video_md(record)
            by_id[record["id"]]["extracted_text_path"] = f"extracted/{record['id']}.md"
            log(f"OK\t{record['id']}\tvideo-metadata")
            n_video += 1
        except Exception as e:
            log(f"FAIL\t{record['id']}\t{e!r}")
            print(f"FAIL video {record['id']}: {e}")
            n_fail += 1

    # Images
    for record in [r for r in idx["files"] if r["type"] == "image"]:
        out = EXTRACTED / f"{record['id']}.md"
        if out.exists() and out.stat().st_size > 0:
            n_skip += 1
            continue
        try:
            write_image_md(record)
            by_id[record["id"]]["extracted_text_path"] = f"extracted/{record['id']}.md"
            log(f"OK\t{record['id']}\timage-ocr")
            n_image += 1
        except Exception as e:
            log(f"FAIL\t{record['id']}\t{e!r}")
            print(f"FAIL image {record['id']}: {e}")
            n_fail += 1

    idx["files"] = list(by_id.values())
    idx["last_updated"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    save_index(idx)

    print(f"[done] videos={n_video} images={n_image} skipped={n_skip} failed={n_fail}")
    return 0 if n_fail == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
