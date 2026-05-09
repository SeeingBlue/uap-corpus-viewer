# war-gov-uap-archive

Local archive of the U.S. Department of War's Unidentified Anomalous Phenomena (UAP) document release, with structured metadata for each file.

## Source

- **Page**: https://www.war.gov/UFO/
- **CSV manifest**: https://www.war.gov/Portals/1/Interactive/2026/UFO/uap-csv.csv
- **Program**: PURSUE - Presidential Unsealing and Reporting System for UAP Encounters
- **Authorizing directive**: Trump Truth Social post, February 19, 2026
- **Initial release date**: May 8, 2026 ("Release 01")
- **Snapshot date for this archive**: 2026-05-08
- **Releasing agency**: U.S. Department of War (formerly Department of Defense)

## Confirmed inventory

Confirmed against the page's CSV manifest on 2026-05-08:

```
Total:    161 records
PDF:      119
Video:     28
Image:     14

By agency:
  Department of War:    82
  FBI:                  57
  NASA:                 15
  Department of State:   7
```

News coverage at launch reported 162; the page and CSV both say 161. We trust the CSV.

The page is a Vue app that loads its record list entirely from one CSV.
Schema documented in `snapshots/2026-05-08/manifest_schema.md`.
The release is described as rolling - additional batches expected every few weeks.

## How to populate the archive

