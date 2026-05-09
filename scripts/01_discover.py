"""01_discover.py - fetch the canonical CSV manifest, build manifest.json.

The war.gov UFO page is a Vue app whose entire record list is loaded from
one CSV at a known URL. We fetch the CSV directly and parse it.
Confirmed via Chrome MCP inspection of the live page on 2026-05-08.

Run from the project root or scripts/ - paths are resolved relative to
this file's location.

If the host has no egress to www.war.gov, save the CSV manually (in your
browser, navigate to CSV_URL and save it as snapshots/<date>/uap-csv.csv)
and re-run; the script will use the saved file.
"""

from __future__ import annotations

import csv
import sys
from io import StringIO
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import (  # noqa: E402
    ERROR_LOG, FETCH_LOG, REQUEST_TIMEOUT_SECONDS, SNAPSHOTS_DIR, USER_AGENT,
    log_line, make_id, now_iso, save_json, today_str,
)

CSV_URL = "https://www.war.gov/Portals/1/Interactive/2026/UFO/uap-csv.csv"
PAGE_URL = "https://www.war.gov/UFO/"

CSV_COLUMNS = [
    "Redaction", "Release Date", "Title", "Type",
    "Video Pairing", "PDF Pairing", "Description Blurb",
    "DVIDS Video ID", "Video Title", "Agency",
    "Incident Date", "Incident Location",
    "PDF | Image Link", "Modal Image",
]

# "Type" column prefixes: V*=video, I*=image, P*=PDF (default).


def classify_type(t):
    if not t:
        return "pdf"
    f = t.strip()[:1].upper()
    return {"V": "video", "I": "image"}.get(f, "pdf")


def normalize_agency(agency):
    if not agency:
        return "unknown"
    a = agency.lower()
    for kw, label in (("fbi", "FBI"), ("war", "DoW"), ("defense", "DoD"),
                      ("nasa", "NASA"), ("state", "State")):
        if kw in a:
            return label
    return agency.strip()


def fetch_text(url, dest):
    if dest.exists() and dest.stat().st_size > 0:
        log_line(FETCH_LOG, "01_discover\tCACHED\t" + url)
        return dest.read_text(encoding="utf-8")
    headers = {"User-Agent": USER_AGENT, "Accept": "text/csv,text/plain,*/*"}
    resp = requests.get(url, headers=headers, timeout=REQUEST_TIMEOUT_SECONDS)
    resp.raise_for_status()
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(resp.text, encoding="utf-8")
    log_line(FETCH_LOG, "01_discover\tOK\t" + url + "\t" + str(len(resp.content)))
    return resp.text


def fld(row, name):
    return (row.get(name) or "").strip()


def build_manifest(csv_text):
    reader = csv.DictReader(StringIO(csv_text))
    seq = {}
    assets = []

    for row in reader:
        title = fld(row, "Title")
        if not title:
            continue
        agency_raw = fld(row, "Agency")
        agency = normalize_agency(agency_raw)
        type_field = fld(row, "Type")
        kind = classify_type(type_field)
        pdf_image = fld(row, "PDF | Image Link")
        dvids_id = fld(row, "DVIDS Video ID")
        source_url = "" if kind == "video" else pdf_image
        seq[agency] = seq.get(agency, 0) + 1

        assets.append({
            "id": make_id(agency, seq[agency], title),
            "type": kind,
            "title": title,
            "agency": agency,
            "agency_raw": agency_raw,
            "type_code": type_field,
            "page_section": "Release 01",
            "release_date": fld(row, "Release Date"),
            "incident_date": fld(row, "Incident Date"),
            "incident_location": fld(row, "Incident Location") or "N/A",
            "summary": fld(row, "Description Blurb"),
            "redaction": fld(row, "Redaction"),
            "video_pairing": fld(row, "Video Pairing"),
            "pdf_pairing": fld(row, "PDF Pairing"),
            "video_title": fld(row, "Video Title"),
            "dvids_video_id": dvids_id,
            "modal_image_url": fld(row, "Modal Image"),
            "source_url": source_url,
            "discovered_on": now_iso(),
        })

    return {
        "snapshot_date": today_str(),
        "source_page": PAGE_URL,
        "csv_manifest_url": CSV_URL,
        "discovered_on": now_iso(),
        "asset_count": len(assets),
        "assets": assets,
    }


def main():
    snap_dir = SNAPSHOTS_DIR / today_str()
    csv_path = snap_dir / "uap-csv.csv"
    manifest_path = snap_dir / "manifest.json"

    print("[discover] snapshot:", today_str())
    print("[discover] CSV:", csv_path)

    try:
        csv_text = fetch_text(CSV_URL, csv_path)
    except requests.RequestException as e:
        log_line(ERROR_LOG, "01_discover\tFETCH_FAIL\t" + CSV_URL + "\t" + str(e))
        if not csv_path.exists():
            print("[discover] could not fetch:", e, file=sys.stderr)
            print("[discover] save the CSV to", csv_path, "and re-run.", file=sys.stderr)
            return 2
        csv_text = csv_path.read_text(encoding="utf-8")

    manifest = build_manifest(csv_text)
    save_json(manifest_path, manifest)

    by_type = {}
    by_agency = {}
    for a in manifest["assets"]:
        by_type[a["type"]] = by_type.get(a["type"], 0) + 1
        by_agency[a["agency"]] = by_agency.get(a["agency"], 0) + 1

    print("[discover] count:", manifest["asset_count"])
    print("[discover] type:", by_type)
    print("[discover] agency:", by_agency)
    print("[discover] manifest:", manifest_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
