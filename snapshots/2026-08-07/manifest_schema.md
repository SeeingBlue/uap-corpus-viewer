# CSV manifest schema (war.gov/UFO/ - Release 05 - 2026-08-07)

Release 05 arrives through the same combined CSV (`uap-data.csv`). It is a
superset: every R1-R4 record is still present, plus 41 new records dated
`8/7/26`. **No new columns**, but one new agency (EOP) and a changed
asset-path convention.

## What's different from 2026-07-10 (R4)

| Aspect | Release 04 | Release 05 (2026-08-07) |
|---|---|---|
| CSV size | ~417 KB / 334 records | ~473 KB / 375 records |
| New columns | none | none (header byte-identical to R4) |
| New agencies | none | **EOP** (Executive Office of the President), 1 record |
| PDF/IMG path | `medialink/ufo/071026/release_04/documents/` | `medialink/ufo/release_05/Aug_07/documents/` - **path shape inverted** |
| Filename style | `<CamelCase_Title>.pdf` | `<DOC-ID>_<Hyphen-Cased-Title>_<year>.pdf` |
| Composition | DoW-heavy (28) + video-heavy (19) | DoW 19 / FBI 17 near-parity; document-heavy (22 PDF, 16 VID, 3 IMG) |
| Geography | maritime / Indo-Pacific | Gulf of Oman + Pacific + CONUS FBI casework; Latin America returns |
| Featured | 10 (R4 records) | 9 (R5 records) - flag rotated off R4 |
| `Featured` values | `YES` | `YES` (5) **and** `Yes` (4) - mixed case |

## CSV URL

```
https://www.war.gov/Portals/1/Interactive/2026/UFO/uap-data.csv
```

472,945 bytes / 375 records as of 2026-08-07. Column header is
byte-identical to R4 (see `../2026-07-10/manifest_schema.md`), including
the same twelve trailing unnamed columns.

## Release 05 URL patterns

```
PDF/IMG (R5):  https://www.war.gov/medialink/ufo/release_05/Aug_07/documents/<ID>_<Title>_<year>.pdf|.jpg
Thumbnail:     https://www.war.gov/medialink/ufo/release_05/Aug_07/thumbnails/<ID>_<Title>_<year>.jpg
```

Two changes from R4, neither of which needs a code change (the CSV
carries the full URL):

1. The date and release segments swapped order - R4 was
   `ufo/071026/release_04/`, R5 is `ufo/release_05/Aug_07/`.
2. The date segment is now a month-name form (`Aug_07`) rather than
   `MMDDYY`.

Videos resolve through DVIDS via the `video:` endpoint, same as R2-R4.
25 of the 41 records carry a direct URL (22 PDF + 3 IMG); the other 16
are DVIDS videos.

## Pipeline changes this release

Two edits, both in `scripts/01_discover.py` (plus a mirror in `_common.py`):

1. `RELEASE_SECTIONS["8/7/26"] = "Release 05"`.
2. `normalize_agency()` gained `("executive office of the president",
   "EOP")`. Without it the label falls through to the raw CSV string and
   `make_id()` slugifies a 20-char truncation, minting ugly
   `executive-office-of-001-*` ids. Upstream's own document ids are
   `EOP-UAP-D001`, so `EOP` is the correct short tag.

`update_deploy.py` gained eleven `NEW_LOCATION_COORDS` entries for R5
geography (Gulf of Oman, Pacific Ocean, Caribbean Sea, Bahia/Brazil,
Afghanistan, Sweden, Puerto Rico, Montana, Utah, Northeastern U.S.), the
`Release 05` → `R5` mapping, and an updated header. `release_patterns.py`
gained the `R5` tuple.

## Mixed-case `Featured`

R5 is the first release to use both `YES` and `Yes` in the `Featured`
column (5 and 4 respectively). `01_discover.py` already normalized with
`.upper() == "YES"`, so all 9 are picked up correctly - but a stricter
comparison would silently have dropped 4 hero records.

## New whitespace codepoint

R5 introduces U+202F NARROW NO-BREAK SPACE (5 occurrences) alongside the
U+00A0 NBSP seen since R3. No code change was needed: `fld()` ends with
`" ".join(v.split())`, and Python's `str.split()` treats both as
whitespace. Full non-ASCII inventory across titles/summaries/locations is
otherwise ordinary typography (curly quotes, en/em dashes, ellipsis,
bullet, é/ü).

## What R5 contains (41 records)

- **DoW (19)**: a Gulf of Oman cluster - one Intelligence Information
  Report plus six clips, all from a single AC-130J gunship live-fire
  sortie on 8 Sep 2021; five Pacific Ocean 2019 Navy clips; four
  CENTCOM Middle East clips (2023, 2025); and three historical
  documents - the 1947 General Staff review of the Scandinavian "Ghost
  Rocket" wave, a 1947-48 Air Materiel Command / Project Sign file, and
  a 1953 Naval Photographic Interpretation Center analysis of the 1950
  Montana and 1952 Utah films.
- **FBI (17)**: eight FD-302 interview records, each paired with a
  digital rendering the Bureau commissioned in 2026 from the witness's
  description, plus one thermal video. Subjects skew triangular
  (Bagram AFB 2002, Colorado Springs 2023 ×2, an unlocated 2011 case)
  and Western US 2026.
- **CIA (2)**: the November 1964 Puerto Rico incident - AD/SA–AD/SI
  memoranda and briefing notes for Walter N. Elder, including an
  AN/SPS-49 radar track from USS Gyatt at 3,800 knots over 21 minutes.
- **State (2)**: US Embassy Rio de Janeiro cables of 14 and 20 Nov 1963
  on the Bahia, Brazil "crashed sphere" story - the second reporting it
  unsubstantiated.
- **EOP (1)**: a CIA FBIS wire report from the files of Edward C. Welsh,
  Executive Secretary of the National Aeronautics and Space Council,
  with handwritten annotations recording the NASC request that started
  the State cable chain above.

## The "Featured" flag rotates (unchanged behaviour)

As in R4, `Featured` marks the page's *current* hero cards, so it moved
off R4's 10 records onto 9 R5 records. Each release's featured-at-launch
count is preserved in its own `snapshots/<date>/manifest.json`;
`release_patterns.py` reads from those, so the cross-release profile
correctly shows R3=10, R4=10, R5=9.

## ID stability check (R4 -> R5 re-discover)

0 duplicate ids, 0 existing ids dropped, 41 brand-new ids (all Release
05), 0 records changed release section. The 5 deprecated R1 records stay
deprecated. `mark_deprecated.py` reported no changes.

Post-fetch: `02_fetch.py` fetched=41 skipped=334 failed=0;
`03_verify.py` ok=375 drift=0 missing=0; `extract_pdfs.py` processed=22
(17 text-layer, 5 OCR, 0 failed).
