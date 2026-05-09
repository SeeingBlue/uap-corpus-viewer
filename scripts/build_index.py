"""build_index.py - Tier C: cross-references, entities, timeline, geo, master index.

Reads:
  metadata/index.json
  extracted/<id>.md

Writes:
  metadata/entities.json     - per-record entity extraction
  metadata/cross_refs.json   - pairing graph + reverse refs
  metadata/timeline.csv      - sorted by incident_date
  metadata/by_location.md    - grouped by incident_location
  extracted/_index.md        - LLM-friendly master map of the corpus
"""

from __future__ import annotations
import csv as csvmod
import json
import re
import sys
from collections import defaultdict
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "metadata" / "index.json"
EXTRACTED = ROOT / "extracted"
META = ROOT / "metadata"

ENTITIES_PATH = META / "entities.json"
CROSS_REFS_PATH = META / "cross_refs.json"
TIMELINE_PATH = META / "timeline.csv"
LOCATIONS_PATH = META / "by_location.md"
LLM_INDEX_PATH = EXTRACTED / "_index.md"


# ---- Entity patterns ---------------------------------------------------

# Military units / agencies (extend as needed)
MIL_UNITS = [
    "USCENTCOM", "CENTCOM", "INDOPACOM", "USAFRICOM", "AFRICOM",
    "EUCOM", "NORTHCOM", "SOUTHCOM", "USSPACECOM", "STRATCOM",
    "USAF", "USN", "USMC", "USA ", "USCG",
    "AARO", "DIA", "ODNI", "NORAD", "NRO", "NSA", "CIA", "FBI",
    "AFOSI", "NCIS",
    "RAF", "Bundeswehr",
]

# Classification markers
CLASSIFICATION = [
    r"\bTOP SECRET//[A-Z/,\s]+\b",
    r"\bTOP SECRET\b",
    r"\bSECRET//[A-Z/,\s]+\b",
    r"\bSECRET\b",
    r"\bCONFIDENTIAL\b",
    r"\bUNCLASSIFIED\b",
    r"\bCUI//[A-Z/,\s]+\b",
    r"\bCUI\b",
    r"\bNOFORN\b",
    r"\bREL TO [A-Z, ]+\b",
    r"\bFOUO\b",
]

# Date patterns
DATE_PATTERNS = [
    r"\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},?\s+\d{4}\b",
    r"\b\d{1,2}\s+(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{4}\b",
    r"\b\d{1,2}/\d{1,2}/\d{2,4}\b",
    r"\b\d{4}-\d{2}-\d{2}\b",
]

# MGRS-like coordinates (common form 38SMC36120 etc.)
MGRS_PAT = r"\b\d{1,2}[A-HJ-NP-Z][A-HJ-NP-Z]{2}\d{4,10}\b"

# Lat/long DMS
LATLONG_DMS = r"\d{1,3}°\d{1,2}['′]\d{1,2}[\"″]?[NSEW]"

# File / case / serial numbers — adjust later
CASE_PAT = r"\b\d{2,3}-HQ-\d{3,6}\b|\b62-HQ-\d{3,6}\b|\bHS\d-\d{6,12}\b|\b\d{3}-DE-\d{4,6}\b"
SERIAL_PAT = r"\b[Ss]erial\s+\d{1,4}\b"
NND_PAT = r"\bNND\s*\d{6,8}\b|\bNW\s*\d{4,8}\b|\bDocId:\s*\d{6,12}\b"

# Aircraft / vehicle types
AIRCRAFT = [
    r"\bF-\d{1,3}[A-Z]?\b",      # F-35, F/A-18
    r"\bMQ-\d+[A-Z]?\b",         # MQ-9
    r"\bRQ-\d+[A-Z]?\b",         # RQ-4
    r"\bC-\d{2,3}[A-Z]?\b",      # C-130
    r"\bE-\d{1,3}[A-Z]?\b",      # E-3
    r"\bP-\d{1,2}[A-Z]?\b",      # P-8
    r"\bB-\d{1,3}[A-Z]?\b",      # B-52, B-2
    r"\bAH-\d{1,3}[A-Z]?\b",     # AH-64
    r"\bUH-\d{1,3}[A-Z]?\b",     # UH-60
    r"\bU-2\b", r"\bSR-71\b",
    r"\bF/A-18\b",
]

# Operation names (very common in mission reports)
OPERATION_PAT = r"\b(?:OP|OPERATION)\s+([A-Z][A-Z\- ]{2,40})"

