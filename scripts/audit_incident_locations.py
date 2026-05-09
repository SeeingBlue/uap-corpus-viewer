"""audit_incident_locations.py - cross-check incident_location across sources.

Mirrors audit_incident_dates.py for location data. Walks metadata/per-file/*.json.
For each record, gathers location candidates from csv (incident_location), title,
summary, and the markdown body extract. Verdict:

  1. `confirmed` - 2+ sources agree on a place (or csv is contained in/contains
     a place that title+body agree on).
  2. `confirmed-by-sequence` - record sits in a numbered title family
     (e.g. DOW-UAP-D{N}) where prev/next neighbors agree on a location and
     the current record's csv disagrees while title/body match neighbors.
  3. Otherwise: `single-source`, `disagree`, or `no-evidence`.

Outputs:
  metadata/incident_location_audit.csv
  metadata/incident_location_audit.md
"""

from __future__ import annotations

import csv
import json
import re
import sys
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PER_FILE_DIR = ROOT / "metadata" / "per-file"
EXTRACTED_DIR = ROOT / "deploy" / "extracted"
OUT_CSV = ROOT / "metadata" / "incident_location_audit.csv"
OUT_MD = ROOT / "metadata" / "incident_location_audit.md"


# ---------- Place-name dictionary ----------
# Each entry: (regex pattern, canonical name, kind)
# kind:
#   "country"      - sovereign state, US state, named city / base
#   "water"        - sea / gulf / strait / ocean
#   "region"       - regional grouping (Middle East, North America, Indo-PACOM,
#                    Western United States, ...). Treated as broader than country.
#   "off-earth"    - Moon / Low Earth Orbit (skipped from "containment" reasoning)
PLACES_RAW = [
    # ---- Middle East countries
    (r"\biraq\b",                                      "Iraq",                  "country"),
    (r"\bsyria\b",                                     "Syria",                 "country"),
    (r"\biran\b",                                      "Iran",                  "country"),
    (r"\bkuwait\b",                                    "Kuwait",                "country"),
    (r"\bsaudi(?:\s+arabia)?\b",                       "Saudi Arabia",          "country"),
    (r"\byemen\b",                                     "Yemen",                 "country"),
    (r"\boman\b",                                      "Oman",                  "country"),
    (r"\b(?:uae|united\s+arab\s+emirates)\b",          "United Arab Emirates",  "country"),
    (r"\bqatar\b",                                     "Qatar",                 "country"),
    (r"\bbahrain\b",                                   "Bahrain",               "country"),
    (r"\bisrael\b",                                    "Israel",                "country"),
    (r"\bjordan\b",                                    "Jordan",                "country"),
    (r"\blebanon\b",                                   "Lebanon",               "country"),
    (r"\bturkey\b",                                    "Turkey",                "country"),
    (r"\begypt\b",                                     "Egypt",                 "country"),
    (r"\bdjibouti\b",                                  "Djibouti",              "country"),
    (r"\bsomalia\b",                                   "Somalia",               "country"),
    # ---- Bodies of water
    # Arabian Gulf and Persian Gulf are interchangeable names for the same body.
    (r"\bpersian\s+gulf\b",                            "Persian Gulf",          "water"),
    (r"\barabian\s+gulf\b",                            "Persian Gulf",          "water"),
    (r"\bstrait\s+of\s+hormuz\b",                      "Strait of Hormuz",      "water"),
    (r"\bgulf\s+of\s+aden\b",                          "Gulf of Aden",          "water"),
    (r"\bgulf\s+of\s+oman\b",                          "Gulf of Oman",          "water"),
    (r"\barabian\s+sea\b",                             "Arabian Sea",           "water"),
    (r"\bmediterranean(?:\s+sea)?\b",                  "Mediterranean Sea",     "water"),
    (r"\baegean(?:\s+sea)?\b",                         "Aegean Sea",            "water"),
    (r"\bred\s+sea\b",                                 "Red Sea",               "water"),
    (r"\beast\s+china\s+sea\b",                        "East China Sea",        "water"),
    (r"\bsouth\s+china\s+sea\b",                       "South China Sea",       "water"),
    (r"\bsea\s+of\s+japan\b",                          "Sea of Japan",          "water"),
    (r"\bblack\s+sea\b",                               "Black Sea",             "water"),
    (r"\bcaspian(?:\s+sea)?\b",                        "Caspian Sea",           "water"),
    (r"\bbaltic(?:\s+sea)?\b",                         "Baltic Sea",            "water"),
    (r"\bpacific(?:\s+ocean)?\b",                      "Pacific Ocean",         "water"),
    (r"\batlantic(?:\s+ocean)?\b",                     "Atlantic Ocean",        "water"),
    (r"\bindian\s+ocean\b",                            "Indian Ocean",          "water"),
    # ---- Europe
    (r"\bgreece\b",                                    "Greece",                "country"),
    (r"\bcyprus\b",                                    "Cyprus",                "country"),
    (r"\bgermany\b",                                   "Germany",               "country"),
    (r"\bnetherlands\b",                               "Netherlands",           "country"),
    (r"\bbelgium\b",                                   "Belgium",               "country"),
    (r"\bfrance\b",                                    "France",                "country"),
    (r"\bspain\b",                                     "Spain",                 "country"),
    (r"\bitaly\b",                                     "Italy",                 "country"),
    (r"\b(?:united\s+kingdom|england|britain)\b",      "United Kingdom",        "country"),
    (r"\bireland\b",                                   "Ireland",               "country"),
    (r"\bnorway\b",                                    "Norway",                "country"),
    (r"\bsweden\b",                                    "Sweden",                "country"),
    (r"\bfinland\b",                                   "Finland",               "country"),
    (r"\bdenmark\b",                                   "Denmark",               "country"),
    (r"\biceland\b",                                   "Iceland",               "country"),
    (r"\bpoland\b",                                    "Poland",                "country"),
    (r"\brussia\b",                                    "Russia",                "country"),
    (r"\bukraine\b",                                   "Ukraine",               "country"),
    # ---- Asia / Pacific
    (r"\bjapan\b",                                     "Japan",                 "country"),
    (r"\b(?:china|prc)\b",                             "China",                 "country"),
    (r"\b(?:south\s+korea|north\s+korea|korea)\b",     "Korea",                 "country"),
    (r"\btaiwan\b",                                    "Taiwan",                "country"),
    (r"\bvietnam\b",                                   "Vietnam",               "country"),
    (r"\bphilippines\b",                               "Philippines",           "country"),
    (r"\baustralia\b",                                 "Australia",             "country"),
    (r"\bindia\b",                                     "India",                 "country"),
    (r"\bpakistan\b",                                  "Pakistan",              "country"),
    (r"\bafghanistan\b",                               "Afghanistan",           "country"),
    (r"\bpapua\s+new\s+guinea\b",                      "Papua New Guinea",      "country"),
    # ---- Central Asia / Caucasus
    (r"\bkazakhstan\b",                                "Kazakhstan",            "country"),
    (r"\bturkmenistan\b",                              "Turkmenistan",          "country"),
    (r"\buzbekistan\b",                                "Uzbekistan",            "country"),
    # Tbilisi/Georgia: avoid matching "Georgia, TN" or US state Georgia
    (r"\btbilisi\b|\bgeorgia\b(?!,?\s*(?:tn|usa|us|united))",  "Georgia (country)", "country"),
    (r"\bashgabat\b",                                  "Ashgabat",              "country"),
    (r"\bazerbaijan\b",                                "Azerbaijan",            "country"),
    # ---- Americas
    (r"\bmexico\b",                                    "Mexico",                "country"),
    (r"\bcanada\b",                                    "Canada",                "country"),
    (r"\bbrazil\b",                                    "Brazil",                "country"),
    (r"\bargentina\b",                                 "Argentina",             "country"),
    # ---- US named places / bases
    (r"\boak\s+ridge\b",                               "Oak Ridge, TN",         "country"),
    (r"\bvandenberg\b",                                "Vandenberg AFB",        "country"),
    (r"\bwright[-\s]?patterson\b",                     "Wright-Patterson AFB",  "country"),
    (r"\bandrews\s+a\.?f\.?b?\b",                      "Andrews AFB",           "country"),
    (r"\bedwards\s+a\.?f\.?b?\b",                      "Edwards AFB",           "country"),
    (r"\bnellis\b",                                    "Nellis AFB",            "country"),
    (r"\bdetroit\b",                                   "Detroit, MI",           "country"),
    (r"\butica\b",                                     "Utica, NY",             "country"),
    (r"\bwalesville\b",                                "Walesville, NY",        "country"),
    # US states (kept short — only seen in this corpus)
    (r"\b(?:texas|TX)\b",                              "Texas",                 "country"),
    (r"\b(?:california|CA)\b",                         "California",            "country"),
    (r"\b(?:arizona|AZ)\b",                            "Arizona",               "country"),
    (r"\b(?:nevada|NV)\b",                             "Nevada",                "country"),
    (r"\b(?:new\s+mexico|NM)\b",                       "New Mexico",            "country"),
    (r"\btennessee\b",                                 "Tennessee",             "country"),
    (r"\b(?:florida|FL)\b",                            "Florida",               "country"),
    (r"\bnew\s+york\b",                                "New York",              "country"),
    (r"\bwashington(?!\s*,?\s*d\.?\s*c\.?)\b",         "Washington (state)",    "country"),
    # ---- Regional descriptors
    (r"\bmiddle\s+east\b",                             "Middle East",           "region"),
    (r"\bnorth\s+america\b",                           "North America",         "region"),
    (r"\bindo[-\s]?pacom\b",                           "Indo-PACOM",            "region"),
    (r"\bcentcom\b",                                   "CENTCOM",               "region"),
    (r"\beucom\b",                                     "EUCOM",                 "region"),
    (r"\bwestern\s+united\s+states\b",                 "Western United States", "region"),
    (r"\beastern\s+united\s+states\b",                 "Eastern United States", "region"),
    (r"\bsouthern\s+united\s+states\b",                "Southern United States","region"),
    (r"\bunited\s+states\b(?!\s+navy)",                "United States",         "region"),
    (r"\bpacific\s+time\s+zone\b",                     "Pacific Time Zone",     "region"),
    # ---- Off-Earth
    (r"\bmoon\b|\blunar\b",                            "Moon",                  "off-earth"),
    (r"\blow\s+earth\s+orbit\b|\bLEO\b",               "Low Earth Orbit",       "off-earth"),
]
PLACES = [(re.compile(p, re.IGNORECASE), name, kind) for p, name, kind in PLACES_RAW]