The Cowork sandbox where this archive was scaffolded cannot reach
www.war.gov (egress proxy returns 403, despite the "All domains" toggle
in Cowork settings - that's a known product wart). The scripts in
`scripts/` are designed to run on **your host machine** where Python has
unrestricted network access.

From PowerShell or cmd in the project root:

```powershell
cd C:\Users\SeeingBlue\Documents\BluNET\war-gov-uap-archive
pip install -r scripts\requirements.txt
python scripts\01_discover.py
python scripts\02_fetch.py
python scripts\03_verify.py
```

Estimated runtime:

| Step | Duration | What it does |
|---|---|---|
| `01_discover.py` | ~2 sec | Fetches the CSV, parses 161 records, writes `snapshots/2026-05-08/uap-csv.csv` and `manifest.json` |
| `02_fetch.py` | ~6 min | Downloads each asset with 2s polite delay, hashes, populates `metadata/index.json`. Resumable - re-run anytime. |
| `03_verify.py` | ~30 sec | Re-hashes everything against `index.json`, flags drift |

Total download size estimate: hard to predict before fetch (typical declassified PDFs run 5-50 MB; videos can be 100+ MB), so probably 1-5 GB across the 161 files.

## Folder layout

```
war-gov-uap-archive/
├── README.md                    <- this file
├── .gitignore
├── snapshots/
│   └── 2026-05-08/
│       ├── manifest_schema.md   <- CSV schema, URL patterns, agency map
│       ├── uap-csv.csv          <- (created by 01_discover.py)
│       └── manifest.json        <- (created by 01_discover.py)
├── files/
│   ├── pdfs/                    <- 119 expected
│   ├── videos/                  <- 28 expected
│   └── images/                  <- 14 expected
├── metadata/
│   ├── index.json               <- canonical record per file (built by 02_fetch.py)
│   ├── index.csv                <- same data flattened, spreadsheet-friendly
│   └── per-file/                <- one rich JSON per file
├── extracted/                   <- Step 5 - PDF text (deferred)
├── logs/
│   ├── fetch.log                <- timestamp, url, status, bytes per fetch
│   └── errors.log               <- 404s, hash mismatches, retries
└── scripts/
    ├── README.md                <- how to run
    ├── requirements.txt         <- requests + beautifulsoup4
    ├── _common.py               <- paths, IDs, agency map, JSON I/O
    ├── 01_discover.py           <- fetch CSV, build manifest.json
    ├── 02_fetch.py              <- download + hash + index, resumable
    ├── 03_verify.py             <- re-hash everything, flag drift
    └── 04_extract.py            <- Step 5 stub (PDF -> text)
```

## Stable ID scheme

Each file gets an ID of the form `<agency>-<seq>-<slug>`:

- `agency` - lowercase short name (`fbi`, `dow`, `nasa`, `state`)
- `seq` - zero-padded sequence number scoped per-agency, in CSV order
- `slug` - slugified title

Example: `fbi-001-65-hs1-834228961-62-hq-83894-section-10`

The mapping `seq -> source URL` is recorded in `manifest.json` so the
scheme is reproducible across re-runs. If the page reorders records
between snapshots, IDs are stable per asset URL.

## Metadata schema (`metadata/index.json`)

`index.json` is the single source of truth for what's in the archive.
One record per file:

```json
{
  "id": "fbi-001-65-hs1-834228961-...",
  "type": "pdf",
  "title": "65_HS1-834228961_62-HQ-83894_Section_10",
  "agency": "FBI",
  "agency_raw": "FBI",
  "type_code": "PDF",
  "page_section": "Release 01",
  "release_date": "5/8/26",
  "incident_date": "N/A",
  "incident_location": "N/A",
  "summary": "The FBI's 62-HQ-83894 case file includes ...",
  "redaction": "",
  "video_pairing": "",
  "pdf_pairing": "",
  "video_title": "",
  "dvids_video_id": "",
  "modal_image_url": "https://www.war.gov/medialink/ufo/release_1/thumbnail/...jpg",
  "source_url": "https://www.war.gov/medialink/ufo/release_1/65_hs1-834228961_62-hq-83894_section_10.pdf",
  "discovered_on": "2026-05-08T...",
  "fetched_on": "2026-05-08T...",
  "local_path": "files/pdfs/fbi-001-...pdf",
  "bytes": 1234567,
  "sha256": "...",
  "http_status": 200,
  "content_type": "application/pdf",
  "etag": "...",
  "last_modified": "...",
  "extracted_text_path": null,
  "status": "ok",
  "notes": ""
}
```

`status` values: `ok`, `pending`, `missing` (404), `fetch_error`,
`incomplete`, `corrupted`, `skipped`.

## Resumability and verification

- `index.json` IS the run state. The fetcher reads it, skips files whose
  recorded sha256 matches their on-disk hash, and only fetches the rest.
- `scripts/03_verify.py` re-hashes everything against the index. Useful
  for catching silent corruption and for diffing across snapshot dates.
- `logs/fetch.log` is append-only; one line per fetch attempt for a
  tamper-evident audit trail.

## Provenance and licensing

- Files in this archive are U.S. federal government works released for
  public access via the PURSUE program; the Department of War states no
  security clearance is required to view them.
- This archive preserves the original files as released. It does not
  modify, redact, or re-encode them. SHA-256 hashes in `index.json` are
  recorded at fetch time so any later modification (intentional or
  accidental) is detectable.
- `snapshots/<date>/uap-csv.csv` is the verbatim manifest at fetch time.
  Future snapshots go under `snapshots/<new-date>/`.

## What's deferred

- **Step 5 - text extraction.** Once the corpus is on disk,
  `scripts/04_extract.py` will use the pdf skill to extract text and
  tables from each PDF into `extracted/<id>.md` for full-text search.
- **Future snapshots.** When Release 02 drops, run discovery into
  `snapshots/<new-date>/`. The fetcher will pick up only the new URLs.

## What was confirmed during reconnaissance

Using the Chrome MCP from the user's actual browser (the one path that
isn't blocked by the sandbox proxy):

1. The page loads cleanly at https://www.war.gov/UFO/
2. The page is driven entirely by `uap-csv.csv` - confirmed via reading
   the page's inline JS source
3. Record count: 161 (vs. 162 in news coverage)
4. Type breakdown and agency breakdown above
5. PDF/image URL pattern: `/medialink/ufo/release_1/<title>.pdf`
6. Videos resolve via DVIDS API (api.dvidshub.net), public read key
   exposed in page source
7. The scripts in `scripts/` were rewritten after this reconnaissance to
   fetch the CSV directly rather than scrape HTML - much cleaner

The CSV itself was loaded into the browser during reconnaissance but not
exfiltrated to disk because (a) the sandbox can't reach war.gov, and
(b) the Chrome MCP's tool-output budgets are too small to pipe a 184KB
file back through cleanly. Running `01_discover.py` from the host fixes
both - it fetches the CSV directly and writes it to
`snapshots/2026-05-08/uap-csv.csv`.
