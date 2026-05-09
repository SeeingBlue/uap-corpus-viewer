# Location Data Accuracy — Investigation Summary

**Inspected:** 161 reports
**Flagged for review:** 82 (HIGH 28 · MEDIUM 5 · LOW 49)

This is the human-curated summary. The full machine-generated audit is in [`location_audit.md`](location_audit.md) (every flag, every report) and [`location_audit.csv`](location_audit.csv) (sortable per-record flags).

---

## How the audit works

For each report I extracted three signals and compared them:

1. **Declared location** — the `Incident Location` column from the war.gov CSV (mirrored into each `.md`'s YAML frontmatter)
2. **Title-derived location** — place names parsed out of the report title (and by extension the source PDF filename, since titles are filename-derived)
3. **Body-derived location** — place names found in the description blurb and extracted body text via an 80+-pattern regex dictionary

Plus a sibling check across reports in the same case-file group (FBI 62-HQ-83894 sections, the DOW D-series, the DOW PR-series, etc).

A flag means the field looks suspicious. It does *not* automatically mean the data is wrong — some "mismatches" are deliberate CSV-modeling choices (a multi-incident file legitimately covering many locations) and some are precision differences (declared `Persian Gulf` is more accurate than title's `Middle East`).

---

## The headline finding

**There are at least 4 high-confidence CSV data errors and 1 likely date typo in the war.gov release.** These look like data-entry mistakes — the filename and title say one place, but the `Incident Location` field has been filled with something else.

### 🔴 Confirmed errors (location field doesn't match filename or title)

| ID | Filename / title says | Declared `Incident Location` | Verdict |
|---|---|---|---|
| **dow-034** (D5) | Arabian Gulf, 2020 | `Mediterranean Sea` | **Wrong** — should be Arabian Gulf |
| **dow-043** (D6) | Arabian Gulf, 2020 | `Pacific Ocean` | **Wrong** — should be Arabian Gulf |
| **dow-053** (D8) | Djibouti, 2025 | `Mediterranean Sea` | **Wrong** — Djibouti is on the Gulf of Aden, not Mediterranean |
| **dow-030** (D42) | Japan, 2023 | `Arabian Gulf` (date `8/31/20`) | **Wrong** — title and data disagree on both location AND year. Either the filename is mislabeled or the location/date fields are from a different report |

The pattern looks like row misalignment in the source spreadsheet — the location values for D5/D6/D8 read like they were accidentally pulled from neighbouring rows (other DoW reports in the archive *are* declared "Mediterranean Sea" or "Pacific Ocean" — D54, D55, D67, D68 etc).

### 🟠 Likely date typo

| ID | Title says | Declared `Incident Date` | Likely intended |
|---|---|---|---|
| **dow-036** (D51) | Pacific Time Zone, March 2023 | `3/23/26` | `3/23/23` — `26` matches the *release date* (5/8/26), suggesting a year-field copy-paste |

### 🟡 Less confident — title mentions a year inconsistent with the date

| ID | Title says | Declared date | Notes |
|---|---|---|---|
| **dow-020** (D27 UAE) | October 2023 | `6/7/24` | Could be report-filed-date vs incident-date confusion |
| **dow-030** (D42 Japan) | 2023 | `8/31/20` | Already flagged above; title year vs date year differ by 3 |

---

## CSV-modeling decisions (not errors, worth knowing)

### Multi-incident case files declared `N/A`

The largest case files in the archive cover *many* incidents at *many* locations across decades. The CSV picks `N/A` for these — defensible, but it means these reports never appear on the globe.

| Case group | Reports | Top places mentioned in bodies |
|---|---|---|
| **FBI 62-HQ-83894** (sections + serials) | 18 | Oak Ridge TN (18×), New York (15×), Mexico (14×), California (14×), Washington (14×), New Mexico (13×), Florida (12×) |
| **DoW Incident Summaries** (38_143685 box) | 3 | New Mexico (3×), Washington (3×), Pacific Ocean, Atlantic Ocean, Mexico, California, Germany |
| **NASA mission docs** | 15 | Moon (12×), Texas (5×), Atlantic, Germany, Japan, Australia |

**Recommendation:** if you want these on the globe, consider replacing `N/A` for the FBI case file with `"United States (multiple)"` and pinning to a generic CONUS centroid, or splitting these into per-incident sub-records derived from the body text.

### DoW Range Fouler / Mission reports declared `N/A` despite title naming a place

These are simple data-entry omissions:

- **dow-022** (D3 Arabian Gulf 2020) — declared N/A
- **dow-029** (D4 Arabian Gulf 2020) — declared N/A
- **dow-050** (D7 Arabian Gulf 2020) — declared N/A
- **dow-035** (D50 INDOPACOM Apr 2025) — declared N/A
- **dow-033** (D49 Vandenberg AFB 2000) — declared N/A

The title is unambiguous in each case. These could safely be filled in.

---

## Patterns that look wrong but aren't

### "Title is more general than declared" — declared field is correct

Eleven HIGH flags fire because the title says `Middle East` but the declared field is more specific (e.g., `Persian Gulf`, `Iraq`, `Syria`). This is the *desired* behavior — the CSV is more precise than the title summary.

Examples: dow-010 (D10), dow-028 (D38), dow-069 (PR37), dow-071 (PR39), dow-072 (PR40), and similar.

### Coastline cases — declared and title are both reasonable

UAE airspace looks out over Persian Gulf and Gulf of Oman. Greek airspace *is* Aegean / Mediterranean. Kuwait borders Iraq. The audit flags these because the strings differ, but geographically there's no contradiction:

- D17/18/20/62 (United Arab Emirates ↔ Persian Gulf / Gulf of Oman)
- D19/26/27 (Greece ↔ Aegean Sea / Mediterranean)
- PR20 (Kuwait ↔ Iraq)
- D31 (Strait of Hormuz ↔ Persian Gulf)

### Multi-year case files

Older DoW files have titles describing a date *span* (the file's coverage), with `Incident Date` set to one specific document inside. These look inconsistent but they're correctly modeled:

- dow-001 (1946-7 Vol 2, dated 12/30/47)
- dow-004 (1948-1955 records, dated 11/8/48)
- dow-006 (Flying Discs 1949, dated 1/9/50)

---

## Suggested next steps

If you want to fix the CSV upstream:

1. **Patch the 4 confirmed location errors** — D5, D6, D8, D42 (location/date both for D42)
2. **Fix the date typo** in D51 (`3/23/26` → `3/23/23`)
3. **Backfill the 5 `N/A` location fields** from titles (D3, D4, D7, D49, D50)
4. **Decide policy for multi-incident files** — leave as `N/A`, or expand into one record per incident

If you want to keep the CSV authoritative and patch downstream (in our viewer), I can add a `location_override` field in the per-file JSON that the globe and patterns view read first.

---

## Files generated

- [`location_audit.md`](location_audit.md) — full per-report audit (43 KB)
- [`location_audit.csv`](location_audit.csv) — sortable per-record flags (32 KB)
- [`location_audit_summary.md`](location_audit_summary.md) — this document

Audit script: `outputs/audit_locations.py` (re-run any time after the corpus is updated).
