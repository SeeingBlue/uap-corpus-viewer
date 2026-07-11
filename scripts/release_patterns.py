"""release_patterns.py - cross-release pattern recognition (R1 vs R2 vs R3).

Separates the corpus by release (page_section) and produces a reproducible,
quantitative comparison across the three war.gov UAP document drops:

  Release 01 - 2026-05-08
  Release 02 - 2026-05-22
  Release 03 - 2026-06-12

For each release it profiles:
  - asset type / agency / redaction / featured counts
  - incident-date distribution by decade
  - incident-location distribution by macro-region
  - object morphology (shape) tag frequencies
  - kinematics / behavior tag frequencies
  - witnessing / sensor context tag frequencies
  - document-class signatures (302, MISREP, cable, IIR, debriefing, ...)
  - sensor/collection modality (radar, IR/FLIR, naked-eye, photographic, ...)

Then it computes cross-release deltas (which patterns rose or fell, what
vocabulary is brand-new in a release) and detects cross-release narrative
threads (the same named incident surfacing in more than one release in a
different evidentiary form).

Outputs:
  metadata/release_patterns.json   - machine-readable, feeds the viewer
  audits/release_patterns.md       - human-readable report

Deterministic: pure keyword/metadata scan, no model calls. The qualitative
companion (audits/cross_release_patterns.md) is produced by a separate
multi-agent workflow that reads the document bodies.
"""

from __future__ import annotations

import csv
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from update_deploy import SHAPE_PATS, BEHAVIOR_PATS, CONTEXT_PATS  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "metadata" / "index.json"
EXTRACTED = ROOT / "extracted"
OUT_JSON = ROOT / "metadata" / "release_patterns.json"
OUT_MD = ROOT / "audits" / "release_patterns.md"

RELEASES = [
    ("R1", "Release 01", "2026-05-08"),
    ("R2", "Release 02", "2026-05-22"),
    ("R3", "Release 03", "2026-06-12"),
    ("R4", "Release 04", "2026-07-10"),
]

# Document-class signatures: a record is tagged with a class when its title
# or body matches. Order matters only for display.
DOC_CLASSES = {
    "FBI FD-302 interview":   [r"\bFD-?302\b", r"\b302 interview\b"],
    "FBI FD-1057":            [r"\bFD-?1057\b"],
    "Mission report (MISREP)": [r"\bMISREP\b", r"\bmission report\b"],
    "Range Fouler report":    [r"\brange fouler\b"],
    "Unresolved UAP report":  [r"\bunresolved uap\b", r"\bunresolved case\b"],
    "State Dept cable":       [r"\bcable\b", r"\bunclas[\s\w]+embassy\b", r"\bSECSTATE\b"],
    "CIA IIR":                [r"\bintelligence information report\b", r"\bIIR\b"],
    "Crew debriefing":        [r"\bdebrief\w*\b"],
    "Incident summary":       [r"\bincident summ\w*\b"],
    "Correspondence/memo":    [r"\bmemorandum\b", r"\bcorrespondence\b"],
    "Congressional/legal":    [r"\bcongress\w*\b", r"\bhouse of representatives\b", r"\bsubpoena\b"],
    "Scientific study":       [r"\bscientific\b", r"\bstudy\b", r"\bpanel\b", r"\banalysis\b"],
}

# Sensor / collection modality.
SENSOR_MODES = {
    "radar":            [r"\bradar\b"],
    "IR/FLIR/thermal":  [r"\bFLIR\b", r"\binfrared\b", r"\bthermal\b", r"\belectro-?optical\b"],
    "naked-eye":        [r"\bnaked eye\b", r"\bvisual(?:ly)? observ\w*\b", r"\bunaided\b"],
    "night-vision":     [r"\bnight vision\b", r"\bNVG\b", r"\bNVD\b"],
    "photographic":     [r"\bphotograph\w*\b", r"\bstill image\b", r"\bcamera\b"],
    "video/sensor feed": [r"\bsensor (?:feed|video|footage)\b", r"\bgun camera\b", r"\barea of contrast\b"],
    "satellite/space":  [r"\bsatellite\b", r"\borbit\w*\b", r"\bspaceborne\b"],
}

