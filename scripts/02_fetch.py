"""02_fetch.py — download every asset in the latest manifest, populate index.

Resumable: re-running skips files whose recorded sha256 already matches
their on-disk hash. Polite: 2-second delay between requests. Robust:
exponential backoff on 429/503, per-file try/except so one bad asset
doesn't kill the run.
"""

from __future__ import annotations

import csv
import hashlib
import sys
import time
from pathlib import Path
from typing import Any

import requests

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import (  # noqa: E402
    ERROR_LOG,
    FETCH_LOG,
    INDEX_CSV_PATH,
    INDEX_PATH,
    PER_FILE_DIR,
    REQUEST_DELAY_SECONDS,
    REQUEST_TIMEOUT_SECONDS,
    SNAPSHOTS_DIR,
    USER_AGENT,
    dest_dir_for_type,
    load_json,
    log_line,
    now_iso,
    save_json,
)

# ---- Helpers ------------------------------------------------------------

CSV_FIELDS = [
    "id", "type", "title", "agency", "agency_raw", "type_code", "page_section",
    "release_date", "incident_date", "incident_location", "summary", "redaction",
    "video_pairing", "pdf_pairing", "video_title", "dvids_video_id",
    "modal_image_url", "source_url", "discovered_on", "fetched_on", "local_path",
    "bytes", "sha256", "http_status", "content_type", "etag", "last_modified",
    "extracted_text_path", "status", "notes",
]

# DVIDS API used to resolve video records to direct mp4 URLs.
# The page exposes its key in cleartext, so this is fine to mirror here.
DVIDS_API = "https://api.dvidshub.net/asset"
DVIDS_API_KEY = "key-68bb60d16b35e"


