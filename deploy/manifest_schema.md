# CSV manifest schema (war.gov/UFO/ - Release 01 - 2026-05-08)

The page at https://www.war.gov/UFO/ is a single-page Vue app. Its entire
record list is loaded from one CSV at a known URL - nothing on the page
is server-rendered.

## CSV URL

```
https://www.war.gov/Portals/1/Interactive/2026/UFO/uap-csv.csv
```

184,203 bytes / 574 lines / 161 records as of 2026-05-08T15:24Z.

## Columns (in CSV order)

| # | Column                | Notes                                                       |
|---|-----------------------|-------------------------------------------------------------|
| 1 | `Redaction`           | Marker; non-empty -> page shows redaction notice on modal   |
| 2 | `Release Date`        | Format `M/D/YY`, e.g. `5/8/26`                              |
| 3 | `Title`               | Asset filename (minus extension), as displayed              |
| 4 | `Type`                | `V*` = video, `I*` = image, `P*`/anything else = PDF        |
| 5 | `Video Pairing`       | Cross-reference id; mostly empty in Release 01              |
| 6 | `PDF Pairing`         | Cross-reference id; mostly empty in Release 01              |
| 7 | `Description Blurb`   | Free-text summary shown in record modal                     |
| 8 | `DVIDS Video ID`      | Numeric id; resolved via api.dvidshub.net/asset             |
| 9 | `Video Title`         | Display title for video records                             |
|10 | `Agency`              | Free-text source agency                                     |
|11 | `Incident Date`       | Free-text date or `N/A`                                     |
|12 | `Incident Location`   | Free-text location or `N/A`                                 |
|13 | `PDF \| Image Link`   | Direct asset URL for non-video records                      |
|14 | `Modal Image`         | Thumbnail URL shown in record-detail modal                  |

The header row in the file has 14 named columns followed by 13 trailing
empty cells (artifact of the source spreadsheet). Column header
capitalization is inconsistent in the source CSV.

## Asset URL patterns

PDFs and images live under a single CDN path. Filename is the title,
lowercased, with spaces underscored:

```
PDF:        https://www.war.gov/medialink/ufo/release_1/<lowercased_title>.pdf
Thumbnail:  https://www.war.gov/medialink/ufo/release_1/thumbnail/<lowercased_title>.jpg
Image:      https://www.war.gov/medialink/ufo/release_1/<lowercased_title>.<ext>
```

Videos do not have a direct URL in the CSV. `DVIDS Video ID` is fetched
at runtime against the DVIDS API, which returns a `files[]` array of
mp4/webm variants. Highest-resolution mp4 wins.

```
DVIDS:  https://api.dvidshub.net/asset?api_key=<key>&id=video:<id>
```

The DVIDS API key is exposed in cleartext in the page's inline JS
(`key-68bb60d16b35e`). It's a public read key intended for rate-limiting
clients; safe to mirror in the fetch pipeline.

## Counts (from the CSV)

```
Total:    161 records
PDF:      119
Video:     28
Image:     14
```

News coverage at launch reported 162. The page itself, and the CSV row
count, both say 161. We trust the CSV.

```
By agency:
  Department of War:    82
  FBI:                  57
  NASA:                 15
  Department of State:   7
```

The CSV's `Agency` field is free-text. The `_common.py` agency
normalizer maps to short tags (`DoW`, `DoD`, `FBI`, `NASA`, `State`).
`agency_raw` in manifest.json preserves the original.

## Page framing

- Title: "Presidential Unsealing and Reporting System for UAP Encounters"
- Acronym: PURSUE
- Authorizing directive: Trump Truth Social post, Feb 19, 2026
- This batch labeled "Release 01 - Cleared for Release May 8, 2026"
- Statement attributed to Secretary of War Pete Hegseth
- Page promises "tranches every few weeks" - plan for rolling snapshots

## A second CSV referenced in source (do not fetch)

The page's source also contains a second component (`#release-table-app-2026`)
pointing to:

```
https://war.dod.afpims.mil/Portals/1/SANDBOXES/BEvans/testing-doc.csv
```

That URL is on a different host (`afpims.mil`), in a `SANDBOXES/BEvans/`
path that screams "internal staging artifact left in production". Not
the canonical manifest. Ignore.

## Sandbox vs host network access (this Cowork session)

The Cowork sandbox where these scripts were authored cannot reach
www.war.gov - the egress proxy returns 403 even with "All domains"
allowed in settings. The scripts in `../../scripts/` are designed to run
on the host machine where Python has unrestricted network access.