# Macro-regions for location bucketing.
REGION_RULES = [
    ("CENTCOM / Middle East", r"iraq|syria|iran|kuwait|saudi|yemen|oman|uae|united arab|qatar|bahrain|persian gulf|arabian|hormuz|gulf of aden|gulf of oman|red sea|djibouti|centcom|middle east"),
    ("INDOPACOM / Pacific", r"japan|korea|china sea|yellow sea|sea of japan|taiwan|philippine|guam|hawaii|indopacom|pacific"),
    ("Europe / Mediterranean", r"greece|aegean|mediterranean|germany|netherlands|turkey|italy|france|spain|black sea|eucom|europe"),
    ("Africa", r"africa|africom|somalia|sudan|libya|egypt"),
    ("CONUS / United States", r"united states|u\.s\.|conus|new mexico|texas|colorado|california|washington|nevada|northcom|sandia|pantex|los alamos|vandenberg|northeastern|western united|southeastern|midwest"),
    ("Former USSR / Central Asia", r"ussr|soviet|russia|kazakhstan|georgia|turkmenistan|azerbaijan|tbilisi|ashgabat"),
    ("Latin America", r"mexico|papua|brazil|argentina"),
    ("Space / off-Earth", r"low earth orbit|cislunar|lunar|moon|apollo|gemini|mercury|skylab"),
]


def load_index():
    return json.loads(INDEX.read_text(encoding="utf-8-sig"))


def read_body(rec) -> str:
    p = rec.get("extracted_text_path")
    if not p:
        return ""
    fp = ROOT / p
    if not fp.exists():
        return ""
    text = fp.read_text(encoding="utf-8", errors="replace")
    if text.startswith("---\n"):
        try:
            text = text[text.index("\n---\n", 4) + 5:]
        except ValueError:
            pass
    return text


def decade_of(rec) -> str | None:
    for field in ("incident_date_inferred", "incident_date"):
        s = (rec.get(field) or "").strip()
        m = re.search(r"\b(19|20)\d{2}\b", s)
        if m:
            y = int(m.group())
            return f"{(y // 10) * 10}s"
        m2 = re.match(r"\d{1,2}/\d{1,2}/(\d{2})\b", s)
        if m2:
            yy = int(m2.group(1))
            y = 1900 + yy if yy >= 27 else 2000 + yy
            return f"{(y // 10) * 10}s"
    return None


def region_of(rec) -> str:
    hay = " ".join([
        rec.get("incident_location_inferred") or "",
        rec.get("incident_location") or "",
        rec.get("title") or "",
    ]).lower()
    for label, pat in REGION_RULES:
        if re.search(pat, hay):
            return label
    if (rec.get("incident_location") or "").strip() in ("", "N/A"):
        return "(unspecified)"
    return "Other"


def tag_hits(body, patmap) -> set:
    lo = body.lower()
    out = set()
    for tag, pats in patmap.items():
        if any(re.search(p, lo) for p in pats):
            out.add(tag)
    return out


def profile_release(records) -> dict:
    prof = {
        "n": len(records),
        "by_type": Counter(),
        "by_agency": Counter(),
        "redacted": 0,
        "featured": 0,
        "by_decade": Counter(),
        "by_region": Counter(),
        "shape": Counter(),
        "behavior": Counter(),
        "context": Counter(),
        "doc_class": Counter(),
        "sensor": Counter(),
        "with_body": 0,
    }
    for r in records:
        prof["by_type"][r.get("type", "?")] += 1
        prof["by_agency"][r.get("agency", "?")] += 1
        if (r.get("redaction") or "").upper() == "TRUE":
            prof["redacted"] += 1
        if r.get("featured"):
            prof["featured"] += 1
        d = decade_of(r)
        if d:
            prof["by_decade"][d] += 1
        prof["by_region"][region_of(r)] += 1
        body = read_body(r)
        hay = (r.get("title", "") + "\n" + r.get("summary", "") + "\n" + body)
        if body:
            prof["with_body"] += 1
        for tag in tag_hits(body, SHAPE_PATS):
            prof["shape"][tag] += 1
        for tag in tag_hits(body, BEHAVIOR_PATS):
            prof["behavior"][tag] += 1
        for tag in tag_hits(body, CONTEXT_PATS):
            prof["context"][tag] += 1
        for tag in tag_hits(hay, DOC_CLASSES):
            prof["doc_class"][tag] += 1
        for tag in tag_hits(hay, SENSOR_MODES):
            prof["sensor"][tag] += 1
    # Convert counters to plain dicts (sorted desc)
    for k, v in list(prof.items()):
        if isinstance(v, Counter):
            prof[k] = dict(v.most_common())
    return prof


