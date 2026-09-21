"""release_catalog.py - compact per-release catalog for analysis workflows.

Writes metadata/release_catalog.json: {"R1": [...], "R2": [...], ...} with
one small dict per active record (id, agency, type, title, incident_date,
incident_location, redaction, featured, summary, extracted). It is the
slice of index.json that the qualitative cross-release read
(audits/cross_release_patterns.md) and the Patterns-tab card work consume,
so it deliberately carries no fetch/hash bookkeeping.

`featured` is featured-AT-LAUNCH, read from each release's own snapshot
manifest - the live CSV flag rotates to the newest drop, so index.json
alone would show every earlier release as 0.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from release_patterns import RELEASES  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "metadata" / "index.json"
OUT = ROOT / "metadata" / "release_catalog.json"


def main():
    idx = json.loads(INDEX.read_text(encoding="utf-8-sig"))
    sec_to_rel = {sec: rel for rel, sec, _ in RELEASES}

    featured_at_launch = set()
    for _, _, date in RELEASES:
        man = ROOT / "snapshots" / date / "manifest.json"
        if man.exists():
            for a in json.loads(man.read_text(encoding="utf-8-sig")).get("assets", []):
                if a.get("featured"):
                    featured_at_launch.add((a["id"], a.get("page_section")))

    catalog = {rel: [] for rel, _, _ in RELEASES}
    for r in idx["files"]:
        if r.get("status") == "deprecated":
            continue
        rel = sec_to_rel.get(r.get("page_section"))
        if not rel:
            continue
        catalog[rel].append({
            "id": r["id"],
            "agency": r.get("agency", ""),
            "type": r.get("type", ""),
            "title": r.get("title", ""),
            "incident_date": r.get("incident_date", ""),
            "incident_location": r.get("incident_location", ""),
            "redaction": (r.get("redaction") or "").upper() == "TRUE",
            "featured": (r["id"], r.get("page_section")) in featured_at_launch,
            "summary": r.get("summary", ""),
            "extracted": r.get("extracted_text_path") or "",
        })

    OUT.write_text(json.dumps(catalog, indent=2, ensure_ascii=False) + "\n",
                   encoding="utf-8")
    print(f"[release_catalog] wrote {OUT}")
    for rel, _, _ in RELEASES:
        n = len(catalog[rel])
        print(f"  {rel}: n={n} featured={sum(1 for x in catalog[rel] if x['featured'])} "
              f"extracted={sum(1 for x in catalog[rel] if x['extracted'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
