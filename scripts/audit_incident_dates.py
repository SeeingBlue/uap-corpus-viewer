"""audit_incident_dates.py - cross-check incident_date across sources.

Walks metadata/per-file/*.json. For each record, gathers date candidates from
csv (incident_date), title, summary, and the markdown body extract. Verdict:

  1. `confirmed` - 2+ sources agree at year+month or better.
  2. `confirmed-by-sequence` - record in a numbered title family (e.g.
     DOW-UAP-D{N}) has a candidate that fits the date range implied by its
     nearest confirmed prev/next neighbors.
  3. Otherwise: `single-source`, `disagree`, or `no-evidence`.

Outputs:
  metadata/incident_date_audit.csv
  metadata/incident_date_audit.md
"""

from __future__ import annotations

import csv
import json
import re
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PER_FILE_DIR = ROOT / "metadata" / "per-file"
EXTRACTED_DIR = ROOT / "deploy" / "extracted"
OUT_CSV = ROOT / "metadata" / "incident_date_audit.csv"
OUT_MD = ROOT / "metadata" / "incident_date_audit.md"

MONTHS = {
    "january": 1, "february": 2, "march": 3, "april": 4, "may": 5, "june": 6,
    "july": 7, "august": 8, "september": 9, "october": 10,
    "november": 11, "december": 12,
    "jan": 1, "feb": 2, "mar": 3, "apr": 4, "jun": 6, "jul": 7,
    "aug": 8, "sep": 9, "sept": 9, "oct": 10, "nov": 11, "dec": 12,
}
MONTH_RE = "(?:" + "|".join(sorted(MONTHS, key=len, reverse=True)) + ")"

BODY_DATE_BLACKLIST_PHRASES = (
    "declassified on", "declassified by", "declassification date",
    "approved for release", "release date", "date of release",
    "date received", "date of receipt", "date forwarded", "date completed",
    "report date", "reporting date", "date of report", "as of",
    "fy", "cy", "mdr", "page ", "exemption",
)

SEQUENCE_PATTERNS = [
    ("DOW-UAP-D",   re.compile(r"DOW-UAP-D(\d+)", re.I)),
    ("DOW-UAP-PR",  re.compile(r"DOW-UAP-PR(\d+)", re.I)),
    ("NASA-UAP-D",  re.compile(r"NASA-UAP-D(\d+)", re.I)),
    ("State-Cable", re.compile(r"State Department UAP Cable (\d+)", re.I)),
    ("FBI-Serial",  re.compile(r"62-HQ-83894_Serial_(\d+)", re.I)),
    ("FBI-Section", re.compile(r"62-HQ-83894_Section_(\d+)", re.I)),
]


@dataclass
class Candidate:
    source: str
    raw: str
    precision: str
    year: int
    month: int | None = None
    day: int | None = None

    def normalized(self) -> str:
        if self.precision == "ymd":
            return f"{self.year:04d}-{self.month:02d}-{self.day:02d}"
        if self.precision == "ym":
            return f"{self.year:04d}-{self.month:02d}"
        return f"{self.year:04d}"


def precision_score(p: str) -> int:
    return {"ymd": 3, "ym": 2, "y": 1}[p]


def _resolve_2digit(yy: int) -> int:
    return 1900 + yy if yy >= 27 else 2000 + yy


def _valid_ymd(y, m, d):
    try:
        date(y, m, d)
    except ValueError:
        return False
    return 1900 <= y <= 2030


def _valid_y(y):
    return 1900 <= y <= 2030