def rate(d, n):
    """Convert a tag-count dict to {tag: (count, pct)} relative to n records."""
    return {k: [c, round(100 * c / n, 1) if n else 0.0] for k, c in d.items()}


# Named cross-release incident threads. Each thread is a label + a matcher
# that flags records (by title/summary/location) likely about that incident.
THREAD_RULES = [
    ("Western US 2025 'glowing orbs' (test range)",
     r"western united states|glowing orb|usper|sensitive (?:government )?testing|test range"),
    ("Colorado Springs UAP incident",
     r"colorado springs|colorado"),
    ("Northeastern US orb sightings 2024-2025",
     r"northeastern|orbs over the pond|new jersey drone"),
    ("Persian Gulf / CENTCOM 2020 cluster",
     r"persian gulf|arabian gulf|strait of hormuz|gulf of aden|arabian sea"),
    ("NASA crewed-spaceflight observations (Mercury/Gemini/Apollo)",
     r"mercury|gemini|apollo|skylab|astronaut"),
    ("1947-1950 Flying Disc era",
     r"flying disc|flying saucer|1947|1948|1949|1950"),
]


def detect_threads(by_rel):
    threads = []
    for label, pat in THREAD_RULES:
        rx = re.compile(pat, re.I)
        hits = {rel: [] for rel, _, _ in RELEASES}
        for rel, _, _ in RELEASES:
            for r in by_rel[rel]:
                hay = " ".join([
                    r.get("title", ""), r.get("summary", ""),
                    r.get("incident_location", ""),
                    r.get("incident_location_inferred", ""),
                ])
                if rx.search(hay):
                    hits[rel].append(r["id"])
        spread = sum(1 for rel in hits if hits[rel])
        threads.append({
            "label": label,
            "releases_spanned": spread,
            "counts": {rel: len(hits[rel]) for rel in hits},
            "ids": hits,
        })
    # Sort: threads that span more releases first, then by total count.
    threads.sort(key=lambda t: (-t["releases_spanned"],
                                -sum(t["counts"].values())))
    return threads


def emergent_vocab(profiles):
    """For each tag family, list tags that appear in a later release but
    were absent (0) in all earlier releases - the 'new vocabulary'."""
    families = ["shape", "behavior", "context", "doc_class", "sensor",
                "by_agency", "by_region", "by_decade"]
    emergent = {rel: {} for rel, _, _ in RELEASES}
    order = [rel for rel, _, _ in RELEASES]
    for fam in families:
        for i, rel in enumerate(order):
            earlier = order[:i]
            cur = set(profiles[rel].get(fam, {}))
            seen_before = set()
            for e in earlier:
                seen_before |= set(profiles[e].get(fam, {}))
            new_here = sorted(cur - seen_before)
            if new_here and i > 0:  # only flag genuinely-new (not R1 baseline)
                emergent[rel][fam] = new_here
    return emergent


def pct(profiles, rel, field, key):
    n = profiles[rel]["n"]
    return round(100 * profiles[rel].get(field, {}).get(key, 0) / n) if n else 0


