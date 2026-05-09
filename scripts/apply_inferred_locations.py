"""apply_inferred_locations.py - write the audit's confirmed locations back into metadata.

Mirrors apply_inferred_dates.py. For each record, runs the same audit pipeline
as audit_incident_locations.py and writes three new fields on the per-file
JSON, the deploy markdown extract, and both index.json files:

  incident_location_inferred           e.g. "Persian Gulf" or "Greece"
  incident_location_inferred_source    e.g. "csv+title", "title-only", "title+body"
  incident_location_inferred_csv_disagrees  true when csv had a value the inferred
                                            location is not consistent with

Application policy (matches the dates pipeline):
  - confirmed                -> always write inferred
  - confirmed-by-sequence    -> always write inferred
  - csv-vs-title             -> always write inferred (title trusted, csv flagged)
  - single-source            -> ONLY write when the sole source is the title.
                                 Other single-source cases (csv-only, body-only)
                                 are too weak to backfill.
  - disagree / no-evidence   -> leave alone

The original `incident_location` field is never overwritten. The viewer/index
should prefer `incident_location_inferred` when present.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PER_FILE_DIR = ROOT / "metadata" / "per-file"
EXTRACTED_DIR = ROOT / "deploy" / "extracted"

# Reuse the audit's logic
sys.path.insert(0, str(ROOT / "scripts"))
import audit_incident_locations as audit  # noqa: E402


def gather_rows():
    files = sorted(PER_FILE_DIR.glob("*.json"))
    rows = []
    for f in files:
        rec = json.loads(f.read_text(encoding="utf-8-sig"))
        rec_id = rec.get("id", f.stem)
        title = rec.get("title", "")
        summary = rec.get("summary", "")
        csv_raw = rec.get("incident_location", "")

        csv_c      = audit.parse_csv_incident_location(csv_raw)
        title_cs   = audit.candidates_from_title(title)
        summary_cs = audit.candidates_from_summary(summary)
        body_cs    = audit.candidates_from_body(EXTRACTED_DIR / f"{rec_id}.md")

        v = audit.evaluate(csv_c, title_cs, summary_cs, body_cs)
        family, seq_n = audit.detect_family(title)

        rows.append({
            "id": rec_id,
            "_path": f,
            "title": title,
            "csv_raw": csv_raw,
            "csv_norm": csv_c.name if csv_c else "",
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

    audit.apply_sequence_inference(rows)
    for r in rows:
        if not isinstance(r["confirming_sources"], list):
            r["confirming_sources"] = []
    return rows


def decide_inferred(r):
    """Return (inferred_location, source_label) or (None, None) if we shouldn't
    backfill this record."""
    label = r["verdict"]
    sources = r["confirming_sources"] or []
    if label in ("confirmed", "confirmed-by-sequence", "csv-vs-title"):
        return r["confirmed_location"], "+".join(sources)
    if label == "single-source":
        # Only accept when the sole signal is the title. Filename-derived,
        # curator-controlled, more reliable than csv-only or body-only.
        if r["_title_cs"] and "title" in sources:
            best = max(r["_title_cs"], key=lambda c: c.precision_score())
            return best.name, "title-only"
    return None, None


def csv_disagrees(r) -> bool:
    """Return True when the csv had a value that's not consistent with
    (and not a coastline neighbor of) the inferred location."""
    csv_norm = r["csv_norm"]
    inferred = r["confirmed_location"]
    if not csv_norm or not inferred:
        return False
    if audit.consistent(csv_norm, inferred):
        return False
    if audit.coastline_neighbor(csv_norm, inferred):
        return False
    return True


# ---- markdown frontmatter / body update -------------------------

YAML_LOCATION_RE = re.compile(r'^(incident_location:\s*"[^"]*")$', re.M)
BODY_LOCATION_RE = re.compile(r'^(\*\*Incident location:\*\*\s*[^\n]+)$', re.M)


def update_markdown(md_path: Path, inferred: str, source: str, csv_disagree: bool) -> bool:
    if not md_path.exists():
        return False
    text = md_path.read_text(encoding="utf-8")
    orig = text

    # 1) YAML frontmatter: insert/replace incident_location_inferred + source.
    new_yaml_lines = (
        f'incident_location_inferred: "{inferred}"\n'
        f'incident_location_inferred_source: "{source}"'
    )
    if csv_disagree:
        new_yaml_lines += '\nincident_location_inferred_csv_disagrees: true'

    # Drop any pre-existing inferred lines first (idempotency)
    text = re.sub(r'^incident_location_inferred(_source|_csv_disagrees)?:\s*[^\n]*\n?', "",
                  text, flags=re.M)
    text = YAML_LOCATION_RE.sub(lambda m: m.group(1) + "\n" + new_yaml_lines, text,
                                count=1)

    # 2) Visible body line: append/replace an "Inferred location" line right
    #    after the existing "Incident location" line.
    inferred_line_parts = [f"**Inferred incident location:** {inferred}"]
    inferred_line_parts.append(f"_(source: {source})_")
    if csv_disagree:
        inferred_line_parts.append("_(csv disagrees)_")
    inferred_line = "  ".join(inferred_line_parts) + "  "

    # Drop existing inferred line for idempotency
    text = re.sub(r'^\*\*Inferred incident location:\*\*[^\n]*\n?', "",
                  text, flags=re.M)
    if BODY_LOCATION_RE.search(text):
        text = BODY_LOCATION_RE.sub(
            lambda m: m.group(1) + "\n" + inferred_line, text, count=1
        )

    if text != orig:
        md_path.write_text(text, encoding="utf-8")
        return True
    return False


def main():
    rows = gather_rows()
    n_written_json = 0
    n_written_md = 0
    n_disagree_csv = 0
    counts = {}
    for r in rows:
        inferred, source = decide_inferred(r)
        counts[r["verdict"]] = counts.get(r["verdict"], 0) + 1
        if inferred is None:
            continue

        csv_dis = csv_disagrees(r)
        if csv_dis:
            n_disagree_csv += 1

        # 1) per-file JSON
        rec = json.loads(r["_path"].read_text(encoding="utf-8-sig"))
        rec.pop("incident_location_inferred", None)
        rec.pop("incident_location_inferred_source", None)
        rec.pop("incident_location_inferred_csv_disagrees", None)

        # Insert after incident_location if present, else append
        new_rec = {}
        for k, v in rec.items():
            new_rec[k] = v
            if k == "incident_location":
                new_rec["incident_location_inferred"] = inferred
                new_rec["incident_location_inferred_source"] = source
                if csv_dis:
                    new_rec["incident_location_inferred_csv_disagrees"] = True
        if "incident_location_inferred" not in new_rec:
            new_rec["incident_location_inferred"] = inferred
            new_rec["incident_location_inferred_source"] = source
            if csv_dis:
                new_rec["incident_location_inferred_csv_disagrees"] = True
        r["_path"].write_text(
            json.dumps(new_rec, indent=4, ensure_ascii=False),
            encoding="utf-8",
        )
        n_written_json += 1

        # 2) markdown extract
        md_path = EXTRACTED_DIR / f"{r['id']}.md"
        if update_markdown(md_path, inferred, source, csv_dis):
            n_written_md += 1

    # 3) Patch the master index.json files (metadata/index.json and
    #    deploy/metadata/index.json).
    inferred_by_id = {}
    for r in rows:
        inferred, source = decide_inferred(r)
        if inferred is None:
            continue
        inferred_by_id[r["id"]] = (inferred, source, csv_disagrees(r))

    for idx_path in (ROOT / "metadata" / "index.json",
                     ROOT / "deploy" / "metadata" / "index.json"):
        if not idx_path.exists():
            continue
        idx = json.loads(idx_path.read_text(encoding="utf-8-sig"))
        for entry in idx.get("files", []):
            rid = entry.get("id")
            entry.pop("incident_location_inferred", None)
            entry.pop("incident_location_inferred_source", None)
            entry.pop("incident_location_inferred_csv_disagrees", None)
            if rid in inferred_by_id:
                inferred, source, csv_dis = inferred_by_id[rid]
                entry["incident_location_inferred"] = inferred
                entry["incident_location_inferred_source"] = source
                if csv_dis:
                    entry["incident_location_inferred_csv_disagrees"] = True
        idx_path.write_text(
            json.dumps(idx, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )

    print(f"verdict counts:        {counts}")
    print(f"json files written:    {n_written_json}")
    print(f"md files updated:      {n_written_md}")
    print(f"csv-disagrees flagged: {n_disagree_csv}")
    print(f"inferred records in index: {len(inferred_by_id)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