# Containment relationships (parent -> set of children). Used to decide whether
# csv "Middle East" agrees with title "Iraq" (yes — contains).
CONTAINMENT = {
    "Middle East": {
        "Iraq", "Syria", "Iran", "Kuwait", "Saudi Arabia", "Yemen", "Oman",
        "United Arab Emirates", "Qatar", "Bahrain", "Israel", "Jordan",
        "Lebanon", "Egypt", "Turkey",
        "Persian Gulf", "Strait of Hormuz", "Gulf of Aden", "Gulf of Oman",
        "Arabian Sea", "Red Sea",
        "CENTCOM",
    },
    "CENTCOM": {
        "Iraq", "Syria", "Iran", "Kuwait", "Saudi Arabia", "Yemen", "Oman",
        "United Arab Emirates", "Qatar", "Bahrain", "Egypt", "Djibouti",
        "Afghanistan", "Pakistan",
        "Persian Gulf", "Strait of Hormuz", "Gulf of Aden", "Gulf of Oman",
        "Arabian Sea", "Red Sea",
    },
    "Indo-PACOM": {
        "Japan", "China", "Korea", "Taiwan", "Vietnam", "Philippines",
        "Australia", "India", "Papua New Guinea",
        "Pacific Ocean", "Indian Ocean",
        "East China Sea", "South China Sea", "Sea of Japan",
    },
    "EUCOM": {
        "Greece", "Cyprus", "Germany", "Netherlands", "Belgium", "France",
        "Spain", "Italy", "United Kingdom", "Ireland", "Norway", "Sweden",
        "Finland", "Denmark", "Iceland", "Poland",
        "Mediterranean Sea", "Aegean Sea", "Black Sea", "Baltic Sea",
        "North Sea", "Atlantic Ocean",
    },
    "United States": {
        "Western United States", "Eastern United States", "Southern United States",
        "Texas", "California", "Arizona", "Nevada", "New Mexico", "Tennessee",
        "Florida", "New York", "Washington (state)",
        "Oak Ridge, TN", "Vandenberg AFB", "Wright-Patterson AFB",
        "Andrews AFB", "Edwards AFB", "Nellis AFB",
        "Detroit, MI", "Utica, NY", "Walesville, NY",
    },
    "North America": {
        "United States", "Canada", "Mexico",
        # Anything United States contains is also under North America.
    },
    "Western United States": {
        "California", "Arizona", "Nevada", "New Mexico",
        "Vandenberg AFB", "Edwards AFB", "Nellis AFB",
    },
    "Eastern United States": {
        "Tennessee", "New York", "Florida",
        "Oak Ridge, TN", "Andrews AFB", "Detroit, MI", "Utica, NY", "Walesville, NY",
    },
    "Pacific Time Zone": {"California", "Nevada", "Washington (state)"},
}

