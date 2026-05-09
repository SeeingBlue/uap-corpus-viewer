# war.gov UAP Release 01 — viewer

Open `/` for the interactive corpus viewer.

This is a re-host of the 161 records publicly released by the U.S.
Department of War on 2026-05-08 under the PURSUE program (Presidential
Unsealing and Reporting System for UAP Encounters).

Original source: https://www.war.gov/UFO/

All bytes are U.S. federal government works released for public access.
SHA-256 hashes for every file are in /metadata/index.json.

- `/`                             interactive viewer (search, network, timeline)
- `/extracted/<id>.md`            per-record extracted text + metadata
- `/metadata/index.json`          full canonical record metadata
- `/metadata/by_location.md`      records grouped by incident location
- `/metadata/timeline.csv`        chronological listing
- `/metadata/cross_refs.json`     pairing graph (DoW MISREP ↔ DoW PR videos)
- `/metadata/entities.json`       per-record entity extraction
- `/manifest_schema.md`           CSV schema documentation
