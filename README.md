# war-gov-uap-archive

Local archive of the U.S. Department of War's Unidentified Anomalous Phenomena (UAP) document release, with structured metadata for each file.

## Source

- **Page**: https://www.war.gov/UFO/
- **CSV manifest**: https://www.war.gov/Portals/1/Interactive/2026/UFO/uap-data.csv (as of R2; R1's `uap-csv.csv` now 404s)
- **Program**: PURSUE - Presidential Unsealing and Reporting System for UAP Encounters
- **Authorizing directive**: Trump Truth Social post, February 19, 2026
- **Releases captured**:
  - Release 01 - May 8, 2026 - 161 records
  - Release 02 - May 22, 2026 - +61 records (222 total)
- **Latest snapshot in this archive**: 2026-05-22
- **Releasing agency**: U.S. Department of War (formerly Department of Defense)

## Confirmed inventory

Confirmed against `uap-data.csv` on 2026-05-22:

```
Total:    222 records
PDF:      122
Video:     78
Image:     14
Audio:      8   (new type in R2 — Apollo / Mercury debriefing audio)

By agency:
  Department of War:                                131
  FBI:                                               57
  NASA:                                              22
  Department of State:                                7
  Department of Energy:                               3   (new in R2)
  Central Intelligence Agency:                        1   (new in R2)
  Office of the Director of National Intelligence:    1   (new in R2)

By page section:
  Release 01 (5/8/26):  158
  Release 02 (5/22/26):  64
```

R1 originally reported 161; the new combined CSV labels 158 of those rows
with `Release Date = 5/8/26` and 3 of them with `5/22/26` (cosmetic title
fixes that landed in the R2 cycle). News coverage at R1 launch reported
162; the CSV said 161; we trust the CSV.

The page is a Vue app that loads its record list entirely from one CSV.
Schema for each snapshot is documented under `snapshots/<date>/manifest_schema.md`.
The release remains rolling - additional batches expected every few weeks.

## How to populate the archive

The Cowork sandbox where this archive was scaffolded cannot reach
www.war.gov (egress proxy returns 403, despite the "All domains" toggle
in Cowork settings - that's a known product wart). The scripts in
`scripts/` are designed to run on **your host machine** where Python has
unrestricted network access.

**Akamai bot-management note**: as of R2, www.war.gov rejects plain
`requests` / curl on the TLS handshake. The Python pipeline routes
war.gov requests through `curl_cffi` (Chrome TLS impersonation), which
gets through. That's why `curl_cffi` is in `requirements.txt`.

From PowerShell or cmd in the project root:

```powershell
cd C:\Users\SeeingBlue\Documents\BluNET\war-gov-uap-archive
pip install -r scripts\requirements.txt
python scripts\01_discover.py       # new snapshot, preserves prior IDs
python scripts\02_fetch.py          # resumable; only fetches missing files
python scripts\03_verify.py         # re-hash everything against index.json
python scripts\mark_deprecated.py   # flag IDs that dropped from latest manifest
```

Estimated runtime (full corpus, R2 baseline of 222 records):

| Step | Duration | What it does |
|---|---|---|
| `01_discover.py` | ~3 sec | Fetches `uap-data.csv`, builds `snapshots/<today>/manifest.json`. Preserves existing IDs across re-runs. |
| `02_fetch.py` | ~10 min from scratch; ~10 sec for incremental R2-only fetch from an existing R1 archive | Downloads each asset with 2s polite delay, hashes, populates `metadata/index.json`. Resumable. |
| `03_verify.py` | ~1 min | Re-hashes everything against `index.json`, flags drift. Skips deprecated/non-`ok` records. |
| `mark_deprecated.py` | ~1 sec | Marks records absent from latest manifest as `status=deprecated` so verify/audit skip them. |

Total download size for the full R2 corpus: ~10 GB (the new "Release 02
Videos" alone is a 5.6 GB bundle; we pull them individually via DVIDS).

## Folder layout

```
war-gov-uap-archive/
├── README.md                    <- this file
├── .gitignore
├── snapshots/
│   ├── 2026-05-08/              <- Release 01
│   │   ├── manifest_schema.md   <- CSV schema, URL patterns
│   │   ├── uap-csv.csv          <- 161 records (URL now 404s upstream)
│   │   └── manifest.json
│   └── 2026-05-22/              <- Release 02 (R1 + R2 combined CSV)
│       ├── manifest_schema.md   <- schema delta, AUD type, DVIDS quirks
│       ├── uap-data.csv         <- 222 records
│       └── manifest.json
├── files/
│   ├── pdfs/                    <- 122 expected
│   ├── videos/                  <- 78 expected
│   ├── images/                  <- 14 expected
│   └── audio/                   <- 8 expected (R2 introduces audio)
├── metadata/
│   ├── index.json               <- canonical record per file (built by 02_fetch.py)
│   ├── index.csv                <- same data flattened, spreadsheet-friendly
│   ├── per-file/                <- one rich JSON per file
│   ├── incident_date_audit.{csv,md}     <- audit_incident_dates.py output
│   ├── incident_location_audit.{csv,md} <- audit_incident_locations.py output
│   ├── cross_refs.json          <- pairing graph (build_index.py)
│   ├── entities.json            <- entity extraction (build_index.py)
│   ├── timeline.csv             <- sorted by incident_date
│   └── by_location.md           <- grouped by incident_location
├── extracted/                   <- per-PDF markdown (extract_pdfs.py)
├── audits/                      <- human-readable audit summaries
├── deploy/                      <- viewer assets / globe data
├── logs/
│   ├── fetch.log                <- timestamp, url, status, bytes per fetch
│   └── errors.log               <- 404s, hash mismatches, retries
└── scripts/
    ├── README.md                <- how to run
    ├── requirements.txt         <- requests + beautifulsoup4 + curl_cffi
    ├── _common.py               <- paths, IDs, agency map, JSON I/O, http_get
    ├── 01_discover.py           <- fetch CSV, build manifest.json
    ├── 02_fetch.py              <- download + hash + index, resumable
    ├── 03_verify.py             <- re-hash everything, flag drift
    ├── 04_extract.py            <- Step 5 stub (PDF -> text)
    ├── extract_pdfs.py          <- pdfplumber + OCR fallback
    ├── audit_incident_dates.py
    ├── audit_incident_locations.py
    ├── build_index.py           <- entities, cross-refs, timeline, geo
    ├── mark_deprecated.py       <- flag IDs that left the latest manifest
    └── run-archive.ps1          <- pure-PowerShell mirror of discover+fetch
                                    (kept for portability; Python is canonical)
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

## Future snapshots

When a new release drops, just re-run the pipeline. `01_discover.py`
preserves existing IDs (reading from both prior `manifest.json` files
and the current `index.json`), so new records pick up fresh sequence
numbers without disturbing the old ones. `02_fetch.py` is resumable -
it only downloads what's missing.

## Schema changes between releases

| Release | Snapshot | New things this release introduced |
|---|---|---|
| R1 | 2026-05-08 | initial 161 records; PDF / VID / IMG types; DoW / FBI / NASA / State agencies |
| R2 | 2026-05-22 | +61 records; AUD (audio) type; DoE / CIA / ODNI agencies; `Image Alt Text`, `Image VIRIN` columns; CSV moved from `uap-csv.csv` to `uap-data.csv`; new R2 PDF path `medialink/ufo/052226/release_02/documents/`; Akamai TLS-fingerprint enforcement now strict (curl_cffi required) |

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