# Expand North America transitively.
CONTAINMENT["North America"] |= CONTAINMENT["United States"]


# Coastline / shared-geography pairs. These are NOT used for clustering —
# Persian Gulf and UAE are different places — but they DO suppress
# "csv disagrees" notes when csv and inferred are coastal neighbors of the
# same airspace. Order doesn't matter; both directions are checked.
COASTLINE_NEIGHBORS = {
    frozenset(p) for p in (
        ("Persian Gulf", "United Arab Emirates"),
        ("Persian Gulf", "Iran"),
        ("Persian Gulf", "Kuwait"),
        ("Persian Gulf", "Iraq"),
        ("Persian Gulf", "Bahrain"),
        ("Persian Gulf", "Qatar"),
        ("Persian Gulf", "Saudi Arabia"),
        ("Persian Gulf", "Oman"),
        ("Persian Gulf", "Strait of Hormuz"),
        ("Gulf of Oman", "United Arab Emirates"),
        ("Gulf of Oman", "Oman"),
        ("Gulf of Oman", "Iran"),
        ("Strait of Hormuz", "United Arab Emirates"),
        ("Strait of Hormuz", "Iran"),
        ("Strait of Hormuz", "Oman"),
        ("Gulf of Aden", "Yemen"),
        ("Gulf of Aden", "Djibouti"),
        ("Gulf of Aden", "Somalia"),
        ("Gulf of Aden", "Arabian Sea"),
        ("Aegean Sea", "Greece"),
        ("Aegean Sea", "Turkey"),
        ("Aegean Sea", "Mediterranean Sea"),
        ("Mediterranean Sea", "Greece"),
        ("Mediterranean Sea", "Italy"),
        ("Mediterranean Sea", "Egypt"),
        ("Mediterranean Sea", "Israel"),
        ("Mediterranean Sea", "Lebanon"),
        ("Mediterranean Sea", "Syria"),
        ("Mediterranean Sea", "Turkey"),
        ("Mediterranean Sea", "Cyprus"),
        ("Mediterranean Sea", "France"),
        ("Mediterranean Sea", "Spain"),
        ("Red Sea", "Egypt"),
        ("Red Sea", "Saudi Arabia"),
        ("Red Sea", "Yemen"),
        ("Red Sea", "Djibouti"),
        ("Arabian Sea", "Oman"),
        ("Arabian Sea", "Yemen"),
        ("Arabian Sea", "India"),
        ("Arabian Sea", "Pakistan"),
    )
}


