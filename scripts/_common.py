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
    "doe": "DoE",
    "energy": "DoE",
    "cia": "CIA",
    "nsa": "NSA",
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


def file_type_for_url(url: str) -> str | None:
    path = urlparse(url).path.lower()
    ext = Path(path).suffix
    if ext in PDF_EXTS:
        return "pdf"
    if ext in VIDEO_EXTS:
        return "video"
    if ext in IMAGE_EXTS:
        return "image"
    return None


def dest_dir_for_type(file_type: str) -> Path:
    return {"pdf": PDF_DIR, "video": VIDEO_DIR, "image": IMAGE_DIR}[file_type]


# ---- JSON I/O -----------------------------------------------------------

def load_json(path: Path, default: Any = None) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


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
