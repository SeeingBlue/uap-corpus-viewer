"""apply_inferred_dates.py - write the audit's confirmed dates back into metadata.

For each record, runs the same audit pipeline as audit_incident_dates.py and
writes two new fields on the per-file JSON:

  incident_date_inferred         e.g. "2023-03" or "1947-06-24"
  incident_date_inferred_source  e.g. "csv+title", "title+sequence", "title-only"

Application policy (per user direction):
  - confirmed            -> always write inferred date (>=2 sources agree)
  - confirmed-by-sequence-> always write inferred date
  - single-source        -> ONLY write when the sole source is the title and
                            the title carries an explicit year. Other single-
                            source cases (csv-only, body-only, summary-only)
                            are too weak to backfill.
  - disagree / no-evidence -> leave alone

The original `incident_date` field is never overwritten. The viewer/index
should prefer `incident_date_inferred` when present.

This script also updates the markdown extracts in deploy/extracted/<id>.md so
the YAML frontmatter and the visible "Incident date" line stay in sync.
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
import audit_incident_dates as audit  # noqa: E402


def gather_rows():
    files = sorted(PER_FILE_DIR.glob("*.json"))
    rows = []
    for f in files:
        rec = json.loads(f.read_text(encoding="utf-8-sig"))
        rec_id = rec.get("id", f.stem)
        title = rec.get("title", "")
        summary = rec.get("summary", "")
        csv_raw = rec.get("incident_date", "")

        csv_c = audit.parse_csv_incident_date(csv_raw)
        title_cs = audit.candidates_from_title(title)
        summary_cs = audit.candidates_from_summary(summary)
        body_cs = audit.candidates_from_body(EXTRACTED_DIR / f"{rec_id}.md")

        v = audit.evaluate(csv_c, title_cs, summary_cs, body_cs)
        family, seq_n = audit.detect_family(title)

        rows.append({
            "id": rec_id,
            "_path": f,
            "title": title,
            "csv_raw": csv_raw,
            "verdict": v.label,
            "confirmed_date": v.confirmed_date,
            "confirming_sources": list(v.confirming_sources),
            "verdict_note": v.note,
            "family": family or "",
            "seq_n": seq_n if seq_n is not None else "",
            "sequence_note": "",
            "_cands": [c for c in [csv_c] + title_cs + summary_cs + body_cs if c],
            "_title_cs": title_cs,
        })

    audit.apply_sequence_inference(rows)
    for r in rows:
        if isinstance(r["confirming_sources"], list):
            pass
        else:
            r["confirming_sources"] = []
    return rows


def decide_inferred(r):
    """Return (inferred_date, source_label) or (None, None) if we shouldn't
    backfill this record."""
    label = r["verdict"]
    sources = r["confirming_sources"] or []
    if label in ("confirmed", "confirmed-by-sequence"):
        return r["confirmed_date"], "+".join(sources)
    if label == "single-source":
        # Only accept when the single signal is a title year. The title is
        # curator-controlled so we trust it more than body or csv-only here.
        title_cs = r["_title_cs"]
        if title_cs and "title" in sources:
            # Use the most specific title candidate
            best = max(title_cs, key=lambda c: audit.precision_score(c.precision))
            return best.normalized(), "title-only"
    return None, None


# ---- markdown frontmatter / body update -------------------------

YAML_INCIDENT_RE = re.compile(r'^(incident_date:\s*"[^"]*")$', re.M)
BODY_INCIDENT_RE = re.compile(r'^(\*\*Incident date:\*\*\s*[^\n]+)$', re.M)


def update_markdown(md_path: Path, inferred: str, source: str, csv_raw: str) -> bool:
    if not md_path.exists():
        return False
    text = md_path.read_text(encoding="utf-8")
    orig = text

    # 1) YAML frontmatter: insert/replace incident_date_inferred + source.
    new_yaml_lines = (
        f'incident_date_inferred: "{inferred}"\n'
        f'incident_date_inferred_source: "{source}"'
    )
    # Drop any pre-existing inferred lines first (idempotency)
    text = re.sub(r'^incident_date_inferred(_source)?:\s*"[^"]*"\n?', "",
                  text, flags=re.M)
    text = YAML_INCIDENT_RE.sub(lambda m: m.group(1) + "\n" + new_yaml_lines, text,
                                count=1)

    # 2) Visible body line: append/replace an "Inferred date" line right
    #    after the existing "Incident date" line.
    inferred_line = (f"**Inferred incident date:** {inferred}  _(source: "
                     f"{source})_  ")
    # Drop existing inferred line for idempotency
    text = re.sub(r'^\*\*Inferred incident date:\*\*[^\n]*\n?', "",
                  text, flags=re.M)
    if BODY_INCIDENT_RE.search(text):
        text = BODY_INCIDENT_RE.sub(
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

        # 1) per-file JSON
        rec = json.loads(r["_path"].read_text(encoding="utf-8-sig"))
        # Remove any prior inferred fields we may have written (idempotency)
        rec.pop("incident_date_inferred", None)
        rec.pop("incident_date_inferred_source", None)
        rec.pop("incident_date_inferred_csv_disagrees", None)

        # Insert after incident_date if present, else append
        new_rec = {}
        for k, v in rec.items():
            new_rec[k] = v
            if k == "incident_date":
                new_rec["incident_date_inferred"] = inferred
                new_rec["incident_date_inferred_source"] = source
                if r["verdict_note"] and "csv" in r["verdict_note"]:
                    new_rec["incident_date_inferred_csv_disagrees"] = True
                    n_disagree_csv += 1
        if "incident_date_inferred" not in new_rec:
            new_rec["incident_date_inferred"] = inferred
            new_rec["incident_date_inferred_source"] = source
        r["_path"].write_text(
            json.dumps(new_rec, indent=4, ensure_ascii=False),
            encoding="utf-8",
        )
        n_written_json += 1

        # 2) markdown extract
        md_path = EXTRACTED_DIR / f"{r['id']}.md"
        if update_markdown(md_path, inferred, source, r["csv_raw"]):
            n_written_md += 1

    # 3) Patch the master index.json files (metadata/index.json and
    #    deploy/metadata/index.json) so build_index.py and the viewer see
    #    the inferred fields.
    inferred_by_id = {}
    for r in rows:
        inferred, source = decide_inferred(r)
        if inferred is None:
            continue
        csv_dis = bool(r["verdict_note"] and "csv" in r["verdict_note"])
        inferred_by_id[r["id"]] = (inferred, source, csv_dis)

    for idx_path in (ROOT / "metadata" / "index.json",
                     ROOT / "deploy" / "metadata" / "index.json"):
        if not idx_path.exists():
            continue
        idx = json.loads(idx_path.read_text(encoding="utf-8-sig"))
        for entry in idx.get("files", []):
            rid = entry.get("id")
            entry.pop("incident_date_inferred", None)
            entry.pop("incident_date_inferred_source", None)
            entry.pop("incident_date_inferred_csv_disagrees", None)
            if rid in inferred_by_id:
                inferred, source, csv_dis = inferred_by_id[rid]
                entry["incident_date_inferred"] = inferred
                entry["incident_date_inferred_source"] = source
                if csv_dis:
                    entry["incident_date_inferred_csv_disagrees"] = True
        idx_path.write_text(
            json.dumps(idx, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )

    print(f"verdict counts:    {counts}")
    print(f"json files written: {n_written_json}")
    print(f"md files updated:   {n_written_md}")
    print(f"csv-disagrees flagged: {n_disagree_csv}")
    print(f"inferred records in index: {len(inferred_by_id)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
