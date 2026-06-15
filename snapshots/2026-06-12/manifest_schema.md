# CSV manifest schema (war.gov/UFO/ - Release 03 - 2026-06-12)

Release 03 is delivered through the same single combined CSV introduced in
R2 (`uap-data.csv`). It is a superset: every R1 + R2 record is still
present, plus 72 new records dated `6/12/26`.

## What's different from 2026-05-22 (R2)

| Aspect | Release 02 | Release 03 (2026-06-12) |
|---|---|---|
| CSV URL | `uap-data.csv` | `uap-data.csv` (unchanged) |
| CSV size | ~298 KB / 222 records | ~366 KB / 294 records |
| Agencies | + DoE, CIA, ODNI | + ICA (Intelligence Community Agency), USG (U.S. Government); CIA grows 1 -> 19 |
| New column | `Image Alt Text`, `Image VIRIN` | `Featured` (prepended; "YES" for 10 hero records) |
| PDF path | `medialink/ufo/052226/release_02/documents/` | `medialink/ufo/061226/release_03/documents/` |
| Title encoding | clean ASCII | UTF-8 non-breaking spaces (U+00A0) sprinkled through titles/summaries |
| Removed/dedup | 3 corrected, 2 deduped | none |

## CSV URL

```
https://www.war.gov/Portals/1/Interactive/2026/UFO/uap-data.csv
```

366,389 bytes / 294 records as of 2026-06-12.

## Columns (in CSV order)

R3 prepends a `Featured` column; the rest match R2.

| # | Column | Notes |
|---|---|---|
| 1 | `Featured` | **NEW.** `YES` for the ~10 records the page features; else empty. Stored as boolean `featured` in our manifest/index. |
| 2 | `Redaction` | Marker; `TRUE` -> redaction notice on modal |
| 3 | `Release Date` | `5/8/26`, `5/22/26`, or `6/12/26`. Maps to `page_section`. |
| 4 | `Title` | Asset filename-ish display title. **R3: contains U+00A0 non-breaking spaces** — normalized to regular spaces in `_discover.fld()`. |
| 5 | `Type` | `V*` video, `I*` image, `A*` audio, else PDF |
| 6 | `Video Pairing` | cross-ref id |
| 7 | `PDF Pairing` | cross-ref id |
| 8 | `Description Blurb` | summary |
| 9 | `DVIDS Video ID` | numeric; resolved via api.dvidshub.net |
| 10 | `Video Title` | display title for video/audio records |
| 11 | `Agency` | free-text source agency |
| 12 | `Incident Date` | free-text date or `N/A` |
| 13 | `Incident Location` | free-text location or `N/A` |
| 14 | `PDF \| Image Link` | direct asset URL for non-video/audio records |
| 15 | `Modal Image` | thumbnail URL |
| 16 | `Image Alt Text` | accessibility alt text |
| 17 | `Image VIRIN` | DoD VIRIN identifier |

## Release 03 URL patterns

PDFs and images (incl. FBI "digital rendering" stills) live under the new
release-dated path; filenames are CamelCase with underscores:

```
PDF/IMG (R3):  https://www.war.gov/medialink/ufo/061226/release_03/documents/<CamelCase_Title>.pdf|.jpg
Thumbnail:     https://www.war.gov/medialink/ufo/061226/release_03/thumbnails/<CamelCase_Title>.jpg
```

Videos and audio still resolve through DVIDS via the `video:` endpoint
(see the R2 schema note — `id=audio:` is not authorized for the public
read key, so AUD records resolve as `video:` too).

## New agencies

The CSV `Agency` field gained three new author strings in R3. Our
normalizer (`_common.AGENCY_KEYWORDS` and `01_discover.normalize_agency`)
maps them as:

| Raw `Agency` | Tag |
|---|---|
| `CIA` / `Central Intelligence Agency` | `CIA` |
| `Intelligence Community Agency` | `ICA` |
| `U.S. Government` | `USG` |

`intelligence community` is tested before `national intelligence` so ICA
does not get mis-tagged as ODNI.

## Counts (from the CSV)

```
Total:    294 records (+72 vs R2)
PDF:      175 (+53)
VID:       84 (+6)
IMG:       24 (+10)
AUD:       11 (+3)

By agency (R3 additions in parens):
  Department of War:                 143  (+12)
  FBI:                                86  (+29)
  NASA:                               33  (+11)
  CIA:                                19  (+18)
  Department of State:                 7
  Department of Energy:                3
  Office of the Director of NI:        1
  Intelligence Community Agency:       1  (new)
  U.S. Government:                     1  (new)

By release section:
  Release 01 (5/8/26):   158
  Release 02 (5/22/26):   64
  Release 03 (6/12/26):   72
```

## Quirks handled in the pipeline

1. **U+00A0 non-breaking spaces** in R3 titles/summaries. Valid UTF-8 but
   invisible; folded to regular spaces + whitespace-collapsed in `fld()`.
2. **Upstream title typo fix**: `DOW-UAP-PR053` changed "Sherical" ->
   "Spherical" between R2 and R3. A title-based identity key would have
   orphaned the record, so DVIDS-keyed records key on the DVIDS id alone.
3. **Shared DVIDS id**: `1007720` is used by two genuinely different clips
   (`DOW-UAP-PR057a` "Spherical UAP in clouds" and `PR057b` "[Platform]
   Observes UAP in East China Sea"). `01_discover.py` maps a DVIDS key to
   an *ordered list* of ids and consumes them positionally (CSV order is
   stable), so both keep distinct, stable ids across re-discovers.
4. **`Featured` flag**: 10 R3 records carry it. Captured as `featured`
   (boolean) through manifest -> index -> viewer.

## ID stability check (R2 -> R3 re-discover)

After adding R3: 0 duplicate ids, 0 non-deprecated existing ids dropped,
72 brand-new ids (all Release 03). The 5 deprecated R1 records stay
deprecated.