def compute_headlines(profiles):
    """A few deterministic, notable deltas phrased as short findings.

    Written to be release-count-agnostic: each headline prints the full
    R1..Rn series for its metric so adding a release needs no rewrite.
    """
    order = [k for k, _, _ in RELEASES]
    last = order[-1]

    def series(field, key):
        return " / ".join(f"{r} {pct(profiles, r, field, key)}%" for r in order)

    def redact_series():
        out = []
        for r in order:
            n = profiles[r]["n"]
            out.append(f"{r} {round(100 * profiles[r]['redacted'] / n) if n else 0}%")
        return " / ".join(out)

    H = []
    H.append({
        "title": "Authoring agency rotates each drop",
        "body": (f"DoW share {series('by_agency','DoW')}; FBI {series('by_agency','FBI')}; "
                 f"CIA {series('by_agency','CIA')}. R1 led with DoW+FBI, R2 was a near-pure "
                 f"DoW video dump, R3 swung to FBI+CIA (adding ICA and USG), and R4 tilts "
                 f"back toward DoW with a fresh NASA/DoE contingent.")
    })
    H.append({
        "title": "Geography: CENTCOM → CONUS → maritime/Pacific",
        "body": (f"CENTCOM/Middle-East share {series('by_region','CENTCOM / Middle East')}; "
                 f"CONUS {series('by_region','CONUS / United States')}; "
                 f"INDOPACOM/Pacific {series('by_region','INDOPACOM / Pacific')}. R1/R2 were "
                 f"Gulf-war-zone heavy, R3 pivoted to the US homeland, and R4 broadens again "
                 f"toward maritime and Pacific (East/South China Sea, Yellow Sea, Atlantic).")
    })
    H.append({
        "title": "Redaction & the Featured flag",
        "body": (f"Redacted share {redact_series()}. Featured hero records: "
                 + ", ".join(f"{r} {profiles[r]['featured']}" for r in order) + ". "
                 f"The Featured flag (debuted in R3) continues in R4; redaction rate tracks "
                 f"composition (already-declassified historical files vs contemporary casework).")
    })
    H.append({
        "title": "Asset mix swings document ↔ video each drop",
        "body": (f"PDF share {series('by_type','pdf')}; video {series('by_type','video')}. "
                 f"R2 and R4 are the video-heavy drops (raw DVIDS clips); R1 and R3 are "
                 f"paper-heavy. R4 adds {profiles[last]['by_type'].get('video',0)} new clips.")
    })
    H.append({
        "title": "Historical reach: 1950s-60s and the space program",
        "body": (f"1950s incidents {series('by_decade','1950s')}; 1960s {series('by_decade','1960s')}. "
                 f"R3 opened the CIA Cold-War lane and the Mercury/Gemini NASA expansion; R4 "
                 f"continues the NASA thread (Apollo 14, STS-80 shuttle) and adds DoE Los Alamos "
                 f"conference material.")
    })
    H.append({
        "title": "Object morphology across the four drops",
        "body": (f"sphere/orb {series('shape','sphere/orb')}; disc {series('shape','disc')}; "
                 f"circular {series('shape','circular')}. Descriptive morphology is richest in "
                 f"the document-heavy drops (R1, R3) and thinnest in the video-heavy ones "
                 f"(R2, R4), whose signal lives mostly in clip titles.")
    })
    return H


def main():
    idx = load_index()
    records = [r for r in idx["files"] if r.get("status") != "deprecated"]
    sec_to_rel = {sec: rel for rel, sec, _ in RELEASES}
    by_rel = defaultdict(list)
    for r in records:
        rel = sec_to_rel.get(r.get("page_section"))
        if rel:
            by_rel[rel].append(r)

    profiles = {rel: profile_release(by_rel[rel]) for rel, _, _ in RELEASES}

    # "Featured" is a live-page flag that rotates to the newest drop, so the
    # current index only shows the latest release's featured records. Recover
    # each release's featured-at-launch count from its OWN snapshot manifest.
    for rel, _, date in RELEASES:
        man_path = ROOT / "snapshots" / date / "manifest.json"
        if man_path.exists():
            man = json.loads(man_path.read_text(encoding="utf-8-sig"))
            own = {r["id"] for r in by_rel[rel]}
            profiles[rel]["featured"] = sum(
                1 for a in man.get("assets", [])
                if a.get("featured") and a["id"] in own)

    threads = detect_threads(by_rel)
    emergent = emergent_vocab(profiles)
    headlines = compute_headlines(profiles)

    result = {
        "generated_for": "war-gov-uap-archive",
        "snapshot": RELEASES[-1][2],
        "releases": [{"key": k, "section": s, "date": d, "n": profiles[k]["n"]}
                     for k, s, d in RELEASES],
        "profiles": profiles,
        "emergent_vocab": emergent,
        "headlines": headlines,
        "threads": threads,
    }
    OUT_JSON.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n",
                        encoding="utf-8")
    write_md(result)
    print(f"[release_patterns] wrote {OUT_JSON}")
    print(f"[release_patterns] wrote {OUT_MD}")
    for rel, _, _ in RELEASES:
        p = profiles[rel]
        print(f"  {rel}: n={p['n']} redacted={p['redacted']} featured={p['featured']}")
    return 0


