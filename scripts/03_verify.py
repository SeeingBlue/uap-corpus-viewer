"""03_verify.py — re-hash every file in the index against its on-disk content.

Catches silent corruption, missing files, and post-hoc tampering. Reports
to stdout; exits non-zero if any file has drifted from its recorded hash.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import INDEX_PATH, load_json  # noqa: E402

import hashlib  # noqa: E402


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fp:
        for chunk in iter(lambda: fp.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    if not INDEX_PATH.exists():
        print("[verify] no index.json — run 02_fetch.py first.", file=sys.stderr)
        return 2

    index = load_json(INDEX_PATH)
    project_root = INDEX_PATH.parent.parent

    ok = drift = missing = unfetched = 0
    for rec in index.get("files", []):
        if rec.get("status") != "ok":
            unfetched += 1
            continue
        p = project_root / rec["local_path"]
        if not p.exists():
            print(f"[verify] MISSING  {rec['id']}  ({rec['local_path']})")
            missing += 1
            continue
        actual = sha256_file(p)
        if actual != rec["sha256"]:
            print(f"[verify] DRIFT    {rec['id']}")
            print(f"           expected {rec['sha256']}")
            print(f"           actual   {actual}")
            drift += 1
        else:
            ok += 1

    print(f"[verify] ok={ok} drift={drift} missing={missing} unfetched={unfetched}")
    return 0 if drift == 0 and missing == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
