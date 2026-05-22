# CSV manifest schema (war.gov/UFO/ - Release 02 - 2026-05-22)

The page at https://www.war.gov/UFO/ is still a single-page Vue app, but
between Release 01 and Release 02 (2026-05-22) the manifest URL changed
and the CSV gained new columns, new agencies, and a new asset type. The
new CSV is a SUPERSET of Release 01: every R1 record is still present,
plus the new ones from R2.

## What's different from 2026-05-08

| Aspect | Release 01 (2026-05-08) | Release 02 (2026-05-22) |
|---|---|---|
| CSV URL | `uap-csv.csv` | `uap-data.csv` (single combined file) |
| CSV size | ~184 KB / 161 records | ~298 KB / 222 records |
| Agencies | DoW, FBI, NASA, State | + DoE, CIA, ODNI |
| Asset types | PDF, VID, IMG | + AUD |
| Extra columns | (none) | `Image Alt Text`, `Image VIRIN` |
| Akamai bot mgmt | already in place | unchanged; still blocks plain `requests` |
| Video bundle | `uapvideos.zip` (1.3 GB) | + `uap052226.zip` (5.6 GB, Release 02 videos) |

Three Release 01 records also had their `Title` cosmetically fixed and
their broken `PDF | Image Link` corrected. The corrected URLs resolve as
"new" records in the diff because the URL is the lookup key; see the
"Deprecated IDs" section below.

## CSV URL

```
https://www.war.gov/Portals/1/Interactive/2026/UFO/uap-data.csv
```

297,955 bytes / 222 records as of 2026-05-22.

The Release 01 URL (`uap-csv.csv` / `uap-release001.csv`) now 404s.

## Columns (in CSV order)

| # | Column                | Notes                                                                  |
|---|-----------------------|------------------------------------------------------------------------|
| 1 | `Redaction`           | Marker; non-empty -> page shows redaction notice on modal              |
| 2 | `Release Date`        | `5/8/26` or `5/22/26`. Maps to `page_section` in our manifest          |
| 3 | `Title`               | Asset filename (minus extension), as displayed                         |
| 4 | `Type`                | `V*` video, `I*` image, `A*` audio, anything else PDF                  |
| 5 | `Video Pairing`       | Cross-reference id                                                     |
| 6 | `PDF Pairing`         | Cross-reference id                                                     |
| 7 | `Description Blurb`   | Free-text summary shown in record modal                                |
| 8 | `DVIDS Video ID`      | Numeric id; resolved via api.dvidshub.net/asset                        |
| 9 | `Video Title`         | Display title for video records                                        |
|10 | `Agency`              | Free-text source agency                                                |
|11 | `Incident Date`       | Free-text date or `N/A`                                                |
|12 | `Incident Location`   | Free-text location or `N/A`                                            |
|13 | `PDF \| Image Link`   | Direct asset URL for non-video records                                 |
|14 | `Modal Image`         | Thumbnail URL shown in record-detail modal                             |
|15 | `Image Alt Text`      | **NEW** in R2. Accessibility alt text for the modal thumbnail          |
|16 | `Image VIRIN`         | **NEW** in R2. DoD's VIRIN identifier for the asset                    |

Same as R1, the header row has ~11 trailing empty columns (spreadsheet
export artifact). The script skips empty `Title` rows.

## Release 02 URL patterns

PDFs in R2 live under a new path scoped by the release-date digits:

```
PDF (R1):  https://www.war.gov/medialink/ufo/release_1/<lowercased_title>.pdf
PDF (R2):  https://www.war.gov/medialink/ufo/052226/release_02/documents/<CamelCase_Title>.pdf
```

R2 PDF filenames are CamelCase with underscores; R1 was lowercased
hyphen-or-underscore. Don't rewrite Title -> URL; trust the
`PDF | Image Link` column.

Videos and audio still resolve through DVIDS. **All DVIDS records,
including those the CSV labels `AUD`, use `id=video:<n>`** -- the DVIDS
public read key on the page is not authorized to query `id=audio:<n>` and
returns 403. The "AUD" records are audio-only mp4s on DVIDS; we resolve
them via the `video:` endpoint and prefer the smallest mp4 variant (no
real video content, so all qualities are equivalent).

## Counts (from the CSV)

```
Total:    222 records (+61 vs R1)
PDF:      122 (+3)
VID:       78 (+50)
IMG:       14 (+0)
AUD:        8 (new type)

By agency:
  Department of War:                                131  (+49)
  FBI:                                               57  (+0)
  NASA:                                              22  (+7)
  Department of State:                                7  (+0)
  Department of Energy:                               3  (new)
  Central Intelligence Agency:                        1  (new)
  Office of the Director of National Intelligence:    1  (new)

By release section:
  Release 01 (5/8/26):  158
  Release 02 (5/22/26):  64
```

## Akamai / TLS impersonation note

Both `www.war.gov/UFO/` and the CSV/CDN endpoints under
`www.war.gov/Portals/...` and `www.war.gov/medialink/...` sit behind
Akamai bot management. Plain `requests` is rejected at the TLS layer
(403 from Akamai's error.edgesuite.net redirect) regardless of headers.
The Python scripts route war.gov requests through `curl_cffi` with Chrome
TLS impersonation - see `_common.http_get` and the dependency in
`scripts/requirements.txt`. DVIDS endpoints don't need impersonation but
do require `Referer: https://www.war.gov/UFO/` and `Origin:
https://www.war.gov` headers, or they return 403 ("origin not associated
with your key").

## Deprecated IDs (carried over from R1)

The R1 CSV shipped three records with broken `PDF | Image Link` URLs.
The R2 CSV corrected them. The corrected URLs match no existing ID in
our prior snapshot, so they get new IDs in this snapshot. The old IDs
remain in `metadata/index.json` for audit traceability but are no longer
referenced from any manifest; their local files are stale.

| Old ID                                                            | What was wrong                          | New ID lives at |
|---|---|---|
| `dow-016-dow-uap-d20-mission-report-iraq-2023`                    | Title said Iraq; URL pointed to "Southern United States 2023" PDF      | New `dow-NNN-dow-uap-d020-...` |
| `state-002-59-64634-711-5612-7-2852`                              | URL pointed to `59_214434_sp_16_7.18.1963.pdf` (= state-001's file)    | New `state-008-...` |
| `dow-018-dow-uap-d23-mission-report-united-arab-emirates-october-2023` | Exact duplicate of `dow-017` (same URL, same sha256). De-duped in R2. | n/a - dropped |
| `dow-024-dow-uap-d32-mission-report-syria-october-2024`           | Exact duplicate of `dow-023`. De-duped in R2.                          | n/a - dropped |
| `dow-025-dow-uap-d32-mission-report-syria-october-2024`           | Exact duplicate of `dow-023`. De-duped in R2.                          | n/a - dropped |

The `fbi-010-...-serial-153` ID was preserved across the snapshot
boundary because `index.json` had a manual URL correction applied
earlier (recorded in the record's `notes` field). `01_discover.py` reads
`index.json` additively so corrected URLs route to existing IDs without
overwriting earlier mappings.

## Cloudfront video bundle

The page also exposes a single zip for bulk download:

```
Release 01 videos: https://d34w7g4gy10iej.cloudfront.net/uapvideos.zip   (1.3 GB)
Release 02 videos: https://d34w7g4gy10iej.cloudfront.net/uap052226.zip   (5.6 GB)
```

Our pipeline pulls individual files via DVIDS so the bundle is just a
faster bulk option for users who want everything at once.
