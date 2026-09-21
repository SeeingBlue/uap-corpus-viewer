"""Shared helpers for the war-gov-uap-archive scripts.

Path resolution, ID generation, agency inference, and JSON I/O.
"""

from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

# ---- Paths --------------------------------------------------------------

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent

SNAPSHOTS_DIR = PROJECT_ROOT / "snapshots"
FILES_DIR = PROJECT_ROOT / "files"
PDF_DIR = FILES_DIR / "pdfs"
VIDEO_DIR = FILES_DIR / "videos"
IMAGE_DIR = FILES_DIR / "images"
AUDIO_DIR = FILES_DIR / "audio"

METADATA_DIR = PROJECT_ROOT / "metadata"
INDEX_PATH = METADATA_DIR / "index.json"
INDEX_CSV_PATH = METADATA_DIR / "index.csv"
PER_FILE_DIR = METADATA_DIR / "per-file"

EXTRACTED_DIR = PROJECT_ROOT / "extracted"

LOGS_DIR = PROJECT_ROOT / "logs"
FETCH_LOG = LOGS_DIR / "fetch.log"
ERROR_LOG = LOGS_DIR / "errors.log"


# ---- Defaults -----------------------------------------------------------

SOURCE_URL = "https://www.war.gov/UFO/"
USER_AGENT = "war-gov-uap-archive/0.1 (+local archive; courteous fetcher)"
REQUEST_DELAY_SECONDS = 2.0
REQUEST_TIMEOUT_SECONDS = 30


# ---- Time helpers -------------------------------------------------------

def now_iso() -> str:
    """ISO-8601 UTC timestamp with 'Z' suffix."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today_str() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


# ---- ID and slug --------------------------------------------------------

_SLUG_STRIP = re.compile(r"[^a-z0-9]+")


def slugify(text: str, max_len: int = 60) -> str:
    if not text:
        return "untitled"
    s = text.lower()
    s = _SLUG_STRIP.sub("-", s).strip("-")
    if len(s) > max_len:
        s = s[:max_len].rstrip("-")
    return s or "untitled"


def make_id(agency: str, seq: int, title: str) -> str:
    return f"{slugify(agency, 20)}-{seq:03d}-{slugify(title)}"


# ---- Agency inference ---------------------------------------------------

# Heuristic mapping. Refine after seeing the actual page.
AGENCY_KEYWORDS = {
    "fbi": "FBI",
    "federal bureau of investigation": "FBI",
    "dod": "DoD",
    "department of defense": "DoD",
    "department of war": "DoW",
    "nasa": "NASA",
    "state department": "State",
    "department of state": "State",
    "usaf": "USAF",
    "air force": "USAF",
    "navy": "USN",
    "army": "USA",
    "department of energy": "DoE",
    "doe": "DoE",
    "energy": "DoE",
    "director of national intelligence": "ODNI",
    "national intelligence": "ODNI",
    "odni": "ODNI",
    "central intelligence agency": "CIA",
    "cia": "CIA",
    "nsa": "NSA",
    # Release 03 introduced two more author labels:
    "intelligence community agency": "ICA",
    "u.s. government": "USG",
    "us government": "USG",
    # Release 05:
    "executive office of the president": "EOP",
    # Release 06:
    "local law enforcement": "LLE",
}


def infer_agency(text: str) -> str:
    if not text:
        return "unknown"
    lo = text.lower()
    for kw, label in AGENCY_KEYWORDS.items():
        if kw in lo:
            return label
    return "unknown"


# ---- Type inference -----------------------------------------------------

PDF_EXTS = {".pdf"}
VIDEO_EXTS = {".mp4", ".mov", ".avi", ".webm", ".mkv", ".m4v"}
IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".gif", ".tif", ".tiff", ".webp"}
AUDIO_EXTS = {".mp3", ".wav", ".m4a", ".aac", ".ogg", ".flac"}


def file_type_for_url(url: str) -> str | None:
    path = urlparse(url).path.lower()
    ext = Path(path).suffix
    if ext in PDF_EXTS:
        return "pdf"
    if ext in VIDEO_EXTS:
        return "video"
    if ext in IMAGE_EXTS:
        return "image"
    if ext in AUDIO_EXTS:
        return "audio"
    return None


def dest_dir_for_type(file_type: str) -> Path:
    return {"pdf": PDF_DIR, "video": VIDEO_DIR,
            "image": IMAGE_DIR, "audio": AUDIO_DIR}[file_type]


# ---- JSON I/O -----------------------------------------------------------

def load_json(path: Path, default: Any = None) -> Any:
    if not path.exists():
        return default
    # utf-8-sig transparently strips a leading BOM if present and is
    # otherwise identical to utf-8. Some prior manifest writes (and any
    # CSV files saved via PowerShell) include a BOM.
    return json.loads(path.read_text(encoding="utf-8-sig"))


def save_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(data, indent=2, ensure_ascii=False, sort_keys=False) + "\n",
        encoding="utf-8",
    )


# ---- Logging ------------------------------------------------------------

def log_line(path: Path, line: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as fp:
        fp.write(f"{now_iso()}\t{line}\n")


# ---- HTTP (war.gov is fronted by Akamai; plain `requests` is 403'd
# because Akamai fingerprints the TLS client hello. curl_cffi impersonates
# a real Chrome TLS handshake, which passes. DVIDS and other hosts work
# fine with plain requests, so we only swap clients per-host.) ------------

WAR_GOV_HOSTS = {"www.war.gov", "war.gov"}


def needs_tls_impersonation(url: str) -> bool:
    return urlparse(url).hostname in WAR_GOV_HOSTS


def http_get(url, *, stream=False, timeout=REQUEST_TIMEOUT_SECONDS,
             headers=None, allow_redirects=True):
    """Single entry point. Routes war.gov through curl_cffi (Chrome impersonation),
    everything else through plain `requests`. Returns a response object with
    .status_code, .headers, .content / .iter_content / .raise_for_status.
    """
    hdrs = {"User-Agent": USER_AGENT}
    if headers:
        hdrs.update(headers)
    if needs_tls_impersonation(url):
        from curl_cffi import requests as cf  # local import: optional dep
        # curl_cffi's API matches requests closely. Force a Chrome impersonation
        # and add a Referer to look like a normal page navigation.
        hdrs.setdefault("Referer", "https://www.war.gov/UFO/")
        hdrs["User-Agent"] = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                              "AppleWebKit/537.36 (KHTML, like Gecko) "
                              "Chrome/130.0.0.0 Safari/537.36")
        return cf.get(url, headers=hdrs, timeout=timeout, stream=stream,
                      impersonate="chrome", allow_redirects=allow_redirects)
    import requests as rq
    return rq.get(url, headers=hdrs, timeout=timeout, stream=stream,
                  allow_redirects=allow_redirects)
