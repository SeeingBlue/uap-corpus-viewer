# CSV manifest schema (war.gov/UFO/ - Release 04 - 2026-07-10)

Release 04 arrives through the same combined CSV (`uap-data.csv`). It is a
superset: every R1-R3 record is still present, plus 40 new records dated
`7/10/26`. **No schema changes** this drop - no new columns, no new
agencies. The pipeline change was a single `RELEASE_SECTIONS` entry.

## What's different from 2026-06-12 (R3)

| Aspect | Release 03 | Release 04 (2026-07-10) |
|---|---|---|
| CSV size | ~366 KB / 294 records | ~417 KB / 334 records |
| New columns | `Featured` | none |
| New agencies | ICA, USG | none (DoW, NASA, CIA, DoE, FBI - all existing) |
| PDF/IMG path | `medialink/ufo/061226/release_03/documents/` | `medialink/ufo/071026/release_04/documents/` |
| Composition | FBI+CIA, document/still heavy | DoW-heavy (28) + video-heavy (19 clips) |
| Geography | CONUS homeland | maritime / Indo-Pacific + US coastal |
| Featured | 10 (R3 records) | 10 (R4 records) - flag rotated off R3 |

## CSV URL

```
https://www.war.gov/Portals/1/Interactive/2026/UFO/uap-data.csv
```

416,714 bytes / 334 records as of 2026-07-10. Columns identical to R3
(see `../2026-06-12/manifest_schema.md`).

## Release 04 URL patterns

```
PDF/IMG (R4):  https://www.war.gov/medialink/ufo/071026/release_04/documents/<CamelCase_Title>.pdf|.jpg
Thumbnail:     https://www.war.gov/medialink/ufo/071026/release_04/thumbnails/<CamelCase_Title>.jpg
```

Videos and audio resolve through DVIDS via the `video:` endpoint, same as
R2/R3.

## What R4 contains (40 records)

- **DoW (28)**: 19 Navy "Unresolved UAP Report" video clips concentrated
  in a new maritime / Indo-Pacific + US-coastal theatre (Yellow Sea,
  East & South China Sea, Atlantic Ocean, Eastern US, Gulf of America),
  plus Range-Fouler debriefs, **and** a batch of late-1940s foundational
  USAF documents - Project Sign Progress Report (1948), analyses of flying
  object incidents, joint US-Canadian aviation correspondence.
- **NASA (7)**: Apollo 14 (1971) and Apollo 17 crew medical debriefings,
  and three STS-80 Space Shuttle *Columbia* unidentified-object images
  from 1996 - extending the space-observation record to the Shuttle era.
- **DoE (2)**: transcript of a 1949 Los Alamos scientific conference on
  aerial phenomena, and a PANTEX unidentified-object incident report.
- **CIA (2)**: 1950s Cold-War memoranda on "unconventional aircraft"
  (incl. a 1955 debrief of a group that reportedly included a U.S.
  Senator).
- **FBI (1)**: UFO-related correspondence.

## The "Featured" flag rotates

`Featured=YES` marks the page's *current* hero cards, so it moved off the
10 R3 records and onto 10 R4 records. Because `02_fetch.py` refreshes
per-record metadata from the latest CSV, `metadata/index.json` shows only
R4 as featured now. Each release's *featured-at-launch* is preserved in
its own `snapshots/<date>/manifest.json`; `scripts/release_patterns.py`
reads featured per-release from those manifests so the cross-release
profile correctly shows R3=10 and R4=10.

## ID stability check (R3 -> R4 re-discover)

0 duplicate ids, 0 non-deprecated existing ids dropped, 40 brand-new ids
(all Release 04). The 5 deprecated R1 records stay deprecated.
