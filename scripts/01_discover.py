"""01_discover.py - fetch the canonical CSV manifest, build manifest.json.

As of Release 02 (5/22/26) war.gov consolidated the manifest into a single
CSV at /Portals/1/Interactive/2026/UFO/uap-data.csv. The Release 01 CSV
(uap-csv.csv / uap-release001.csv) now 404s. The new CSV is a superset:
every Release 01 record is still there, plus 60+ new ones dated 5/22/26.

war.gov is now behind Akamai bot management. Plain `requests` gets a 403
because Akamai fingerprints the TLS handshake. `_common.http_get` routes
war.gov requests through curl_cffi with Chrome impersonation, which gets
through.

If the host has no egress at all, save the CSV manually (in your browser,
navigate to CSV_URL and save it as snapshots/<date>/uap-data.csv) and
re-run; the script will use the saved file.

ID stability: we read all prior manifest.json files under snapshots/ and
build a (source_url|dvids_id) -> existing_id lookup. Records that match a
prior snapshot keep their existing ID; truly new records get the next
unused sequence number for their agency. That keeps the on-disk filename
and the metadata/per-file/*.json filename stable across re-discovers.
"""

from __future__ import annotations

import csv
import sys
from io import StringIO
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import (  # noqa: E402
    ERROR_LOG, FETCH_LOG, INDEX_PATH, REQUEST_TIMEOUT_SECONDS, SNAPSHOTS_DIR,
    http_get, load_json, log_line, make_id, now_iso, save_json, today_str,
)

CSV_URL = "https://www.war.gov/Portals/1/Interactive/2026/UFO/uap-data.csv"
LEGACY_CSV_URL = "https://www.war.gov/Portals/1/Interactive/2026/UFO/uap-csv.csv"
PAGE_URL = "https://www.war.gov/UFO/"

# Release Date -> page_section label. Add new entries as releases drop.
RELEASE_SECTIONS = {
    "5/8/26":  "Release 01",
    "5/22/26": "Release 02",
}


# "Type" column prefixes: V*=video, I*=image, A*=audio, P*=PDF (default).
def classify_type(t):
    if not t:
        return "pdf"
    f = t.strip()[:1].upper()
    return {"V": "video", "I": "image", "A": "audio"}.get(f, "pdf")


def normalize_agency(agency):
    if not agency:
        return "unknown"
    a = agency.lower()
    # Order matters: most specific keyword first.
    for kw, label in (
        ("fbi", "FBI"),
        ("director of national intelligence", "ODNI"),
        ("national intelligence", "ODNI"),
        ("central intelligence", "CIA"),
        ("cia", "CIA"),
        ("department of energy", "DoE"),
        ("energy", "DoE"),
        ("department of war", "DoW"),
        ("war", "DoW"),
        ("department of defense", "DoD"),
        ("defense", "DoD"),
        ("nasa", "NASA"),
        ("state", "State"),
    ):
        if kw in a:
            return label
    return agency.strip()


def fetch_csv(url, dest):
    if dest.exists() and dest.stat().st_size > 0:
        log_line(FETCH_LOG, "01_discover\tCACHED\t" + url)
        return dest.read_text(encoding="utf-8-sig")
    resp = http_get(url, headers={"Accept": "text/csv,text/plain,*/*"},
                    timeout=REQUEST_TIMEOUT_SECONDS)
    resp.raise_for_status()
    dest.parent.mkdir(parents=True, exist_ok=True)
    # Akamai/war.gov serves a UTF-8 BOM. Preserve raw bytes to disk;
    # decode with utf-8-sig for in-memory use so the BOM doesn't leak
    # into the first column name.
    dest.write_bytes(resp.content)
    log_line(FETCH_LOG, "01_discover\tOK\t" + url + "\t" + str(len(resp.content)))
    return resp.content.decode("utf-8-sig")


def fld(row, name):
    return (row.get(name) or "").strip()


def asset_key(source_url, dvids_id):
    """Stable identity for an asset across snapshots."""
    if source_url:
        return ("url", source_url.lower())
    if dvids_id:
        return ("dvids", str(dvids_id))
    return None


