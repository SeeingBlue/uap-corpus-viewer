"""update_deploy.py - rebuild the inlined data blobs in deploy/index.html.

deploy/index.html is the deployed corpus viewer (Vercel). It carries
three large inlined constants generated from project metadata:
  * DATA              - records + edges (~350 KB)
  * RECORD_COORDS     - per-record [lng, lat] for the globe view
  * PATTERN_FEATURES  - per-record shape/behavior/context tags

This script rebuilds all three from current metadata/* + extracted/*.md,
preserving the geocoding effort already invested in R1 and extending it
to Release 02 records with a built-in dictionary for the new location
labels.

It also:
  * Updates the page title, header h1, and snapshot meta line.
  * Keeps PATTERN_FINDINGS in place; new cross-release findings are
    inserted via separate edits.

The visual R1/R2 distinction (timeline row borders, globe dot color,
new filter chips) lives as targeted Edit changes in deploy/index.html
itself, not in this script.
"""

from __future__ import annotations

import csv
import json
import random
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "metadata" / "index.json"
ENTITIES = ROOT / "metadata" / "entities.json"
CROSS_REFS = ROOT / "metadata" / "cross_refs.json"
DATE_AUDIT = ROOT / "metadata" / "incident_date_audit.csv"
LOC_AUDIT = ROOT / "metadata" / "incident_location_audit.csv"
EXTRACTED_DIR = ROOT / "extracted"
DEPLOY_HTML = ROOT / "deploy" / "index.html"


# ---------- Geocoding ------------------------------------------------------

# Built-in [lng, lat] coordinates for location strings that R2 introduced
# (or that R1 used but didn't have entries for). Picked as representative
# central points - good enough for a globe-scale visualization.
NEW_LOCATION_COORDS = {
    # Military commands (HQ or area-of-responsibility centroid)
    "CENTCOM":              [50.583, 26.227],   # AOR centroid - Persian Gulf
    "USCENTCOM":            [50.583, 26.227],
    "NORTHCOM":             [-98.5, 39.5],      # CONUS centroid
    "USNORTHCOM":           [-98.5, 39.5],
    "AFRICOM":              [25.0, 5.0],        # Africa centroid
    "USAFRICOM":            [25.0, 5.0],
    "EUCOM":                [9.18, 48.78],      # Stuttgart HQ
    "USEUCOM":              [9.18, 48.78],
    "INDOPACOM":            [-157.85, 21.31],   # Honolulu HQ
    "USINDOPACOM":          [-157.85, 21.31],
    "SOUTHCOM":             [-80.27, 25.79],    # Miami HQ
    "USSOUTHCOM":           [-80.27, 25.79],

    # US regions
    "Western United States":      [-115.0, 39.0],
    "Eastern United States":      [-78.0, 38.0],
    "Southern United States":     [-92.0, 32.0],
    "Northern United States":     [-96.0, 47.0],
    "Southeastern United States": [-83.0, 33.0],
    "Southwestern United States": [-110.0, 33.0],
    "Northeastern United States": [-74.0, 42.0],
    "Northwestern United States": [-120.0, 46.5],
    "Midwestern United States":   [-93.0, 41.0],
    "Central United States":      [-99.0, 38.0],
    "Continental United States":  [-98.5, 39.5],

    # Countries / regions
    "USSR":          [100.0, 60.0],     # Russia/USSR centroid
    "Soviet Union":  [100.0, 60.0],
    "Russia":        [100.0, 60.0],
    "Kazakhstan":    [67.0, 48.0],
    "Iran":          [53.7, 32.4],

    # US states / locations
    "New Mexico":   [-106.0, 34.5],
    "Texas":        [-99.9, 31.0],
    "Sandia Base":  [-106.55, 35.05],   # Albuquerque, NM
    "Pantex":       [-101.55, 35.31],   # Amarillo, TX
    "Pajarito":     [-106.32, 35.85],   # Los Alamos NM area
    # Release 03 additions
    "Westen United States":   [-115.0, 39.0],  # CSV typo for "Western"
    "Colorado Springs":       [-104.82, 38.83],
    "Colorado":               [-105.5, 39.0],
    "Cape Kennedy":           [-80.60, 28.49],  # Cape Canaveral, FL
    "Houston":                [-95.37, 29.76],
    "New Jersey":             [-74.5, 40.1],
    "Washington State":       [-120.74, 47.4],
    "Florida":                [-81.5, 28.0],

    # Foreign cities/countries new in R3
    "Budapest":     [19.04, 47.50],
    "Hungary":      [19.5, 47.0],
    "Australia":    [134.0, -25.0],
    "Harare":       [31.05, -17.83],
    "Zimbabwe":     [29.15, -19.0],
    "Baku":         [49.87, 40.41],
    "Azerbaijan":   [47.6, 40.4],
    "Ladakh":       [77.6, 34.2],       # Himalayan tri-border record
    "Sikkim":       [88.5, 27.5],

    # Generic fallback - MUST stay after every more-specific "* United
    # States" key above so substring matching prefers the specific region.
    "United States": [-98.5, 39.5],

    # Water bodies
    "Yellow Sea":             [123.0, 35.0],
    "East China Sea":         [124.0, 30.0],
    "South China Sea":        [115.0, 15.0],
    "North Atlantic Ocean":   [-30.0, 45.0],
    "South Atlantic Ocean":   [-15.0, -25.0],

    # Off-Earth (drop a marker on the equator at the prime meridian for
    # display - the globe doesn't render space, but we still want a dot
    # so the record isn't hidden). Slightly offset so multiple records
    # don't perfectly collide.
    "Low Earth Orbit":  [0.0, 0.0],
    "Cislunar Space":   [0.5, 0.0],
    "Moon":             [1.0, 0.0],
    "Lunar Surface":    [1.0, 0.0],
}


