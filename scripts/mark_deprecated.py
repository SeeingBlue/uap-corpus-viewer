"""mark_deprecated.py - flag records that no longer appear in the latest manifest.

After a new snapshot, some records in metadata/index.json may no longer
appear in the latest snapshots/<date>/manifest.json because:

  - The source CSV de-duplicated records that pointed to the same URL
    (R2 dropped duplicates of dow-uap-d23 UAE and dow-uap-d32 Syria).
  - The source CSV corrected a broken `PDF | Image Link` URL; the
    corrected URL produced a new ID. The old ID now points at a stale
    or wrong-content file.

We don't delete these records (the on-disk files are real artifacts; the
provenance trail is worth keeping), but we mark them so:

  - 03_verify.py skips them
  - audit scripts skip them
  - downstream consumers know they're not part of the current corpus

Sets `status` to `deprecated` and writes a reason into `notes`. Idempotent.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import (  # noqa: E402
    INDEX_PATH, PER_FILE_DIR, SNAPSHOTS_DIR, load_json, now_iso, save_json,
)


def latest_manifest_ids():
    snap_dirs = sorted(p for p in SNAPSHOTS_DIR.iterdir() if p.is_dir())
    for d in reversed(snap_dirs):
        m = d / "manifest.json"
        if m.exists():
            data = load_json(m)
            return d.name, {a["id"] for a in data.get("assets", [])}
    return None, set()


def main() -> int:
    snap_date, current_ids = latest_manifest_ids()
    if not current_ids:
        print("[deprecate] no manifest found.", file=sys.stderr)
        return 2
    print(f"[deprecate] checking against manifest snapshot {snap_date}: "
          f"{len(current_ids)} active IDs")

    index = load_json(INDEX_PATH)
    if not index:
        print("[deprecate] no index.json.", file=sys.stderr)
        return 2

    changed = 0
    for rec in index.get("files", []):
        if rec["id"] in current_ids:
            # If a previously-deprecated record reappears in a future
            # manifest, reactivate it so it's eligible for fetch/verify.
            if rec.get("status") == "deprecated":
                rec["status"] = "ok" if rec.get("sha256") else "pending"
                rec["notes"] = (rec.get("notes") or "") + \
                    f" | reactivated {now_iso()}"
                changed += 1
            continue
        if rec.get("status") == "deprecated":
            continue
        rec["status"] = "deprecated"
        existing_notes = rec.get("notes") or ""
        rec["notes"] = (
            f"{existing_notes} | deprecated {now_iso()} - not in "
            f"manifest {snap_date} (URL or duplicate fixed upstream)"
        ).strip(" |")
        per_file = PER_FILE_DIR / f"{rec['id']}.json"
        if per_file.exists():
            save_json(per_file, rec)
        changed += 1

    if changed:
        index["last_updated"] = now_iso()
        save_json(INDEX_PATH, index)
        print(f"[deprecate] updated {changed} record(s) in {INDEX_PATH.name}")
    else:
        print("[deprecate] no changes.")

    deprecated = [r["id"] for r in index.get("files", [])
                  if r.get("status") == "deprecated"]
    print(f"[deprecate] total deprecated: {len(deprecated)}")
    for did in sorted(deprecated):
        print(f"  - {did}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