def more_specific(child: str, parent: str) -> bool:
    """True iff child is strictly contained in parent under regional containment.
    Strict — does NOT include coastline overlap."""
    if child == parent:
        return False
    return child in CONTAINMENT.get(parent, set())


def coastline_neighbor(a: str, b: str) -> bool:
    """True iff a and b share a coastline / overlapping operational airspace."""
    return frozenset((a, b)) in COASTLINE_NEIGHBORS


def consistent(a: str, b: str) -> bool:
    """Used for clustering: a and b refer to the same place, possibly with one
    more specific than the other. Strict — no coastline overlap."""
    return a == b or more_specific(a, b) or more_specific(b, a)


def geographically_related(a: str, b: str) -> bool:
    """Looser test for verdict notes: are these even in the same neighborhood?
    True iff consistent() OR coastline neighbors."""
    return consistent(a, b) or coastline_neighbor(a, b)


# ---------- Candidate model ----------

@dataclass
class Candidate:
    source: str           # "csv" | "title" | "summary" | "body"
    raw: str              # original matched text
    name: str             # canonical normalized name
    kind: str             # "country" | "water" | "region" | "off-earth"

    def precision_score(self) -> int:
        # specific places > regional groupings
        return {"country": 3, "water": 3, "region": 2, "off-earth": 1}[self.kind]


