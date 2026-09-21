# CSV manifest schema (war.gov/UFO/ - Release 06 - 2026-09-18)

Release 06 arrives through the same combined CSV (`uap-data.csv`). It is a
superset: every R1-R5 record is still present, plus 72 new records dated
`9/18/26` - the largest drop since R3 and tied with it. **No new
columns**, but one new agency (LLE) and yet another asset-path
convention.

## What's different from 2026-08-07 (R5)

| Aspect | Release 05 | Release 06 (2026-09-18) |
|---|---|---|
| CSV size | ~473 KB / 375 records | ~646 KB / 447 records |
| New columns | none | none (header byte-identical to R5) |
| New agencies | EOP (1 record) | **LLE** (Local Law Enforcement), 5 records |
| PDF path | `medialink/ufo/release_05/Aug_07/documents/` | `medialink/ufo/sept-18/release-06/assets/` - month-name date first again, hyphenated release, `assets/` instead of `documents/` |
| Thumbnail path | `.../Aug_07/thumbnails/` | `.../release-06/thumbs/` |
| Filename style | `<DOC-ID>_<Hyphen-Cased-Title>_<year>.pdf` | `<DOC-ID>_<Hyphen-Cased-Title-With-Date>.pdf` (date folded into the title slug, no trailing `_<year>`) |
| Composition | DoW 19 / FBI 17; 22 PDF, 16 VID, 3 IMG | DoW 67 / LLE 5; **56 PDF**, 15 VID, 1 AUD, 0 IMG - the most document-heavy drop yet |
| Geography | Gulf of Oman + Pacific + CONUS FBI | Las Vegas, Nevada (37 - the AAWSAP DIRDs), Washington D.C. (7), Colorado (5), Yellow Sea (5), Middle East / Iraq (9), Tremonton Utah (3), Boston (2) |
| Featured | 9 (R5 records) | 10 (R6 records) - flag rotated off R5 |
| `Featured` values | `YES` / `Yes` | `YES` only |
| Redaction | mixed | 65 of 72 `TRUE` (90%) |

## CSV URL

```
https://www.war.gov/Portals/1/Interactive/2026/UFO/uap-data.csv
```

646,408 bytes / 447 records as of 2026-09-18. Column header is
byte-identical to R4 and R5 (see `../2026-07-10/manifest_schema.md`).

## Release 06 URL patterns

```
PDF (R6):      https://www.war.gov/medialink/ufo/sept-18/release-06/assets/<ID>_<Title-With-Date>.pdf
Thumbnail:     https://www.war.gov/medialink/ufo/sept-18/release-06/thumbs/<ID>_<Title-With-Date>.jpg
```

Third path convention in three releases (R4 `ufo/071026/release_04/documents/`,
R5 `ufo/release_05/Aug_07/documents/`, R6 `ufo/sept-18/release-06/assets/`).
As before the CSV carries the full URL, so no code change is needed.

Videos and audio resolve through DVIDS via the `video:` endpoint, same as
R2-R5 (the single AUD record, PR160, is an audio-only mp4 like the NASA
debriefs). 56 of the 72 records carry a direct URL; the other 16 are
DVIDS ids in the 1023396-1023416 range.

### Spaces inside four asset URLs

Four R6 `PDF | Image Link` values contain a literal space (upstream
typo - `DOW-UAP-D114_...May-18- 2010.pdf`, `D124_...DIRD-Space Access-...`,
`D132_...Vacuum-Spacetime Metric-...`, `D135_ AAWSAP-DIRD-...`). curl_cffi
percent-encodes them on the wire and war.gov serves the files, so
`02_fetch.py` needed no change; the raw string is preserved in
`source_url` for provenance.

## Pipeline changes this release

Three edits in `scripts/01_discover.py` (plus the usual mirror in
`_common.py`):