def _candidates_in_text(text, source, allow_year_only=True, slug_mode=False):
    if not text:
        return []
    work = re.sub(r"[-_]+", " ", text) if slug_mode else text
    work_lc = work.lower()
    out = []

    for m in re.finditer(r"\b(\d{4})-(\d{1,2})-(\d{1,2})\b", work):
        y, mo, d = int(m.group(1)), int(m.group(2)), int(m.group(3))
        if _valid_ymd(y, mo, d):
            out.append(Candidate(source, m.group(0), "ymd", y, mo, d))

    for sep in ("/", r"\\", "-"):
        for m in re.finditer(rf"\b(\d{{1,2}}){sep}(\d{{1,2}}){sep}(\d{{4}})\b", work):
            mo, d, y = int(m.group(1)), int(m.group(2)), int(m.group(3))
            if _valid_ymd(y, mo, d):
                out.append(Candidate(source, m.group(0), "ymd", y, mo, d))
    for sep in ("/", r"\\"):
        for m in re.finditer(rf"\b(\d{{1,2}}){sep}(\d{{1,2}}){sep}(\d{{2}})\b(?!\d)", work):
            mo, d, yy = int(m.group(1)), int(m.group(2)), int(m.group(3))
            y = _resolve_2digit(yy)
            if _valid_ymd(y, mo, d):
                out.append(Candidate(source, m.group(0), "ymd", y, mo, d))

    for m in re.finditer(rf"\b({MONTH_RE})\s+(\d{{1,2}}),?\s+(\d{{4}})\b", work_lc):
        mo, d, y = MONTHS[m.group(1)], int(m.group(2)), int(m.group(3))
        if _valid_ymd(y, mo, d):
            out.append(Candidate(source, m.group(0), "ymd", y, mo, d))
    for m in re.finditer(rf"\b(\d{{1,2}})\s+({MONTH_RE})\s+(\d{{4}})\b", work_lc):
        d, mo, y = int(m.group(1)), MONTHS[m.group(2)], int(m.group(3))
        if _valid_ymd(y, mo, d):
            out.append(Candidate(source, m.group(0), "ymd", y, mo, d))

    for m in re.finditer(rf"\b({MONTH_RE})\s+(\d{{4}})\b", work_lc):
        mo, y = MONTHS[m.group(1)], int(m.group(2))
        if _valid_y(y):
            out.append(Candidate(source, m.group(0), "ym", y, mo))

    if allow_year_only:
        for m in re.finditer(r"(?<!\d)(19[3-9]\d|20[0-2]\d)(?!\d)", work):
            out.append(Candidate(source, m.group(0), "y", int(m.group(1))))

    by_norm = {}
    for c in out:
        by_norm.setdefault(c.normalized(), c)
    cands = list(by_norm.values())
    ymd_year_months = {(c.year, c.month) for c in cands if c.precision == "ymd"}
    specific_years = {c.year for c in cands if c.precision in ("ym", "ymd")}
    return [c for c in cands
            if not (c.precision == "y" and c.year in specific_years)
            and not (c.precision == "ym" and (c.year, c.month) in ymd_year_months)]


def parse_csv_incident_date(s):
    if not s:
        return None
    s = s.strip()
    if not s or s.upper() in {"N/A", "N\\A"}:
        return None
    cs = _candidates_in_text(s, "csv")
    if not cs:
        return None
    cs.sort(key=lambda c: -precision_score(c.precision))
    return cs[0]


def candidates_from_title(title):
    return _candidates_in_text(title or "", "title", slug_mode=True)


def candidates_from_summary(summary):
    return _candidates_in_text(summary or "", "summary", allow_year_only=False)


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


def candidates_from_body(md_path):
    if not md_path.exists():
        return []
    raw = md_path.read_text(encoding="utf-8", errors="replace")
    body = _strip_md_for_body(raw)
    body_lc = body.lower()
    cs = _candidates_in_text(body, "body", allow_year_only=False)
    keep = []
    for c in cs:
        idx = body.find(c.raw)
        if idx == -1:
            keep.append(c); continue
        window = body_lc[max(0, idx - 60): idx + len(c.raw) + 60]
        if any(p in window for p in BODY_DATE_BLACKLIST_PHRASES):
            continue
        keep.append(c)
    return keep