def jitter_coord(base, key):
    """Deterministic small offset so coincident-location records don't
    perfectly overlap on the globe. Keyed off the record id so the
    offset is stable across re-runs."""
    rng = random.Random(key)
    lng, lat = base
    return [lng + rng.uniform(-1.5, 1.5), lat + rng.uniform(-1.2, 1.2)]


def geocode(loc, rec_id):
    """Best-effort lookup. Returns [lng, lat] or None."""
    if not loc:
        return None
    s = loc.strip()
    if not s or s in ("N/A", "-"):
        return None
    if s in NEW_LOCATION_COORDS:
        return jitter_coord(NEW_LOCATION_COORDS[s], rec_id)
    # Case-insensitive match
    for k, v in NEW_LOCATION_COORDS.items():
        if k.lower() == s.lower():
            return jitter_coord(v, rec_id)
    # Try substring (e.g. "Sandia Base, NM" matches "Sandia Base")
    for k, v in NEW_LOCATION_COORDS.items():
        if k.lower() in s.lower():
            return jitter_coord(v, rec_id)
    return None


# ---------- Pattern feature scanner ---------------------------------------

# Lightweight keyword scanner for R2 records: scan the extracted body
# and pull out shape / behavior / context tags. Same vocabulary as the
# existing PATTERN_FEATURES entries so the patterns view stays coherent.
SHAPE_PATS = {
    "disc":         [r"\bdisc(?:s|oid|-?shape|oid)?\b", r"\bsaucer\b"],
    "circular":     [r"\bcircular\b", r"\bround\b"],
    "cylinder":     [r"\bcylinder\b", r"\bcylindrical\b"],
    "cigar":        [r"\bcigar(?:-shape)?\b"],
    "sphere/orb":   [r"\borb\b", r"\bspheric(?:al)?\b", r"\bsphere\b"],
    "triangle":     [r"\btriangular?\b", r"\bv-shape\b"],
    "diamond":      [r"\bdiamond(?:-shape)?\b"],
    "egg":          [r"\begg-?shape\b"],
    "tic-tac":      [r"\btic[-\s]?tac\b"],
    "elongated":    [r"\belongated\b", r"\boblong\b"],
    "line/streak":  [r"\bstreak\b", r"\bbright\s+line\b"],
    "irregular":    [r"\birregular\b"],
    "rectangle":    [r"\brectangular?\b"],
    "boomerang":    [r"\bboomerang\b"],
    "dome":         [r"\bdome\b"],
    "point/dot":    [r"\bpoint\s+source\b", r"\bdot\b"],
}
BEHAVIOR_PATS = {
    "formation":              [r"\bformation\b", r"\bin\s+a\s+line\b"],
    "hover/stationary":       [r"\bhover(?:ing|ed)?\b", r"\bstationary\b", r"\bmotionless\b"],
    "vanish/disappear":       [r"\bvanish(?:ed|ing)?\b", r"\bdisappear(?:ed|ing)?\b"],
    "high speed":             [r"\bhigh\s+speed\b", r"\bextreme(?:ly)?\s+fast\b"],
    "high altitude":          [r"\bhigh\s+altitude\b"],
    "low altitude":           [r"\blow\s+altitude\b"],
    "aerobatic/maneuver":     [r"\bmaneuver(?:ing|ed)?\b", r"\baerobat\w+\b"],
    "right-angle turn":       [r"\bright[-\s]angle\s+turn\b", r"\b90[-\s]degree\s+turn\b"],
    "zigzag":                 [r"\bzig[-\s]?zag\b"],
    "instantaneous accel":    [r"\binstant(?:aneous)?\s+accel\w*\b", r"\binstant(?:aneous)?\s+(?:speed|movement)\b"],
    "loud/sound":             [r"\bloud\b", r"\bnoise\b", r"\bsound(?:ed|ing)?\b"],
    "silent":                 [r"\bsilent(?:ly)?\b", r"\bno\s+sound\b"],
    "pulsating/blinking":     [r"\bpulsat\w*\b", r"\bblink\w*\b", r"\bflash\w*\b"],
    "rotation/spin":          [r"\brotat\w*\b", r"\bspin(?:ning)?\b"],
    "trail/contrail":         [r"\btrail\b", r"\bcontrail\b"],
    "split/multiply":         [r"\bsplit\s+into\b", r"\bbroke\s+apart\b", r"\bsplit\s+in\s+two\b"],
    "merge":                  [r"\bmerged?\b"],
    "EM/radar interference":  [r"\bradar\s+jam\w*\b", r"\binterfere\w+\b.*radar", r"\belectrical\s+interfere\w*\b"],
    "engine/electrical effect": [r"\bengine\s+stall\w*\b", r"\belectrical\s+failure\b"],
    "light beam":             [r"\bbeam(?:s)?\s+of\s+light\b", r"\blight\s+beam\b"],
}
CONTEXT_PATS = {
    "photographed":              [r"\bphotograph\w*\b", r"\bimage\w*\s+capture"],
    "near nuclear/sensitive":    [r"\bnuclear\b", r"\bsensitive\s+(?:facility|site)\b", r"\bweapons\s+depot\b"],
    "near airbase":              [r"\bair\s*base\b", r"\bAFB\b", r"\bairfield\b"],
    "military aircraft witness": [r"\b(?:fighter|F-\d+|aircrew|pilot)\b"],
    "civilian aircraft witness": [r"\bcommercial\s+pilot\b", r"\bairline\s+pilot\b"],
    "civilian witness":          [r"\bcivilian\s+witness\b", r"\beyewitness\b"],
    "police witness":            [r"\bpolice\s+(?:officer|witness)\b", r"\bdeputy\b"],
    "ground military witness":   [r"\bground\s+(?:crew|troops)\b", r"\bsoldier\w*\b"],
    "naval/maritime":            [r"\bship\b", r"\bvessel\b", r"\bnaval\b", r"\bcarrier\b"],
    "radar tracked":             [r"\bradar\s+(?:contact|track|return)\b"],
    "night/dark":                [r"\bnight\b", r"\bdark\b", r"\bevening\b"],
    "day/morning":               [r"\bdaylight\b", r"\bmorning\b", r"\bnoon\b"],
}