1. `RELEASE_SECTIONS["9/18/26"] = "Release 06"`.
2. `normalize_agency()` gained `("local law enforcement", "LLE")`.
   Upstream's own ids are `LLE-UAP-D001` / `LLE-UAP-PR001..004`; without
   the entry the label falls through to the raw string and `make_id()`
   mints `local-law-enforcemen-001-*`.
3. `fld()` now expands the typographic ligatures U+FB01 `ﬁ` and U+FB02
   `ﬂ` to `fi` / `fl`. They appear (9 occurrences) in four MISREP
   summaries, pasted straight out of PDF text; they render fine but
   defeat plain-text search. Titles are unaffected, so no ID is.

`release_patterns.py` gained the `R6` tuple and a few CONUS region
keywords (Utah, Las Vegas, Massachusetts, Boston). `update_deploy.py`
gained the `Release 06` → `R6` mapping, the R6 `NEW_LOCATION_COORDS`
block (Las Vegas / Nevada, Tremonton, Boston, Washington D.C., Iraq) and
an updated header.

`02_fetch.py` also got a fix that R6 exposed: `merge_record()` used to
overwrite `source_url` with the manifest value on every run, and for
DVIDS-resolved clips the manifest value is empty. Each release's fetch
therefore blanked the resolved mp4 URL of every clip from earlier
releases in `index.json` (the per-file JSONs kept theirs). The merge now
keeps an existing resolved URL, and already-fetched clips with none are
re-resolved through the DVIDS API (metadata only, no re-download).

## New agency: LLE

`Local Law Enforcement` is the first non-federal author label in the
corpus. All five records are one submission: a local law enforcement
officer in Colorado reported a "silent" object with "red, blue, and
green flashing lights" to AARO with four clips of rear-facing cell-phone
footage (PR001-PR004, October 2023 / January 2024, bottom half blurred
by AARO) and a narrated transcript (D001, paired with PR004). It joins
the R3/R5 Colorado Springs thread.

## What R6 contains (72 records)

- **AAWSAP (44 PDF)**: the contract file of the Defense Intelligence
  Agency's Advanced Aerospace Weapon System Applications Program
  (contract HHM402-08-C-0072, awarded 22 Sep 2008; the CSV summaries
  describe the program as active 2008-2012, the records themselves run to
  a December 2010 extension). Seven administrative records located
  `Washington, D.C.`
  - the July 2008 Statement of Objectives (D110), the September 2008
  solicitation and original order to Bigelow Aerospace Advanced Space
  Studies (D111), and contract modifications P00001-P00005 (D112-D116)
  - plus 37 Defense Intelligence Reference Documents (DIRDs, D117-D153,
  December 2009 - January 2011) all located `Las Vegas, Nevada`, the
  contractor's home. Topics run from metallic glasses, spintronics and
  metamaterials through antigravity, warp drive / dark energy,
  traversable wormholes, negative-mass propulsion and quantum-vacuum
  energy to biosensors, high-energy lasers, hypersonic tracking and
  cognitive limits on multi-spacecraft control. D110 and D111 each
  carry a 43-way `PDF Pairing` to the rest of the set.
- **Tremonton 1952 + Ruppelt (7)**: Project Blue Book's file (D102) and
  photo file (D103) on the Newhouse film, the film itself as a DVIDS
  clip (PR159), Newhouse's 1957 Navy personnel record (D104), the USAF
  "Flying Discs" file for late 1952 (D105), and the 1952 Ruppelt
  presentation as transcript (D154) and audio (PR160, Boston). D102
  pairs backwards to R5's 1953 Navy film analysis (dow-176), whose
  `Video Pairing` was updated upstream to point at PR159.
- **CENTCOM (10)**: four MISREPs (D106-D109; Iraq 2022, Middle East
  2025 x2, Middle East/Iraq 2022), two Iraq 2022 "Unresolved UAP
  Report" PDFs (PR130, PR131) and four clips (PR133, PR135, PR140,
  PR141) paired to the MISREPs.
- **Indo-Pacific (6)**: Yellow Sea / East China Sea 2023 clips
  (PR143, PR144, PR148, PR150-PR152), continuing R4's maritime thread.