def _top_table(d, n, limit=8):
    rows = list(d.items())[:limit]
    if not rows:
        return "_(none)_\n"
    out = "| tag | count | % of release |\n|---|---|---|\n"
    for k, c in rows:
        out += f"| {k} | {c} | {round(100*c/n,1) if n else 0}% |\n"
    return out


def write_md(result):
    rels = result["releases"]
    keys = " vs ".join(r["key"] for r in rels)
    n_word = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
              6: "six"}.get(len(rels), str(len(rels)))
    L = []
    L.append(f"# Cross-release pattern recognition ({keys})\n")
    L.append(f"Deterministic keyword/metadata profile of the {n_word} war.gov "
             "UAP document drops. Generated by `scripts/release_patterns.py`. The "
             "qualitative companion (deeper reading of document bodies) lives "
             "in `audits/cross_release_patterns.md`.\n")
    L.append("## Release sizes\n")
    L.append("| release | section | dropped | records |\n|---|---|---|---|")
    for r in rels:
        L.append(f"| {r['key']} | {r['section']} | {r['date']} | {r['n']} |")
    L.append("")

    L.append("## Headline shifts\n")
    for h in result.get("headlines", []):
        L.append(f"- **{h['title']}** — {h['body']}")
    L.append("")

    P = result["profiles"]
    order = [r["key"] for r in rels]

    def side_by_side(field, title):
        L.append(f"## {title}\n")
        keys = []
        for rel in order:
            for k in P[rel].get(field, {}):
                if k not in keys:
                    keys.append(k)
        L.append("| tag | " + " | ".join(order) + " |")
        L.append("|---|" + "---|" * len(order))
        for k in keys:
            cells = []
            for rel in order:
                c = P[rel].get(field, {}).get(k, 0)
                n = P[rel]["n"]
                cells.append(f"{c} ({round(100*c/n)}%)" if n else "0")
            L.append(f"| {k} | " + " | ".join(cells) + " |")
        L.append("")

    side_by_side("by_agency", "Authoring agency")
    side_by_side("by_type", "Asset type")
    side_by_side("by_decade", "Incident decade")
    side_by_side("by_region", "Macro-region")
    side_by_side("shape", "Object morphology (shape)")
    side_by_side("behavior", "Kinematics / behavior")
    side_by_side("context", "Witness / context")
    side_by_side("doc_class", "Document class")
    side_by_side("sensor", "Sensor / collection modality")

    L.append("## Redaction & featured\n")
    L.append("| release | redacted | % | featured |\n|---|---|---|---|")
    for rel in order:
        p = P[rel]
        L.append(f"| {rel} | {p['redacted']} | "
                 f"{round(100*p['redacted']/p['n']) if p['n'] else 0}% | {p['featured']} |")
    L.append("")

    L.append("## Emergent vocabulary (new in later releases)\n")
    L.append("Tags/labels first appearing in a release, absent from all "
             "earlier ones.\n")
    for rel in order[1:]:
        ev = result["emergent_vocab"].get(rel, {})
        if not ev:
            continue
        L.append(f"### New in {rel}\n")
        for fam, tags in ev.items():
            L.append(f"- **{fam}**: {', '.join(tags)}")
        L.append("")

    L.append("## Cross-release narrative threads\n")
    L.append("Named incidents/themes traced across releases. A thread spanning "
             "2+ releases means the same story surfaced again in a later drop, "
             "usually in a different evidentiary form.\n")
    L.append("| thread | " + " | ".join(order) + " | releases spanned |")
    L.append("|---|" + "---|" * (len(order) + 1))
    for t in result["threads"]:
        c = t["counts"]
        cells = " | ".join(str(c.get(rel, 0)) for rel in order)
        L.append(f"| {t['label']} | {cells} | {t['releases_spanned']} |")
    L.append("")

    OUT_MD.parent.mkdir(parents=True, exist_ok=True)
    OUT_MD.write_text("\n".join(L) + "\n", encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