def scan_features(body_text):
    out = {"shape": [], "behavior": [], "context": []}
    lower = body_text.lower()
    for tag, pats in SHAPE_PATS.items():
        if any(re.search(p, lower) for p in pats):
            out["shape"].append(tag)
    for tag, pats in BEHAVIOR_PATS.items():
        if any(re.search(p, lower) for p in pats):
            out["behavior"].append(tag)
    for tag, pats in CONTEXT_PATS.items():
        if any(re.search(p, lower) for p in pats):
            out["context"].append(tag)
    return out


# ---------- Data assembly --------------------------------------------------

def load_audit_inferences():
    """Read both audit CSVs and merge {id -> {date, date_src, date_disagrees,
    loc, loc_src, loc_disagrees}}."""
    out = {}
    if DATE_AUDIT.exists():
        with DATE_AUDIT.open(encoding="utf-8-sig") as f:
            for row in csv.DictReader(f):
                e = out.setdefault(row["id"], {})
                e["date"] = row.get("confirmed_date", "")
                e["date_src"] = row.get("confirming_sources", "")
                # csv_norm is the audit's normalization of the CSV value.
                # A "disagrees" flag is implicit when verdict==disagree.
                e["date_disagrees"] = row.get("verdict") == "disagree"
    if LOC_AUDIT.exists():
        with LOC_AUDIT.open(encoding="utf-8-sig") as f:
            for row in csv.DictReader(f):
                e = out.setdefault(row["id"], {})
                e["loc"] = row.get("confirmed_location", "")
                e["loc_src"] = row.get("confirming_sources", "")
                e["loc_disagrees"] = row.get("verdict") == "disagree"
    return out