def _candidates_in_text(text, source, *, slug_mode=False):
    if not text:
        return []
    work = re.sub(r"[-_]+", " ", text) if slug_mode else text
    out = []
    seen = set()
    for rx, name, kind in PLACES:
        m = rx.search(work)
        if m and name not in seen:
            out.append(Candidate(source, m.group(0), name, kind))
            seen.add(name)
    return out


def parse_csv_incident_location(s):
    if not s:
        return None
    s = s.strip()
    if not s or s.upper() in {"N/A", "N\\A", "NONE", "TBD"}:
        return None
    cs = _candidates_in_text(s, "csv")
    if not cs:
        # Free-text we don't recognize — preserve as a literal so the audit
        # still has something to compare against.
        return Candidate("csv", s, s, "country")
    # CSV is short — usually one place. Take the most specific one.
    cs.sort(key=lambda c: -c.precision_score())
    return cs[0]


def candidates_from_title(title):
    return _candidates_in_text(title or "", "title", slug_mode=True)


def candidates_from_summary(summary):
    return _candidates_in_text(summary or "", "summary")


def _strip_md_for_body(md_text):
    text = md_text
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            text = text[end + 4:]
    parts = re.split(r"\n##\s", text, maxsplit=1)
    if len(parts) == 2:
        text = "## " + parts[1]
    return text


# Body phrases that indicate the surrounding text is administrative metadata,
# not a real incident location.
BODY_LOCATION_BLACKLIST = (
    "declassified by", "release date", "approved for release",
    "originating activity", "department of state", "department of war",
    "courtesy of", "copy to", "from:", "to:",
    "bureau of", "consulate", "embassy of",
)


def candidates_from_body(md_path):
    if not md_path.exists():
        return []
    raw = md_path.read_text(encoding="utf-8", errors="replace")
    body = _strip_md_for_body(raw)
    body_lc = body.lower()
    cs_all = []
    for rx, name, kind in PLACES:
        for m in rx.finditer(body):
            idx = m.start()
            window = body_lc[max(0, idx - 60): idx + 60]
            if any(p in window for p in BODY_LOCATION_BLACKLIST):
                continue
            cs_all.append((idx, Candidate("body", m.group(0), name, kind)))
    # De-dupe: keep first occurrence per canonical name.
    seen, out = set(), []
    for idx, c in sorted(cs_all, key=lambda x: x[0]):
        if c.name in seen:
            continue
        seen.add(c.name)
        out.append(c)
    return out


# ---------- Verdict ----------

@dataclass
class Verdict:
    label: str
    confirmed_location: str
    confirming_sources: list = field(default_factory=list)
    note: str = ""