def load_prior_ids():
    """Build (asset_key -> existing_id, agency -> max_seq) from authoritative
    on-disk state.

    Lookup sources, in precedence order (later overrides earlier):
    1. All prior snapshots/<date>/manifest.json (oldest first)
    2. metadata/index.json - this carries any manual URL corrections the
       user has made since the original snapshot, so it's the most
       trustworthy mapping.
    """
    id_by_key = {}
    max_seq = {}

    def absorb(a, *, prefer):
        k = asset_key(a.get("source_url", ""), a.get("dvids_video_id", ""))
        if k and (prefer or k not in id_by_key):
            id_by_key[k] = a["id"]
        parts = a["id"].split("-", 2)
        if len(parts) >= 2 and parts[1].isdigit():
            seq = int(parts[1])
            ag = a.get("agency", "")
            max_seq[ag] = max(max_seq.get(ag, 0), seq)

    for snap_dir in sorted(p for p in SNAPSHOTS_DIR.iterdir() if p.is_dir()):
        mpath = snap_dir / "manifest.json"
        if not mpath.exists():
            continue
        for a in load_json(mpath, default={}).get("assets", []):
            absorb(a, prefer=False)

    # index.json reflects on-disk reality (including any manual URL fixes
    # the user has applied after the original snapshot). We add its keys
    # ADDITIVELY - so a corrected URL routes to the existing ID, without
    # overwriting a duplicate URL's claim on its earliest-seen ID.
    if INDEX_PATH.exists():
        for a in load_json(INDEX_PATH, default={}).get("files", []):
            absorb(a, prefer=False)

    return id_by_key, max_seq


def build_manifest(csv_text):
    reader = csv.DictReader(StringIO(csv_text))
    prior_ids, max_seq = load_prior_ids()
    # next_seq[agency] = next number to hand out for a brand-new record.
    next_seq = dict(max_seq)
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
        # PDF/image link comes from the CSV; videos and audio resolve via DVIDS.
        source_url = "" if kind in ("video", "audio") else pdf_image

        release_date = fld(row, "Release Date")
        page_section = RELEASE_SECTIONS.get(release_date, f"Release ({release_date})")

        key = asset_key(source_url, dvids_id)
        existing = prior_ids.get(key) if key else None
        if existing:
            asset_id = existing
        else:
            next_seq[agency] = next_seq.get(agency, 0) + 1
            asset_id = make_id(agency, next_seq[agency], title)

        assets.append({
            "id": asset_id,
            "type": kind,
            "title": title,
            "agency": agency,
            "agency_raw": agency_raw,
            "type_code": type_field,
            "page_section": page_section,
            "release_date": release_date,
            "incident_date": fld(row, "Incident Date"),
            "incident_location": fld(row, "Incident Location") or "N/A",
            "summary": fld(row, "Description Blurb"),
            "redaction": fld(row, "Redaction"),
            "video_pairing": fld(row, "Video Pairing"),
            "pdf_pairing": fld(row, "PDF Pairing"),
            "video_title": fld(row, "Video Title"),
            "dvids_video_id": dvids_id,
            "modal_image_url": fld(row, "Modal Image"),
            "image_alt_text": fld(row, "Image Alt Text"),
            "image_virin": fld(row, "Image VIRIN"),
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
    csv_path = snap_dir / "uap-data.csv"
    manifest_path = snap_dir / "manifest.json"

    print("[discover] snapshot:", today_str())
    print("[discover] CSV:", csv_path)

    try:
        csv_text = fetch_csv(CSV_URL, csv_path)
    except Exception as e:  # noqa: BLE001
        log_line(ERROR_LOG, "01_discover\tFETCH_FAIL\t" + CSV_URL + "\t" + str(e))
        if not csv_path.exists():
            print("[discover] could not fetch:", e, file=sys.stderr)
            print("[discover] save the CSV to", csv_path, "and re-run.", file=sys.stderr)
            return 2
        csv_text = csv_path.read_text(encoding="utf-8-sig")

    manifest = build_manifest(csv_text)
    save_json(manifest_path, manifest)

    by_type = {}
    by_agency = {}
    by_section = {}
    for a in manifest["assets"]:
        by_type[a["type"]] = by_type.get(a["type"], 0) + 1
        by_agency[a["agency"]] = by_agency.get(a["agency"], 0) + 1
        by_section[a["page_section"]] = by_section.get(a["page_section"], 0) + 1

    print("[discover] count:", manifest["asset_count"])
    print("[discover] type:", by_type)
    print("[discover] agency:", by_agency)
    print("[discover] section:", by_section)
    print("[discover] manifest:", manifest_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