- **Colorado LLE cluster (5)**: above.

## The "Featured" flag rotates (unchanged behaviour)

`Featured` moved off R5's 9 records onto 10 R6 records (the Tremonton
Blue Book file and the film itself, the two AAWSAP framing documents,
two DIRDs, the Ruppelt transcript and audio, and two LLE clips). Each release's featured-at-launch count is preserved in its
own `snapshots/<date>/manifest.json`; `release_patterns.py` reads from
those, so the cross-release profile shows R3=10, R4=10, R5=9, R6=10.

## Upstream edits to prior records

Besides the Featured rotation, exactly one prior record changed:
`DOW-UAP-D098` (R5, dow-176) gained `Video Pairing = DOW-UAP-PR159` and
`PDF Pairing = D103 | D104 | D105` - a cross-release pairing into R6.
The PR057a/PR057b DVIDS-id collision from R3 is unchanged and still
handled positionally.

## Upstream data quirks inside R6 (not fixed - recorded as released)

- `DOW-UAP-D109`'s `Description Blurb` is a copy of `D108`'s (six
  spherical objects, 480 mph, July 2025). The D109 document itself is a
  5 May 2022 Iraq MISREP reporting objects at 80-180 mph, 1-2 m across;
  its paired clips PR140/PR141 quote the correct numbers.
- `LLE-UAP-PR004`'s summary says the footage is from "January 2024"
  while its title, `Incident Date` and the paired transcript say October
  2023. `DOW-UAP-PR133`'s summary says "2024" against a 2025 title and
  MISREP.
- `DOW-UAP-PR140` has an empty `Incident Date` and `Incident Location`
  despite its "Middle East, 2022" title (the only R6 row with either
  field blank). `D109` is titled "Middle East, 2022" but located `Iraq`.
- Two redaction conventions in one release: the 2022 CENTCOM MISREPs
  carry E.O. 13526 category codes (`1.4a`, `1.4g`) and a "USCENTCOM MDR
  26-0084 to 26-0095 - Approved for Release to AARO" footer, while the
  2025 ones and the LLE transcript use FOIA-style `(b)(1)(B)` /
  `(b)(6)` / `(b)(7)(A)`. The 2025 MISREP form has a dedicated "UAP"
  block (event type, maneuverability, physical state, "Under Intelligent
  Control") that the 2022 form lacks.

## ID stability check (R5 -> R6 re-discover)

0 duplicate ids, 0 existing ids dropped, 72 brand-new ids (all Release
06), 0 records changed release section. The 5 deprecated R1 records stay
deprecated. `mark_deprecated.py` reported no changes.

Post-fetch: `02_fetch.py` fetched=72 skipped=375 failed=0
url_backfilled=118 (the DVIDS-URL repair described above); R6 adds 3.3 GB,
mostly the 15 clips. `03_verify.py` ok=447 drift=0 missing=0.
`extract_pdfs.py` processed=56 (53 text-layer, 3 OCR, 0 failed) - the OCR
cases are the two single-frame IR stills (PR130, PR131, no text to find)
and the LLE transcript (clean). `audit_incident_dates.py`: R6 71
confirmed / 1 single-source. `audit_incident_locations.py`: 31 confirmed,
31 "disagree" - the DIRD bodies name many places, so the audit declines to
confirm the CSV's contract-address location and the viewer falls back to
the CSV value for geocoding (build_coords now does this fallback
explicitly; the Ruppelt transcript, audit-placed at Oak Ridge, TN, also
gained a dictionary entry). `release_patterns.py`: R6 n=72 redacted=65
featured=10; emergent vocabulary is just the LLE agency (a "tic-tac" shape
hit turned out to be "tic-tac-toe" in a DIRD on DNA computing and is now
excluded by the scanner). `update_deploy.py`: 447 records, 1309 edges (the
AAWSAP 43-way pairings), 388 geocoded.
