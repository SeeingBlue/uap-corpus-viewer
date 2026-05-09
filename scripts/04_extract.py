"""04_extract.py — extract text from each PDF into extracted/<id>.md.

DEFERRED — Step 5 of the project plan. Stub only.

Once the corpus is on disk and verified, this script will use the pdf
skill (or pypdf as a fallback) to extract text and tables from each PDF
and write a markdown file per document for full-text search.

Plan to flesh out after the bytes are local.
"""

from __future__ import annotations

import sys


def main() -> int:
    print("[extract] not yet implemented — deferred to Step 5.", file=sys.stderr)
    print("[extract] populate files/pdfs/ first via 02_fetch.py.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