def cands_compatible(a, b):
    """Strict pairwise compatibility (used for sequence-range checks). Two
    candidates are compatible if the more specific fits inside the less
    specific. ymd vs ymd needs same day."""
    if a.year != b.year:
        return False
    if a.precision == "y" and b.precision == "y":
        return a.source != "body" and b.source != "body"
    if a.precision == "y" or b.precision == "y":
        return True
    if a.month != b.month:
        return False
    if a.precision == "ym" or b.precision == "ym":
        return True
    return a.day == b.day


def cluster_at_level(cands, level):
    """Group candidates by their (year[, month[, day]]) at the given level.
    Returns dict[key] -> list[Candidate]. Candidates whose precision is
    coarser than the level are skipped (e.g. year-only at ym level)."""
    groups = {}
    for c in cands:
        if level == "ymd" and c.precision != "ymd":
            continue
        if level == "ym" and c.precision == "y":
            continue
        if level == "ymd":
            key = (c.year, c.month, c.day)
        elif level == "ym":
            key = (c.year, c.month)
        else:
            key = (c.year,)
        groups.setdefault(key, []).append(c)
    return groups


def find_best_cluster(all_cands):
    """Find the strongest agreement: highest precision level with >=2 distinct
    sources. Year-level clusters require at least one non-body source."""
    for level in ("ymd", "ym", "y"):
        groups = cluster_at_level(all_cands, level)
        best = None
        for key, items in groups.items():
            sources = {x.source for x in items}
            if len(sources) < 2:
                continue
            if level == "y" and all(s == "body" for s in sources):
                continue
            score = (len(sources),
                     sum(precision_score(x.precision) for x in items))
            if best is None or score > best[0]:
                best = (score, level, key, sources, items)
        if best:
            return best
    return None


@dataclass
class Verdict:
    label: str
    confirmed_date: str
    confirming_sources: list
    note: str = ""


def evaluate(csv_c, title_cs, summary_cs, body_cs):
    all_cands = ([csv_c] if csv_c else []) + title_cs + summary_cs + body_cs
    if not all_cands:
        return Verdict("no-evidence", "", [], "")

    best = find_best_cluster(all_cands)
    if best is not None:
        score, level, key, sources, items = best
        # Confirmed date: strongest precision representative whose key matches
        # at this level.
        if level == "ymd":
            rep = items[0]
            confirmed = f"{key[0]:04d}-{key[1]:02d}-{key[2]:02d}"
        elif level == "ym":
            confirmed = f"{key[0]:04d}-{key[1]:02d}"
        else:
            confirmed = f"{key[0]:04d}"
        note = ""
        if csv_c is not None and csv_c.source not in sources:
            note = f"csv `{csv_c.normalized()}` disagrees"
        elif csv_c is not None and level == "ym" and csv_c.precision == "ymd":
            # CSV had a specific day but didn't match the cluster's day - note
            # which source disagreed at day-level.
            day_disagreers = [x for x in items
                              if x.source != "csv" and x.precision == "ymd"
                              and x.day != csv_c.day]
            if day_disagreers:
                note = (f"csv day {csv_c.day} differs from " +
                        ", ".join(f"{x.source} day {x.day}" for x in day_disagreers))
        return Verdict("confirmed", confirmed, sorted(sources), note)

    sources_present = {c.source for c in all_cands}
    if len(sources_present) <= 1:
        return Verdict("single-source", "", list(sources_present), "")
    return Verdict("disagree", "", list(sources_present), "")


def detect_family(title):
    for fam, pat in SEQUENCE_PATTERNS:
        m = pat.search(title or "")
        if m:
            return fam, int(m.group(1))
    return None, None


def normalized_to_ordinal(norm):
    if not norm:
        return None
    parts = norm.split("-")
    if len(parts) == 3:
        return (int(parts[0]), int(parts[1]), int(parts[2]))
    if len(parts) == 2:
        return (int(parts[0]), int(parts[1]), 15)
    return (int(parts[0]), 6, 15)