# Naive person-name regex: 2-3 capitalized words. Heavy false positives but
# we filter against a stop-word list of known non-name capitalized phrases.
NAME_PAT = re.compile(r"\b([A-Z][a-z]+(?:\s[A-Z]\.?)?\s[A-Z][a-z]+(?:\s[A-Z][a-z]+)?)\b")
NAME_STOP = set("""United States America War Defense Force Air Navy Army
Department Office Bureau Federal Atlantic Pacific Middle East South North
West Reserve Section Sub Volume Page Date Type Title Document File Report
Mission Director Headquarters Information Analysis Anomaly Resolution
General Material Command Records Classification Authority Declassified
January February March April May June July August September October November December
Monday Tuesday Wednesday Thursday Friday Saturday Sunday
Persian Arabian Gulf Mediterranean Sea Ocean Hemisphere Arctic Antarctic
""".split())


# Common US states + territories for location enrichment
US_STATES = {
    "AL": "Alabama", "AK": "Alaska", "AZ": "Arizona", "AR": "Arkansas",
    "CA": "California", "CO": "Colorado", "CT": "Connecticut", "DE": "Delaware",
    "FL": "Florida", "GA": "Georgia", "HI": "Hawaii", "ID": "Idaho",
    "IL": "Illinois", "IN": "Indiana", "IA": "Iowa", "KS": "Kansas",
    "KY": "Kentucky", "LA": "Louisiana", "ME": "Maine", "MD": "Maryland",
    "MA": "Massachusetts", "MI": "Michigan", "MN": "Minnesota", "MS": "Mississippi",
    "MO": "Missouri", "MT": "Montana", "NE": "Nebraska", "NV": "Nevada",
    "NH": "New Hampshire", "NJ": "New Jersey", "NM": "New Mexico", "NY": "New York",
    "NC": "North Carolina", "ND": "North Dakota", "OH": "Ohio", "OK": "Oklahoma",
    "OR": "Oregon", "PA": "Pennsylvania", "RI": "Rhode Island", "SC": "South Carolina",
    "SD": "South Dakota", "TN": "Tennessee", "TX": "Texas", "UT": "Utah",
    "VT": "Vermont", "VA": "Virginia", "WA": "Washington", "WV": "West Virginia",
    "WI": "Wisconsin", "WY": "Wyoming", "DC": "District of Columbia",
}


# ---- Helpers -----------------------------------------------------------

def load_index():
    return json.loads(INDEX.read_text(encoding="utf-8-sig"))


def read_md_body(path: Path) -> str:
    """Strip frontmatter, return body text."""
    if not path.exists():
        return ""
    text = path.read_text(encoding="utf-8")
    if text.startswith("---\n"):
        try:
            end = text.index("\n---\n", 4)
            text = text[end + 5:]
        except ValueError:
            pass
    return text


def find_all(patterns, text, flags=0) -> list[str]:
    out = []
    for p in patterns:
        if isinstance(p, str):
            out.extend(re.findall(p, text, flags))
        else:
            out.extend(p.findall(text))
    return out


def dedupe_preserve(items: list[str]) -> list[str]:
    seen = set()
    out = []
    for x in items:
        s = x.strip() if isinstance(x, str) else x
        if not s:
            continue
        if s in seen:
            continue
        seen.add(s)
        out.append(s)
    return out


def extract_entities(record: dict, body: str) -> dict:
    """Pull entities out of a single record's body text."""
    rid = record["id"]

    # Military units (exact-string match, case-sensitive for acronyms)
    found_units = []
    for u in MIL_UNITS:
        if u in body:
            found_units.append(u.strip())

    # Classification markers
    found_classification = []
    for p in CLASSIFICATION:
        for m in re.findall(p, body):
            found_classification.append(m if isinstance(m, str) else m[0])

    # Dates mentioned in body (separate from incident_date metadata)
    found_dates = find_all(DATE_PATTERNS, body, re.IGNORECASE)

    # Coordinates
    mgrs = re.findall(MGRS_PAT, body)
    latlong = re.findall(LATLONG_DMS, body)

    # Case / serial / archive numbers
    case_nums = re.findall(CASE_PAT, body)
    serials = re.findall(SERIAL_PAT, body)
    nnds = re.findall(NND_PAT, body)

    # Aircraft
    aircraft = find_all(AIRCRAFT, body)

    # Operations
    operations = re.findall(OPERATION_PAT, body)

    # Naive person names
    candidates = NAME_PAT.findall(body)
    names = []
    for n in candidates:
        parts = n.split()
        # Filter: skip if any token is in stop list
        if any(p in NAME_STOP for p in parts):
            continue
        # Skip place-y patterns
        if "United States" in n or "Air Force" in n:
            continue
        names.append(n)

    # US-state mentions (look for ", TN" / ", Texas" / "Tennessee" anchored to spelling)
    state_mentions = []
    for code, name in US_STATES.items():
        if re.search(rf"\b{re.escape(name)}\b", body):
            state_mentions.append(name)
        elif re.search(rf",\s+{code}\b", body):
            state_mentions.append(f"{code} ({name})")

    return {
        "id": rid,
        "military_units":  dedupe_preserve(found_units),
        "classification":  dedupe_preserve(found_classification),
        "dates_in_body":   dedupe_preserve(found_dates)[:50],   # cap
        "mgrs":            dedupe_preserve(mgrs)[:30],
        "latlong":         dedupe_preserve(latlong)[:30],
        "case_numbers":    dedupe_preserve(case_nums),
        "serials":         dedupe_preserve(serials),
        "archive_ids":     dedupe_preserve(nnds),
        "aircraft":        dedupe_preserve(aircraft),
        "operations":      dedupe_preserve(operations),
        "us_states":       dedupe_preserve(state_mentions),
        "names":           dedupe_preserve(names)[:100],
    }