def resolve_dvids_video(video_id: str) -> tuple[str, str] | None:
    """Return (best_mp4_url, video_title) for a DVIDS video id, or None."""
    if not video_id:
        return None
    try:
        r = requests.get(
            DVIDS_API,
            params={"api_key": DVIDS_API_KEY, "id": f"video:{video_id}"},
            headers={"User-Agent": USER_AGENT},
            timeout=REQUEST_TIMEOUT_SECONDS,
        )
        r.raise_for_status()
        data = r.json()
        d = data.get("results") or data.get("data") or data
        files = d.get("files") or []
        mp4s = [f for f in files if f.get("type") == "video/mp4"]
        if not mp4s:
            return None
        best = max(mp4s, key=lambda f: f.get("height", 0) or 0)
        return best.get("src", ""), d.get("title", "") or ""
    except (requests.RequestException, ValueError, KeyError):
        return None


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fp:
        for chunk in iter(lambda: fp.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def latest_manifest() -> dict | None:
    if not SNAPSHOTS_DIR.exists():
        return None
    snapshot_dirs = sorted(p for p in SNAPSHOTS_DIR.iterdir() if p.is_dir())
    for d in reversed(snapshot_dirs):
        m = d / "manifest.json"
        if m.exists():
            return load_json(m)
    return None


def load_index() -> dict:
    return load_json(INDEX_PATH, default={
        "schema_version": 1,
        "source_page": "https://www.war.gov/UFO/",
        "first_snapshot": None,
        "last_updated": None,
        "files": [],
    })


def index_by_id(index: dict) -> dict[str, dict]:
    return {rec["id"]: rec for rec in index.get("files", [])}


def write_csv(records: list[dict]) -> None:
    INDEX_CSV_PATH.parent.mkdir(parents=True, exist_ok=True)
    with INDEX_CSV_PATH.open("w", encoding="utf-8", newline="") as fp:
        writer = csv.DictWriter(fp, fieldnames=CSV_FIELDS)
        writer.writeheader()
        for r in records:
            writer.writerow({k: r.get(k, "") for k in CSV_FIELDS})


def write_per_file(record: dict) -> None:
    path = PER_FILE_DIR / f"{record['id']}.json"
    save_json(path, record)


# ---- Fetch with backoff -------------------------------------------------

def fetch_with_backoff(url: str, dest: Path) -> tuple[requests.Response, int]:
    """Return (response, bytes_written). Streams to disk to avoid RAM blowup."""
    headers = {"User-Agent": USER_AGENT}
    backoff = [4, 8, 16, 32, 60]
    attempt = 0
    while True:
        try:
            with requests.get(
                url, headers=headers, timeout=REQUEST_TIMEOUT_SECONDS, stream=True
            ) as r:
                if r.status_code in (429, 503) and attempt < len(backoff):
                    wait = backoff[attempt]
                    log_line(FETCH_LOG, f"02_fetch\tBACKOFF\t{url}\t{r.status_code}\t{wait}s")
                    time.sleep(wait)
                    attempt += 1
                    continue
                r.raise_for_status()
                dest.parent.mkdir(parents=True, exist_ok=True)
                tmp = dest.with_suffix(dest.suffix + ".part")
                bytes_written = 0
                with tmp.open("wb") as fp:
                    for chunk in r.iter_content(1 << 20):
                        if chunk:
                            fp.write(chunk)
                            bytes_written += len(chunk)
                expected = r.headers.get("Content-Length")
                if expected is not None and int(expected) != bytes_written:
                    tmp.unlink(missing_ok=True)
                    raise IOError(
                        f"truncated: got {bytes_written} bytes, expected {expected}"
                    )
                tmp.replace(dest)
                return r, bytes_written
        except requests.RequestException as e:
            if attempt < len(backoff):
                wait = backoff[attempt]
                log_line(FETCH_LOG, f"02_fetch\tRETRY\t{url}\t{e}\t{wait}s")
                time.sleep(wait)
                attempt += 1
                continue
            raise


# ---- Main ---------------------------------------------------------------

def merge_record(existing: dict | None, asset: dict) -> dict:
    """Carry over fetch state from prior runs; refresh page-level metadata."""
    base: dict[str, Any] = {
        "id": asset["id"],
        "type": asset["type"],
        "title": asset["title"],
        "agency": asset["agency"],
        "agency_raw": asset.get("agency_raw", ""),
        "type_code": asset.get("type_code", ""),
        "page_section": asset.get("page_section", "Release 01"),
        "release_date": asset.get("release_date", ""),
        "incident_date": asset.get("incident_date", ""),
        "incident_location": asset.get("incident_location", "N/A"),
        "summary": asset.get("summary", ""),
        "redaction": asset.get("redaction", ""),
        "video_pairing": asset.get("video_pairing", ""),
        "pdf_pairing": asset.get("pdf_pairing", ""),
        "video_title": asset.get("video_title", ""),
        "dvids_video_id": asset.get("dvids_video_id", ""),
        "modal_image_url": asset.get("modal_image_url", ""),
        "source_url": asset["source_url"],
        "discovered_on": asset["discovered_on"],
        "fetched_on": "",
        "local_path": "",
        "bytes": 0,
        "sha256": "",
        "http_status": 0,
        "content_type": "",
        "etag": "",
        "last_modified": "",
        "extracted_text_path": None,
        "status": "pending",
        "notes": "",
    }
    if existing:
        for k in ("fetched_on", "local_path", "bytes", "sha256", "http_status",
                 "content_type", "etag", "last_modified", "extracted_text_path",
                 "status", "notes"):
            base[k] = existing.get(k, base[k])
    return base


def already_have(record: dict) -> bool:
    if record["status"] != "ok" or not record["sha256"] or not record["local_path"]:
        return False
    p = Path(record["local_path"])
    if not p.is_absolute():
        p = INDEX_PATH.parent.parent / record["local_path"]
    if not p.exists():
        return False
    return sha256_file(p) == record["sha256"]


def main() -> int:
    manifest = latest_manifest()
    if manifest is None:
        print("[fetch] no manifest found. Run 01_discover.py first.", file=sys.stderr)
        return 2

    index = load_index()
    if index.get("first_snapshot") is None:
        index["first_snapshot"] = manifest["snapshot_date"]
    by_id = index_by_id(index)

    fetched = skipped = failed = 0
    for asset in manifest["assets"]:
        rec = merge_record(by_id.get(asset["id"]), asset)
        by_id[asset["id"]] = rec

        if already_have(rec):
            skipped += 1
            continue

        # Videos are referenced by DVIDS asset id rather than direct URL.
        # Resolve the highest-resolution mp4 URL via the DVIDS API on demand.
        if rec["type"] == "video" and not rec["source_url"]:
            resolved = resolve_dvids_video(rec["dvids_video_id"])
            if resolved is None:
                rec["status"] = "fetch_error"
                rec["notes"] = f"DVIDS resolve failed for id={rec['dvids_video_id']}"
                failed += 1
                log_line(ERROR_LOG,
                         f"02_fetch\tDVIDS_RESOLVE_FAIL\t{rec['dvids_video_id']}")
                write_per_file(rec)
                time.sleep(REQUEST_DELAY_SECONDS)
                continue
            rec["source_url"], dvids_title = resolved
            if dvids_title and not rec.get("video_title"):
                rec["video_title"] = dvids_title

        ext = Path(rec["source_url"].split("?")[0]).suffix.lower() or {
            "pdf": ".pdf", "video": ".mp4", "image": ".jpg",
        }[rec["type"]]
        local = dest_dir_for_type(rec["type"]) / f"{rec['id']}{ext}"

        try:
            resp, n = fetch_with_backoff(rec["source_url"], local)
            rec.update({
                "fetched_on": now_iso(),
                "local_path": str(local.relative_to(INDEX_PATH.parent.parent)).replace("\\", "/"),
                "bytes": n,
                "sha256": sha256_file(local),
                "http_status": resp.status_code,
                "content_type": resp.headers.get("Content-Type", ""),
                "etag": resp.headers.get("ETag", ""),
                "last_modified": resp.headers.get("Last-Modified", ""),
                "status": "ok",
            })
            fetched += 1
            log_line(FETCH_LOG, f"02_fetch\tOK\t{rec['source_url']}\t{n}")
        except requests.HTTPError as e:
            code = e.response.status_code if e.response is not None else 0
            rec["http_status"] = code
            rec["status"] = "missing" if code == 404 else "fetch_error"
            rec["notes"] = f"HTTPError: {e}"
            failed += 1
            log_line(ERROR_LOG, f"02_fetch\t{rec['status'].upper()}\t{rec['source_url']}\t{e}")
        except Exception as e:  # noqa: BLE001 - keep run going
            rec["status"] = "fetch_error"
            rec["notes"] = repr(e)
            failed += 1
            log_line(ERROR_LOG, f"02_fetch\tEXCEPTION\t{rec['source_url']}\t{e!r}")

        write_per_file(rec)
        time.sleep(REQUEST_DELAY_SECONDS)

    index["files"] = list(by_id.values())
    index["last_updated"] = now_iso()
    save_json(INDEX_PATH, index)
    write_csv(index["files"])

    print(f"[fetch] fetched={fetched} skipped={skipped} failed={failed} "
          f"total={len(index['files'])}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