def cand_overlaps_range(cand, lo, hi):
    if cand.precision == "ymd":
        cand_lo = cand_hi = (cand.year, cand.month, cand.day)
    elif cand.precision == "ym":
        cand_lo = (cand.year, cand.month, 1)
        nm = cand.month + 1
        ny = cand.year + (1 if nm == 13 else 0)
        nm = 1 if nm == 13 else nm
        cand_hi = (ny, nm, 1)
    else:
        cand_lo = (cand.year, 1, 1)
        cand_hi = (cand.year + 1, 1, 1)
    return not (cand_hi < lo or cand_lo > hi)


def apply_sequence_inference(rows):
    by_family = {}
    for r in rows:
        if r["family"]:
            by_family.setdefault(r["family"], []).append(r)
    for fam, group in by_family.items():
        group.sort(key=lambda r: r["seq_n"])
        for r in group:
            r["_ord"] = normalized_to_ordinal(r["confirmed_date"]) if r["verdict"] == "confirmed" else None

        for i, r in enumerate(group):
            if r["verdict"] == "confirmed":
                continue
            prev_o = next_o = None
            prev_n = next_n = None
            for j in range(i - 1, -1, -1):
                if group[j]["_ord"] is not None:
                    prev_o = group[j]["_ord"]; prev_n = group[j]["seq_n"]; break
            for j in range(i + 1, len(group)):
                if group[j]["_ord"] is not None:
                    next_o = group[j]["_ord"]; next_n = group[j]["seq_n"]; break
            if prev_o is None and next_o is None:
                continue
            lo = prev_o or (1900, 1, 1)
            hi = next_o or (2030, 12, 31)
            if lo > hi:
                r["sequence_note"] = (
                    f"{fam} neighbors disagree with sequence direction "
                    f"({prev_n}={prev_o}, {next_n}={next_o})"
                )
                continue

            cands = r["_cands"]
            if not cands:
                # Record has no date candidates at all - suggest the implied range.
                r["verdict"] = "sequence-suggests"
                r["confirmed_date"] = ""
                r["confirming_sources"] = ["sequence"]
                pieces = []
                if prev_n is not None:
                    prev_row = next(g for g in group if g["seq_n"] == prev_n)
                    pieces.append(f"prev={fam}{prev_n}@{prev_row['confirmed_date']}")
                if next_n is not None:
                    next_row = next(g for g in group if g["seq_n"] == next_n)
                    pieces.append(f"next={fam}{next_n}@{next_row['confirmed_date']}")
                r["sequence_note"] = "; ".join(pieces) + f"; implied range {lo}..{hi}"
                continue

            fitting = [c for c in cands if cand_overlaps_range(c, lo, hi)]
            non_fitting = [c for c in cands if not cand_overlaps_range(c, lo, hi)]

            if fitting:
                best = max(fitting, key=lambda c: precision_score(c.precision))
                r["verdict"] = "confirmed-by-sequence"
                r["confirmed_date"] = best.normalized()
                r["confirming_sources"] = sorted({best.source, "sequence"})
                pieces = []
                if prev_n is not None:
                    prev_row = next(g for g in group if g["seq_n"] == prev_n)
                    pieces.append(f"prev={fam}{prev_n}@{prev_row['confirmed_date']}")
                if next_n is not None:
                    next_row = next(g for g in group if g["seq_n"] == next_n)
                    pieces.append(f"next={fam}{next_n}@{next_row['confirmed_date']}")
                r["sequence_note"] = "; ".join(pieces)
                if non_fitting:
                    r["sequence_note"] += "; non-fit sources: " + ", ".join(
                        f"{c.source}={c.normalized()}" for c in non_fitting
                    )
            elif cands:
                r["sequence_note"] = (
                    f"all candidates fall outside {fam}{prev_n}..{next_n} "
                    f"range [{prev_o}..{next_o}]"
                )


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
        csv_raw = rec.get("incident_date", "")

        csv_c = parse_csv_incident_date(csv_raw)
        title_cs = candidates_from_title(title)
        summary_cs = candidates_from_summary(summary)
        body_cs = candidates_from_body(EXTRACTED_DIR / f"{rec_id}.md")

        v = evaluate(csv_c, title_cs, summary_cs, body_cs)
        family, seq_n = detect_family(title)

        rows.append({
            "id": rec_id,
            "agency": rec.get("agency", ""),
            "title": title,
            "summary": short(summary, 200),
            "csv_raw": csv_raw,
            "csv_norm": csv_c.normalized() if csv_c else "",
            "title_dates": "; ".join(c.normalized() for c in title_cs),
            "summary_dates": "; ".join(c.normalized() for c in summary_cs),
            "body_dates": "; ".join(c.normalized() for c in body_cs),
            "verdict": v.label,
            "confirmed_date": v.confirmed_date,
            "confirming_sources": ", ".join(v.confirming_sources),
            "verdict_note": v.note,
            "family": family or "",
            "seq_n": seq_n if seq_n is not None else "",
            "sequence_note": "",
            "_cands": [c for c in [csv_c] + title_cs + summary_cs + body_cs if c],
        })

    apply_sequence_inference(rows)

    for r in rows:
        r.pop("_cands", None)
        r.pop("_ord", None)
        if isinstance(r["confirming_sources"], list):
            r["confirming_sources"] = ", ".join(r["confirming_sources"])

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = ["id", "agency", "family", "seq_n", "title", "summary",
                  "csv_raw", "csv_norm", "title_dates", "summary_dates",
                  "body_dates", "verdict", "confirmed_date",
                  "confirming_sources", "verdict_note", "sequence_note"]
    with OUT_CSV.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fieldnames)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in fieldnames})

    counts = {}
    for r in rows:
        counts[r["verdict"]] = counts.get(r["verdict"], 0) + 1

    lines = []
    lines.append("# Incident Date audit (v2)\n")
    lines.append(f"Records audited: **{len(rows)}**\n")
    lines.append("Verdict counts:\n")
    for v, n in sorted(counts.items(), key=lambda kv: -kv[1]):
        lines.append(f"- `{v}`: {n}")
    lines.append("")
    lines.append("**Confirmation rules.** A date is `confirmed` when 2+ of "
                 "{csv, title, summary, body} agree at year+month precision or "
                 "better (year-only matches don't count). A date is "
                 "`confirmed-by-sequence` when the record sits in a numbered "
                 "title family (e.g. DOW-UAP-D{N}) and one of its candidates "
                 "fits the date range implied by the nearest confirmed prev/"
                 "next neighbors.\n")

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
            if r["title_dates"]:
                lines.append(f"- **title dates:** {r['title_dates']}")
            if r["summary_dates"]:
                lines.append(f"- **summary dates:** {r['summary_dates']}")
            if r["body_dates"]:
                lines.append(f"- **body dates (filtered):** {r['body_dates']}")
            if r["confirmed_date"]:
                lines.append(f"- **confirmed date:** `{r['confirmed_date']}` "
                             f"(via {r['confirming_sources']})")
            if r["verdict_note"]:
                lines.append(f"- **note:** {r['verdict_note']}")
            if r["sequence_note"]:
                lines.append(f"- **sequence:** {r['sequence_note']}")
            if r["summary"]:
                lines.append(f"- **summary:** {r['summary']}")
            lines.append("")

    section("Disagreements (multiple sources, none corroborate)", "disagree")
    section("Sequence suggests a range (no direct candidates)", "sequence-suggests")
    section("Single-source (no corroboration)", "single-source")
    section("No evidence anywhere", "no-evidence")
    section("Confirmed by sequence (sole source fits neighbor range)", "confirmed-by-sequence")
    section("Confirmed (>=2 sources agree)", "confirmed")

    OUT_MD.write_text("\n".join(lines), encoding="utf-8")

    print(f"wrote {OUT_CSV.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")
    print("verdict counts:", counts)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