def normalize_year_from_csv(s):
    """1947-2026 corpus pivot for 2-digit years."""
    m = re.match(r"^(\d{1,2})/(\d{1,2})/(\d{2})\b(.*)$", s)
    if m:
        mo, day, yy, rest = m.groups()
        yyi = int(yy)
        full = (1900 + yyi) if yyi >= 27 else (2000 + yyi)
        return f"{mo}/{day}/{full}{rest}"
    return s


def extract_year(date_str):
    if not date_str:
        return None
    m = re.search(r"\b(\d{4})\b", date_str)
    if m:
        y = int(m.group(1))
        return y if 1900 <= y <= 2030 else None
    return None


def build_data(index, entities, cross_refs, audit):
    records = []
    by_id = {r["id"]: r for r in index["files"]}

    for r in index["files"]:
        if r.get("status") == "deprecated":
            continue
        rid = r["id"]
        a = audit.get(rid, {})
        ents = entities.get(rid, {}) if isinstance(entities, dict) else {}

        # Year for timeline x-axis: prefer the audited inferred date.
        year = extract_year(a.get("date") or "") or \
               extract_year(normalize_year_from_csv(r.get("incident_date") or "")) or \
               extract_year(r.get("release_date") or "")

        release = {"Release 03": "R3", "Release 02": "R2"}.get(
            r.get("page_section"), "R1")

        records.append({
            "id": rid,
            "type": r["type"],
            "title": r["title"],
            "agency": r["agency"],
            "agency_raw": r.get("agency_raw", ""),
            "release_date": r.get("release_date", ""),
            "page_section": r.get("page_section", "Release 01"),
            "release": release,
            "incident_date": r.get("incident_date", ""),
            "incident_date_inferred": a.get("date", "") or "",
            "incident_date_inferred_source": a.get("date_src", "") or "",
            "incident_date_inferred_csv_disagrees": bool(a.get("date_disagrees")),
            "incident_location": r.get("incident_location", "N/A"),
            "incident_location_inferred": a.get("loc", "") or "",
            "incident_location_inferred_source": a.get("loc_src", "") or "",
            "incident_location_inferred_csv_disagrees": bool(a.get("loc_disagrees")),
            "summary": r.get("summary", ""),
            "redaction": r.get("redaction", ""),
            "featured": bool(r.get("featured")),
            "source_url": r.get("source_url", ""),
            "modal_image_url": r.get("modal_image_url", ""),
            "bytes": r.get("bytes", 0),
            "sha256": r.get("sha256", ""),
            "extracted_text_path": r.get("extracted_text_path"),
            "year": year,
            "ents": ents,
        })

    # Build edges from cross_refs.cross_refs (pair-code adjacency)
    edges = []
    seen = set()
    cr = cross_refs.get("cross_refs", {}) if isinstance(cross_refs, dict) else {}
    for src, targets in cr.items():
        for t in targets:
            key = tuple(sorted((src, t)))
            if key in seen or src == t:
                continue
            seen.add(key)
            edges.append({"source": src, "target": t})

    return {
        "snapshot_date": "2026-05-22",
        "total": len(records),
        "records": records,
        "edges": edges,
    }


def build_coords(records, existing_coords):
    """Preserve existing coords; geocode R2 records (and any others
    missing) using the built-in dictionary."""
    coords = dict(existing_coords)
    for r in records:
        rid = r["id"]
        if rid in coords:
            continue
        loc = (r.get("incident_location_inferred") or
               r.get("incident_location") or "").strip()
        c = geocode(loc, rid)
        if c is not None:
            coords[rid] = c
    return coords


def build_pattern_features(records, existing_features):
    """Preserve existing tags; scan extracted markdown for new IDs."""
    feats = dict(existing_features)
    for r in records:
        rid = r["id"]
        if rid in feats:
            continue
        md = EXTRACTED_DIR / f"{rid}.md"
        body = md.read_text(encoding="utf-8", errors="replace") if md.exists() else ""
        feats[rid] = scan_features(body)
    return feats


# ---------- HTML patching --------------------------------------------------