def evaluate(csv_c, title_cs, summary_cs, body_cs):
    # 1) Build the candidate set
    all_cands = ([csv_c] if csv_c else []) + title_cs + summary_cs + body_cs
    if not all_cands:
        return Verdict("no-evidence", "", [], "")

    # 2) Group candidates by canonical name, tracking which sources voted for it
    by_name: dict[str, set[str]] = {}
    by_kind: dict[str, str] = {}
    for c in all_cands:
        by_name.setdefault(c.name, set()).add(c.source)
        by_kind[c.name] = c.kind

    # 3) For every pair (a, b) where a contains b, also count a's votes for b's
    #    sources for the purpose of "agreement at the more specific level".
    #    But we don't WRITE these merged votes — only use them for tie-breaking.

    # 4) Find clusters with 2+ distinct sources voting on consistent places
    #    (same canonical OR via containment).
    candidates_ranked = []  # (votes, precision, name)
    for name in by_name:
        # union of sources for `name` AND any consistent ancestor/descendant
        votes = set(by_name[name])
        for other, srcs in by_name.items():
            if other == name:
                continue
            # Only the more specific name benefits from the broader name's
            # vote (e.g. Iraq benefits from "Middle East") — not the other
            # way around. Strict containment only — coastline overlap does
            # NOT propagate votes (UAE doesn't get votes from Persian Gulf).
            if more_specific(name, other):
                # `other` is broader and strictly contains us; absorb its sources.
                votes |= srcs
        candidates_ranked.append((len(votes), Candidate("", "", name, by_kind[name]).precision_score(), name, votes))

    # Find the strongest cluster:
    # - prefer >=2 distinct sources
    # - prefer specific over regional
    confirmed = None
    candidates_ranked.sort(key=lambda x: (-x[0], -x[1]))
    for n_votes, prec, name, votes in candidates_ranked:
        if n_votes >= 2:
            confirmed = (name, votes, prec)
            break

    if confirmed:
        name, votes, prec = confirmed
        # CSV disagreement note: csv had a value, but it's not consistent with
        # the confirmed place. Coastline neighbors are NOT flagged as
        # disagreements (Persian Gulf <-> UAE is the same airspace).
        note = ""
        if csv_c is not None and csv_c.name != name:
            if more_specific(name, csv_c.name):
                # csv is broader, inferred is the more specific child — fine.
                pass
            elif more_specific(csv_c.name, name):
                note = f"csv `{csv_c.name}` is more specific than the agreed cluster"
            elif coastline_neighbor(csv_c.name, name):
                # Same operational airspace — not a real disagreement.
                pass
            else:
                note = f"csv `{csv_c.name}` disagrees"
        return Verdict("confirmed", name, sorted(votes), note)

    # No 2-source cluster -> single-source, csv-vs-title, or disagree.
    sources_present = {c.source for c in all_cands}
    if len(sources_present) <= 1:
        # Single-source. Pick the most specific candidate.
        best = max(all_cands, key=lambda c: c.precision_score())
        return Verdict("single-source", best.name, [best.source], "")

    # csv vs title pair (with possible body/summary noise that supports neither).
    # Three sub-cases:
    #   1. coastline neighbors        -> confirmed at the country (more specific)
    #   2. one strictly contains other -> confirmed at the more specific name
    #   3. truly disagree              -> trust the title (filename-derived)
    csv_set   = [c for c in all_cands if c.source == "csv"]
    title_set = [c for c in all_cands if c.source == "title"]
    other_set = [c for c in all_cands if c.source not in ("csv", "title")]
    if csv_set and title_set:
        csv_name   = csv_set[0].name
        csv_kind   = csv_set[0].kind
        title_pick = max(title_set, key=lambda c: c.precision_score())
        title_name = title_pick.name
        title_kind = title_pick.kind

        # Does the body/summary noise actually corroborate either side?
        def supports(target):
            return any(consistent(c.name, target) or
                       coastline_neighbor(c.name, target)
                       for c in other_set)
        other_for_csv   = supports(csv_name)
        other_for_title = supports(title_name)

        if consistent(csv_name, title_name):
            prefer = title_name if more_specific(title_name, csv_name) else csv_name
            return Verdict("confirmed", prefer, ["csv", "title"], "")

        if coastline_neighbor(csv_name, title_name):
            # Same operational airspace. Prefer the country over the water.
            if csv_kind == "country" and title_kind == "water":
                prefer = csv_name
            elif title_kind == "country" and csv_kind == "water":
                prefer = title_name
            else:
                prefer = title_name
            return Verdict("confirmed", prefer, ["csv", "title"], "")

        # Real disagreement. If body/summary do not support either side,
        # the title (filename) wins.
        if not other_for_csv and not other_for_title:
            note = f"csv `{csv_name}` disagrees with title (filename)"
            return Verdict("csv-vs-title", title_name, ["title"], note)

    # Multiple sources but no agreement -- disagree.
    sketch = "; ".join(sorted({f"{c.source}={c.name}" for c in all_cands}))
    return Verdict("disagree", "", sorted(sources_present), sketch)


# ---------- Sequence inference ----------

SEQUENCE_PATTERNS = [
    ("DOW-UAP-D",   re.compile(r"DOW-UAP-D(\d+)", re.I)),
    ("DOW-UAP-PR",  re.compile(r"DOW-UAP-PR(\d+)", re.I)),
    ("NASA-UAP-D",  re.compile(r"NASA-UAP-D(\d+)", re.I)),
    ("State-Cable", re.compile(r"State Department UAP Cable (\d+)", re.I)),
    ("FBI-Serial",  re.compile(r"62-HQ-83894_Serial_(\d+)", re.I)),
    ("FBI-Section", re.compile(r"62-HQ-83894_Section_(\d+)", re.I)),
]


def detect_family(title):
    for fam, pat in SEQUENCE_PATTERNS:
        m = pat.search(title or "")
        if m:
            return fam, int(m.group(1))
    return None, None


