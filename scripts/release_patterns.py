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
    """A few deterministic, notable deltas phrased as short findings."""
    H = []

    def top(rel, field):
        d = profiles[rel].get(field, {})
        return max(d, key=d.get) if d else "-"

    H.append({
        "title": "Authoring agency rotates each drop",
        "body": (f"R1 led with DoW + FBI ({pct(profiles,'R1','by_agency','DoW')}% / "
                 f"{pct(profiles,'R1','by_agency','FBI')}%); R2 was a near-pure DoW "
                 f"video dump ({pct(profiles,'R2','by_agency','DoW')}% DoW, 0% FBI); "
                 f"R3 swings to FBI + CIA ({pct(profiles,'R3','by_agency','FBI')}% FBI, "
                 f"{pct(profiles,'R3','by_agency','CIA')}% CIA) and introduces ICA and USG.")
    })
    H.append({
        "title": "Geography flips from CENTCOM to CONUS",
        "body": (f"CENTCOM/Middle-East share: R1 {pct(profiles,'R1','by_region','CENTCOM / Middle East')}%, "
                 f"R2 {pct(profiles,'R2','by_region','CENTCOM / Middle East')}%, "
                 f"R3 {pct(profiles,'R3','by_region','CENTCOM / Middle East')}%. "
                 f"CONUS share climbs to {pct(profiles,'R3','by_region','CONUS / United States')}% in R3 — "
                 f"the newest drop is a domestic-US story (Western US, Colorado Springs, Northeastern orbs).")
    })
    H.append({
        "title": "Redaction collapses in R3",
        "body": (f"Redacted share: R1 {round(100*profiles['R1']['redacted']/profiles['R1']['n'])}%, "
                 f"R2 {round(100*profiles['R2']['redacted']/profiles['R2']['n'])}%, "
                 f"R3 {round(100*profiles['R3']['redacted']/profiles['R3']['n'])}%. "
                 f"R3 also debuts the 'Featured' flag with {profiles['R3']['featured']} hero records — "
                 f"a more curated, less-redacted presentation.")
    })
    H.append({
        "title": "Asset mix: documents → video → documents",
        "body": (f"PDF share: R1 {pct(profiles,'R1','by_type','pdf')}%, "
                 f"R2 {pct(profiles,'R2','by_type','pdf')}%, R3 {pct(profiles,'R3','by_type','pdf')}%. "
                 f"R2 was {pct(profiles,'R2','by_type','video')}% video (raw DVIDS clips); R3 returns "
                 f"to a paper-heavy mix with a wave of FBI still images.")
    })
    H.append({
        "title": "R3 reaches deeper into the 1950s-60s",
        "body": (f"Mid-century incidents jump in R3: 1950s {pct(profiles,'R3','by_decade','1950s')}% "
                 f"(R1 {pct(profiles,'R1','by_decade','1950s')}%), 1960s {pct(profiles,'R3','by_decade','1960s')}% "
                 f"(R1 {pct(profiles,'R1','by_decade','1960s')}%) — driven by CIA Cold-War files and the "
                 f"Mercury/Gemini NASA expansion.")
    })
    H.append({
        "title": "Shape vocabulary returns in R3",
        "body": (f"R2's raw clips carried almost no descriptive language; R3 restores rich morphology — "
                 f"sphere/orb {pct(profiles,'R3','shape','sphere/orb')}%, disc {pct(profiles,'R3','shape','disc')}%, "
                 f"circular {pct(profiles,'R3','shape','circular')}% — closer to R1's witness-narrative texture "
                 f"(sphere/orb {pct(profiles,'R1','shape','sphere/orb')}%).")
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
    threads = detect_threads(by_rel)
    emergent = emergent_vocab(profiles)
    headlines = compute_headlines(profiles)

    result = {
        "generated_for": "war-gov-uap-archive",
        "snapshot": "2026-06-12",
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
    L = []
    L.append("# Cross-release pattern recognition (R1 vs R2 vs R3)\n")
    L.append("Deterministic keyword/metadata profile of the three war.gov UAP "
             "document drops. Generated by `scripts/release_patterns.py`. The "
             "qualitative companion (deeper reading of document bodies) lives "
             "in `audits/cross_release_patterns.md`.\n")
    rels = result["releases"]
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

    def side_by_side(field, title):
        L.append(f"## {title}\n")
        keys = []
        for rel in ("R1", "R2", "R3"):
            for k in P[rel].get(field, {}):
                if k not in keys:
                    keys.append(k)
        L.append("| tag | R1 | R2 | R3 |")
        L.append("|---|---|---|---|")
        for k in keys:
            r1 = P["R1"].get(field, {}).get(k, 0)
            r2 = P["R2"].get(field, {}).get(k, 0)
            r3 = P["R3"].get(field, {}).get(k, 0)
            n1, n2, n3 = P["R1"]["n"], P["R2"]["n"], P["R3"]["n"]
            def pct(c, n):
                return f"{c} ({round(100*c/n)}%)" if n else "0"
            L.append(f"| {k} | {pct(r1,n1)} | {pct(r2,n2)} | {pct(r3,n3)} |")
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
    for rel in ("R1", "R2", "R3"):
        p = P[rel]
        L.append(f"| {rel} | {p['redacted']} | "
                 f"{round(100*p['redacted']/p['n']) if p['n'] else 0}% | {p['featured']} |")
    L.append("")

    L.append("## Emergent vocabulary (new in R2 / R3)\n")
    L.append("Tags/labels first appearing in a release, absent from all "
             "earlier ones.\n")
    for rel in ("R2", "R3"):
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
    L.append("| thread | R1 | R2 | R3 | releases spanned |")
    L.append("|---|---|---|---|---|")
    for t in result["threads"]:
        c = t["counts"]
        L.append(f"| {t['label']} | {c['R1']} | {c['R2']} | {c['R3']} | "
                 f"{t['releases_spanned']} |")
    L.append("")

    OUT_MD.parent.mkdir(parents=True, exist_ok=True)
    OUT_MD.write_text("\n".join(L) + "\n", encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