def replace_const_line(text, const_name, new_json):
    """Replace `  const NAME = {...};` with a freshly-serialized object.

    We use brace/bracket-balanced string scanning rather than re.sub
    because re.sub interprets backslash sequences in the replacement
    string (a JSON-escaped `\\n` would be turned back into a literal
    newline by re.sub, breaking JSON.parse in the browser).
    """
    marker = f"  const {const_name} = "
    start = text.find(marker)
    if start < 0:
        raise RuntimeError(f"failed to find const {const_name}")
    body_start = start + len(marker)
    # Brace/bracket scan with string-state awareness.
    i = body_start
    depth = 0
    in_str = False
    esc = False
    while i < len(text):
        c = text[i]
        if in_str:
            if esc:
                esc = False
            elif c == "\\":
                esc = True
            elif c == '"':
                in_str = False
        else:
            if c == '"':
                in_str = True
            elif c in "{[":
                depth += 1
            elif c in "}]":
                depth -= 1
                if depth == 0:
                    i += 1
                    break
        i += 1
    # Expect a trailing semicolon immediately after.
    if i >= len(text) or text[i] != ";":
        raise RuntimeError(f"const {const_name}: expected ; at offset {i}")
    return text[:body_start] + new_json + ";" + text[i + 1:]


def update_header(text, total, counts):
    text = re.sub(r"<title>[^<]+</title>",
                  "<title>war.gov UAP Release 01 + 02 + 03 — corpus viewer</title>",
                  text, count=1)
    text = re.sub(r"<h1>[^<]+</h1>",
                  "<h1>war.gov / UFO — Release 01 + 02 + 03</h1>",
                  text, count=1)
    meta = (f'PURSUE · snapshot 2026-06-12 · {total} records · '
            f'R1={counts.get("R1",0)} R2={counts.get("R2",0)} R3={counts.get("R3",0)}')
    text = re.sub(r'<span class="meta mono">[^<]+</span>',
                  f'<span class="meta mono">{meta}</span>',
                  text, count=1)
    return text


def main():
    print(f"[update_deploy] reading {INDEX}")
    index = json.loads(INDEX.read_text(encoding="utf-8-sig"))
    entities = json.loads(ENTITIES.read_text(encoding="utf-8-sig")) if ENTITIES.exists() else {}
    cross_refs = json.loads(CROSS_REFS.read_text(encoding="utf-8-sig")) if CROSS_REFS.exists() else {}
    audit = load_audit_inferences()

    print(f"[update_deploy] reading {DEPLOY_HTML}")
    html = DEPLOY_HTML.read_text(encoding="utf-8")

    # Pull existing coords and pattern features out of the current HTML.
    m = re.search(r"const RECORD_COORDS = (\{[^\n]+\});", html)
    existing_coords = json.loads(m.group(1)) if m else {}
    m = re.search(r"const PATTERN_FEATURES = (\{[^\n]+\});", html)
    existing_features = json.loads(m.group(1)) if m else {}

    data = build_data(index, entities, cross_refs, audit)
    print(f"[update_deploy] built {data['total']} records, {len(data['edges'])} edges")
    coords = build_coords(data["records"], existing_coords)
    print(f"[update_deploy] coords: {len(coords)} (added {len(coords)-len(existing_coords)})")
    feats = build_pattern_features(data["records"], existing_features)
    print(f"[update_deploy] pattern features: {len(feats)} (added {len(feats)-len(existing_features)})")

    data_json = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    coords_json = json.dumps(coords, ensure_ascii=False, separators=(",", ":"))
    feats_json = json.dumps(feats, ensure_ascii=False, separators=(",", ":"))

    html = replace_const_line(html, "DATA", data_json)
    html = replace_const_line(html, "RECORD_COORDS", coords_json)
    html = replace_const_line(html, "PATTERN_FEATURES", feats_json)
    rel_counts = {}
    for r in data["records"]:
        rel_counts[r["release"]] = rel_counts.get(r["release"], 0) + 1
    html = update_header(html, data["total"], rel_counts)

    # Optional release_patterns.json -> inline as RELEASE_PATTERNS for the
    # viewer's cross-release comparison panel.
    rp = ROOT / "metadata" / "release_patterns.json"
    if rp.exists():
        rp_json = json.dumps(json.loads(rp.read_text(encoding="utf-8-sig")),
                             ensure_ascii=False, separators=(",", ":"))
        try:
            html = replace_const_line(html, "RELEASE_PATTERNS", rp_json)
            print("[update_deploy] inlined RELEASE_PATTERNS")
        except RuntimeError:
            print("[update_deploy] RELEASE_PATTERNS const not in template (skipped)")

    DEPLOY_HTML.write_text(html, encoding="utf-8", newline="\n")
    print(f"[update_deploy] wrote {DEPLOY_HTML} ({len(html):,} bytes)")
    print(f"[update_deploy] release counts: {rel_counts}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