def apply_sequence_inference(rows):
    """For records in a numbered family, if the immediate prev/next neighbors
    both confirm the same location AND this record's csv contradicts it AND
    the title also matches the neighbors, upgrade to `confirmed-by-sequence`."""
    by_family = {}
    for r in rows:
        if r["family"]:
            by_family.setdefault(r["family"], []).append(r)

    for fam, group in by_family.items():
        group.sort(key=lambda r: r["seq_n"])
        for i, r in enumerate(group):
            if r["verdict"] == "confirmed":
                continue
            # Find the closest prev/next confirmed neighbors
            prev_loc = next_loc = None
            prev_n = next_n = None
            for j in range(i - 1, -1, -1):
                if group[j]["verdict"] == "confirmed":
                    prev_loc = group[j]["confirmed_location"]
                    prev_n = group[j]["seq_n"]
                    break
            for j in range(i + 1, len(group)):
                if group[j]["verdict"] == "confirmed":
                    next_loc = group[j]["confirmed_location"]
                    next_n = group[j]["seq_n"]
                    break
            if not prev_loc and not next_loc:
                continue
            # Need agreement between prev and next (or only one neighbor exists)
            anchor_loc = None
            if prev_loc and next_loc and consistent(prev_loc, next_loc):
                # Pick the more specific one (strict containment only)
                if prev_loc == next_loc:
                    anchor_loc = prev_loc
                elif more_specific(next_loc, prev_loc):
                    # next is more specific child of prev
                    anchor_loc = next_loc
                elif more_specific(prev_loc, next_loc):
                    # prev is more specific child of next
                    anchor_loc = prev_loc
                else:
                    anchor_loc = prev_loc
            elif prev_loc and not next_loc:
                anchor_loc = prev_loc
            elif next_loc and not prev_loc:
                anchor_loc = next_loc
            if not anchor_loc:
                continue

            # Does any of THIS record's title/body candidate equal the anchor or
            # represent a more-specific subset of it? Strict — don't accept a
            # broader match (anchor=Iraq, candidate="Middle East" should NOT
            # promote) and don't accept coastline neighbors (anchor=Iraq,
            # candidate=Persian Gulf should NOT promote — different places).
            def cand_matches_anchor(cand_name):
                return cand_name == anchor_loc or more_specific(cand_name, anchor_loc)

            t_match = any(cand_matches_anchor(c.name) for c in r["_title_cs"])
            b_match = any(cand_matches_anchor(c.name) for c in r["_body_cs"])
            if not (t_match or b_match):
                continue

            sources = []
            if t_match: sources.append("title")
            if b_match: sources.append("body")
            sources.append("sequence")

            r["verdict"] = "confirmed-by-sequence"
            r["confirmed_location"] = anchor_loc
            r["confirming_sources"] = sorted(set(sources))
            pieces = []
            if prev_n is not None:
                pieces.append(f"prev={fam}{prev_n}@{prev_loc}")
            if next_n is not None:
                pieces.append(f"next={fam}{next_n}@{next_loc}")
            r["sequence_note"] = "; ".join(pieces)
            # CSV disagreement note (coastline neighbors are not flagged)
            csv_norm = r["csv_norm"]
            if csv_norm and not consistent(csv_norm, anchor_loc) \
                    and not coastline_neighbor(csv_norm, anchor_loc):
                r["verdict_note"] = (r["verdict_note"] + " | " if r["verdict_note"] else "") + \
                    f"csv `{csv_norm}` disagrees with sequence-anchored `{anchor_loc}`"


# ---------- Reporting ----------

def short(s, n=80):
    s = " ".join((s or "").split())
    return s if len(s) <= n else s[: n - 1] + "…"