def _normalize_2digit_year(s):
    """Re-map 2-digit years using a 1947-2026 corpus pivot.

    strptime's default %y window (1969-2068) misreads e.g. '10/14/65' as 2065.
    For this corpus, anything >= 27 is 19xx, everything else is 20xx.
    Returns the original string if no 2-digit year is found.
    """
    import re as _re
    m = _re.match(r"^(\d{1,2})/(\d{1,2})/(\d{2})\b(.*)$", s)
    if m:
        mo, day, yy, rest = m.groups()
        yyi = int(yy)
        full = (1900 + yyi) if yyi >= 27 else (2000 + yyi)
        return f"{mo}/{day}/{full}{rest}"
    return s

# ---- Main --------------------------------------------------------------

def main():
    idx = load_index()
    records = idx["files"]
    by_id = {r["id"]: r for r in records}

    # ---- Entity extraction --------------------------------------------
    print("[1/4] extracting entities from extracted bodies...")
    entities = {}
    for r in records:
        md_path = EXTRACTED / f"{r['id']}.md"
        body = read_md_body(md_path)
        ents = extract_entities(r, body)
        entities[r["id"]] = ents

    ENTITIES_PATH.write_text(
        json.dumps(entities, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"     -> {ENTITIES_PATH}")

    # ---- Cross-references ---------------------------------------------
    # CSV columns "Video Pairing" and "PDF Pairing" carry the page's own
    # cross-link metadata. Build a graph of which records are paired.
    print("[2/4] building cross-reference graph...")
    pairs = defaultdict(set)  # rid -> set of paired rids
    pair_codes = {}           # short code -> [rid, ...]

    # First, index records by their pair codes (e.g., "DOW-UAP-D10")
    pair_re = re.compile(r"\b([A-Z]+(?:-[A-Z0-9]+){1,3})\b")
    for r in records:
        # Extract the short code from the title
        title = r.get("title", "")
        for m in pair_re.findall(title):
            if any(t in m for t in ("UAP", "FBI", "VID", "SR", "PR")):
                pair_codes.setdefault(m, []).append(r["id"])

    # Resolve pairings by scanning multiple sources for code references:
    #   1. The CSV's video_pairing / pdf_pairing columns (sometimes empty)
    #   2. The Description Blurb (often references paired records by code)
    #   3. The first 2KB of the extracted body (sometimes lists related records)
    # Pair codes look like DOW-UAP-D10, DOW-UAP-PR19, NASA-UAP-D3, etc.
    # Use case-insensitive matching so DoW/DOW/dow all work.
    code_lookup_re = re.compile(
        r"\b([A-Za-z]{2,5}(?:-[A-Z][A-Za-z0-9]{1,4}){1,3})\b"
    )

    # Build a case-insensitive code -> [rid, ...] lookup
    code_to_rids = {}
    for code, rids in pair_codes.items():
        code_to_rids.setdefault(code.upper(), []).extend(rids)

    for r in records:
        rid = r["id"]
        # Sources of pairing references for this record
        sources = [
            r.get("video_pairing", ""),
            r.get("pdf_pairing", ""),
            r.get("summary", ""),
        ]
        # Plus first 2KB of extracted body
        md = EXTRACTED / f"{rid}.md"
        if md.exists():
            body = read_md_body(md)[:2000]
            sources.append(body)

        text = " | ".join(sources)
        for code in code_lookup_re.findall(text):
            up = code.upper()
            for other in code_to_rids.get(up, []):
                if other != rid:
                    pairs[rid].add(other)
                    pairs[other].add(rid)

    cross_refs = {rid: sorted(others) for rid, others in pairs.items()}
    CROSS_REFS_PATH.write_text(
        json.dumps({
            "pair_codes": pair_codes,
            "cross_refs": cross_refs,
        }, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"     -> {CROSS_REFS_PATH}  ({sum(len(v) for v in cross_refs.values())//2} unique pairs)")

    # ---- Timeline -----------------------------------------------------
    print("[3/4] building timeline + geographic indexes...")

    def parse_date(s):
        """Parse a date string with the 1947-2026 corpus convention.

        For 2-digit years (e.g., '10/14/65'): years 27-99 are 19xx,
        years 00-26 are 20xx. This avoids strptime's default sliding
        window putting historical dates in the future.
        """
        s = (s or "").strip()
        if not s or s.upper() == "N/A":
            return None
        # Hand-fix the 2-digit-year ambiguity before strptime sees it
        s_norm = _normalize_2digit_year(s)
        for fmt in ("%m/%d/%Y", "%Y-%m-%d", "%B %Y", "%B %d, %Y", "%d %B %Y"):
            try:
                return datetime.strptime(s_norm, fmt).date().isoformat()
            except ValueError:
                pass
        # Year-only patterns
        m = re.match(r"^\s*(\d{4})\s*$", s)
        if m:
            return f"{m.group(1)}-01-01"
        m = re.search(r"(\d{4})", s)
        if m:
            return f"{m.group(1)}-01-01"
        return None

    def best_date_for_sorting(r):
        """Prefer the audited inferred date when present, falling back to the
        upstream csv `incident_date`. Inferred dates are already ISO-shaped
        (YYYY, YYYY-MM, YYYY-MM-DD) so they only need light normalization."""
        inf = (r.get("incident_date_inferred") or "").strip()
        if inf:
            if len(inf) == 4:
                return f"{inf}-01-01"
            if len(inf) == 7:
                return f"{inf}-01"
            return inf
        return parse_date(r.get("incident_date"))

    timeline = []
    for r in records:
        d = best_date_for_sorting(r)
        timeline.append((d, r))
    # Sort: known dates first ascending, unknowns last
    timeline.sort(key=lambda t: (t[0] is None, t[0] or "", t[1]["id"]))

    with TIMELINE_PATH.open("w", encoding="utf-8", newline="") as f:
        w = csvmod.writer(f)
        w.writerow(["sort_date", "incident_date_raw", "incident_date_inferred",
                    "incident_date_inferred_source", "id", "type", "agency",
                    "title", "incident_location", "summary_short"])
        for d, r in timeline:
            short = (r.get("summary") or "").replace("\n", " ").strip()[:200]
            w.writerow([d or "", r.get("incident_date", ""),
                        r.get("incident_date_inferred", ""),
                        r.get("incident_date_inferred_source", ""),
                        r["id"], r["type"], r["agency"],
                        r.get("title", ""), r.get("incident_location", ""),
                        short])
    print(f"     -> {TIMELINE_PATH}")

    # ---- Geographic index ---------------------------------------------
    by_loc = defaultdict(list)
    for r in records:
        loc = (r.get("incident_location") or "").strip() or "Unknown"
        by_loc[loc].append(r)

    lines = ["# Records by incident location",
             "",
             f"_Generated from `metadata/index.json` covering {len(records)} records._",
             ""]
    for loc, rs in sorted(by_loc.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        lines.append(f"## {loc}  ({len(rs)} records)")
        lines.append("")
        for r in sorted(rs, key=lambda r: r["id"]):
            d = (r.get("incident_date_inferred") or r.get("incident_date") or "—")
            lines.append(f"- **[{r['agency']}]** `{r['id']}` — {d} — {r['title']}")
        lines.append("")
    LOCATIONS_PATH.write_text("\n".join(lines), encoding="utf-8")
    print(f"     -> {LOCATIONS_PATH}")

    # ---- Master LLM-friendly index ------------------------------------
    print("[4/4] writing master LLM-friendly index...")
    lines = []
    lines.append("# war.gov UAP Release 01 — master index")
    lines.append("")
    lines.append(f"This file is a navigation map for the {len(records)}-record "
                 "Department of War UAP archive. Every record has a "
                 "corresponding `<id>.md` file in this directory with "
                 "frontmatter metadata + extracted text body. PII (names, "
                 "locations, military units) is preserved verbatim per the "
                 "war.gov Trump-directive policy: redactions only protect "
                 "eyewitness identities and non-UAP-related sensitive military "
                 "site information.")
    lines.append("")
    lines.append("## Counts")
    lines.append("")
    lines.append("| | |")
    lines.append("|---|---:|")
    lines.append(f"| Total records | {len(records)} |")
    type_count = defaultdict(int)
    agency_count = defaultdict(int)
    for r in records:
        type_count[r["type"]] += 1
        agency_count[r["agency"]] += 1
    for t, c in sorted(type_count.items()):
        lines.append(f"| {t}s | {c} |")
    lines.append("")
    lines.append("| Agency | Count |")
    lines.append("|---|---:|")
    for a, c in sorted(agency_count.items(), key=lambda kv: -kv[1]):
        lines.append(f"| {a} | {c} |")
    lines.append("")

    # Records by agency, then incident_date
    lines.append("## Records by agency")
    lines.append("")
    by_agency = defaultdict(list)
    for r in records:
        by_agency[r["agency"]].append(r)
    for a in sorted(by_agency.keys(), key=lambda x: -len(by_agency[x])):
        rs = by_agency[a]
        lines.append(f"### {a}  ({len(rs)} records)")
        lines.append("")
        # Sort by inferred date if present, else parsed incident_date
        rs2 = sorted(rs, key=lambda r: (best_date_for_sorting(r) or "9999",
                                        r["id"]))
        for r in rs2:
            d = (r.get("incident_date_inferred") or r.get("incident_date") or "—")
            loc = r.get("incident_location") or "—"
            paired = cross_refs.get(r["id"], [])
            paired_str = f" ↔ paired with {', '.join('`'+p+'`' for p in paired)}" if paired else ""
            lines.append(f"- `{r['id']}` ({r['type']}, {d}, {loc}) "
                         f"— [{r['title']}]({r['id']}.md){paired_str}")
        lines.append("")

    # Notable cross-references
    if cross_refs:
        lines.append("## Cross-references (pairings)")
        lines.append("")
        lines.append("DoW mission reports often pair with DoW PR videos via the "
                     "page's `Video Pairing` and `PDF Pairing` columns:")
        lines.append("")
        seen = set()
        for rid, others in sorted(cross_refs.items()):
            for o in others:
                key = tuple(sorted([rid, o]))
                if key in seen:
                    continue
                seen.add(key)
                a = by_id[rid]
                b = by_id[o]
                lines.append(f"- [`{rid}`]({rid}.md) ({a['type']}) ↔ "
                             f"[`{o}`]({o}.md) ({b['type']})")
        lines.append("")

    # Top entity buckets
    lines.append("## Aggregate entity stats")
    lines.append("")
    all_units = defaultdict(int)
    all_locations = defaultdict(int)
    all_states = defaultdict(int)
    all_aircraft = defaultdict(int)
    all_classification = defaultdict(int)
    for rid, e in entities.items():
        for u in e["military_units"]:
            all_units[u] += 1
        for s in e["us_states"]:
            all_states[s] += 1
        for a in e["aircraft"]:
            all_aircraft[a] += 1
        for c in e["classification"]:
            all_classification[c] += 1
    for r in records:
        loc = (r.get("incident_location") or "").strip()
        if loc and loc != "N/A":
            all_locations[loc] += 1

    def top_table(title, d, n=20):
        if not d:
            return
        lines.append(f"### {title}")
        lines.append("")
        lines.append("| value | records |")
        lines.append("|---|---:|")
        for k, v in sorted(d.items(), key=lambda kv: -kv[1])[:n]:
            lines.append(f"| {k} | {v} |")
        lines.append("")

    top_table("Top incident locations (from CSV metadata)", all_locations, 30)
    top_table("Top US states mentioned in document bodies", all_states, 30)
    top_table("Top military units mentioned", all_units, 30)
    top_table("Aircraft references", all_aircraft, 20)
    top_table("Classification markers seen", all_classification, 20)

    # Quick links
    lines.append("## Auxiliary indexes")
    lines.append("")
    lines.append("- `../metadata/index.json` — full per-record canonical metadata")
    lines.append("- `../metadata/entities.json` — per-record entity extraction")
    lines.append("- `../metadata/cross_refs.json` — pairing graph")
    lines.append("- `../metadata/timeline.csv` — chronological listing")
    lines.append("- `../metadata/by_location.md` — records grouped by incident location")
    lines.append("- `../snapshots/2026-05-08/uap-csv.csv` — original war.gov manifest")
    lines.append("- `../snapshots/2026-05-08/manifest_schema.md` — CSV schema docs")
    lines.append("")

    LLM_INDEX_PATH.write_text("\n".join(lines), encoding="utf-8")
    print(f"     -> {LLM_INDEX_PATH}")

    print()
    print("[done]")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
