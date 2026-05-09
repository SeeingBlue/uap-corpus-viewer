# scripts

Reproducible pipeline for the war.gov UFO archive. Designed to run on a host machine (where there's no egress restriction), not the Cowork sandbox.

## Setup

```bash
pip install -r requirements.txt
```

## Pipeline

```bash
# 1. Fetch the page, save HTML, extract asset URLs + page-level metadata
python 01_discover.py

# 2. Download all assets, hash, populate metadata. Resumable — re-run anytime.
python 02_fetch.py

# 3. Re-hash everything against index.json. Catches corruption / drift.
python 03_verify.py

# 4. (Deferred — Step 5) Extract text from PDFs into ../extracted/<id>.md
python 04_extract.py
```

All scripts read/write paths relative to the project root (the parent of this folder). Run them from `scripts/` or from the project root — they'll find the right files either way.

## Configuration

Edit the constants at the top of each script if you need to override defaults:

- `SOURCE_URL` — the page to crawl (default: `https://www.war.gov/UFO/`)
- `SNAPSHOT_DATE` — date subfolder under `snapshots/` (default: today)
- `REQUEST_DELAY_SECONDS` — polite delay between requests in `02_fetch.py` (default: 2.0)
- `USER_AGENT` — set to identify the archiver politely

## What each script writes

| Script | Reads | Writes |
|---|---|---|
| 01_discover.py | live page | `snapshots/<date>/page.html`, `snapshots/<date>/manifest.json` |
| 02_fetch.py | latest `manifest.json` | `files/<type>/<id>.<ext>`, updates `metadata/index.json`, `logs/fetch.log`, `logs/errors.log` |
| 03_verify.py | `metadata/index.json` + `files/` | report to stdout, optional update to `index.json` |
| 04_extract.py | `files/pdfs/` | `extracted/<id>.md` |