def main():
    files = sorted(PER_FILE_DIR.glob("*.json"))
    if not files:
        print(f"no per-file metadata under {PER_FILE_DIR}", file=sys.stderr)
        return 1

    rows = []
    for f in files:
        rec = json.loads(f.read_text(encoding="utf-8-sig"))
        rec_id = rec.get("id", f.stem)
        title = rec.get("title", "")
        summary = rec.get("summary", "")
        csv_raw = rec.get("incident_location", "")

        csv_c = parse_csv_incident_location(csv_raw)
        title_cs   = candidates_from_title(title)
        summary_cs = candidates_from_summary(summary)
        body_cs    = candidates_from_body(EXTRACTED_DIR / f"{rec_id}.md")

        v = evaluate(csv_c, title_cs, summary_cs, body_cs)
        family, seq_n = detect_family(title)

        rows.append({
            "id": rec_id,
            "agency": rec.get("agency", ""),
            "title": title,
            "summary": short(summary, 200),
            "csv_raw": csv_raw,
            "csv_norm": csv_c.name if csv_c else "",
            "title_locs":   "; ".join(c.name for c in title_cs),
            "summary_locs": "; ".join(c.name for c in summary_cs),
            "body_locs":    "; ".join(c.name for c in body_cs[:8]),
            "verdict": v.label,
            "confirmed_location": v.confirmed_location,
            "confirming_sources": list(v.confirming_sources),
            "verdict_note": v.note,
            "family": family or "",
            "seq_n": seq_n if seq_n is not None else "",
            "sequence_note": "",
            "_title_cs": title_cs,
            "_body_cs":  body_cs,
        })

    apply_sequence_inference(rows)

    # Flatten for output
    for r in rows:
        r.pop("_title_cs", None)
        r.pop("_body_cs",  None)
        if isinstance(r["confirming_sources"], list):
            r["confirming_sources"] = ", ".join(r["confirming_sources"])

    # Write CSV
    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = ["id", "agency", "family", "seq_n", "title", "summary",
                  "csv_raw", "csv_norm", "title_locs", "summary_locs",
                  "body_locs", "verdict", "confirmed_location",
                  "confirming_sources", "verdict_note", "sequence_note"]
    with OUT_CSV.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fieldnames)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in fieldnames})

    counts = Counter(r["verdict"] for r in rows)
    csv_disagrees = sum(1 for r in rows
                        if "csv `" in (r["verdict_note"] or "")
                        and "disagrees" in (r["verdict_note"] or ""))

    # Write Markdown
    lines = []
    lines.append("# Incident Location audit\n")
    lines.append(f"Records audited: **{len(rows)}**\n")
    lines.append("Verdict counts:\n")
    for v, n in sorted(counts.items(), key=lambda kv: -kv[1]):
        lines.append(f"- `{v}`: {n}")
    lines.append("")
    lines.append(f"**CSV disagreements flagged:** {csv_disagrees}")
    lines.append("")
    lines.append("**Confirmation rules.** A location is `confirmed` when 2+ of "
                 "{csv, title, summary, body} agree on a place — either by exact "
                 "match or via containment (a CSV value of `Middle East` agrees "
                 "with a title of `Iraq`). A location is `confirmed-by-sequence` "
                 "when the record sits in a numbered family (e.g. DOW-UAP-D{N}) "
                 "where prev/next neighbors agree on a location AND the current "
                 "record's title or body matches them, with the CSV disagreeing.\n")

    def section(title_label, key):
        sub = [r for r in rows if r["verdict"] == key]
        if not sub:
            return
        lines.append(f"\n## {title_label} ({len(sub)})\n")
        for r in sub:
            lines.append(f"### `{r['id']}`")
            if r["family"]:
                lines.append(f"- **family:** `{r['family']}{r['seq_n']}`")
            lines.append(f"- **title:** {r['title']}")
            lines.append(f"- **csv:** `{r['csv_raw']}` -> `{r['csv_norm'] or '-'}`")
            if r["title_locs"]:
                lines.append(f"- **title locations:** {r['title_locs']}")
            if r["summary_locs"]:
                lines.append(f"- **summary locations:** {r['summary_locs']}")
            if r["body_locs"]:
                lines.append(f"- **body locations (top 8):** {r['body_locs']}")
            if r["confirmed_location"]:
                lines.append(f"- **confirmed location:** `{r['confirmed_location']}` "
                             f"(via {r['confirming_sources']})")
            if r["verdict_note"]:
                lines.append(f"- **note:** {r['verdict_note']}")
            if r["sequence_note"]:
                lines.append(f"- **sequence:** {r['sequence_note']}")
            if r["summary"]:
                lines.append(f"- **summary:** {r['summary']}")
            lines.append("")

    section("Disagreements (multiple sources, none corroborate)", "disagree")
    section("Single-source (no corroboration)", "single-source")
    section("No evidence anywhere", "no-evidence")
    section("Confirmed by sequence (neighbors and title/body agree, csv disagrees)", "confirmed-by-sequence")
    section("Confirmed (>=2 sources agree)", "confirmed")

    OUT_MD.write_text("\n".join(lines), encoding="utf-8")

    print(f"wrote {OUT_CSV.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")
    print("verdict counts:", dict(counts))
    print(f"csv disagreements: {csv_disagrees}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
