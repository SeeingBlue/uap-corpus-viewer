# war.gov UAP Release 01–06 — viewer

Open `/` for the interactive corpus viewer.

This is a re-host of the 447 records publicly released by the U.S.
Department of War between 2026-05-08 and 2026-09-18 under the PURSUE
program (Presidential Unsealing and Reporting System for UAP Encounters),
in six drops: R1 May 8 (158), R2 May 22 (64), R3 Jun 12 (72),
R4 Jul 10 (40), R5 Aug 7 (41), R6 Sep 18 (72).

Original source: https://www.war.gov/UFO/

All bytes are U.S. federal government works released for public access.
SHA-256 hashes for every file are in /metadata/index.json.

- `/`                             interactive viewer (timeline, globe, patterns, releases)
- `/extracted/<id>.md`            per-record extracted text + metadata
- `/metadata/index.json`          full canonical record metadata
- `/metadata/by_location.md`      records grouped by incident location
- `/metadata/timeline.csv`        chronological listing
- `/metadata/cross_refs.json`     pairing graph (DoW MISREP ↔ DoW PR videos, AAWSAP set, ...)
- `/metadata/entities.json`       per-record entity extraction
- `/metadata/release_patterns.json` cross-release profile (feeds the Releases tab)
- `/manifest_schema.md`           CSV schema documentation
