# Incident Date audit (v2)

Records audited: **339**

Verdict counts:

- `confirmed`: 249
- `single-source`: 57
- `confirmed-by-sequence`: 23
- `disagree`: 6
- `no-evidence`: 2
- `sequence-suggests`: 2

**Confirmation rules.** A date is `confirmed` when 2+ of {csv, title, summary, body} agree at year+month precision or better (year-only matches don't count). A date is `confirmed-by-sequence` when the record sits in a numbered title family (e.g. DOW-UAP-D{N}) and one of its candidates fits the date range implied by the nearest confirmed prev/next neighbors.


## Disagreements (multiple sources, none corroborate) (6)

### `cia-019-cia-uap-019-australian-dept-of-defense-scientific-and-intel`
- **title:** CIA-UAP-019, Australian Dept of Defense Scientific and Intel Aspects of the UFO Problem
- **csv:** `1971` -> `1971`
- **body dates (filtered):** 1953-02-16; 1948-09; 1952-03; 1953-01; 1953-09; 1969-12; 1950-10; 1957-11
- **summary:** Dated to 1971, an Australian review of the USAF Project Blue Book. This document was released by the National Archives of Australia.

### `dow-084-dow-uap-pr051-syrian-uap-instant-acceleration`
- **family:** `DOW-UAP-PR51`
- **title:** DOW-UAP-PR051, "Syrian UAP instant acceleration"
- **csv:** `2021` -> `2021`
- **summary dates:** 2026-03-06; 2024-06
- **sequence:** DOW-UAP-PR neighbors disagree with sequence direction (50=(2022, 8, 26), 53=(2022, 6, 15))
- **summary:** On March 6, 2026, eight members of the U.S. House of Representatives requested access to 51 potentially UAP-related records allegedly held by the Department of War and the Intelligence Community. The…

### `dow-095-dow-uap-pr059-nag-uap-1-jun-20`
- **family:** `DOW-UAP-PR59`
- **title:** DOW-UAP-PR059, "NAG UAP 1 Jun 20"
- **csv:** `2020` -> `2020`
- **summary dates:** 2026-03-06; 2024-06
- **sequence:** DOW-UAP-PR neighbors disagree with sequence direction (57=(2023, 1, 15), 60=(2021, 6, 15))
- **summary:** On March 6, 2026, eight members of the U.S. House of Representatives requested access to 51 potentially UAP-related records allegedly held by the Department of War and the Intelligence Community. The…

### `dow-103-dow-uap-pr067-multiple-spherical-uap-uso-near-sub-callsign-2`
- **family:** `DOW-UAP-PR67`
- **title:** DOW-UAP-PR067, "Multiple Spherical UAP USO near Sub. [CALLSIGN] 2022/03/25 in and out of water"
- **csv:** `` -> `-`
- **title dates:** 2022
- **summary dates:** 2026-03-06; 2024-05
- **sequence:** DOW-UAP-PR neighbors disagree with sequence direction (66=(2024, 4, 24), 68=(2023, 6, 15))
- **summary:** On March 6, 2026, eight members of the U.S. House of Representatives requested access to 51 potentially UAP-related records allegedly held by the Department of War and the Intelligence Community. The…

### `fbi-018-65-hs1-101634279-100-de-26505`
- **title:** 65_HS1-101634279_100-DE-26505
- **csv:** `11/7/57` -> `1957-11-07`
- **body dates (filtered):** 1951-05-02; 1966-10-02; 1966-10-11
- **summary:** An FBI report from 1957 detailing the interview with Wladyslaw Krasuski, who recounted seeing a large, circular, vertically-rising vehicle in 1944 Germany near a German military compound.

### `odni-001-odni-uap-d001-usper-narrative-senior-usic-official`
- **title:** ODNI-UAP-D001, USPER Narrative, Senior USIC Official
- **csv:** `2025` -> `2025`
- **summary dates:** 2026-05-08
- **summary:** This document is a first-hand account written by a currently serving (May 2026) senior U.S. intelligence official. The official was part of a team investigating reports of unusual noises and sighting…


## Sequence suggests a range (no direct candidates) (2)

### `nasa-032-nasa-uap-d024-apollo-16-scientific-debriefing`
- **family:** `NASA-UAP-D24`
- **title:** NASA-UAP-D024, “Apollo 16 Scientific Debriefing”
- **csv:** `` -> `-`
- **sequence:** prev=NASA-UAP-D23@1962; next=NASA-UAP-D26@1971; implied range (1962, 6, 15)..(1971, 6, 15)
- **summary:** This debriefing includes presentations from principal investigators of various Apollo experiments. The principal investigators describe preliminary results of their work to educate the Apollo crews a…

### `nasa-033-nasa-uap-d025-apollo-16-scientific-debriefing`
- **family:** `NASA-UAP-D25`
- **title:** NASA-UAP-D025, “Apollo 16 Scientific Debriefing”
- **csv:** `` -> `-`
- **sequence:** prev=NASA-UAP-D23@1962; next=NASA-UAP-D26@1971; implied range (1962, 6, 15)..(1971, 6, 15)
- **summary:** At 32:41, the speaker makes an off-handed comment, “Could be an alien starbase or something, I don’t know” when discussing correlations between experimental data sets.


## Single-source (no corroboration) (57)

### `cia-005-cia-uap-004-case-17708-closed-and-dr-leon-davidson`
- **title:** CIA-UAP-004, CASE 17708 (CLOSED) and DR. Leon Davidson
- **csv:** `1958` -> `1958`
- **summary:** This 1958 CIA memorandum discussing a phone conversation with Dr. Leon Davidson regarding concerns about a destroyed "space message and its transmitter." A redacted version of this memorandum has bee…

### `cia-010-cia-uap-009-unknown-flying-objects-observed-over-budapest`
- **title:** CIA-UAP-009, Unknown Flying Objects Observed Over Budapest
- **csv:** `1957` -> `1957`
- **summary:** This is a 1957 CIA Information Report regarding UFO sightings over Budapest. A more redacted version of this report has been available on CIA's public website.

### `cia-014-cia-uap-013-report-of-unusual-flying-object-sightings-and-at`
- **title:** CIA-UAP-013, Report of Unusual Flying Object Sightings and Attendant Scientific Activity
- **csv:** `1956` -> `1956`
- **summary:** This 1956 CIA Information Report describes flying object sightings reported by a Budapest-based sub-source, including a sketch showing the objects' suspected formation and flight path between Budapes…

### `cia-016-cia-uap-015-project-blue-book-special-report-no-14-analysis`
- **title:** CIA-UAP-015, Project Blue Book Special Report No. 14 (Analysis of Reports of Unidentified Aerial Objects)
- **csv:** `` -> `-`
- **body dates (filtered):** 1952-04-30; 1948-07-29; 1952-04-20; 1951-01-20; 1952-07-19; 1948-07-24; 1952-12-22; 1952-06-06; 1948-07-31; 1947-08-13; 1949-05-24; 1950-03-20; 1952-08-25; 1955-05-05; 1954-08-12; 1955-01-01; 1952-04-29; 1953-01
- **summary:** This is the USAF Project Blue Book with a CIA cover sheet stating the document is "Official Record Copy." With the exception of the handwritten note on the first page, the content of this document ha…

### `cia-018-cia-uap-018-report-of-unusual-flying-object-sightings-and-at`
- **title:** CIA-UAP-018, Report of Unusual Flying Object Sightings and Attendant Scientific Activity
- **csv:** `1955` -> `1955`
- **summary:** A 1955 report on a UFO sighting in Hungary. The information came from a letter between Hungarian relatives, living in the USA and Budapest. A more redacted version of the report has been available on…

### `dow-007-38-143685-box-incident-summaries-101-172`
- **title:** 38_143685_box_Incident_Summaries_101-172
- **csv:** `N/A` -> `-`
- **body dates (filtered):** 1948-02-20; 1948-02-18; 1948-04-11; 1948-03-11; 1948-03-23; 1948-07-24; 1948-07-04; 1948-07-08; 1947-07-01; 1948-03-09; 1948-03-08; 1918-03-29; 1948-04-18; 1948-06-20; 1947-12-12; 1948-05-25; 1948-05-28; 1948-06-30; 1948-07-10; 1918-07-01; 1948-07-31; 1948-07-17; 1948-07-29; 1948-05-06; 1948-05-05; 1948-05-10; 1913-02; 1947-06
- **summary:** Each of these incident summaries includes a "Check-List - Unidentified Flying Objects" that contains details about the incident. Many summaries also include witness lists or statements and other narr…

### `dow-008-38-143685-box-incident-summaries-173-233`
- **title:** 38_143685_box_Incident_Summaries_173-233
- **csv:** `N/A` -> `-`
- **body dates (filtered):** 1948-09-23; 1948-10-15; 1948-10-21; 1948-10-20; 1948-08-19; 1948-10-29; 1948-09-22; 1948-10-24; 1948-10-17; 1948-11-29; 1948-12-05; 1948-12-06; 1948-08-04; 1949-01-01; 1947-10
- **summary:** Each of these incident summaries includes a "Check-List - Unidentified Flying Objects" that contains details about the incident. Many summaries also include witness lists or statements and other narr…

### `dow-009-38-143685-box7-incident-summaries-1-100`
- **title:** 38_143685_box7_Incident_Summaries_1-100
- **csv:** `N/A` -> `-`
- **body dates (filtered):** 1948-02-19; 1947-07-04; 1947-06-01; 1947-07-07; 1947-07-06; 1947-06-29; 1947-06-28; 1947-05-19; 1947-12-30; 1948-01-05; 1967-07; 1916-12
- **summary:** Each of these incident summaries includes a "Check-List - Unidentified Flying Objects" that contains details about the incident. Many summaries also include witness lists or statements and other narr…

### `dow-053-dow-uap-d8-mission-report-djibouti-2025`
- **family:** `DOW-UAP-D8`
- **title:** DOW-UAP-D8, Mission Report, Djibouti, 2025
- **csv:** `N/A` -> `-`
- **title dates:** 2025
- **sequence:** all candidates fall outside DOW-UAP-DNone..10 range [None..(2022, 5, 15)]
- **summary:** This document is a Mission Report (MISREP), a standardized reporting form the U.S. Military uses to record the circumstances surrounding its operations. U.S. military services often use MISREPs to re…

### `dow-070-dow-uap-pr38-unresolved-uap-report-middle-east-2013`
- **family:** `DOW-UAP-PR38`
- **title:** DOW-UAP-PR38, Unresolved UAP Report, Middle East, 2013
- **csv:** `N/A` -> `-`
- **title dates:** 2013
- **sequence:** all candidates fall outside DOW-UAP-PR36..50 range [(2020, 5, 15)..(2022, 8, 26)]
- **summary:** The United States Central Command submitted a report of an unidentified anomalous phenomenon to the All-domain Anomaly Resolution Office (AARO) consisting of one minute and 46 seconds of video footag…

### `dow-075-dow-uap-pr43-unresolved-uap-report-africa-2025`
- **family:** `DOW-UAP-PR43`
- **title:** DOW-UAP-PR43, Unresolved UAP Report, Africa, 2025
- **csv:** `N/A` -> `-`
- **title dates:** 2025
- **sequence:** all candidates fall outside DOW-UAP-PR36..50 range [(2020, 5, 15)..(2022, 8, 26)]
- **summary:** The United States Africa Command submitted a report of an unidentified anomalous phenomenon to the All-domain Anomaly Resolution Office (AARO) consisting of two seconds of video footage from an infra…

### `dow-078-dow-uap-pr46-unresolved-uap-report-indopacom-2024`
- **family:** `DOW-UAP-PR46`
- **title:** DOW-UAP-PR46, Unresolved UAP Report, INDOPACOM, 2024
- **csv:** `N/A` -> `-`
- **title dates:** 2024
- **sequence:** all candidates fall outside DOW-UAP-PR36..50 range [(2020, 5, 15)..(2022, 8, 26)]
- **summary:** The United States Indo-Pacific Command submitted a report of an unidentified anomalous phenomenon to the All-domain Anomaly Resolution Office (AARO) consisting of nine seconds of video footage from a…

### `dow-079-dow-uap-pr47-unresolved-uap-report-indopacom-2023`
- **family:** `DOW-UAP-PR47`
- **title:** DOW-UAP-PR47, Unresolved UAP Report, INDOPACOM, 2023
- **csv:** `N/A` -> `-`
- **title dates:** 2023
- **sequence:** all candidates fall outside DOW-UAP-PR36..50 range [(2020, 5, 15)..(2022, 8, 26)]
- **summary:** The United States Indo-Pacific Command submitted a report of an unidentified anomalous phenomenon to the All-domain Anomaly Resolution Office (AARO) consisting of one minute and 59 seconds of video f…

### `dow-080-dow-uap-pr48-unresolved-uap-report-indopacom-2024`
- **family:** `DOW-UAP-PR48`
- **title:** DOW-UAP-PR48, Unresolved UAP Report, INDOPACOM, 2024
- **csv:** `N/A` -> `-`
- **title dates:** 2024
- **sequence:** all candidates fall outside DOW-UAP-PR36..50 range [(2020, 5, 15)..(2022, 8, 26)]
- **summary:** The United States Indo-Pacific Command submitted a report of an unidentified anomalous phenomenon to the All-domain Anomaly Resolution Office (AARO) consisting of one minute and 39 seconds of video f…

### `dow-081-dow-uap-pr49-unresolved-uap-report-department-of-the-army-20`
- **family:** `DOW-UAP-PR49`
- **title:** DOW-UAP-PR49, Unresolved UAP Report, Department of the Army, 2026
- **csv:** `N/A` -> `-`
- **title dates:** 2026
- **sequence:** all candidates fall outside DOW-UAP-PR36..50 range [(2020, 5, 15)..(2022, 8, 26)]
- **summary:** The Department of the Army submitted a report of an unidentified anomalous phenomenon to the All-domain Anomaly Resolution Office (AARO) consisting of one minute and 49 seconds of video from an infra…

### `dow-082-western-us-event`
- **title:** Western US Event
- **csv:** `2023` -> `2023`
- **summary:** This document is a summary of statements by seven US PERSONs employed by the federal government who separately reported observing several unidentified anomalous phenomena in the western United States…

### `dow-087-dow-uap-pr052-uap-uso-formation-callsign-mission`
- **family:** `DOW-UAP-PR52`
- **title:** DOW-UAP-PR052, "UAP USO Formation [CALLSIGN] (Mission)"
- **csv:** `` -> `-`
- **summary dates:** 2026-03-06; 2024-06
- **sequence:** DOW-UAP-PR neighbors disagree with sequence direction (50=(2022, 8, 26), 53=(2022, 6, 15))
- **summary:** On March 6, 2026, eight members of the U.S. House of Representatives requested access to 51 potentially UAP-related records allegedly held by the Department of War and the Intelligence Community. The…

### `dow-091-dow-uap-pr056-spherical-uap-pulsing-over-water-callsign`
- **family:** `DOW-UAP-PR56`
- **title:** DOW-UAP-PR056, "Spherical UAP pulsing over water [CALLSIGN]"
- **csv:** `` -> `-`
- **summary dates:** 2026-03-06; 2024-06
- **sequence:** all candidates fall outside DOW-UAP-PR55..57 range [(2020, 11, 23)..(2023, 6, 15)]
- **summary:** On March 6, 2026, eight members of the U.S. House of Representatives requested access to 51 potentially UAP-related records allegedly held by the Department of War and the Intelligence Community. The…

### `dow-094-dow-uap-pr058-callsign-mission-uap`
- **family:** `DOW-UAP-PR58`
- **title:** DOW-UAP-PR058, "[CALLSIGN] (Mission) UAP"
- **csv:** `` -> `-`
- **summary dates:** 2026-03-06; 2024-06
- **sequence:** DOW-UAP-PR neighbors disagree with sequence direction (57=(2023, 1, 15), 60=(2021, 6, 15))
- **summary:** On March 6, 2026, eight members of the U.S. House of Representatives requested access to 51 potentially UAP-related records allegedly held by the Department of War and the Intelligence Community. The…

### `dow-105-dow-uap-pr069-f-a-18-flir-uap`
- **family:** `DOW-UAP-PR69`
- **title:** DOW-UAP-PR069, "F/A-18 FLIR UAP"
- **csv:** `` -> `-`
- **summary dates:** 2026-03-06; 2023-07
- **sequence:** all candidates fall outside DOW-UAP-PR68..70 range [(2023, 6, 15)..(2023, 6, 15)]
- **summary:** On March 6, 2026, eight members of the U.S. House of Representatives requested access to 51 potentially UAP-related records allegedly held by the Department of War and the Intelligence Community. The…

### `dow-145-dow-uap-d086-usnavy-report-of-flying-discs-1948`
- **family:** `DOW-UAP-D86`
- **title:** DOW-UAP-D086, USNavy-Report-of-Flying-Discs_1948
- **csv:** `` -> `-`
- **title dates:** 1948
- **sequence:** all candidates fall outside DOW-UAP-D85..89 range [(1953, 6, 15)..(2020, 6, 15)]
- **summary:** This document is a memorandum from the Commandant of the 5th Naval District, and it cites a memorandum related to "flying discs" from the Chief of Naval Operations. The memorandum requests that naval…

### `dow-146-dow-uap-d087-u-s-air-force-analysis-of-flying-objects-in-the`
- **family:** `DOW-UAP-D87`
- **title:** DOW-UAP-D087, U.S. Air Force Analysis of Flying Objects in the United States, 1-100
- **csv:** `` -> `-`
- **body dates (filtered):** 1947-07-07; 1947-06-29; 1947-12-30; 1947-11-02; 1947-10
- **sequence:** all candidates fall outside DOW-UAP-D85..89 range [(1953, 6, 15)..(2020, 6, 15)]
- **summary:** Includes a "Check-List - Unidentified Flying Objects" that contains details about the incident. Many summaries also include witness lists or statements and other narrative reports or descriptions.

### `dow-147-dow-uap-d088-u-s-air-force-analysis-of-flying-objects-in-the`
- **family:** `DOW-UAP-D88`
- **title:** DOW-UAP-D088, U.S. Air Force Analysis of Flying Objects in the United States, 101-172
- **csv:** `` -> `-`
- **body dates (filtered):** 1948-02-20; 1947-11-24; 1948-04-11; 1948-07-24; 1947-06-24; 1947-07-14; 1948-03-08; 1948-03-05; 1948-03-09; 1948-03-29; 1946-04-09; 1948-05-28; 1948-07-01; 1948-07-29; 1948-07-30; 1948-07-26; 1948-07-20; 1913-02; 1945-04
- **sequence:** all candidates fall outside DOW-UAP-D85..89 range [(1953, 6, 15)..(2020, 6, 15)]
- **summary:** Includes a "Check-List - Unidentified Flying Objects" that contains details about the incident. Many summaries also include witness lists or statements and other narrative reports or descriptions.

### `fbi-021-fbi-photo-a1`
- **title:** FBI Photo A1
- **csv:** `Late 2025` -> `2025`
- **summary:** The Federal Bureau of Investigation (FBI) submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of a still image derived from …

### `fbi-022-fbi-photo-a2`
- **title:** FBI Photo A2
- **csv:** `Late 2025` -> `2025`
- **summary:** The Federal Bureau of Investigation (FBI) submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of a still image derived from …

### `fbi-023-fbi-photo-a3`
- **title:** FBI Photo A3
- **csv:** `Late 2025` -> `2025`
- **summary:** The Federal Bureau of Investigation (FBI) submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of a still image derived from …

### `fbi-024-fbi-photo-a4`
- **title:** FBI Photo A4
- **csv:** `Late 2025` -> `2025`
- **summary:** The Federal Bureau of Investigation (FBI) submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of a still image derived from …

### `fbi-025-fbi-photo-a5`
- **title:** FBI Photo A5
- **csv:** `Late 2025` -> `2025`
- **summary:** The Federal Bureau of Investigation (FBI) submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of a still image derived from …

### `fbi-026-fbi-photo-a6`
- **title:** FBI Photo A6
- **csv:** `Late 2025` -> `2025`
- **summary:** The Federal Bureau of Investigation (FBI) submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of a still image derived from …

### `fbi-027-fbi-photo-a7`
- **title:** FBI Photo A7
- **csv:** `Late 2025` -> `2025`
- **summary:** The Federal Bureau of Investigation (FBI) submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of a still image derived from …

### `fbi-028-fbi-photo-a8`
- **title:** FBI Photo A8
- **csv:** `Late 2025` -> `2025`
- **summary:** The Federal Bureau of Investigation (FBI) submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of a still image derived from …

### `fbi-029-fbi-photo-b1`
- **title:** FBI Photo B1
- **csv:** `Late 2025` -> `2025`
- **summary:** The Federal Bureau of Investigation (FBI) submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of a still image derived from …

### `fbi-030-fbi-photo-b10`
- **title:** FBI Photo B10
- **csv:** `Late 2025` -> `2025`
- **summary:** The Federal Bureau of Investigation (FBI) submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of a still image derived from …

### `fbi-031-fbi-photo-b11`
- **title:** FBI Photo B11
- **csv:** `Late 2025` -> `2025`
- **summary:** The Federal Bureau of Investigation (FBI) submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of a still image derived from …

### `fbi-032-fbi-photo-b12`
- **title:** FBI Photo B12
- **csv:** `Late 2025` -> `2025`
- **summary:** The Federal Bureau of Investigation (FBI) submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of a still image derived from …

### `fbi-033-fbi-photo-b13`
- **title:** FBI Photo B13
- **csv:** `Late 2025` -> `2025`
- **summary:** The Federal Bureau of Investigation (FBI) submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of a still image derived from …

### `fbi-034-fbi-photo-b14`
- **title:** FBI Photo B14
- **csv:** `Late 2025` -> `2025`
- **summary:** The Federal Bureau of Investigation (FBI) submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of a still image derived from …

### `fbi-035-fbi-photo-b15`
- **title:** FBI Photo B15
- **csv:** `Late 2025` -> `2025`
- **summary:** The Federal Bureau of Investigation (FBI) submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of a still image derived from …

### `fbi-036-fbi-photo-b16`
- **title:** FBI Photo B16
- **csv:** `Late 2025` -> `2025`
- **summary:** The Federal Bureau of Investigation (FBI) submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of a still image derived from …

### `fbi-037-fbi-photo-b17`
- **title:** FBI Photo B17
- **csv:** `Late 2025` -> `2025`
- **summary:** The Federal Bureau of Investigation (FBI) submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of a still image derived from …

### `fbi-038-fbi-photo-b18`
- **title:** FBI Photo B18
- **csv:** `Late 2025` -> `2025`
- **summary:** The Federal Bureau of Investigation (FBI) submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of a still image derived from …

### `fbi-039-fbi-photo-b19`
- **title:** FBI Photo B19
- **csv:** `Late 2025` -> `2025`
- **summary:** The Federal Bureau of Investigation (FBI) submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of a still image derived from …

### `fbi-040-fbi-photo-b2`
- **title:** FBI Photo B2
- **csv:** `Late 2025` -> `2025`
- **summary:** The Federal Bureau of Investigation (FBI) submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of a still image derived from …

### `fbi-041-fbi-photo-b20`
- **title:** FBI Photo B20
- **csv:** `Late 2025` -> `2025`
- **summary:** The Federal Bureau of Investigation (FBI) submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of a still image derived from …

### `fbi-042-fbi-photo-b21`
- **title:** FBI Photo B21
- **csv:** `Late 2025` -> `2025`
- **summary:** The Federal Bureau of Investigation (FBI) submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of a still image derived from …

### `fbi-043-fbi-photo-b22`
- **title:** FBI Photo B22
- **csv:** `Late 2025` -> `2025`
- **summary:** The Federal Bureau of Investigation (FBI) submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of a still image derived from …

### `fbi-044-fbi-photo-b23`
- **title:** FBI Photo B23
- **csv:** `Late 2025` -> `2025`
- **summary:** The Federal Bureau of Investigation (FBI) submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of a still image derived from …

### `fbi-045-fbi-photo-b24`
- **title:** FBI Photo B24
- **csv:** `Late 2025` -> `2025`
- **summary:** The Federal Bureau of Investigation (FBI) submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of a still image derived from …

### `fbi-046-fbi-photo-b3`
- **title:** FBI Photo B3
- **csv:** `Late 2025` -> `2025`
- **summary:** The Federal Bureau of Investigation (FBI) submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of a still image derived from …

### `fbi-047-fbi-photo-b4`
- **title:** FBI Photo B4
- **csv:** `Late 2025` -> `2025`
- **summary:** The Federal Bureau of Investigation (FBI) submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of a still image derived from …

### `fbi-048-fbi-photo-b5`
- **title:** FBI Photo B5
- **csv:** `Late 2025` -> `2025`
- **summary:** The Federal Bureau of Investigation (FBI) submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of a still image derived from …

### `fbi-049-fbi-photo-b6`
- **title:** FBI Photo B6
- **csv:** `Late 2025` -> `2025`
- **summary:** The Federal Bureau of Investigation (FBI) submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of a still image derived from …

### `fbi-050-fbi-photo-b7`
- **title:** FBI Photo B7
- **csv:** `Late 2025` -> `2025`
- **summary:** The Federal Bureau of Investigation (FBI) submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of a still image derived from …

### `fbi-051-fbi-photo-b8`
- **title:** FBI Photo B8
- **csv:** `Late 2025` -> `2025`
- **summary:** The Federal Bureau of Investigation (FBI) submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of a still image derived from …

### `fbi-052-fbi-photo-b9`
- **title:** FBI Photo B9
- **csv:** `Late 2025` -> `2025`
- **summary:** The Federal Bureau of Investigation (FBI) submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of a still image derived from …

### `fbi-053-usper-statement-about-uap-sighting`
- **title:** USPER Statement about UAP Sighting
- **csv:** `Late 2025` -> `2025`
- **summary:** This is an FBI 302 interview conducted with a senior US intelligence official regarding his first-hand account of a UAP encounter at a US military facility. USPER relayed to FBI agents that he and ot…

### `nasa-001-255-413270-ufo-s-and-defense-what-should-we-prepare-for`
- **title:** 255_413270_UFO's_and_Defense_What_Should_we_Prepare_For
- **csv:** `` -> `-`
- **body dates (filtered):** 2001-04-30; 1901-07-01; 1971-09-04; 1994-01-28; 1977-03-07; 1976-03-03; 1957-07-17; 1990-03-21; 1990-04-19; 1995-07-31; 1954-08-16; 1979-12-09; 1965-07-01; 1967-08-29; 1981-01-08; 1982-10-21; 1988-09-29; 1979-03-10; 1979-03-13; 1999-07-29; 1996-06-10; 1947-06-24; 1987-09-21; 2001-05-03; 2000-05-21; 2001-01-27; 1953-01-18; 2000-06-17; 1995-03; 1993-03; 1974-02; 1977-05; 1996-02; 1997-06; 1947-07; 1969-12; 1969-10; 1997-07; 1996-03; 1994-09; 1945-03; 1949-12; 1946-10; 1949-02; 1995-02; 1952-12; 1946-12; 1944-06; 1997-03; 2000-10
- **summary:** This file contains an independent report on UFOs written by the French association COMETA (previously published in the French magazine VDS in 1999), which details the results of a study by the Instit…


## No evidence anywhere (2)

### `doe-001-doe-uap-d001-enhanced-pantex-imagery`
- **title:** DOE-UAP-D001, Enhanced PANTEX Imagery
- **csv:** `` -> `-`
- **summary:** A Pantex Unidentified Object Incident Report that includes an enhanced image from ground surveillance radar tower.

### `dow-038-dow-uap-d54-mission-report-mediterranean-sea-na`
- **family:** `DOW-UAP-D54`
- **title:** DOW-UAP-D54, Mission Report, Mediterranean Sea, NA
- **csv:** `N/A` -> `-`
- **sequence:** DOW-UAP-D neighbors disagree with sequence direction (52=(2024, 6, 15), 55=(2016, 11, 18))
- **summary:** This document is a Mission Report (MISREP), a standardized reporting form the U.S. Military uses to record the circumstances surrounding its operations. U.S. military services often use MISREPs to re…


## Confirmed by sequence (sole source fits neighbor range) (23)

### `dow-020-dow-uap-d27-mission-report-united-arab-emirates-october-2023`
- **family:** `DOW-UAP-D27`
- **title:** DOW-UAP-D27, Mission Report, United Arab Emirates, October 2023
- **csv:** `6/7/24` -> `2024-06-07`
- **title dates:** 2023-10
- **body dates (filtered):** 2025-10-28; 2025-10-24
- **confirmed date:** `2024-06-07` (via csv, sequence)
- **sequence:** prev=DOW-UAP-D25@2024-01; next=DOW-UAP-D28@2024-09; non-fit sources: title=2023-10, body=2025-10-28, body=2025-10-24
- **summary:** This document is a Mission Report (MISREP), a standardized reporting form the U.S. Military uses to record the circumstances surrounding its operations. U.S. military services often use MISREPs to re…

### `dow-022-dow-uap-d3-mission-report-arabian-gulf-2020`
- **family:** `DOW-UAP-D3`
- **title:** DOW-UAP-D3, Mission Report, Arabian Gulf, 2020
- **csv:** `N/A` -> `-`
- **title dates:** 2020
- **confirmed date:** `2020` (via sequence, title)
- **sequence:** next=DOW-UAP-D10@2022-05
- **summary:** This document is a Mission Report (MISREP), a standardized reporting form the U.S. Military uses to record the circumstances surrounding its operations. U.S. military services often use MISREPs to re…

### `dow-029-dow-uap-d4-mission-report-arabian-gulf-2020`
- **family:** `DOW-UAP-D4`
- **title:** DOW-UAP-D4, Mission Report, Arabian Gulf, 2020
- **csv:** `N/A` -> `-`
- **title dates:** 2020
- **confirmed date:** `2020` (via sequence, title)
- **sequence:** next=DOW-UAP-D10@2022-05
- **summary:** This document is a Mission Report (MISREP), a standardized reporting form the U.S. Military uses to record the circumstances surrounding its operations. U.S. military services often use MISREPs to re…

### `dow-034-dow-uap-d5-mission-report-arabian-gulf-2020`
- **family:** `DOW-UAP-D5`
- **title:** DOW-UAP-D5, Mission Report, Arabian Gulf, 2020
- **csv:** `N/A` -> `-`
- **title dates:** 2020
- **confirmed date:** `2020` (via sequence, title)
- **sequence:** next=DOW-UAP-D10@2022-05
- **summary:** This document is a Mission Report (MISREP), a standardized reporting form the U.S. Military uses to record the circumstances surrounding its operations. U.S. military services often use MISREPs to re…

### `dow-043-dow-uap-d6-mission-report-arabian-gulf-2020`
- **family:** `DOW-UAP-D6`
- **title:** DOW-UAP-D6, Mission Report, Arabian Gulf, 2020
- **csv:** `N/A` -> `-`
- **title dates:** 2020
- **confirmed date:** `2020` (via sequence, title)
- **sequence:** next=DOW-UAP-D10@2022-05
- **summary:** This document is a Mission Report (MISREP), a standardized reporting form the U.S. Military uses to record the circumstances surrounding its operations. U.S. military services often use MISREPs to re…

### `dow-050-dow-uap-d7-mission-report-arabian-gulf-2020`
- **family:** `DOW-UAP-D7`
- **title:** DOW-UAP-D7, Mission Report, Arabian Gulf, 2020
- **csv:** `N/A` -> `-`
- **title dates:** 2020
- **confirmed date:** `2020` (via sequence, title)
- **sequence:** next=DOW-UAP-D10@2022-05
- **summary:** This document is a Mission Report (MISREP), a standardized reporting form the U.S. Military uses to record the circumstances surrounding its operations. U.S. military services often use MISREPs to re…

### `dow-055-dow-uap-pr20-unresolved-uap-report-kuwait-may-2022`
- **family:** `DOW-UAP-PR20`
- **title:** DOW-UAP-PR20, Unresolved UAP Report, Kuwait, May 2022
- **csv:** `N/A` -> `-`
- **title dates:** 2022-05
- **body dates (filtered):** 2025-10-17; 2026-03-10
- **confirmed date:** `2022-05` (via sequence, title)
- **sequence:** prev=DOW-UAP-PR19@2022-05; next=DOW-UAP-PR21@2022-05; non-fit sources: body=2025-10-17, body=2026-03-10
- **summary:** The United States Central Command submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of a still image derived from a U.S. m…

### `dow-069-dow-uap-pr37-unresolved-uap-report-middle-east-2020`
- **family:** `DOW-UAP-PR37`
- **title:** DOW-UAP-PR37, Unresolved UAP Report, Middle East, 2020
- **csv:** `N/A` -> `-`
- **title dates:** 2020
- **confirmed date:** `2020` (via sequence, title)
- **sequence:** prev=DOW-UAP-PR36@2020-05; next=DOW-UAP-PR50@2022-08-26
- **summary:** The United States Central Command submitted a report of an unidentified anomalous phenomenon to the All-domain Anomaly Resolution Office (AARO) consisting of nine seconds of video footage from an inf…

### `dow-071-dow-uap-pr39-unresolved-uap-report-middle-east-2020`
- **family:** `DOW-UAP-PR39`
- **title:** DOW-UAP-PR39, Unresolved UAP Report, Middle East, 2020
- **csv:** `N/A` -> `-`
- **title dates:** 2020
- **confirmed date:** `2020` (via sequence, title)
- **sequence:** prev=DOW-UAP-PR36@2020-05; next=DOW-UAP-PR50@2022-08-26
- **summary:** The United States Central Command submitted a report of an unidentified anomalous phenomenon to the All-domain Anomaly Resolution Office (AARO) consisting of five seconds of video footage from an inf…

### `dow-072-dow-uap-pr40-unresolved-uap-report-middle-east-2020`
- **family:** `DOW-UAP-PR40`
- **title:** DOW-UAP-PR40, Unresolved UAP Report, Middle East, 2020
- **csv:** `N/A` -> `-`
- **title dates:** 2020
- **confirmed date:** `2020` (via sequence, title)
- **sequence:** prev=DOW-UAP-PR36@2020-05; next=DOW-UAP-PR50@2022-08-26
- **summary:** The United States Central Command submitted a report of an unidentified anomalous phenomenon to the All-domain Anomaly Resolution Office (AARO) consisting of one minute and three seconds of video foo…

### `dow-073-dow-uap-pr41-unresolved-uap-report-middle-east-2020`
- **family:** `DOW-UAP-PR41`
- **title:** DOW-UAP-PR41, Unresolved UAP Report, Middle East, 2020
- **csv:** `N/A` -> `-`
- **title dates:** 2020
- **confirmed date:** `2020` (via sequence, title)
- **sequence:** prev=DOW-UAP-PR36@2020-05; next=DOW-UAP-PR50@2022-08-26
- **summary:** The United States Central Command submitted a report of an unidentified anomalous phenomenon to the All-domain Anomaly Resolution Office (AARO) consisting of one minute and 34 seconds of video footag…

### `dow-074-dow-uap-pr42-unresolved-uap-report-middle-east-2020`
- **family:** `DOW-UAP-PR42`
- **title:** DOW-UAP-PR42, Unresolved UAP Report, Middle East, 2020
- **csv:** `N/A` -> `-`
- **title dates:** 2020
- **confirmed date:** `2020` (via sequence, title)
- **sequence:** prev=DOW-UAP-PR36@2020-05; next=DOW-UAP-PR50@2022-08-26
- **summary:** The United States Central Command submitted a report of an unidentified anomalous phenomenon to the All-domain Anomaly Resolution Office (AARO) consisting of four minutes and 53 seconds of video foot…

### `dow-076-dow-uap-pr44-unresolved-uap-report-middle-east-2020`
- **family:** `DOW-UAP-PR44`
- **title:** DOW-UAP-PR44, Unresolved UAP Report, Middle East, 2020
- **csv:** `N/A` -> `-`
- **title dates:** 2020
- **confirmed date:** `2020` (via sequence, title)
- **sequence:** prev=DOW-UAP-PR36@2020-05; next=DOW-UAP-PR50@2022-08-26
- **summary:** The United States Central Command submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of five minutes and 11 seconds of vide…

### `dow-077-dow-uap-pr45-unresolved-uap-report-middle-east-2020`
- **family:** `DOW-UAP-PR45`
- **title:** DOW-UAP-PR45, Unresolved UAP Report, Middle East, 2020
- **csv:** `N/A` -> `-`
- **title dates:** 2020
- **confirmed date:** `2020` (via sequence, title)
- **sequence:** prev=DOW-UAP-PR36@2020-05; next=DOW-UAP-PR50@2022-08-26
- **summary:** The Department of the Air Force submitted a report of an unidentified anomalous phenomenon to the All-domain Anomaly Resolution Office (AARO) consisting of 58 seconds of video footage from an infrare…

### `dow-134-dow-uap-pr098-ufos-in-formation-over-persian-gulf`
- **family:** `DOW-UAP-PR98`
- **title:** DOW-UAP-PR098, "UFOs in formation over Persian Gulf?"
- **csv:** `` -> `-`
- **summary dates:** 2026-03-06; 2019-10
- **confirmed date:** `2019-10` (via sequence, summary)
- **sequence:** prev=DOW-UAP-PR97@2019; next=DOW-UAP-PR100@2023; non-fit sources: summary=2026-03-06
- **summary:** On March 6, 2026, eight members of the U.S. House of Representatives requested access to 51 potentially UAP-related records allegedly held by the Department of War and the Intelligence Community. The…

### `dow-135-dow-uap-pr099-hi-res-callsign-observes-uap-on-25sep19-at-171`
- **family:** `DOW-UAP-PR99`
- **title:** DOW-UAP-PR099, "Hi-Res: [CALLSIGN] Observes UAP on 25SEP19 at 1715Z"
- **csv:** `2023` -> `2023`
- **summary dates:** 2026-03-06; 2019-11
- **confirmed date:** `2019-11` (via sequence, summary)
- **sequence:** prev=DOW-UAP-PR97@2019; next=DOW-UAP-PR100@2023; non-fit sources: summary=2026-03-06
- **summary:** On March 6, 2026, eight members of the U.S. House of Representatives requested access to 51 potentially UAP-related records allegedly held by the Department of War and the Intelligence Community. The…

### `fbi-005-65-hs1-834228961-62-hq-83894-section-5`
- **family:** `FBI-Section5`
- **title:** 65_HS1-834228961_62-HQ-83894_Section_5
- **csv:** `N/A` -> `-`
- **summary dates:** 1947-06; 1968-07
- **body dates (filtered):** 1950-03-28; 1950-04-18; 1949-06-30; 1950-04-17; 1949-07-26; 1949-07-15; 1949-07-10; 1964-11-18; 1949-08-16; 1949-08-21; 1949-10-12; 1949-10-08; 1949-10-02; 1949-09-26; 1949-09-25; 1949-10-19; 1950-02-20; 1950-02-12; 1950-03-10; 1950-03-22; 1950-03-31; 1950-03-03; 1950-03-01; 1950-03-06; 1950-03-14; 1950-03-02; 1950-03-05; 1950-03-07; 1959-04-07; 1950-04-07; 1950-04-11; 1950-03-19; 1950-05-17; 1950-04-04; 1950-04-08; 1950-04-13; 1950-05-31; 1950-06-08; 1950-06-02; 1950-06-15; 1950-05-25; 1950-06-29; 1950-06-25; 1950-07-11; 1950-07-04; 1950-07-18; 1950-07-01; 1950-07-28; 1950-07-03; 1950-06-28; 1950-07-25; 1950-08-29; 1949-01-18; 1950-05-22; 1950-05-23; 1948-12
- **confirmed date:** `1947-06` (via sequence, summary)
- **sequence:** prev=FBI-Section4@1947; next=FBI-Section6@1947; non-fit sources: summary=1968-07, body=1950-03-28, body=1950-04-18, body=1949-06-30, body=1950-04-17, body=1949-07-26, body=1949-07-15, body=1949-07-10, body=1964-11-18, body=1949-08-16, body=1949-08-21, body=1949-10-12, body=1949-10-08, body=1949-10-02, body=1949-09-26, body=1949-09-25, body=1949-10-19, body=1950-02-20, body=1950-02-12, body=1950-03-10, body=1950-03-22, body=1950-03-31, body=1950-03-03, body=1950-03-01, body=1950-03-06, body=1950-03-14, body=1950-03-02, body=1950-03-05, body=1950-03-07, body=1959-04-07, body=1950-04-07, body=1950-04-11, body=1950-03-19, body=1950-05-17, body=1950-04-04, body=1950-04-08, body=1950-04-13, body=1950-05-31, body=1950-06-08, body=1950-06-02, body=1950-06-15, body=1950-05-25, body=1950-06-29, body=1950-06-25, body=1950-07-11, body=1950-07-04, body=1950-07-18, body=1950-07-01, body=1950-07-28, body=1950-07-03, body=1950-06-28, body=1950-07-25, body=1950-08-29, body=1949-01-18, body=1950-05-22, body=1950-05-23, body=1948-12
- **summary:** The FBI's 62-HQ-83894 case file includes investigative records, eyewitness testimonies, and public reports concerning Unidentified Flying Objects and flying discs documented between June 1947 and Jul…

### `fbi-011-65-hs1-834228961-62-hq-83894-serial-164`
- **family:** `FBI-Serial164`
- **title:** 65_HS1-834228961_62-HQ-83894_Serial_164
- **csv:** `N/A` -> `-`
- **summary dates:** 1947-06; 1968-07
- **body dates (filtered):** 1949-02-15; 1948-01-21; 1948-03-25
- **confirmed date:** `1949-02-15` (via body, sequence)
- **sequence:** prev=FBI-Serial153@1947
- **summary:** The FBI's 62-HQ-83894 case file includes investigative records, eyewitness testimonies, and public reports concerning Unidentified Flying Objects and flying discs documented between June 1947 and Jul…

### `fbi-012-65-hs1-834228961-62-hq-83894-serial-220`
- **family:** `FBI-Serial220`
- **title:** 65_HS1-834228961_62-HQ-83894_Serial_220
- **csv:** `N/A` -> `-`
- **summary dates:** 1947-06; 1968-07
- **body dates (filtered):** 1950-03-19
- **confirmed date:** `1950-03-19` (via body, sequence)
- **sequence:** prev=FBI-Serial153@1947
- **summary:** The FBI's 62-HQ-83894 case file includes investigative records, eyewitness testimonies, and public reports concerning Unidentified Flying Objects and flying discs documented between June 1947 and Jul…

### `fbi-013-65-hs1-834228961-62-hq-83894-serial-403`
- **family:** `FBI-Serial403`
- **title:** 65_HS1-834228961_62-HQ-83894_Serial_403
- **csv:** `N/A` -> `-`
- **summary dates:** 1947-06; 1968-07
- **confirmed date:** `1947-06` (via sequence, summary)
- **sequence:** prev=FBI-Serial153@1947
- **summary:** The FBI's 62-HQ-83894 case file includes investigative records, eyewitness testimonies, and public reports concerning Unidentified Flying Objects and flying discs documented between June 1947 and Jul…

### `fbi-014-65-hs1-834228961-62-hq-83894-serial-438`
- **family:** `FBI-Serial438`
- **title:** 65_HS1-834228961_62-HQ-83894_Serial_438
- **csv:** `N/A` -> `-`
- **summary dates:** 1947-06; 1968-07
- **body dates (filtered):** 1964-05-08; 1964-04-24; 1964-04-25
- **confirmed date:** `1964-05-08` (via body, sequence)
- **sequence:** prev=FBI-Serial153@1947
- **summary:** The FBI's 62-HQ-83894 case file includes investigative records, eyewitness testimonies, and public reports concerning Unidentified Flying Objects and flying discs documented between June 1947 and Jul…

### `fbi-015-65-hs1-834228961-62-hq-83894-serial-449`
- **family:** `FBI-Serial449`
- **title:** 65_HS1-834228961_62-HQ-83894_Serial_449
- **csv:** `N/A` -> `-`
- **summary dates:** 1947-06; 1968-07
- **body dates (filtered):** 1966-09-22; 1966-09-19; 1966-05-04; 1964-04-24; 1966-06-04; 1966-06-23; 1966-06-25; 1966-07-08; 1966-07-09; 1966-07-10; 1966-03-05; 1965-10-25; 1966-04-30; 1965-12-13; 1966-05-09; 1966-05-15; 1966-04-18; 1965-01-15; 1966-03-22
- **confirmed date:** `1966-09-22` (via body, sequence)
- **sequence:** prev=FBI-Serial153@1947
- **summary:** The FBI's 62-HQ-83894 case file includes investigative records, eyewitness testimonies, and public reports concerning Unidentified Flying Objects and flying discs documented between June 1947 and Jul…

### `fbi-020-65-hs1-834228961-62-hq-83894-section-8`
- **family:** `FBI-Section8`
- **title:** 65_HS1-834228961_62-HQ-83894_Section_8
- **csv:** `N/A` -> `-`
- **summary dates:** 1947-06; 1968-07
- **body dates (filtered):** 1954-07-23; 1954-07-29; 1954-06-07; 1954-11-02; 1954-06-08; 1954-07-22; 1954-09-28; 1954-10-20; 1954-06-06; 1954-11-13; 1954-09-13; 1954-09-21; 1954-09-05; 1954-09-18; 1954-11-30; 1955-01-05; 1955-01-15; 1956-04-09; 1956-04-05; 1956-04-06; 1956-08-15; 1956-08-14; 1956-07-16; 1956-07-30; 1956-09-07; 1957-01-11; 1957-04-18; 1957-04-12; 1957-04-24; 1957-03-28; 1954-07-02; 1964-11-19; 1954-02-13; 1953-12-31; 1954-05-27; 1954-08-01; 1954-08-09; 1954-06-01; 1954-08-12; 1954-08-07; 1954-09-30; 1954-09-22; 1953-12-23; 1954-05-07; 1954-08-26; 1954-10-01; 1954-12-09; 1954-12-17; 1954-12-06; 1955-01-06; 1955-01-07; 1955-01-18; 1955-07-26; 1955-07-24; 1955-11-08; 1956-04-13; 1956-04-02; 1956-04-10; 1996-04-26; 1956-05-04; 1956-05-08; 1956-05-05; 1956-05-11; 1956-08-31; 1956-09-20; 1956-10-12; 1956-10-05; 1957-01-02; 1957-02-20; 1957-02-08; 1957-03-15; 1957-03-14; 1957-03-25; 1957-03-12; 1957-03-19; 1957-04-23; 1957-03-01; 1957-11-05; 1957-11-06; 1957-11-07; 1957-11-12; 1957-11-19; 1957-11-08; 1951-05-02; 1957-11-15; 1955-10; 1953-03
- **confirmed date:** `1947-06` (via sequence, summary)
- **sequence:** prev=FBI-Section7@1947; next=FBI-Section9@1947; non-fit sources: summary=1968-07, body=1954-07-23, body=1954-07-29, body=1954-06-07, body=1954-11-02, body=1954-06-08, body=1954-07-22, body=1954-09-28, body=1954-10-20, body=1954-06-06, body=1954-11-13, body=1954-09-13, body=1954-09-21, body=1954-09-05, body=1954-09-18, body=1954-11-30, body=1955-01-05, body=1955-01-15, body=1956-04-09, body=1956-04-05, body=1956-04-06, body=1956-08-15, body=1956-08-14, body=1956-07-16, body=1956-07-30, body=1956-09-07, body=1957-01-11, body=1957-04-18, body=1957-04-12, body=1957-04-24, body=1957-03-28, body=1954-07-02, body=1964-11-19, body=1954-02-13, body=1953-12-31, body=1954-05-27, body=1954-08-01, body=1954-08-09, body=1954-06-01, body=1954-08-12, body=1954-08-07, body=1954-09-30, body=1954-09-22, body=1953-12-23, body=1954-05-07, body=1954-08-26, body=1954-10-01, body=1954-12-09, body=1954-12-17, body=1954-12-06, body=1955-01-06, body=1955-01-07, body=1955-01-18, body=1955-07-26, body=1955-07-24, body=1955-11-08, body=1956-04-13, body=1956-04-02, body=1956-04-10, body=1996-04-26, body=1956-05-04, body=1956-05-08, body=1956-05-05, body=1956-05-11, body=1956-08-31, body=1956-09-20, body=1956-10-12, body=1956-10-05, body=1957-01-02, body=1957-02-20, body=1957-02-08, body=1957-03-15, body=1957-03-14, body=1957-03-25, body=1957-03-12, body=1957-03-19, body=1957-04-23, body=1957-03-01, body=1957-11-05, body=1957-11-06, body=1957-11-07, body=1957-11-12, body=1957-11-19, body=1957-11-08, body=1951-05-02, body=1957-11-15, body=1955-10, body=1953-03
- **summary:** The FBI's 62-HQ-83894 case file includes investigative records, eyewitness testimonies, and public reports concerning Unidentified Flying Objects and flying discs documented between June 1947 and Jul…


## Confirmed (>=2 sources agree) (249)

### `cia-001-cia-uap-d001-intelligence-information-report-ussr-1973`
- **title:** CIA-UAP-D001, Intelligence Information Report, USSR, 1973
- **csv:** `12/20/73` -> `1973-12-20`
- **title dates:** 1973
- **confirmed date:** `1973` (via csv, title)
- **summary:** This document is a Central Intelligence Agency (CIA) intelligence information report (IIR) that describes human intelligence gathering activities in the Union of Soviet Socialist Republics (USSR). Th…

### `cia-002-cia-uap-017-placement-on-high-alert-due-to-perceived-aggress`
- **title:** CIA-UAP-017, Placement on High Alert Due to Perceived Aggressive Foreign Posturing
- **csv:** `July, 2008` -> `2008`
- **summary dates:** 2008-07
- **body dates (filtered):** 2008-07-03; 2008-07-02
- **confirmed date:** `2008-07` (via body, summary)
- **note:** csv `2008` disagrees
- **summary:** A never before released July 2008 report on a UFO sighting at the Harare International Airport. Individuals debated if the sighting was an advanced reconnaissance device of a foreign government or of…

### `cia-003-cia-uap-002-scientific-advisory-panel-on-unidentified-flying`
- **title:** CIA-UAP-002, Scientific Advisory Panel on Unidentified Flying Objects, Report, 1952-1953
- **csv:** `1952-1953` -> `1952`
- **title dates:** 1952; 1953
- **body dates (filtered):** 1953-01-17; 1953-03-13; 1953-03-12; 1952-07-02; 1953-02-18; 1953-02-25; 1950-08-15; 1952-07-19; 1952-08-05; 1952-10-13; 1944-06; 1949-10; 1951-01
- **confirmed date:** `1952` (via body, csv, title)
- **summary:** This file contains correspondence and reports dated 1952–1953 from the Scientific Advisory Panel on Unidentified Flying Objects, convened by the CIA’s Office of Scientific Intelligence. The panel’s p…

### `cia-004-cia-uap-003-the-central-intelligence-agency-and-overhead-rec`
- **title:** CIA-UAP-003, The Central Intelligence Agency and Overhead Reconnaissance; The U-2 and OXCART Programs, 1954-1974
- **csv:** `1954-1974` -> `1954`
- **title dates:** 1954; 1974
- **body dates (filtered):** 1953-04-15; 1957-05-06; 1956-07-10; 1954-07-04; 1960-05-01; 1950-04-08; 1952-06-13; 1983-12-14; 1952-10-07; 1985-08-19; 1988-08-28; 1953-11-30; 1954-03-05; 1988-07-23; 1954-06-07; 1985-05-20; 1954-05-12; 1983-05-23; 1955-05-13; 1984-11-08; 1954-10-15; 1987-04-22; 1952-06-15; 1985-06-21; 1985-04-24; 1953-08-03; 1985-05-22; 1955-08-29; 1954-03-23; 1953-10-21; 1953-10-26; 1954-08-02; 1954-09-24; 1954-04-15; 1954-07-26; 1954-09-13; 1954-11-05; 1954-11-18; 1954-11-19; 1954-11-24; 1954-11-26; 1954-12-02; 1955-04-28; 1954-12-03; 1949-06-20; 1954-12-22; 1955-03-02; 1955-02-21; 1983-08-05; 1988-08-26; 1955-01-28; 1955-01-31; 1956-01-24; 1955-04-12; 1986-05-12; 1955-04-29; 1955-08-03; 1955-06-27; 1965-10-12; 1986-04-03; 1983-10-04; 1986-04-24; 1955-07-27; 1986-03-14; 1955-08-04; 1955-08-08; 1955-09-22; 1955-10-03; 1955-11-28; 1986-03-06; 1956-04-14; 1956-05-15; 1988-10-12; 1956-08-01; 1956-09-17; 1956-12-09; 1960-08-15; 1954-12-13; 1987-05-21; 1955-12-27; 1956-02-15; 1956-02-07; 1956-03-05; 1956-02-24; 1956-06-21; 1956-01-10; 1956-04-29; 1956-05-07; 1956-05-28; 1955-07-21; 1956-05-31; 1956-01-30; 1955-05-23; 1955-05-30; 1956-02-27; 1956-05-11; 1955-09-26; 1956-04-23; 1956-06-20; 1956-06-22; 1956-02-20; 1956-05-04; 1956-06-23; 1956-07-02; 1956-07-05; 1956-07-04; 1956-07-09; 1987-07-08; 1956-07-11; 1956-07-19; 1956-11-26; 1956-07-30; 1956-07-26; 1956-08-29; 1956-09-11; 1956-10-15; 1956-10-29; 1956-10-28; 1956-10-30; 1956-11-01; 1956-12-18; 1956-11-06; 1956-11-07; 1956-10-03; 1956-10-23; 1956-11-15; 1956-11-20; 1956-12-10; 1986-05-07; 1960-01-04; 1960-01-07; 1956-12-15; 1956-12-22; 1957-03-18; 1957-04-02; 1957-04-12; 1957-06-08; 1957-09-16; 1957-06-07; 1957-08-22; 1957-08-28; 1959-07-09; 1957-08-21; 1957-09-06; 1957-08-23; 1957-08-10; 1957-04-25; 1957-10-11; 1957-10-03; 1957-09-20; 1957-11-15; 1957-10-13; 1958-11-06; 1957-08-27; 1958-03-05; 1958-06-27; 1957-10-27; 1958-03-01; 1958-03-07; 1958-07-07; 1958-06-25; 1958-10-11; 1958-07-29; 1958-07-09; 1958-09-08; 1985-02-16; 1958-07-15; 1958-02-07; 1959-10-06; 1959-02-16; 1958-12-04; 1957-10-04; 1958-05-29; 1959-02-17; 1959-06-18; 1959-07-07; 1959-02-12; 1959-06-09; 1959-09-27; 1959-09-12; 1959-12-06; 1960-02-02; 1960-02-05; 1960-04-09; 1960-03-14; 1960-04-26; 1960-05-16; 1962-02-13; 1960-05-07; 1960-05-27; 1960-07-08; 1960-07-25; 1960-05-31; 1960-08-17; 1962-03-06; 1965-04-25; 1961-03-21; 1969-09-25; 1960-08-09; 1962-03-01; 1960-05-06; 1961-01-18; 1959-01-01; 1962-02-17; 1962-07-30; 1962-09-30; 1963-08-05; 1962-02-07; 1961-01-25; 1964-01-15; 1961-09-14; 1961-09-25; 1961-10-01; 1961-09-21; 1962-12-14; 1960-10-27; 1960-12-11; 1961-04-20; 1962-08-30; 1962-10-16; 1962-11-14; 1962-10-14; 1963-02-27; 1962-10-24; 1962-10-04; 1962-10-06; 1962-11-20; 1962-10-12; 1962-10-13; 1962-10-01; 1963-11-30; 1963-12-09; 1957-09-25; 1958-03-24; 1958-03-28; 1958-06-10; 1958-07-16; 1959-05-14; 1959-09-13; 1959-09-24; 1960-06-06; 1961-03-03; 1961-03-06; 1962-01-12; 1962-02-23; 1962-01-13; 1962-03-13; 1962-03-26; 1962-07-28; 1962-09-03; 1962-08-11; 1962-09-08; 1962-09-09; 1962-12-17; 1962-12-25; 1962-12-28; 1963-01-20; 1962-11-11; 1962-12-05; 1964-03-31; 1964-05-24; 1963-05-28; 1963-11-01; 1964-03-16; 1964-07-07; 1964-08-06; 1964-10-16; 1964-12-09; 1965-01-11; 1964-10-26; 1964-11-22; 1964-11-25; 1964-12-19; 1965-01-08; 1967-09-08; 1967-12-13; 1968-01-05; 1968-03-16; 1968-04-03; 1968-03-31; 1968-05-18; 1969-01-05; 1970-11-24; 1973-12-12; 1973-03-30; 1973-07-21; 1974-01-06; 1964-03-02; 1964-04-24; 1968-12-11; 1966-11-23; 1971-02-09; 1970-11-10; 1973-10-08; 1972-08-12; 1973-08-30; 1958-04-23; 1958-06-26; 1958-07-23; 1958-12-17; 1958-09-24; 1958-11-12; 1958-12-22; 1959-07-14; 1959-07-20; 1984-12-05; 1959-08-20; 1959-09-14; 1959-11-18; 1960-11-15; 1962-02-27; 1961-09-11; 1962-02-26; 1962-04-25; 1962-04-30; 1962-05-02; 1963-01-15; 1963-11-12; 1963-01-21; 1963-10-22; 1964-02-29; 1963-11-29; 1964-02-25; 1963-05-24; 1964-07-09; 1965-12-28; 1965-01-27; 1965-08-03; 1965-11-20; 1965-04-30; 1962-07-05; 1962-07-06; 1963-04-05; 1964-08-05; 1964-11-05; 1962-10-23; 1964-08-17; 1965-03-18; 1965-06-03; 1966-12-21; 1967-01-05; 1967-05-04; 1967-05-17; 1967-05-29; 1967-12-31; 1967-10-30; 1968-03-08; 1968-01-23; 1968-05-08; 1966-12-12; 1966-12-28; 1967-11-03; 1968-05-16; 1968-06-08; 1968-06-04; 1967-01-26; 1960-05-28; 1960-08-19; 1957-06-20; 1957-08-05; 1957-08-11; 1957-09-10; 1965-11-15; 1966-11-21; 1954-05-24; 1957-01-28; 1959-02-09; 1956-03-12; 1954-06-18; 1956-05-18; 1954-08-23; 1954-06-28; 1955-02-14; 1959-02-23; 1984-11-02; 1984-09-20; 1987-02-20; 1992-04; 1951-02; 1951-10; 1950-06; 1951-04; 1950-03; 1952-09; 1953-03; 1953-07; 1954-01; 1953-06; 1952-02; 1953-01; 1954-02; 1966-08; 1975-07; 1972-12; 1974-12; 1958-08; 1959-04; 1963-03; 1961-11; 1977-08; 1961-05; 1958-01; 1959-03; 1961-07; 1967-07; 1963-06; 1965-02; 1968-02; 1971-05; 1969-04; 1972-03; 1973-01; 1963-09; 1974-08; 1969-12; 1970-08; 1973-06; 1968-07; 1960-09; 1961-08; 1962-06; 1966-09; 1966-07; 1976-05; 1967-04; 1971-01
- **confirmed date:** `1954` (via body, csv, title)
- **summary:** This CIA History Staff document chronicles the complete history of the U-2 and OXCART (A-12) high-altitude reconnaissance aircraft programs from 1954 to 1974, detailing their development, operations …

### `cia-006-cia-uap-005-german-scientist-s-article-on-flying-discs`
- **title:** CIA-UAP-005, German Scientist's Article on 'Flying Discs'
- **csv:** `1950` -> `1950`
- **body dates (filtered):** 1950-07-31
- **confirmed date:** `1950` (via body, csv)
- **summary:** This 1950 CIA Information Report from Chile discusses a German scientist's article theorizing that "Flying Discs" could be explained as a new type of aircraft based on aerodynamic principles develope…

### `cia-007-cia-uap-006-sighting-of-unconventional-aircraft`
- **title:** CIA-UAP-006, Sighting Of Unconventional Aircraft
- **csv:** `November, 1955` -> `1955`
- **summary dates:** 1955-10-04; 1955-11
- **confirmed date:** `1955` (via csv, summary)
- **summary:** This CIA information report from November 1955 describes a US national's eyewitness account of triangular aircraft with wing lights launch at a steep angle from an airfield near Baku, Azerbaijan on O…

### `cia-008-cia-uap-007-current-status-of-unidentified-flying-objects-uf`
- **title:** CIA-UAP-007, Current Status Of Unidentified Flying Objects (UFO) Project.
- **csv:** `December, 1953` -> `1953`
- **summary dates:** 1953-12
- **body dates (filtered):** 1953-12-17
- **confirmed date:** `1953-12` (via body, summary)
- **note:** csv `1953` disagrees
- **summary:** This December 1953 memorandum provides a status update on the Air Force's UFO project activities, including ongoing intelligence operations, equipment procurement for photographing UFOs, and Canada’s…

### `cia-009-cia-uap-008-speculative-paper-by-n-kardashev-and-a-sakharov`
- **title:** CIA-UAP-008, Speculative Paper By N Kardashev and A Sakharov on Charged Mass in Space at Conference on Origins Of Life, Armenia, 6-8 September 1971/Low Scientific Level Of Other Soviet Papers
- **csv:** `1972` -> `1972`
- **title dates:** 1971-09-08
- **body dates (filtered):** 1971-09-06; 1911-09-08
- **confirmed date:** `1971-09` (via body, title)
- **note:** csv `1972` disagrees
- **summary:** This 1972 CIA Intelligence Information Report summarizes a US attendee's observations of a speculative paper regarding charged mass behavior in space presented by Soviet scientists N.S. Kardashev and…

### `cia-011-cia-uap-010-report-on-conversations-with-soviet-scientists-o`
- **title:** CIA-UAP-010, Report on Conversations with Soviet Scientists on Subject of Unidentified Flying Objects in the USSR
- **csv:** `August, 1967` -> `1967`
- **summary dates:** 1967-08
- **confirmed date:** `1967` (via csv, summary)
- **summary:** This CIA document from August 1967 reports on conversations about UFO sightings with Soviet scientists during a US astrophysicist's trip to the USSR.

### `cia-012-cia-uap-011-the-sary-shagan-weapons-testing-range`
- **title:** CIA-UAP-011, The Sary Shagan Weapons Testing Range
- **csv:** `December, 1973` -> `1973`
- **summary dates:** 1973-12
- **confirmed date:** `1973` (via csv, summary)
- **summary:** This CIA Intelligence Information Report from December 1973 provides information on the Soviet Sary Shagan Weapons Testing Range, including details about its facilities, weapons systems (System-75 SA…

### `cia-013-cia-uap-012-combating-fatigue-in-crewmembers`
- **title:** CIA-UAP-012, Combating Fatigue In Crewmembers
- **csv:** `November, 1976` -> `1976`
- **summary dates:** 1976-11
- **confirmed date:** `1976` (via csv, summary)
- **summary:** This November 1976 CIA Foreign Intelligence Information Report summarizes Soviet Aeroflot's involvement in aerospace medical research, including their methods for combating crew fatigue through physi…

### `cia-015-cia-uap-014-british-activity-in-the-field-of-unidentified-fl`
- **title:** CIA-UAP-014, British activity in the Field of "Unidentified Flying Objects"
- **csv:** `December, 1952` -> `1952`
- **summary dates:** 1952-12
- **confirmed date:** `1952` (via csv, summary)
- **summary:** A December 1952 Memo on the activities the British are taking to identify UFOs. The memo references a UFO sighting at an RAF field seen by high officials and RAF pilots. A more redacted version of th…

### `cia-017-cia-uap-016-sightings-of-unidentified-flying-objects-in-lada`
- **title:** CIA-UAP-016, Sightings of Unidentified Flying Objects in Ladakh, Nepal, Sikkim and Bhutan
- **csv:** `1968` -> `1968`
- **body dates (filtered):** 1968-03-04; 1968-02-19; 1968-02-21
- **confirmed date:** `1968` (via body, csv)
- **summary:** A 1968 report about UFO sightings in Ladakh, Nepal, Sikkim and Bhutan. Seven UFO sightings are listed that took place between 19 Feb. to 25 Mar. 1968. A more redacted version of the report has been a…

### `cia-020-cia-uap-d020-memorandum-on-unconventional-aircraft-sightings`
- **title:** CIA-UAP-D020, Memorandum on Unconventional Aircraft Sightings, 1955
- **csv:** `1955` -> `1955`
- **title dates:** 1955
- **confirmed date:** `1955` (via csv, title)
- **summary:** This memorandum summarizes a Central Intelligence Agency (CIA) debriefing of a group of four individuals who reported observing a “flying saucer” or “unconventional aircraft” in 1955. The group, whic…

### `cia-021-cia-uap-d021-analysis-of-unconventional-aircraft-sightings-1`
- **title:** CIA-UAP-D021, Analysis of Unconventional Aircraft Sightings, 1955
- **csv:** `1955` -> `1955`
- **title dates:** 1955
- **confirmed date:** `1955` (via csv, title)
- **summary:** Sections 1 and 2 of this memorandum document a 1955 analysis of reports of “flying saucers” or “unconventional aircraft,” referencing the incident described in observer debriefings contained within C…

### `doe-002-doe-uap-d002-james-tuck-correspondence-1970s`
- **title:** DOE-UAP-D002, James Tuck Correspondence, 1970s
- **csv:** `1970s` -> `1970`
- **title dates:** 1970
- **confirmed date:** `1970` (via csv, title)
- **summary:** Personal correspondence to and from James Tuck, a Los Alamos National Laboratory-affiliated physicist, regarding his interest in unidentified anomalous phenomena circa 1970s.

### `doe-003-doe-uap-d003-pajarito-astronomers-invitation-1986`
- **title:** DOE-UAP-D003, Pajarito Astronomers Invitation, 1986
- **csv:** `5/20/86` -> `1986-05-20`
- **title dates:** 1986
- **body dates (filtered):** 1986-05-20; 1986-05-29
- **confirmed date:** `1986-05-20` (via body, csv)
- **summary:** A letter to the members of the Pajarito Astronomers club regarding an upcoming meeting featuring a presentation from a Los Alamos National Laboratory-affiliated physicist, Dr. John Warren, titled “Wh…

### `doe-004-doe-uap-d004-los-alamos-conference-on-aerial-phenomena-1949`
- **title:** DOE-UAP-D004, Los Alamos Conference on Aerial Phenomena, 1949
- **csv:** `3/22/49` -> `1949-03-22`
- **title dates:** 1949
- **confirmed date:** `1949` (via csv, title)
- **summary:** This document is a transcript of a 1949 conference held at Los Alamos Scientific Laboratory (now Los Alamos National Laboratory), Los Alamos, New Mexico. Attendees included several eminent scientists…

### `doe-005-doe-uap-d005-pantex-unidentified-object-incident-report-2015`
- **title:** DOE-UAP-D005, Pantex Unidentified Object Incident Report, 2015
- **csv:** `9/1/15` -> `2015-09-01`
- **title dates:** 2015
- **summary dates:** 2015-09-01; 2026-05-22
- **confirmed date:** `2015-09-01` (via csv, summary)
- **summary:** This file contains imagery and a report documenting the circumstances surrounding a September 1, 2015, incident involving an unidentified object intruding the airspace above the Pantex Plant near Ama…

### `dow-001-18-100754-general-1946-7-vol-2`
- **title:** 18_100754_ General 1946-7_Vol_2
- **csv:** `12/30/47` -> `1947-12-30`
- **title dates:** 1946
- **body dates (filtered):** 1947-08-29; 1947-11-18; 1947-11-12; 1947-11-24; 1947-10-22; 1947-09-05; 1947-08-22; 1947-12; 1987-10
- **confirmed date:** `1947-12` (via body, csv)
- **summary:** This file contains memorandums and correspondence related to flying disc/saucer sightings and that those are a matter of concern for the Air Materiel Command.

### `dow-002-18-6369445-general-1948-vol-1`
- **title:** 18_6369445_General_1948_Vol_1
- **csv:** `6/15/48` -> `1948-06-15`
- **title dates:** 1948
- **body dates (filtered):** 1948-03-11; 1948-06-03; 1948-06-15; 1948-05-27; 1948-04-12; 1948-02-06; 1948-03-09; 1948-03-05; 1948-03-08; 1948-03-07; 1948-02-12; 1947-12-30; 1948-03-03; 1948-01-07; 1948-02-24; 1948-02-13
- **confirmed date:** `1948-06-15` (via body, csv)
- **summary:** This file contains memorandums, correspondence, and forms related to the reporting of information on flying discs and investigations into sightings.

### `dow-003-331-120752-numeric-files-1944-1945-37153-german-armament-equ`
- **title:** 331_120752_Numeric_Files_1944–1945_37153_German_Armament_Equipment_Documents
- **csv:** `3/18/45` -> `1945-03-18`
- **title dates:** 1944; 1945
- **body dates (filtered):** 1945-03-14; 1945-03-01; 1945-02-04; 1945-02-05; 1945-01-16; 1945-01-25; 1945-01-30; 1944-12-15; 1944-12-17; 1944-12-23; 1944-12-24; 1944-12-27; 1944-12-28; 1944-12-31; 1945-01-02; 1945-01-15; 1915-02
- **confirmed date:** `1945-03` (via body, csv)
- **note:** csv day 18 differs from body day 14, body day 1
- **summary:** This file contains SHAEF messages and memorandums related to "night phenomena (foofighters)," flak rockets, unidentified cylindrical objects, and blinking lights. The documents include multiple refer…

### `dow-004-341-110448-records-relating-to-the-collection-and-disseminat`
- **title:** 341_110448_Records_Relating_to_the_Collection_and_Dissemination_of_Intelligence_1948-1955-TS_CONT_No.2_2-5300-2-5399
- **csv:** `11/8/48` -> `1948-11-08`
- **title dates:** 1948; 1955
- **summary dates:** 1948-11
- **confirmed date:** `1948-11` (via csv, summary)
- **summary:** An Air Force intelligence report from November 1948 relating to unidentified flying objects and flying saucers.

### `dow-005-341-110677-numerical-file-5-2500`
- **title:** 341_110677_Numerical_File,_5-2500
- **csv:** `10/14/55` -> `1955-10-14`
- **summary dates:** 1955-10-14
- **confirmed date:** `1955-10-14` (via csv, summary)
- **summary:** Air Intelligence Information Report, 14 October 1955, Report of eye witness account of the ascent and flight of a unconventional aircraft in the trans-Caucasus region on the USSR.

### `dow-006-342-hs1-416511228-319-1-flying-discs-1949`
- **title:** 342_HS1-416511228_319.1 Flying Discs 1949
- **csv:** `1/9/50` -> `1950-01-09`
- **title dates:** 1949
- **body dates (filtered):** 1950-01-09; 1948-11-02; 1950-01-06; 1949-08-23; 1949-07-28; 1949-08-01; 1949-07-30; 1949-07-24; 1949-07-25; 1919-06-26; 1949-06-10; 1949-05-02; 1949-06-15; 1949-04-08; 1949-04-11; 1949-04-23; 1949-04-14; 1949-04-18; 1948-06-28; 1949-03-01; 1948-02-06; 1949-02-28; 1949-02-17; 1948-03-24; 1949-02-08; 1949-02-06; 1949-02-07; 1919-02-07; 1948-02-26; 1949-01-08; 1949-01-04; 1949-01-17; 1946-08-15; 1949-01-19; 1949-01-12; 1948-12-03; 1948-12-06; 1949-01-24; 1949-01-01; 1948-11-17; 1948-12-13; 1948-12-11; 1947-12-20; 1919-01-01; 1946-11-19; 1943-12-06; 1918-12-09
- **confirmed date:** `1950-01-09` (via body, csv)
- **summary:** This file primarily contains incident reports on Unidentified Flying Objects (UFOs) written in compliance with the 1948 Flight Service Regulation (FSR) 200-4. The incidents were witnessed by military…

### `dow-010-dow-uap-d10-mission-report-middle-east-may-2022`
- **family:** `DOW-UAP-D10`
- **title:** DOW-UAP-D10, Mission Report, Middle East, May 2022
- **csv:** `5/6/22` -> `2022-05-06`
- **title dates:** 2022-05
- **body dates (filtered):** 2025-10-07
- **confirmed date:** `2022-05` (via csv, title)
- **summary:** This document is a Mission Report (MISREP), a standardized reporting form the U.S. Military uses to record the circumstances surrounding its operations. U.S. military services often use MISREPs to re…

### `dow-011-dow-uap-d12-mission-report-iraq-may-2022`
- **family:** `DOW-UAP-D12`
- **title:** DOW-UAP-D12, Mission Report, Iraq, May 2022
- **csv:** `5/20/22` -> `2022-05-20`
- **title dates:** 2022-05
- **body dates (filtered):** 2025-10-08
- **confirmed date:** `2022-05` (via csv, title)
- **summary:** This document is a Mission Report (MISREP), a standardized reporting form the U.S. Military uses to record the circumstances surrounding its operations. U.S. military services often use MISREPs to re…

### `dow-012-dow-uap-d14-mission-report-iraq-may-2022`
- **family:** `DOW-UAP-D14`
- **title:** DOW-UAP-D14, Mission Report, Iraq, May 2022
- **csv:** `5/29/22` -> `2022-05-29`
- **title dates:** 2022-05
- **body dates (filtered):** 2025-10-08
- **confirmed date:** `2022-05` (via csv, title)
- **summary:** This document is a Mission Report (MISREP), a standardized reporting form the U.S. Military uses to record the circumstances surrounding its operations. U.S. military services often use MISREPs to re…

### `dow-013-dow-uap-d16-mission-report-syria-july-2022`
- **family:** `DOW-UAP-D16`
- **title:** DOW-UAP-D16, Mission Report, Syria, July 2022
- **csv:** `7/31/22` -> `2022-07-31`
- **title dates:** 2022-07
- **body dates (filtered):** 2025-10-17; 2025-10-08
- **confirmed date:** `2022-07` (via csv, title)
- **summary:** This document is a Mission Report (MISREP), a standardized reporting form the U.S. Military uses to record the circumstances surrounding its operations. U.S. military services often use MISREPs to re…

### `dow-014-dow-uap-d18-mission-report-iraq-december-2022`
- **family:** `DOW-UAP-D18`
- **title:** DOW-UAP-D18, Mission Report, Iraq, December 2022
- **csv:** `12/1/22` -> `2022-12-01`
- **title dates:** 2022-12
- **body dates (filtered):** 2025-10-17; 2025-10-08
- **confirmed date:** `2022-12` (via csv, title)
- **summary:** This document is a Mission Report (MISREP), a standardized reporting form the U.S. Military uses to record the circumstances surrounding its operations. U.S. military services often use MISREPs to re…

### `dow-015-dow-uap-d19-mission-report-syria-february-21-2023`
- **family:** `DOW-UAP-D19`
- **title:** DOW-UAP-D19, Mission Report, Syria, February 21, 2023
- **csv:** `2/21/23` -> `2023-02-21`
- **title dates:** 2023-02-21
- **body dates (filtered):** 2025-10-17; 2025-10-08
- **confirmed date:** `2023-02-21` (via csv, title)
- **summary:** This document is a Mission Report (MISREP), a standardized reporting form the U.S. Military uses to record the circumstances surrounding its operations. U.S. military services often use MISREPs to re…

### `dow-016-dow-uap-d20-mission-report-iraq-2023`
- **family:** `DOW-UAP-D20`
- **title:** DOW-UAP-D20, Mission Report, Iraq, 2023
- **csv:** `3/31/23` -> `2023-03-31`
- **title dates:** 2023
- **body dates (filtered):** 2025-10-17; 2025-10-08
- **confirmed date:** `2023` (via csv, title)
- **summary:** This document is a Mission Report (MISREP), a standardized reporting form the U.S. Military uses to record the circumstances surrounding its operations. U.S. military services often use MISREPs to re…

### `dow-017-dow-uap-d23-mission-report-united-arab-emirates-october-2023`
- **family:** `DOW-UAP-D23`
- **title:** DOW-UAP-D23, Mission Report, United Arab Emirates, October 2023
- **csv:** `10/31/23` -> `2023-10-31`
- **title dates:** 2023-10
- **confirmed date:** `2023-10` (via csv, title)
- **summary:** This document is a Mission Report (MISREP), a standardized reporting form the U.S. Military uses to record the circumstances surrounding its operations. U.S. military services often use MISREPs to re…

### `dow-018-dow-uap-d23-mission-report-united-arab-emirates-october-2023`
- **family:** `DOW-UAP-D23`
- **title:** DOW-UAP-D23, Mission Report, United Arab Emirates, October 2023
- **csv:** `10/31/23` -> `2023-10-31`
- **title dates:** 2023-10
- **confirmed date:** `2023-10` (via csv, title)
- **summary:** This document is a Mission Report (MISREP), a standardized reporting form the U.S. Military uses to record the circumstances surrounding its operations. U.S. military services often use MISREPs to re…

### `dow-019-dow-uap-d25-mission-report-greece-january-2024`
- **family:** `DOW-UAP-D25`
- **title:** DOW-UAP-D25, Mission Report, Greece, January 2024
- **csv:** `1/25/24` -> `2024-01-25`
- **title dates:** 2024-01
- **body dates (filtered):** 2025-10-28; 2025-10-24
- **confirmed date:** `2024-01` (via csv, title)
- **summary:** This document is a Mission Report (MISREP), a standardized reporting form the U.S. Military uses to record the circumstances surrounding its operations. U.S. military services often use MISREPs to re…

### `dow-021-dow-uap-d28-mission-report-iraq-september-2024`
- **family:** `DOW-UAP-D28`
- **title:** DOW-UAP-D28, Mission Report, Iraq, September 2024
- **csv:** `9/20/24` -> `2024-09-20`
- **title dates:** 2024-09
- **body dates (filtered):** 2025-10-28; 2025-10-24
- **confirmed date:** `2024-09` (via csv, title)
- **summary:** This document is a Mission Report (MISREP), a standardized reporting form the U.S. Military uses to record the circumstances surrounding its operations. U.S. military services often use MISREPs to re…

### `dow-023-dow-uap-d32-mission-report-syria-october-2024`
- **family:** `DOW-UAP-D32`
- **title:** DOW-UAP-D32, Mission Report, Syria, October 2024
- **csv:** `10/20/24` -> `2024-10-20`
- **title dates:** 2024-10
- **body dates (filtered):** 2025-10-28; 2025-10-24
- **confirmed date:** `2024-10` (via csv, title)
- **summary:** This document is a Mission Report (MISREP), a standardized reporting form the U.S. Military uses to record the circumstances surrounding its operations. U.S. military services often use MISREPs to re…

### `dow-024-dow-uap-d32-mission-report-syria-october-2024`
- **family:** `DOW-UAP-D32`
- **title:** DOW-UAP-D32, Mission Report, Syria, October 2024
- **csv:** `10/20/24` -> `2024-10-20`
- **title dates:** 2024-10
- **body dates (filtered):** 2025-10-28; 2025-10-24
- **confirmed date:** `2024-10` (via csv, title)
- **summary:** This document is a Mission Report (MISREP), a standardized reporting form the U.S. Military uses to record the circumstances surrounding its operations. U.S. military services often use MISREPs to re…

### `dow-025-dow-uap-d32-mission-report-syria-october-2024`
- **family:** `DOW-UAP-D32`
- **title:** DOW-UAP-D32, Mission Report, Syria, October 2024
- **csv:** `10/20/24` -> `2024-10-20`
- **title dates:** 2024-10
- **body dates (filtered):** 2025-10-28; 2025-10-24
- **confirmed date:** `2024-10` (via csv, title)
- **summary:** This document is a Mission Report (MISREP), a standardized reporting form the U.S. Military uses to record the circumstances surrounding its operations. U.S. military services often use MISREPs to re…

### `dow-026-dow-uap-d33-mission-report-greece-october-2023`
- **family:** `DOW-UAP-D33`
- **title:** DOW-UAP-D33, Mission Report, Greece, October 2023
- **csv:** `10/27/23` -> `2023-10-27`
- **title dates:** 2023-10
- **body dates (filtered):** 2026-01-22
- **confirmed date:** `2023-10` (via csv, title)
- **summary:** This document is a Mission Report (MISREP), a standardized reporting form the U.S. Military uses to record the circumstances surrounding its operations. U.S. military services often use MISREPs to re…

### `dow-027-dow-uap-d35-mission-report-greece-october-2023`
- **family:** `DOW-UAP-D35`
- **title:** DOW-UAP-D35, Mission Report, Greece, October 2023
- **csv:** `10/29/23` -> `2023-10-29`
- **title dates:** 2023-10
- **body dates (filtered):** 2026-01-22
- **confirmed date:** `2023-10` (via csv, title)
- **summary:** This document is a Mission Report (MISREP), a standardized reporting form the U.S. Military uses to record the circumstances surrounding its operations. U.S. military services often use MISREPs to re…

### `dow-028-dow-uap-d38-range-fouler-debrief-middle-east-may-2020`
- **family:** `DOW-UAP-D38`
- **title:** DOW-UAP-D38, Range Fouler Debrief, Middle East, May 2020
- **csv:** `5/14/20` -> `2020-05-14`
- **title dates:** 2020-05
- **body dates (filtered):** 2020-05-14; 2026-01-26
- **confirmed date:** `2020-05-14` (via body, csv)
- **summary:** This document is a Range Fouler Debrief, a standardized reporting form the U.S. Navy uses to record the circumstances surrounding an unauthorized intrusion into controlled airspace during active mili…

### `dow-030-dow-uap-d42-range-fouler-debrief-japan-2023`
- **family:** `DOW-UAP-D42`
- **title:** DOW-UAP-D42, Range Fouler Debrief, Japan, 2023
- **csv:** `8/31/20` -> `2020-08-31`
- **title dates:** 2023
- **body dates (filtered):** 2020-08-31; 2026-03-16
- **confirmed date:** `2020-08-31` (via body, csv)
- **summary:** This document is a Range Fouler Debrief Form, a standardized reporting form the U.S. Navy uses to record the circumstances surrounding an unauthorized intrusion into controlled airspace during active…

### `dow-031-dow-uap-d44-range-fouler-reporting-form-gulf-of-aden-october`
- **family:** `DOW-UAP-D44`
- **title:** DOW-UAP-D44, Range Fouler Reporting Form, Gulf of Aden, October 2020
- **csv:** `10/15/20` -> `2020-10-15`
- **title dates:** 2020-10
- **body dates (filtered):** 2020-10-15; 2026-03-27
- **confirmed date:** `2020-10-15` (via body, csv)
- **summary:** This document is a Range Fouler Reporting Form, a standardized reporting form the U.S. Navy uses to record the circumstances surrounding an unauthorized intrusion into controlled airspace during acti…

### `dow-032-dow-uap-d48-department-of-the-air-force-report-1996`
- **family:** `DOW-UAP-D48`
- **title:** DOW-UAP-D48, Department of the Air Force Report, 1996
- **csv:** `9/10/96` -> `1996-09-10`
- **title dates:** 1996
- **body dates (filtered):** 1996-09-10; 1996-01-31; 1964-08-14; 1973-03-06; 1965-03-02; 1959-12-12; 1958-04-19; 1981-12-18; 1963-05-01; 1958-12-30; 1961-04-25; 1959-07-21; 1992-08-22; 1986-05-03; 1993-10-05; 1980-12-08; 1969-08-27; 1965-11-30; 1962-01-24; 1965-02-23; 1957-06-11; 1957-09-25; 1957-12-17; 1958-01-10; 1958-02-07; 1958-04-05; 1958-06-03; 1958-07-19; 1958-08-28; 1958-09-14; 1958-09-18; 1958-11-17; 1958-12-18; 1959-01-15; 1959-01-27; 1959-02-04; 1959-02-20; 1959-03-18; 1959-04-14; 1959-05-18; 1959-06-06; 1959-07-28; 1959-08-11; 1959-08-24; 1959-09-09; 1959-09-16; 1959-10-06; 1959-10-09; 1959-10-29; 1959-11-04; 1959-11-24; 1959-11-26; 1959-12-08; 1959-12-18; 1960-01-06; 1960-01-26; 1960-02-11; 1960-02-26; 1960-03-08; 1960-03-10; 1960-04-07; 1960-04-22; 1960-05-06; 1960-05-20; 1960-05-24; 1960-06-11; 1960-06-22; 1960-06-27; 1960-07-02; 1960-07-22; 1960-07-29; 1960-08-09; 1960-08-12; 1960-09-12; 1960-09-16; 1960-09-19; 1960-09-25; 1960-09-29; 1960-10-11; 1960-10-12; 1960-10-13; 1960-10-22; 1960-11-15; 1960-11-29; 1960-12-15; 1960-12-16; 1961-01-23; 1961-01-24; 1961-01-31; 1961-02-21; 1961-02-24; 1961-03-13; 1961-03-24; 1961-05-12; 1961-05-24; 1961-05-26; 1961-06-07; 1961-07-06; 1961-07-12; 1961-07-31; 1961-08-08; 1961-08-22; 1961-08-23; 1961-09-08; 1961-09-09; 1961-09-13; 1961-10-02; 1961-10-05; 1961-10-21; 1961-11-10; 1961-11-18; 1961-11-22; 1961-11-29; 1961-12-01; 1961-12-07; 1961-12-12; 1961-12-19; 1961-12-20; 1961-12-22; 1962-01-17; 1962-01-23; 1962-01-26; 1962-02-13; 1962-02-16; 1962-02-20; 1962-02-21; 1962-02-28; 1962-03-07; 1962-04-09; 1962-04-11; 1962-04-23; 1962-04-26; 1962-05-08; 1962-05-11; 1962-05-24; 1962-06-17; 1962-06-26; 1962-07-12; 1962-07-13; 1962-07-18; 1962-07-19; 1962-07-22; 1962-08-01; 1962-08-05; 1962-08-09; 1962-08-10; 1962-08-13; 1962-08-27; 1962-09-19; 1962-10-02; 1962-10-03; 1962-10-18; 1962-10-19; 1962-10-26; 1962-11-07; 1962-11-11; 1962-11-14; 1962-12-05; 1962-12-12; 1962-12-17; 1963-01-25; 1963-01-31; 1963-02-13; 1963-02-28; 1963-03-01; 1963-03-09; 1963-03-11; 1963-03-15; 1963-03-16; 1963-03-21; 1963-03-23; 1963-04-24; 1963-04-26; 1963-05-09; 1963-05-15; 1963-06-04; 1963-06-12; 1963-07-03; 1963-07-12; 1963-07-18; 1963-07-26; 1963-07-30; 1963-07-31; 1963-08-24; 1963-09-06; 1963-09-11; 1963-09-25; 1963-10-03; 1963-10-07; 1963-10-16; 1963-10-25; 1963-11-04; 1963-11-13; 1963-11-27; 1963-12-18; 1964-01-30; 1964-02-12; 1964-02-25; 1964-03-11; 1964-04-01; 1964-04-03; 1964-04-14; 1964-04-23; 1964-05-19; 1964-06-18; 1964-06-30; 1964-07-06; 1964-07-17; 1964-07-28; 1964-07-29; 1964-08-07; 1964-08-27; 1964-08-31; 1964-09-04; 1964-09-15; 1964-09-22; 1964-09-23; 1964-10-08; 1964-10-23; 1964-11-05; 1964-11-28; 1964-12-01; 1964-12-04; 1964-12-11; 1964-12-22; 1965-01-08; 1965-01-12; 1965-01-21; 1965-01-23; 1965-02-17; 1965-02-27; 1965-03-12; 1965-03-21; 1965-03-26; 1965-04-03; 1965-04-06; 1965-04-28; 1965-05-22; 1965-05-27; 1965-06-03; 1965-06-08; 1965-06-10; 1965-06-25; 1965-07-01; 1965-07-12; 1965-07-20; 1965-08-03; 1965-08-04; 1965-08-05; 1965-08-11; 1965-08-26; 1965-09-29; 1965-09-30; 1965-10-05; 1965-10-25; 1965-11-08; 1965-11-29; 1965-12-20; 1966-01-19; 1966-02-10; 1966-02-11; 1966-02-15; 1966-02-19; 1966-03-04; 1966-03-16; 1966-03-18; 1966-03-19; 1966-03-30; 1966-04-07; 1966-04-08; 1966-04-19; 1966-05-03; 1966-05-13; 1966-05-14; 1966-05-17; 1966-05-26; 1966-05-30; 1966-06-01; 1966-06-03; 1966-06-06; 1966-06-09; 1966-06-10; 1966-06-26; 1966-06-30; 1966-07-12; 1966-07-13; 1966-07-18; 1966-08-08; 1966-08-10; 1966-08-16; 1966-08-19; 1966-09-12; 1966-09-16; 1966-09-20; 1966-10-05; 1966-10-11; 1966-10-12; 1966-10-26; 1966-11-02; 1966-11-06; 1966-11-11; 1966-12-05; 1966-12-06; 1966-12-11; 1966-12-21; 1967-01-17; 1967-01-22; 1967-02-02; 1967-02-04; 1967-02-13; 1967-03-05; 1967-03-16; 1967-04-05; 1967-04-07; 1967-04-17; 1967-04-19; 1967-05-04; 1967-05-19; 1967-05-22; 1967-06-04; 1967-06-09; 1967-06-14; 1967-07-06; 1967-07-14; 1967-07-22; 1967-07-27; 1967-07-29; 1967-08-01; 1967-09-08; 1967-10-11; 1967-10-14; 1967-10-27; 1967-11-05; 1967-11-07; 1967-11-10; 1967-12-21; 1968-01-07; 1968-01-31; 1968-02-26; 1968-03-04; 1968-03-06; 1968-04-06; 1968-04-18; 1968-04-27; 1968-05-03; 1968-06-01; 1968-06-22; 1968-06-29; 1968-07-11; 1968-08-06; 1968-08-10; 1968-08-16; 1968-09-25; 1968-09-27; 1968-11-16; 1968-11-24; 1968-12-07; 1969-01-16; 1969-02-24; 1969-03-17; 1969-03-27; 1969-04-12; 1969-08-12; 1969-08-20; 1969-09-16; 1969-10-10; 1969-12-03; 1969-12-12; 1970-02-08; 1970-03-13; 1970-05-30; 1970-06-09; 1970-06-19; 1970-08-31; 1970-11-30; 1970-12-22; 1971-04-05; 1971-05-08; 1971-05-30; 1971-06-29; 1971-08-06; 1971-09-01; 1971-12-04; 1972-01-22; 1972-03-02; 1972-06-13; 1972-10-02; 1973-04-05; 1973-08-23; 1973-11-03; 1974-03-06; 1974-03-23; 1974-07-13; 1975-05-22; 1977-05-26; 1978-01-06; 1978-05-13; 1978-05-20; 1978-06-26; 1978-10-13; 1978-11-13; 1978-12-10; 1979-02-24; 1979-05-04; 1979-06-27; 1979-09-20; 1980-01-17; 1980-02-09; 1980-03-03; 1980-04-26; 1980-05-29; 1980-10-31; 1980-12-06; 1981-02-21; 1981-05-23; 1981-06-23; 1981-08-06; 1981-12-15; 1982-03-05; 1982-09-28; 1982-12-20; 1983-02-09; 1983-03-28; 1983-05-19; 1983-06-09; 1983-07-14; 1983-11-17; 1984-02-05; 1984-06-09; 1984-06-13; 1984-09-08; 1984-12-12; 1985-03-12; 1985-06-30; 1985-09-28; 1985-10-08; 1986-02-09; 1986-09-17; 1986-12-05; 1987-03-26; 1987-05-15; 1987-06-19; 1988-02-02; 1988-09-24; 1989-09-25; 1990-04-11; 1990-07-25; 1990-12-01; 1991-04-18; 1991-05-14; 1991-11-28; 1991-12-07; 1992-02-11; 1992-03-14; 1992-06-10; 1992-07-02; 1993-03-25; 1993-07-19; 1993-08-09; 1993-09-03; 1993-12-16; 1994-04-13; 1994-06-24; 1994-08-03; 1994-08-29; 1994-10-06; 1994-11-29; 1994-12-30; 1995-01-10; 1995-01-29; 1995-03-22; 1995-03-24; 1995-04-07; 1995-05-23; 1995-05-31; 1995-07-31; 1995-08-29; 1995-10-22; 1995-12-02; 1995-12-15; 1996-04-03; 1996-04-30; 1996-07-25; 1960-05-13; 1960-11-23; 1961-03-25; 1961-08-15; 1962-02-08; 1962-06-19; 1962-07-10; 1962-09-18; 1962-10-27; 1962-12-13; 1963-04-02; 1963-05-07; 1963-06-19; 1963-11-26; 1963-12-21; 1964-01-21; 1964-03-19; 1964-08-19; 1964-10-03; 1964-12-21; 1965-01-22; 1965-02-03; 1965-05-29; 1965-08-25; 1965-11-06; 1965-12-16; 1966-02-03; 1966-02-28; 1966-05-25; 1966-07-01; 1966-08-17; 1966-10-02; 1966-12-14; 1967-01-11; 1967-01-26; 1967-03-08; 1967-03-22; 1967-04-20; 1967-05-24; 1967-07-19; 1967-09-07; 1967-09-27; 1967-10-18; 1967-12-13; 1968-01-11; 1968-07-04; 1968-09-18; 1968-11-08; 1968-12-05; 1968-12-15; 1968-12-18; 1969-01-22; 1969-01-30; 1969-02-05; 1969-02-26; 1969-05-21; 1969-06-21; 1969-06-29; 1969-07-26; 1969-08-09; 1969-11-22; 1970-01-14; 1970-01-23; 1970-03-20; 1970-04-22; 1970-07-23; 1970-08-19; 1970-12-11; 1971-02-03; 1971-03-13; 1971-04-01; 1971-09-29; 1971-10-21; 1972-01-31; 1972-03-11; 1972-07-23; 1972-09-22; 1972-10-15; 1972-11-10; 1972-12-10; 1973-04-20; 1973-06-10; 1973-07-16; 1973-10-26; 1973-11-06; 1973-12-16; 1974-01-19; 1974-04-13; 1974-05-17; 1974-10-10; 1974-11-15; 1974-11-22; 1974-12-18; 1975-01-22; 1975-02-06; 1975-04-09; 1975-05-07; 1975-06-12; 1975-06-21; 1975-08-08; 1975-08-26; 1975-10-16; 1975-11-19; 1975-12-12; 1976-01-17; 1976-02-19; 1976-03-26; 1976-04-22; 1976-05-04; 1978-01-26; 1978-03-05; 1979-01-30; 1980-02-14; 1980-09-09; 1980-11-15; 1981-05-22; 1981-08-03; 1981-09-24; 1981-10-06; 1981-11-20; 1982-01-15; 1982-02-26; 1982-04-10; 1982-06-09; 1982-07-16; 1982-08-26; 1982-10-27; 1983-01-26; 1983-04-11; 1983-04-28; 1983-05-26; 1983-06-28; 1983-07-28; 1983-09-08; 1983-09-22; 1984-03-01; 1984-08-16; 1984-09-21; 1984-11-14; 1986-09-05; 1987-02-26; 1987-03-20; 1988-02-08; 1989-02-14; 1989-03-24; 1989-06-10; 1989-08-18; 1989-08-27; 1989-10-21; 1989-11-18; 1989-12-11; 1990-01-24; 1990-02-14; 1990-03-26; 1990-04-13; 1990-06-01; 1990-06-11; 1990-08-02; 1990-08-18; 1990-10-01; 1990-10-30; 1990-11-26; 1991-01-07; 1991-03-08; 1991-04-12; 1991-05-29; 1991-07-03; 1992-02-23; 1992-04-09; 1992-05-13; 1992-06-07; 1992-07-07; 1992-07-24; 1992-08-31; 1992-09-09; 1992-10-12; 1992-11-22; 1992-12-18; 1993-02-03; 1993-03-30; 1993-05-13; 1993-06-26; 1993-08-30; 1993-10-26; 1993-12-08; 1994-02-19; 1994-03-10; 1994-11-01; 1995-08-05; 1995-11-04; 1995-12-30; 1996-01-14; 1996-02-17; 1996-02-24; 1996-03-27; 1996-04-24; 1996-05-24; 1996-07-16; 1958-12-20; 1959-02-03; 1959-02-06; 1959-02-25; 1959-04-03; 1959-05-04; 1959-08-14; 1960-02-02; 1960-02-05; 1960-02-24; 1960-03-22; 1960-04-08; 1960-04-21; 1960-04-28; 1960-05-27; 1960-06-24; 1960-07-01; 1960-07-28; 1960-08-10; 1960-08-30; 1960-09-28; 1960-10-07; 1960-10-24; 1960-12-20; 1961-01-20; 1961-02-10; 1961-02-20; 1961-03-03; 1961-03-28; 1961-03-31; 1961-05-03; 1961-05-23; 1961-06-24; 1961-07-20; 1961-07-25; 1961-08-03; 1961-09-06; 1961-09-07; 1961-09-23; 1961-09-28; 1961-10-06; 1961-10-24; 1961-11-21; 1961-12-13; 1961-12-15; 1962-01-20; 1962-01-29; 1962-02-23; 1962-03-16; 1962-05-04; 1962-06-07; 1962-07-11; 1962-07-25; 1962-09-12; 1962-10-06; 1962-10-12; 1962-12-06; 1962-12-19; 1963-01-10; 1963-01-29; 1963-02-06; 1963-02-16; 1963-03-30; 1963-04-04; 1963-04-13; 1963-04-19; 1963-04-27; 1963-05-13; 1963-05-24; 1963-05-29; 1963-06-20; 1963-07-16; 1963-08-21; 1963-08-30; 1963-09-17; 1963-09-23; 1963-11-01; 1963-11-09; 1963-11-14; 1963-12-12; 1963-12-16; 1964-01-15; 1964-01-23; 1964-02-17; 1964-02-26; 1964-03-13; 1964-03-23; 1964-07-30; 1964-08-11; 1964-08-13; 1964-09-01; 1964-10-02; 1964-11-04; 1964-12-08; 1964-12-10; 1965-01-19; 1965-02-11; 1965-03-05; 1965-03-23; 1965-04-30; 1965-05-06; 1965-05-21; 1965-06-14; 1965-06-18; 1965-06-30; 1965-07-21; 1965-08-16; 1965-08-21; 1965-09-21; 1965-10-15; 1965-10-20; 1965-11-27; 1965-12-04; 1965-12-15; 1965-12-21; 1965-12-22; 1966-02-17; 1966-03-25; 1966-04-05; 1966-04-20; 1966-05-24; 1966-06-16; 1966-07-22; 1966-07-29; 1966-08-26; 1966-09-28; 1966-11-03; 1966-11-24; 1967-01-18; 1967-02-24; 1967-03-17; 1967-04-12; 1967-04-26; 1967-04-28; 1967-06-20; 1967-06-23; 1967-07-01; 1967-08-16; 1967-09-11; 1967-09-19; 1967-10-25; 1967-12-05; 1968-01-18; 1968-02-28; 1968-03-13; 1968-04-02; 1968-04-17; 1968-06-05; 1968-06-12; 1968-06-13; 1968-08-21; 1968-09-10; 1968-09-26; 1968-11-06; 1968-11-19; 1968-12-04; 1969-02-09; 1969-03-04; 1969-04-15; 1969-05-20; 1969-05-23; 1969-06-03; 1969-08-23; 1969-10-24; 1970-04-08; 1970-04-15; 1970-06-25; 1970-08-18; 1970-10-23; 1970-11-06; 1971-01-21; 1971-03-20; 1971-04-22; 1971-05-05; 1971-06-20; 1971-08-12; 1971-08-27; 1971-10-23; 1971-11-02; 1972-01-20; 1972-02-16; 1972-03-01; 1972-03-17; 1972-05-20; 1972-05-24; 1972-07-07; 1972-09-01; 1972-10-10; 1972-10-11; 1972-12-21; 1973-03-09; 1973-05-16; 1973-06-12; 1973-06-26; 1973-07-13; 1973-08-21; 1973-09-27; 1973-10-05; 1973-11-10; 1973-12-13; 1974-02-11; 1974-02-13; 1974-03-01; 1974-04-10; 1974-05-30; 1974-06-06; 1974-08-14; 1974-10-29; 1974-12-10; 1975-01-09; 1975-03-09; 1975-04-18; 1975-05-20; 1975-06-08; 1975-08-07; 1975-08-20; 1975-09-09; 1975-10-09; 1975-12-04; 1975-12-14; 1976-01-15; 1976-03-14; 1976-03-22; 1976-06-02; 1976-06-25; 1976-07-08; 1976-08-06; 1976-12-19; 1977-05-12; 1977-09-05; 1978-02-24; 1978-03-16; 1978-06-10; 1978-06-14; 1978-08-04; 1978-12-13; 1979-05-28; 1979-06-10; 1979-10-01; 1979-11-21; 1980-02-06; 1980-06-18; 1980-12-13; 1981-02-28; 1981-03-16; 1981-04-24; 1981-09-03; 1981-10-31; 1982-01-21; 1982-03-06; 1982-05-11; 1982-10-30; 1982-11-17; 1983-04-15; 1983-06-20; 1983-07-31; 1984-01-31; 1984-04-14; 1984-04-17; 1984-06-25; 1984-08-28; 1984-12-04; 1984-12-22; 1985-02-07; 1985-08-28; 1986-04-18; 1987-02-11; 1987-10-26; 1987-11-29; 1988-09-02; 1988-09-05; 1988-11-06; 1989-05-10; 1989-09-04; 1989-09-05; 1990-01-01; 1990-03-14; 1990-06-08; 1990-06-23; 1990-11-13; 1991-11-17; 1992-04-25; 1992-09-25; 1992-11-28; 1993-08-02; 1994-01-25; 1994-02-07; 1994-05-03; 1994-08-27; 1995-05-14; 1995-07-10; 1995-11-06; 1996-07-02; 1957-01-25; 1957-04-19; 1957-05-21; 1957-08-30; 1957-09-20; 1957-10-03; 1957-10-11; 1957-10-24; 1957-12-07; 1957-12-19; 1958-01-28; 1958-02-28; 1958-04-23; 1958-06-04; 1958-06-13; 1958-07-11; 1958-07-12; 1958-07-23; 1958-07-26; 1958-08-06; 1958-08-17; 1958-10-11; 1958-11-05; 1958-11-08; 1958-11-26; 1958-12-05; 1958-12-16; 1959-01-23; 1959-01-30; 1959-02-28; 1959-03-21; 1959-03-26; 1959-04-07; 1959-04-22; 1959-04-24; 1959-05-12; 1959-05-21; 1959-05-22; 1959-06-11; 1959-06-25; 1959-06-29; 1959-07-24; 1959-08-05; 1959-08-07; 1959-08-27; 1959-09-12; 1959-09-17; 1959-09-22; 1959-10-13; 1959-10-28; 1959-11-03; 1959-11-19; 1959-12-01; 1959-12-17; 1960-01-14; 1960-02-09; 1960-02-29; 1960-03-11; 1960-04-01; 1960-04-13; 1960-08-18; 1960-10-04; 1960-11-30; 1961-06-28; 1961-11-15; 1962-01-15; 1962-05-02; 1962-05-10; 1962-10-31; 1963-09-18; 1964-03-24; 1964-07-22; 1964-10-27; 1996-03-13; 1996-02-25; 1996-04-04; 1990-09-19; 1995-09-30; 1991-07-23; 1996-09-01; 1992-02-19; 1965-04-26; 1991-06-18; 1996-08; 1988-07
- **confirmed date:** `1996-09-10` (via body, csv)
- **summary:** This report describes the Modeling of Unlikely Space-Booster Failures in Risk Calculations, documenting historical launch failure modes and recommending corrective actions to address them using novel…

### `dow-033-dow-uap-d49-launch-summary-vandenberg-afb-2000`
- **family:** `DOW-UAP-D49`
- **title:** DOW-UAP-D49, Launch Summary, Vandenberg AFB, 2000
- **csv:** `2/3/00` -> `2000-02-03`
- **title dates:** 2000
- **body dates (filtered):** 2000-02-03; 1958-12-16; 1992-06-01; 1992-07-01; 1961-04-01; 1971-04-01; 1963-07-01; 1997-08-04; 1994-03-13; 1967-07-01; 1965-08-16; 1997-09; 1964-07; 1983-03
- **confirmed date:** `2000-02-03` (via body, csv)
- **summary:** This report summarizes the historical record of launches occurring at Vandenberg Air Force Base between 1958 and 2000.

### `dow-035-dow-uap-d50-email-correspondence-indopacom-april-2025`
- **family:** `DOW-UAP-D50`
- **title:** DOW-UAP-D50, Email Correspondence, INDOPACOM, April 2025
- **csv:** `4/10/2025-4/11/2025` -> `2025-04-10`
- **title dates:** 2025-04
- **confirmed date:** `2025-04` (via csv, title)
- **summary:** This document is email correspondence describing the content of a mission report and requesting clarification on its content. All descriptive and estimative language contained in this report reflects…

### `dow-036-dow-uap-d51-email-correspondence-pacific-time-zone-march-202`
- **family:** `DOW-UAP-D51`
- **title:** DOW-UAP-D51, Email Correspondence, Pacific Time Zone, March 2023
- **csv:** `3/23/26` -> `2026-03-23`
- **title dates:** 2023-03
- **body dates (filtered):** 2023-03
- **confirmed date:** `2023-03` (via body, title)
- **note:** csv `2026-03-23` disagrees
- **summary:** This document is email correspondence describing the content of a mission report and requesting clarification on its content. All descriptive and estimative language contained in this report reflects…

### `dow-037-dow-uap-d52-email-correspondance-na-august-2024`
- **family:** `DOW-UAP-D52`
- **title:** DOW-UAP-D52, Email Correspondance, NA, August 2024
- **csv:** `10/31/24` -> `2024-10-31`
- **title dates:** 2024-08
- **confirmed date:** `2024` (via csv, title)
- **summary:** This document is email correspondence describing the content of a mission report and requesting clarification on its content. All descriptive and estimative language contained in this report reflects…

### `dow-039-dow-uap-d55-mission-report-syria-november-2016`
- **family:** `DOW-UAP-D55`
- **title:** DOW-UAP-D55, Mission Report, Syria, November 2016
- **csv:** `11/18/16` -> `2016-11-18`
- **title dates:** 2016-11
- **body dates (filtered):** 2026-03-27; 2016-11-18
- **confirmed date:** `2016-11-18` (via body, csv)
- **summary:** This document is a mission briefing summarizing an observation of Unidentified Anomalous Phenomena (UAP) by a U.S. military platform near Latakia, Syria. A U.S. military pilot flying a P-8A aircraft …

### `dow-040-dow-uap-d56-range-fouler-debrief-arabian-sea-august-2020`
- **family:** `DOW-UAP-D56`
- **title:** DOW-UAP-D56, Range Fouler Debrief, Arabian Sea, August 2020
- **csv:** `8/24/20` -> `2020-08-24`
- **title dates:** 2020-08
- **body dates (filtered):** 2020-08-24
- **confirmed date:** `2020-08-24` (via body, csv)
- **summary:** This document is a Range Fouler Debrief Form, a standardized reporting form the U.S. Navy uses to record the circumstances surrounding an unauthorized intrusion into controlled airspace during active…

### `dow-041-dow-uap-d57-range-fouler-reporting-form-gulf-of-aden-septemb`
- **family:** `DOW-UAP-D57`
- **title:** DOW-UAP-D57, Range Fouler Reporting Form, Gulf of Aden, September 2020
- **csv:** `9/4/20` -> `2020-09-04`
- **title dates:** 2020-09
- **body dates (filtered):** 2020-09-04; 2026-03-16
- **confirmed date:** `2020-09-04` (via body, csv)
- **summary:** This document is a Range Fouler Reporting Form, a standardized reporting form the U.S. Navy uses to record the circumstances surrounding an unauthorized intrusion into controlled airspace during acti…

### `dow-042-dow-uap-d58-range-fouler-debrief-na-october-2020`
- **family:** `DOW-UAP-D58`
- **title:** DOW-UAP-D58, Range Fouler Debrief, NA, October 2020
- **csv:** `10/27/20` -> `2020-10-27`
- **title dates:** 2020-10
- **body dates (filtered):** 2020-10-27; 2026-03-27
- **confirmed date:** `2020-10-27` (via body, csv)
- **summary:** This document is a Range Fouler Debrief, a standardized reporting form the U.S. Navy uses to record the circumstances surrounding an unauthorized intrusion into controlled airspace during active mili…

### `dow-044-dow-uap-d60-mission-report-persian-gulf-august-2020`
- **family:** `DOW-UAP-D60`
- **title:** DOW-UAP-D60, Mission Report, Persian Gulf, August 2020
- **csv:** `8/8/20` -> `2020-08-08`
- **title dates:** 2020-08
- **confirmed date:** `2020-08` (via csv, title)
- **summary:** This document is a Mission Report (MISREP), a standardized reporting form the U.S. Military uses to record the circumstances surrounding its operations. U.S. military services often use MISREPs to re…

### `dow-045-dow-uap-d61-mission-report-persian-gulf-august-2020`
- **family:** `DOW-UAP-D61`
- **title:** DOW-UAP-D61, Mission Report, Persian Gulf, August 2020
- **csv:** `8/27/20` -> `2020-08-27`
- **title dates:** 2020-08
- **body dates (filtered):** 2026-01-22
- **confirmed date:** `2020-08` (via csv, title)
- **summary:** This document is a Mission Report (MISREP), a standardized reporting form the U.S. Military uses to record the circumstances surrounding its operations. U.S. military services often use MISREPs to re…

### `dow-046-dow-uap-d62-mission-report-strait-of-hormuz-september-2020`
- **family:** `DOW-UAP-D62`
- **title:** DOW-UAP-D62, Mission Report, Strait of Hormuz, September 2020
- **csv:** `9/16/20` -> `2020-09-16`
- **title dates:** 2020-09
- **body dates (filtered):** 2026-01-22
- **confirmed date:** `2020-09` (via csv, title)
- **summary:** This document is a Mission Report (MISREP), a standardized reporting form the U.S. Military uses to record the circumstances surrounding its operations. U.S. military services often use MISREPs to re…

### `dow-047-dow-uap-d63-mission-report-strait-of-hormuz-october-2020`
- **family:** `DOW-UAP-D63`
- **title:** DOW-UAP-D63, Mission Report, Strait of Hormuz, October 2020
- **csv:** `10/1/20` -> `2020-10-01`
- **title dates:** 2020-10
- **confirmed date:** `2020-10` (via csv, title)
- **summary:** This document is a Mission Report (MISREP), a standardized reporting form the U.S. Military uses to record the circumstances surrounding its operations. U.S. military services often use MISREPs to re…

### `dow-048-dow-uap-d64-mission-report-iran-november-2020`
- **family:** `DOW-UAP-D64`
- **title:** DOW-UAP-D64, Mission Report, Iran, November 2020
- **csv:** `11/2/20` -> `2020-11-02`
- **title dates:** 2020-11
- **summary dates:** 2020-11-02
- **confirmed date:** `2020-11-02` (via csv, summary)
- **summary:** This document is a Mission Report (MISREP), a standardized reporting form the U.S. Military uses to record the circumstances surrounding its operations. U.S. military services often use MISREPs to re…

### `dow-049-dow-uap-d65-mission-report-persian-gulf-july-2020`
- **family:** `DOW-UAP-D65`
- **title:** DOW-UAP-D65, Mission Report, Persian Gulf, July 2020
- **csv:** `7/16/20` -> `2020-07-16`
- **title dates:** 2020-07
- **summary dates:** 2020-07-16
- **confirmed date:** `2020-07-16` (via csv, summary)
- **summary:** This document is a Mission Report (MISREP), a standardized reporting form the U.S. Military uses to record the circumstances surrounding its operations. U.S. military services often use MISREPs to re…

### `dow-051-dow-uap-d74-mission-report-syria-november-2023`
- **family:** `DOW-UAP-D74`
- **title:** DOW-UAP-D74, Mission Report, Syria, November 2023
- **csv:** `11/9/23` -> `2023-11-09`
- **title dates:** 2023-11
- **body dates (filtered):** 2025-06-02
- **confirmed date:** `2023-11` (via csv, title)
- **summary:** This document is a Mission Report (MISREP), a standardized reporting form the U.S. Military uses to record the circumstances surrounding its operations. U.S. military services often use MISREPs to re…

### `dow-052-dow-uap-d75-mission-report-gulf-of-aden-july-2024`
- **family:** `DOW-UAP-D75`
- **title:** DOW-UAP-D75, Mission Report, Gulf of Aden, July 2024
- **csv:** `7/14/24` -> `2024-07-14`
- **title dates:** 2024-07
- **summary dates:** 2024-07-14
- **body dates (filtered):** 2025-06-02
- **confirmed date:** `2024-07-14` (via csv, summary)
- **summary:** This document is a Mission Report (MISREP), a standardized reporting form the U.S. Military uses to record the circumstances surrounding its operations. U.S. military services often use MISREPs to re…

### `dow-054-dow-uap-pr19-unresolved-uap-report-middle-east-may-2022`
- **family:** `DOW-UAP-PR19`
- **title:** DOW-UAP-PR19, Unresolved UAP Report, Middle East, May 2022
- **csv:** `N/A` -> `-`
- **title dates:** 2022-05
- **body dates (filtered):** 2022-05
- **confirmed date:** `2022-05` (via body, title)
- **summary:** The United States Central Command submitted a report of an unidentified anomalous phenomenon to the All-domain Anomaly Resolution Office (AARO) consisting of five seconds of video footage from an inf…

### `dow-056-dow-uap-pr21-unresolved-uap-report-iraq-may-2022`
- **family:** `DOW-UAP-PR21`
- **title:** DOW-UAP-PR21, Unresolved UAP Report, Iraq, May 2022
- **csv:** `N/A` -> `-`
- **title dates:** 2022-05
- **body dates (filtered):** 2022-05
- **confirmed date:** `2022-05` (via body, title)
- **summary:** The United States Central Command submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of ten seconds of video footage from a…

### `dow-057-dow-uap-pr22-unresolved-uap-report-syria-july-2022`
- **family:** `DOW-UAP-PR22`
- **title:** DOW-UAP-PR22, Unresolved UAP Report, Syria, July 2022
- **csv:** `N/A` -> `-`
- **title dates:** 2022-07
- **body dates (filtered):** 2022-07
- **confirmed date:** `2022-07` (via body, title)
- **summary:** The United States Central Command submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of 14 seconds of video footage from an…

### `dow-058-dow-uap-pr23-unresolved-uap-report-iraq-december-2022`
- **family:** `DOW-UAP-PR23`
- **title:** DOW-UAP-PR23, Unresolved UAP Report, Iraq, December 2022
- **csv:** `N/A` -> `-`
- **title dates:** 2022-12
- **body dates (filtered):** 2022-12
- **confirmed date:** `2022-12` (via body, title)
- **summary:** The United States Central Command submitted a report of an unidentified anomalous phenomenon to the All-domain Anomaly Resolution Office (AARO) consisting of ten seconds of video footage from an infr…

### `dow-059-dow-uap-pr26-unresolved-uap-report-united-arab-emirates-octo`
- **family:** `DOW-UAP-PR26`
- **title:** DOW-UAP-PR26, Unresolved UAP Report, United Arab Emirates, October 2023
- **csv:** `N/A` -> `-`
- **title dates:** 2023-10
- **body dates (filtered):** 2023-10
- **confirmed date:** `2023-10` (via body, title)
- **summary:** The United States Central Command submitted a report of an unidentified anomalous phenomenon to the All-domain Anomaly Resolution Office (AARO) consisting of 43 seconds of video footage from an infra…

### `dow-060-dow-uap-pr27-unresolved-uap-report-united-arab-emirates-octo`
- **family:** `DOW-UAP-PR27`
- **title:** DOW-UAP-PR27, Unresolved UAP Report, United Arab Emirates, October 2023
- **csv:** `N/A` -> `-`
- **title dates:** 2023-10
- **body dates (filtered):** 2023-10
- **confirmed date:** `2023-10` (via body, title)
- **summary:** The United States Central Command submitted a report of an unidentified anomalous phenomenon to the All-domain Anomaly Resolution Office (AARO) consisting of four minutes and 57 seconds of video foot…

### `dow-061-dow-uap-pr28-unresolved-uap-report-greece-january-2024`
- **family:** `DOW-UAP-PR28`
- **title:** DOW-UAP-PR28, Unresolved UAP Report, Greece, January 2024
- **csv:** `N/A` -> `-`
- **title dates:** 2024-01
- **body dates (filtered):** 2024-01
- **confirmed date:** `2024-01` (via body, title)
- **summary:** The United States Central Command submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of one minute and five seconds of vide…

### `dow-062-dow-uap-pr29-unresolved-uap-report-united-arab-emirates-june`
- **family:** `DOW-UAP-PR29`
- **title:** DOW-UAP-PR29, Unresolved UAP Report, United Arab Emirates, June 2024
- **csv:** `N/A` -> `-`
- **title dates:** 2024-06
- **body dates (filtered):** 2024-06
- **confirmed date:** `2024-06` (via body, title)
- **summary:** The United States Northern Command submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of 21 seconds of video footage from a…

### `dow-063-dow-uap-pr31-unresolved-uap-report-syria-october-2024`
- **family:** `DOW-UAP-PR31`
- **title:** DOW-UAP-PR31, Unresolved UAP Report, Syria, October 2024
- **csv:** `N/A` -> `-`
- **title dates:** 2024-10
- **body dates (filtered):** 2024-10
- **confirmed date:** `2024-10` (via body, title)
- **summary:** The United States Central Command submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of five seconds of video footage from …

### `dow-064-dow-uap-pr32-unresolved-uap-report-syria-october-2024`
- **family:** `DOW-UAP-PR32`
- **title:** DOW-UAP-PR32, Unresolved UAP Report, Syria, October 2024
- **csv:** `N/A` -> `-`
- **title dates:** 2024-10
- **body dates (filtered):** 2024-10
- **confirmed date:** `2024-10` (via body, title)
- **summary:** The United States Central Command submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of six seconds of video footage from a…

### `dow-065-dow-uap-pr33-unresolved-uap-report-syria-october-2024`
- **family:** `DOW-UAP-PR33`
- **title:** DOW-UAP-PR33, Unresolved UAP Report, Syria, October 2024
- **csv:** `N/A` -> `-`
- **title dates:** 2024-10
- **body dates (filtered):** 2024-10
- **confirmed date:** `2024-10` (via body, title)
- **summary:** The United States Central Command submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of five seconds of video footage from …

### `dow-066-dow-uap-pr34-unresolved-uap-report-greece-october-2023`
- **family:** `DOW-UAP-PR34`
- **title:** DOW-UAP-PR34, Unresolved UAP Report, Greece, October 2023
- **csv:** `N/A` -> `-`
- **title dates:** 2023-10
- **body dates (filtered):** 2023-10
- **confirmed date:** `2023-10` (via body, title)
- **summary:** The United States Central Command submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of two minutes and 57 seconds of video…

### `dow-067-dow-uap-pr35-unresolved-uap-report-greece-october-2023`
- **family:** `DOW-UAP-PR35`
- **title:** DOW-UAP-PR35, Unresolved UAP Report, Greece, October 2023
- **csv:** `N/A` -> `-`
- **title dates:** 2023-10
- **body dates (filtered):** 2023-10
- **confirmed date:** `2023-10` (via body, title)
- **summary:** The United States Central Command submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of 24 seconds of video footage from an…

### `dow-068-dow-uap-pr36-unresolved-uap-report-middle-east-may-2020`
- **family:** `DOW-UAP-PR36`
- **title:** DOW-UAP-PR36, Unresolved UAP Report, Middle East, May 2020
- **csv:** `N/A` -> `-`
- **title dates:** 2020-05
- **body dates (filtered):** 2020-05
- **confirmed date:** `2020-05` (via body, title)
- **summary:** The United States Central Command submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of two minutes and 17 seconds of video…

### `dow-083-dow-uap-pr050-4-uap-formation-iran-26-aug-2022-over-water-ca`
- **family:** `DOW-UAP-PR50`
- **title:** DOW-UAP-PR050, "4 UAP Formation Iran 26 Aug 2022 over water [CALLSIGN]"
- **csv:** `2022` -> `2022`
- **title dates:** 2022-08-26
- **summary dates:** 2026-03-06; 2022-08-26; 2024-06
- **confirmed date:** `2022-08-26` (via summary, title)
- **note:** csv `2022` disagrees
- **summary:** On March 6, 2026, eight members of the U.S. House of Representatives requested access to 51 potentially UAP-related records allegedly held by the Department of War and the Intelligence Community. The…

### `dow-085-dow-uap-d017-uap-reported-at-sandia-base-1948-1950`
- **family:** `DOW-UAP-D17`
- **title:** DOW-UAP-D017, UAP Reported at Sandia Base, 1948-1950
- **csv:** `1948-1950` -> `1948`
- **title dates:** 1948; 1950
- **body dates (filtered):** 1949-04-07; 1949-08-10; 1949-11-29; 1950-05-25; 1949-02-17; 1949-10-14; 1950-02-25; 1949-05-18; 1949-04-09; 1948-12-31; 1949-02-16; 1949-04-27; 1948-12-05; 1949-02-18; 1949-03-16; 1949-03-07; 1948-03
- **confirmed date:** `1948` (via body, csv, title)
- **summary:** This file contains 116 pages of documentation from the Armed Forces Special Weapons Program (AFSWP) – the direct, post-World War II successor to the Manhattan Project – and from the U.S. Air Force – …

### `dow-086-dow-uap-d020-mission-report-iraq-2023`
- **family:** `DOW-UAP-D20`
- **title:** DOW-UAP-D020, Mission Report, Iraq, 2023
- **csv:** `3/31/23` -> `2023-03-31`
- **title dates:** 2023
- **body dates (filtered):** 2025-10-17; 2025-10-08
- **confirmed date:** `2023` (via csv, title)
- **summary:** This document is a Mission Report (MISREP), a standardized reporting form the U.S. Military uses to record the circumstances surrounding its operations. U.S. military services often use MISREPs to re…

### `dow-088-dow-uap-pr053-cigar-shaped-or-fast-sherical-uap-clip-15-oct`
- **family:** `DOW-UAP-PR53`
- **title:** DOW-UAP-PR053, "Cigar Shaped or Fast Sherical UAP clip 15 OCT 22"
- **csv:** `2022` -> `2022`
- **summary dates:** 2026-03-06; 2022-10; 2024-06
- **confirmed date:** `2022` (via csv, summary)
- **summary:** On March 6, 2026, eight members of the U.S. House of Representatives requested access to 51 potentially UAP-related records allegedly held by the Department of War and the Intelligence Community. The…

### `dow-089-dow-uap-pr054-spherical-uap-erratic-movement-callsign-missio`
- **family:** `DOW-UAP-PR54`
- **title:** DOW-UAP-PR054, "Spherical UAP Erratic movement [CALLSIGN] (Mission) 2022"
- **csv:** `2022` -> `2022`
- **title dates:** 2022
- **summary dates:** 2026-03-06; 2022-08; 2024-06
- **confirmed date:** `2022` (via csv, summary, title)
- **summary:** On March 6, 2026, eight members of the U.S. House of Representatives requested access to 51 potentially UAP-related records allegedly held by the Department of War and the Intelligence Community. The…

### `dow-090-dow-uap-pr055-spherical-uap-over-afg-in-and-out-of-clouds-23`
- **family:** `DOW-UAP-PR55`
- **title:** DOW-UAP-PR055, "Spherical UAP over AFG in and out of clouds 23 Nov 2020"
- **csv:** `2020` -> `2020`
- **title dates:** 2020-11-23
- **summary dates:** 2026-03-06; 2020-11-23; 2024-06
- **confirmed date:** `2020-11-23` (via summary, title)
- **note:** csv `2020` disagrees
- **summary:** On March 6, 2026, eight members of the U.S. House of Representatives requested access to 51 potentially UAP-related records allegedly held by the Department of War and the Intelligence Community. The…

### `dow-092-dow-uap-pr057a-spherical-uap-in-clouds`
- **family:** `DOW-UAP-PR57`
- **title:** DOW-UAP-PR057a, "Spherical UAP in clouds"
- **csv:** `2023` -> `2023`
- **summary dates:** 2026-03-06; 2023-01-05; 2024-06
- **confirmed date:** `2023` (via csv, summary)
- **summary:** On March 6, 2026, eight members of the U.S. House of Representatives requested access to 51 potentially UAP-related records allegedly held by the Department of War and the Intelligence Community. The…

### `dow-093-dow-uap-pr057b-platform-observes-uap-in-east-china-sea-05-ja`
- **family:** `DOW-UAP-PR57`
- **title:** DOW-UAP-PR057b, "[Platform] Observes UAP in East China Sea 05 JAN 2023 INDOPACOM"
- **csv:** `2023` -> `2023`
- **title dates:** 2023-01-05
- **summary dates:** 2026-03-06; 2023-01; 2024-06
- **confirmed date:** `2023-01` (via summary, title)
- **note:** csv `2023` disagrees
- **summary:** On March 6, 2026, eight members of the U.S. House of Representatives requested access to 51 potentially UAP-related records allegedly held by the Department of War and the Intelligence Community. The…

### `dow-096-dow-uap-pr060-spherical-uap-callsign-2021-04-12-obj-2`
- **family:** `DOW-UAP-PR60`
- **title:** DOW-UAP-PR060, "Spherical UAP [CALLSIGN] 2021/04/12 obj 2"
- **csv:** `2021` -> `2021`
- **title dates:** 2021
- **summary dates:** 2026-03-06; 2024-06
- **confirmed date:** `2021` (via csv, title)
- **summary:** On March 6, 2026, eight members of the U.S. House of Representatives requested access to 51 potentially UAP-related records allegedly held by the Department of War and the Intelligence Community. The…

### `dow-097-dow-uap-pr061-spherical-uap-callsign-2021-04-12-vid-0`
- **family:** `DOW-UAP-PR61`
- **title:** DOW-UAP-PR061, "Spherical UAP [CALLSIGN] 2021/04/12 vid 0"
- **csv:** `2021` -> `2021`
- **title dates:** 2021
- **summary dates:** 2026-03-06; 2024-06
- **confirmed date:** `2021` (via csv, title)
- **summary:** On March 6, 2026, eight members of the U.S. House of Representatives requested access to 51 potentially UAP-related records allegedly held by the Department of War and the Intelligence Community. The…

### `dow-098-dow-uap-pr062-spherical-uap-callsign-2021-04-12-vid-1`
- **family:** `DOW-UAP-PR62`
- **title:** DOW-UAP-PR062, "Spherical UAP [CALLSIGN] 2021/04/12 vid 1"
- **csv:** `2021` -> `2021`
- **title dates:** 2021
- **summary dates:** 2026-03-06; 2024-05
- **confirmed date:** `2021` (via csv, title)
- **summary:** On March 6, 2026, eight members of the U.S. House of Representatives requested access to 51 potentially UAP-related records allegedly held by the Department of War and the Intelligence Community. The…

### `dow-099-dow-uap-pr063-spherical-uap-callsign-2021-04-12-vid-2`
- **family:** `DOW-UAP-PR63`
- **title:** DOW-UAP-PR063, "Spherical UAP [CALLSIGN] 2021/04/12 vid 2"
- **csv:** `2021` -> `2021`
- **title dates:** 2021
- **summary dates:** 2026-03-06; 2024-05
- **confirmed date:** `2021` (via csv, title)
- **summary:** On March 6, 2026, eight members of the U.S. House of Representatives requested access to 51 potentially UAP-related records allegedly held by the Department of War and the Intelligence Community. The…

### `dow-100-dow-uap-pr064-afsoc-kabul-uap-jul-2017`
- **family:** `DOW-UAP-PR64`
- **title:** DOW-UAP-PR064, "AFSOC Kabul UAP Jul 2017"
- **csv:** `` -> `-`
- **title dates:** 2017-07
- **summary dates:** 2026-03-06; 2017-07; 2024-06
- **confirmed date:** `2017-07` (via summary, title)
- **summary:** On March 6, 2026, eight members of the U.S. House of Representatives requested access to 51 potentially UAP-related records allegedly held by the Department of War and the Intelligence Community. The…

### `dow-101-dow-uap-pr065-uscg-c-144-tyndall-uap-2-tic-tac-ir-hot-24-apr`
- **family:** `DOW-UAP-PR65`
- **title:** DOW-UAP-PR065, "USCG C-144 Tyndall UAP 2 TIC TAC IR hot 24 April 2024"
- **csv:** `2024` -> `2024`
- **title dates:** 2024-04-24
- **summary dates:** 2026-03-06; 2024-04-24; 2024-06
- **confirmed date:** `2024-04-24` (via summary, title)
- **note:** csv `2024` disagrees
- **summary:** On March 6, 2026, eight members of the U.S. House of Representatives requested access to 51 potentially UAP-related records allegedly held by the Department of War and the Intelligence Community. The…

### `dow-102-dow-uap-pr066-uscg-c-144-tyndall-uap-1-tic-tac-ir-hot-24-apr`
- **family:** `DOW-UAP-PR66`
- **title:** DOW-UAP-PR066, "USCG C-144 Tyndall UAP 1 TIC TAC IR hot 24 April 2024"
- **csv:** `2024` -> `2024`
- **title dates:** 2024-04-24
- **summary dates:** 2026-03-06; 2024-04-24; 2024-06
- **confirmed date:** `2024-04-24` (via summary, title)
- **note:** csv `2024` disagrees
- **summary:** On March 6, 2026, eight members of the U.S. House of Representatives requested access to 51 potentially UAP-related records allegedly held by the Department of War and the Intelligence Community. The…

### `dow-104-dow-uap-pr068-iir-1-666-s0151-23-video-footage-of-unidentifi`
- **family:** `DOW-UAP-PR68`
- **title:** DOW-UAP-PR068, "IIR 1 666 S0151 23/Video Footage of Unidentified Aerial Phenomenon (UAP) captured by fifth generation aircraft on 20 Jan 23"
- **csv:** `2023` -> `2023`
- **summary dates:** 2026-03-06; 2023-07
- **confirmed date:** `2023` (via csv, summary)
- **summary:** On March 6, 2026, eight members of the U.S. House of Representatives requested access to 51 potentially UAP-related records allegedly held by the Department of War and the Intelligence Community. The…

### `dow-106-dow-uap-pr070-iir-1-655-s0301-23-eglin-afb-aircrew-observed`
- **family:** `DOW-UAP-PR70`
- **title:** DOW-UAP-PR070, "IIR 1 655 S0301 23/Eglin AFB Aircrew Observed Unidentified Aerial Phenomena (UAP) on 13 Feb 23"
- **csv:** `2023` -> `2023`
- **summary dates:** 2026-03-06; 2023-03
- **confirmed date:** `2023` (via csv, summary)
- **summary:** On March 6, 2026, eight members of the U.S. House of Representatives requested access to 51 potentially UAP-related records allegedly held by the Department of War and the Intelligence Community. The…

### `dow-107-dow-uap-pr071-usaf-ang-f-16c-callsign-callsign-shoots-down-u`
- **family:** `DOW-UAP-PR71`
- **title:** DOW-UAP-PR071, "USAF ANG F-16C (callsign [CALLSIGN]) Shoots Down UAP over Lake Huron with [Weapon System], 12 Feb 2023"
- **csv:** `2023` -> `2023`
- **title dates:** 2023-02-12
- **summary dates:** 2026-03-06; 2023-02-12
- **confirmed date:** `2023-02-12` (via summary, title)
- **note:** csv `2023` disagrees
- **summary:** On March 6, 2026, eight members of the U.S. House of Representatives requested access to 51 potentially UAP-related records allegedly held by the Department of War and the Intelligence Community. The…

### `dow-108-dow-uap-pr072-administrative-revision-iir-1777-j0032-22-kaza`
- **family:** `DOW-UAP-PR72`
- **title:** DOW-UAP-PR072, "ADMINISTRATIVE REVISION: IIR 1777 J0032 22 Kazakhstan - UAP in the vicinity of Karaganda International Airport"
- **csv:** `2022` -> `2022`
- **summary dates:** 2026-03-06; 2022-03; 2023-04
- **confirmed date:** `2022` (via csv, summary)
- **summary:** On March 6, 2026, eight members of the U.S. House of Representatives requested access to 51 potentially UAP-related records allegedly held by the Department of War and the Intelligence Community. The…

### `dow-109-dow-uap-pr073-iir-1-655-s0053-23-several-unidentified-aerial`
- **family:** `DOW-UAP-PR73`
- **title:** DOW-UAP-PR073, IIR 1 655 S0053 23/Several Unidentified Aerial Phenomenon Encountered In The Vicinity of Columbus OH"
- **csv:** `2022` -> `2022`
- **summary dates:** 2026-03-06; 2022-11; 2023-03
- **confirmed date:** `2022` (via csv, summary)
- **summary:** On March 6, 2026, eight members of the U.S. House of Representatives requested access to 51 potentially UAP-related records allegedly held by the Department of War and the Intelligence Community. The…

### `dow-110-dow-uap-pr074-callsign-mission-hd-20220613`
- **family:** `DOW-UAP-PR74`
- **title:** DOW-UAP-PR074, "[CALLSIGN] (Mission)HD_20220613"
- **csv:** `2022` -> `2022`
- **summary dates:** 2026-03-06; 2022-06
- **confirmed date:** `2022` (via csv, summary)
- **summary:** On March 6, 2026, eight members of the U.S. House of Representatives requested access to 51 potentially UAP-related records allegedly held by the Department of War and the Intelligence Community. The…

### `dow-111-dow-uap-pr075-09jun2021-platform-observed-uap-in-the-ecs`
- **family:** `DOW-UAP-PR75`
- **title:** DOW-UAP-PR075, "09JUN2021 [Platform] observed UAP in the ECS"
- **csv:** `2021` -> `2021`
- **title dates:** 2021
- **summary dates:** 2026-03-06; 2021-06
- **confirmed date:** `2021` (via csv, summary, title)
- **summary:** On March 6, 2026, eight members of the U.S. House of Representatives requested access to 51 potentially UAP-related records allegedly held by the Department of War and the Intelligence Community. The…

### `dow-112-dow-uap-pr076-03-january-2021-callsign-mission-observes-uap`
- **family:** `DOW-UAP-PR76`
- **title:** DOW-UAP-PR076, "03 January 2021 [CALLSIGN] (Mission) observes UAP"
- **csv:** `2021` -> `2021`
- **title dates:** 2021-01-03
- **summary dates:** 2026-03-06; 2021-01-03
- **confirmed date:** `2021-01-03` (via summary, title)
- **note:** csv `2021` disagrees
- **summary:** On March 6, 2026, eight members of the U.S. House of Representatives requested access to 51 potentially UAP-related records allegedly held by the Department of War and the Intelligence Community. The…

### `dow-113-dow-uap-pr077-2-november-2020-callsign-callsign-observes-and`
- **family:** `DOW-UAP-PR77`
- **title:** DOW-UAP-PR077, "2 November 2020 [CALLSIGN] [CALLSIGN] Observes and tracks UAP 1 of 2"
- **csv:** `2020` -> `2020`
- **title dates:** 2020-11-02
- **summary dates:** 2026-03-06; 2020-11-02
- **confirmed date:** `2020-11-02` (via summary, title)
- **note:** csv `2020` disagrees
- **summary:** On March 6, 2026, eight members of the U.S. House of Representatives requested access to 51 potentially UAP-related records allegedly held by the Department of War and the Intelligence Community. The…

### `dow-114-dow-uap-pr078-2-november-2020-callsign-callsign-observes-and`
- **family:** `DOW-UAP-PR78`
- **title:** DOW-UAP-PR078, "2 November 2020 [CALLSIGN] [CALLSIGN] Observes and tracks UAP 2 of 2"
- **csv:** `2020` -> `2020`
- **title dates:** 2020-11-02
- **summary dates:** 2026-03-06; 2020-11-02
- **confirmed date:** `2020-11-02` (via summary, title)
- **note:** csv `2020` disagrees
- **summary:** On March 6, 2026, eight members of the U.S. House of Representatives requested access to 51 potentially UAP-related records allegedly held by the Department of War and the Intelligence Community. The…

### `dow-115-dow-uap-pr079-29-october-2020-callsign-mission-observes-3-fa`
- **family:** `DOW-UAP-PR79`
- **title:** DOW-UAP-PR079, "29 October 2020 [CALLSIGN] (Mission) observes 3 fast moving UAP's"
- **csv:** `2020` -> `2020`
- **title dates:** 2020-10-29
- **summary dates:** 2026-03-06; 2020-10-29
- **confirmed date:** `2020-10-29` (via summary, title)
- **note:** csv `2020` disagrees
- **summary:** On March 6, 2026, eight members of the U.S. House of Representatives requested access to 51 potentially UAP-related records allegedly held by the Department of War and the Intelligence Community. The…

### `dow-116-dow-uap-pr080-20-october-2020-callsign-callsign-observes-uap`
- **family:** `DOW-UAP-PR80`
- **title:** DOW-UAP-PR080, "20 October 2020 [CALLSIGN] [CALLSIGN] Observes UAP"
- **csv:** `2020` -> `2020`
- **title dates:** 2020-10-20
- **summary dates:** 2026-03-06; 2020-10-20
- **confirmed date:** `2020-10-20` (via summary, title)
- **note:** csv `2020` disagrees
- **summary:** On March 6, 2026, eight members of the U.S. House of Representatives requested access to 51 potentially UAP-related records allegedly held by the Department of War and the Intelligence Community. The…

### `dow-117-dow-uap-pr081-18-oct-2020-callsign-observes-uap`
- **family:** `DOW-UAP-PR81`
- **title:** DOW-UAP-PR081, "18 Oct 2020 [CALLSIGN] observes UAP"
- **csv:** `2020` -> `2020`
- **title dates:** 2020-10-18
- **summary dates:** 2026-03-06; 2020-10-18
- **confirmed date:** `2020-10-18` (via summary, title)
- **note:** csv `2020` disagrees
- **summary:** On March 6, 2026, eight members of the U.S. House of Representatives requested access to 51 potentially UAP-related records allegedly held by the Department of War and the Intelligence Community. The…

### `dow-118-dow-uap-pr082-16-oct-2020-callsign-views-uap`
- **family:** `DOW-UAP-PR82`
- **title:** DOW-UAP-PR082, "16 OCT 2020 [CALLSIGN] views UAP"
- **csv:** `2020` -> `2020`
- **title dates:** 2020-10-16
- **summary dates:** 2026-03-06; 2020-10-16
- **confirmed date:** `2020-10-16` (via summary, title)
- **note:** csv `2020` disagrees
- **summary:** On March 6, 2026, eight members of the U.S. House of Representatives requested access to 51 potentially UAP-related records allegedly held by the Department of War and the Intelligence Community. The…

### `dow-119-dow-uap-pr083-7-october-2020-callsign-observes-uap`
- **family:** `DOW-UAP-PR83`
- **title:** DOW-UAP-PR083, "7 October 2020 [CALLSIGN] observes UAP"
- **csv:** `2020` -> `2020`
- **title dates:** 2020-10-07
- **summary dates:** 2026-03-06; 2020-10-07
- **confirmed date:** `2020-10-07` (via summary, title)
- **note:** csv `2020` disagrees
- **summary:** On March 6, 2026, eight members of the U.S. House of Representatives requested access to 51 potentially UAP-related records allegedly held by the Department of War and the Intelligence Community. The…

### `dow-120-dow-uap-pr084-17-sept-2020-callsign-observes-uap`
- **family:** `DOW-UAP-PR84`
- **title:** DOW-UAP-PR084, "17 Sept 2020 [CALLSIGN] observes UAP"
- **csv:** `2020` -> `2020`
- **title dates:** 2020-09-17
- **summary dates:** 2026-03-06; 2020-09-17
- **confirmed date:** `2020-09-17` (via summary, title)
- **note:** csv `2020` disagrees
- **summary:** On March 6, 2026, eight members of the U.S. House of Representatives requested access to 51 potentially UAP-related records allegedly held by the Department of War and the Intelligence Community. The…

### `dow-121-dow-uap-pr085-16-sept-2020-callsign-callsign-observes-uap`
- **family:** `DOW-UAP-PR85`
- **title:** DOW-UAP-PR085, "16 Sept 2020 [CALLSIGN] [CALLSIGN] observes UAP"
- **csv:** `2020` -> `2020`
- **title dates:** 2020-09-16
- **summary dates:** 2026-03-06; 2020-09-16
- **confirmed date:** `2020-09-16` (via summary, title)
- **note:** csv `2020` disagrees
- **summary:** On March 6, 2026, eight members of the U.S. House of Representatives requested access to 51 potentially UAP-related records allegedly held by the Department of War and the Intelligence Community. The…

### `dow-122-dow-uap-pr086-uap-from-dec-2019-east-coast`
- **family:** `DOW-UAP-PR86`
- **title:** DOW-UAP-PR086, "UAP from Dec 2019 (East Coast)"
- **csv:** `2019` -> `2019`
- **title dates:** 2019-12
- **summary dates:** 2026-03-06; 2019-12; 2020-09
- **confirmed date:** `2019-12` (via summary, title)
- **note:** csv `2019` disagrees
- **summary:** On March 6, 2026, eight members of the U.S. House of Representatives requested access to 51 potentially UAP-related records allegedly held by the Department of War and the Intelligence Community. The…

### `dow-123-dow-uap-pr087-05-september-2020-callsign-uap`
- **family:** `DOW-UAP-PR87`
- **title:** DOW-UAP-PR087, "05 September 2020 [CALLSIGN] UAP"
- **csv:** `2020` -> `2020`
- **title dates:** 2020-09-05
- **summary dates:** 2026-03-06; 2020-09-05
- **confirmed date:** `2020-09-05` (via summary, title)
- **note:** csv `2020` disagrees
- **summary:** On March 6, 2026, eight members of the U.S. House of Representatives requested access to 51 potentially UAP-related records allegedly held by the Department of War and the Intelligence Community. The…

### `dow-124-dow-uap-pr088-31-aug-callsign-callsign-observes-uap`
- **family:** `DOW-UAP-PR88`
- **title:** DOW-UAP-PR088, "31 AUG [CALLSIGN] [CALLSIGN] Observes UAP"
- **csv:** `2020` -> `2020`
- **summary dates:** 2026-03-06; 2020-08-31
- **confirmed date:** `2020` (via csv, summary)
- **summary:** On March 6, 2026, eight members of the U.S. House of Representatives requested access to 51 potentially UAP-related records allegedly held by the Department of War and the Intelligence Community. The…

### `dow-125-dow-uap-pr089-31-aug-callsign-callsign-observes-uap-part2`
- **family:** `DOW-UAP-PR89`
- **title:** DOW-UAP-PR089, "31 AUG [CALLSIGN] [CALLSIGN] Observes UAP part2"
- **csv:** `2020` -> `2020`
- **summary dates:** 2026-03-06; 2020-08-31
- **confirmed date:** `2020` (via csv, summary)
- **summary:** On March 6, 2026, eight members of the U.S. House of Representatives requested access to 51 potentially UAP-related records allegedly held by the Department of War and the Intelligence Community. The…

### `dow-126-dow-uap-pr090-24-aug-2020-callsign-mission-observes-uap`
- **family:** `DOW-UAP-PR90`
- **title:** DOW-UAP-PR090, "24 AUG 2020 [CALLSIGN] (Mission) Observes UAP"
- **csv:** `2020` -> `2020`
- **title dates:** 2020-08-24
- **summary dates:** 2026-03-06; 2020-08-24
- **confirmed date:** `2020-08-24` (via summary, title)
- **note:** csv `2020` disagrees
- **summary:** On March 6, 2026, eight members of the U.S. House of Representatives requested access to 51 potentially UAP-related records allegedly held by the Department of War and the Intelligence Community. The…

### `dow-127-dow-uap-pr091-21-aug-callsign-observes-uap-in-persian-gulf`
- **family:** `DOW-UAP-PR91`
- **title:** DOW-UAP-PR091, "21 AUG [CALLSIGN] Observes UAP in Persian Gulf"
- **csv:** `2020` -> `2020`
- **summary dates:** 2026-03-06; 2020-08-21
- **confirmed date:** `2020` (via csv, summary)
- **summary:** On March 6, 2026, eight members of the U.S. House of Representatives requested access to 51 potentially UAP-related records allegedly held by the Department of War and the Intelligence Community. The…

### `dow-128-dow-uap-pr092-08-aug-2020-callsign-callsign-uap-observation`
- **family:** `DOW-UAP-PR92`
- **title:** DOW-UAP-PR092, "08 AUG 2020 [CALLSIGN] [CALLSIGN] UAP observation"
- **csv:** `2020` -> `2020`
- **title dates:** 2020-08-08
- **summary dates:** 2026-03-06; 2020-08-08
- **confirmed date:** `2020-08-08` (via summary, title)
- **note:** csv `2020` disagrees
- **summary:** On March 6, 2026, eight members of the U.S. House of Representatives requested access to 51 potentially UAP-related records allegedly held by the Department of War and the Intelligence Community. The…

### `dow-129-dow-uap-pr093-may-05-2020-gulf-of-arabia-callsign-platform-d`
- **family:** `DOW-UAP-PR93`
- **title:** DOW-UAP-PR093, "May 05 2020 Gulf of Arabia [CALLSIGN] (Platform) Dual UAP"
- **csv:** `2020` -> `2020`
- **title dates:** 2020-05-05
- **summary dates:** 2026-03-06; 2020-05-05; 2020-07
- **confirmed date:** `2020-05-05` (via summary, title)
- **note:** csv `2020` disagrees
- **summary:** On March 6, 2026, eight members of the U.S. House of Representatives requested access to 51 potentially UAP-related records allegedly held by the Department of War and the Intelligence Community. The…

### `dow-130-dow-uap-pr094-callsign-mission-hd-2020-02-13`
- **family:** `DOW-UAP-PR94`
- **title:** DOW-UAP-PR094, "[CALLSIGN] (Mission) - HD 2020-02-13"
- **csv:** `2020` -> `2020`
- **title dates:** 2020
- **summary dates:** 2020-02-13; 2026-03-06
- **confirmed date:** `2020` (via csv, summary, title)
- **summary:** 46. DOW-UAP-PR094, “[CALLSIGN] (Mission) - HD 2020-02-13” On March 6, 2026, eight members of the U.S. House of Representatives requested access to 51 potentially UAP-related records allegedly held by…

### `dow-131-dow-uap-pr095-may-05-2020-gulf-of-arabia-callsign-platform-d`
- **family:** `DOW-UAP-PR95`
- **title:** DOW-UAP-PR095, "May 05 2020 Gulf of Arabia [CALLSIGN] (Platform) Dual UAP"
- **csv:** `2020` -> `2020`
- **title dates:** 2020-05-05
- **summary dates:** 2026-03-06; 2020-05-05
- **confirmed date:** `2020-05-05` (via summary, title)
- **note:** csv `2020` disagrees
- **summary:** On March 6, 2026, eight members of the U.S. House of Representatives requested access to 51 potentially UAP-related records allegedly held by the Department of War and the Intelligence Community. The…

### `dow-132-dow-uap-pr096-hh11-03-july-2018-uaps`
- **family:** `DOW-UAP-PR96`
- **title:** DOW-UAP-PR096, "HH11 03 July 2018 UAPs"
- **csv:** `2018` -> `2018`
- **title dates:** 2018-07-03
- **summary dates:** 2026-03-06; 2018-07-03; 2020-07
- **confirmed date:** `2018-07-03` (via summary, title)
- **note:** csv `2018` disagrees
- **summary:** On March 6, 2026, eight members of the U.S. House of Representatives requested access to 51 potentially UAP-related records allegedly held by the Department of War and the Intelligence Community. The…

### `dow-133-dow-uap-pr097-hi-res-callsign-observes-uap-on-25sep19-at-213`
- **family:** `DOW-UAP-PR97`
- **title:** DOW-UAP-PR097, "Hi-Res: [CALLSIGN] Observes UAP on 25SEP19 at 2135Z"
- **csv:** `2019` -> `2019`
- **summary dates:** 2026-03-06; 2019-10
- **confirmed date:** `2019` (via csv, summary)
- **summary:** On March 6, 2026, eight members of the U.S. House of Representatives requested access to 51 potentially UAP-related records allegedly held by the Department of War and the Intelligence Community. The…

### `dow-136-dow-uap-d084-us-army-flying-saucer-study-1949`
- **family:** `DOW-UAP-D84`
- **title:** DOW-UAP-D084, US Army-Flying-Saucer-Study_1949
- **csv:** `` -> `-`
- **title dates:** 1949
- **body dates (filtered):** 1949-04-05; 1949-01
- **confirmed date:** `1949` (via body, title)
- **summary:** This file contains an Evaluation Study of the Phenomenon (Flying Saucers) prepared at the request of the Plans & Operations Divisions of the General Staff, U.S. Army (P&O, GSUSA) to determine if the …

### `dow-137-dow-uap-d077-aaro-unresolved-case-analysis-update-western-un`
- **family:** `DOW-UAP-D77`
- **title:** DOW-UAP-D077, AARO Unresolved Case Analysis Update: Western United States Event
- **csv:** `2023` -> `2023`
- **summary dates:** 2026-06
- **body dates (filtered):** 2026-06-05; 2026-05; 2023-10
- **confirmed date:** `2026-06` (via body, summary)
- **note:** csv `2023` disagrees
- **summary:** This memorandum summarizes the All-domain Anomaly Resolution Office’s (AARO) ongoing analysis of a reported incident near a sensitive national security site in the western United States involving uni…

### `dow-138-dow-uap-d078-notional-map-western-united-states-event`
- **family:** `DOW-UAP-D78`
- **title:** DOW-UAP-D078, Notional Map: Western United States Event
- **csv:** `October, 2023` -> `2023`
- **summary dates:** 2023-10
- **body dates (filtered):** 2023-10
- **confirmed date:** `2023-10` (via body, summary)
- **note:** csv `2023` disagrees
- **summary:** This image is a notional representation of four incidents reportedly involving unidentified anomalous phenomena in the western United States, as seen from above. This illustration depicts multiple in…

### `dow-139-dow-uap-d079-narrative-statement-1-western-united-states-eve`
- **family:** `DOW-UAP-D79`
- **title:** DOW-UAP-D079, Narrative Statement 1, Western United States Event, 2023
- **csv:** `October, 2023` -> `2023`
- **title dates:** 2023
- **summary dates:** 2023-10
- **body dates (filtered):** 2026-06-02; 2026-05; 2023-10
- **confirmed date:** `2023-10` (via body, summary)
- **note:** csv `2023` disagrees
- **summary:** This memorandum presents the first-hand narrative from Witness 1 provided to the All-domain Anomaly Resolution Office (AARO). Witness 1 was one of several United States (U.S.) federal law enforcement…

### `dow-140-dow-uap-d080-narrative-statement-2-western-united-states-eve`
- **family:** `DOW-UAP-D80`
- **title:** DOW-UAP-D080, Narrative Statement 2, Western United States Event, 2023
- **csv:** `October, 2023` -> `2023`
- **title dates:** 2023
- **summary dates:** 2023-10
- **body dates (filtered):** 2026-06-02; 2026-05; 2023-10
- **confirmed date:** `2023-10` (via body, summary)
- **note:** csv `2023` disagrees
- **summary:** This memorandum presents the first-hand narrative from Witness 2 provided to the All-domain Anomaly Resolution Office (AARO). Witness 2 was one of several United States (U.S.) federal law enforcement…

### `dow-141-dow-uap-d081-narrative-statement-3-western-united-states-eve`
- **family:** `DOW-UAP-D81`
- **title:** DOW-UAP-D081, Narrative Statement 3, Western United States Event, 2023
- **csv:** `October, 2023` -> `2023`
- **title dates:** 2023
- **summary dates:** 2023-10
- **body dates (filtered):** 2026-06-02; 2026-05; 2023-10
- **confirmed date:** `2023-10` (via body, summary)
- **note:** csv `2023` disagrees
- **summary:** This memorandum presents the first-hand narrative from Witness 3 provided to the All-domain Anomaly Resolution Office (AARO). Witness 3 was one of several United States (U.S.) federal law enforcement…

### `dow-142-dow-uap-d082-narrative-statement-4-western-united-states-eve`
- **family:** `DOW-UAP-D82`
- **title:** DOW-UAP-D082, Narrative Statement 4, Western United States Event, 2023
- **csv:** `October, 2023` -> `2023`
- **title dates:** 2023
- **summary dates:** 2023-10
- **body dates (filtered):** 2026-06-02; 2026-05; 2023-10
- **confirmed date:** `2023-10` (via body, summary)
- **note:** csv `2023` disagrees
- **summary:** This memorandum presents the first-hand narrative from Witness 4 provided to the All-domain Anomaly Resolution Office (AARO). Witness 4 was one of several United States (U.S.) federal law enforcement…

### `dow-143-dow-uap-d083-narrative-statement-5-western-united-states-eve`
- **family:** `DOW-UAP-D83`
- **title:** DOW-UAP-D083, Narrative Statement 5, Western United States Event, 2023
- **csv:** `October, 2023` -> `2023`
- **title dates:** 2023
- **summary dates:** 2023-10
- **body dates (filtered):** 2026-05; 2023-10
- **confirmed date:** `2023-10` (via body, summary)
- **note:** csv `2023` disagrees
- **summary:** This memorandum presents the first-hand narrative from Witness 5 provided to the All-domain Anomaly Resolution Office (AARO). Witness 5 was one of several United States (U.S.) federal law enforcement…

### `dow-144-dow-uap-d085-transmission-of-cia-scientific-advisory-panel-r`
- **family:** `DOW-UAP-D85`
- **title:** DOW-UAP-D085_Transmission-of-CIA-Scientific-Advisory-Panel-Rept_1953
- **csv:** `1953` -> `1953`
- **title dates:** 1953
- **confirmed date:** `1953` (via csv, title)
- **summary:** This file contains a copy of the CIA's 1953 "Report of the Scientific Panel on Unidentified Flying Objects" that was sent to the Secretary of Defense.

### `dow-148-dow-uap-d094-analysis-of-flying-object-incidents-in-the-unit`
- **family:** `DOW-UAP-D94`
- **title:** DOW-UAP-D094, Analysis of Flying Object Incidents in the United States, 1949
- **csv:** `4/28/49` -> `1949-04-28`
- **title dates:** 1949
- **summary dates:** 1949-04-28
- **confirmed date:** `1949-04-28` (via csv, summary)
- **summary:** This file contains a U.S. Air Force (USAF) Air Intelligence Division study, “Analysis of Flying Object Incidents in the United States,” Study No. 203, dated 04/28/1949. The analysis includes an asses…

### `dow-149-dow-uap-d097-project-sign-progress-report-1948`
- **family:** `DOW-UAP-D97`
- **title:** DOW-UAP-D097, Project Sign Progress Report, 1948
- **csv:** `1948` -> `1948`
- **title dates:** 1948
- **confirmed date:** `1948` (via csv, title)
- **summary:** This file contains an initial report from the Air Materiel Command regarding Project Sign. Project Sign was a 1948-1949 U.S. Air Force program to investigate the nature and origin of unidentified fly…

### `dow-150-dow-uap-pr104-unresolved-uap-report-yellow-sea-2025`
- **family:** `DOW-UAP-PR104`
- **title:** DOW-UAP-PR104, Unresolved UAP Report, Yellow Sea, 2025
- **csv:** `2025` -> `2025`
- **title dates:** 2025
- **confirmed date:** `2025` (via csv, title)
- **summary:** The United States Indo-Pacific Command submitted a report of an unidentified anomalous phenomenon to the All-domain Anomaly Resolution Office (AARO) consisting of 18 seconds of video footage from an …

### `dow-151-dow-uap-pr105-unresolved-uap-report-east-china-sea-2025`
- **family:** `DOW-UAP-PR105`
- **title:** DOW-UAP-PR105, Unresolved UAP Report, East China Sea, 2025
- **csv:** `2025` -> `2025`
- **title dates:** 2025
- **confirmed date:** `2025` (via csv, title)
- **summary:** The United States Indo-Pacific Command submitted a report of an unidentified anomalous phenomenon to the All-domain Anomaly Resolution Office (AARO) consisting of 5 minutes of video footage from an i…

### `dow-152-dow-uap-pr113-unresolved-uap-report-western-united-states-19`
- **family:** `DOW-UAP-PR113`
- **title:** DOW-UAP-PR113, Unresolved UAP Report, Western United States, 1996
- **csv:** `1996` -> `1996`
- **title dates:** 1996
- **confirmed date:** `1996` (via csv, title)
- **summary:** The United States Navy Unidentified Anomalous Phenomena Task Force (UAPTF) transferred this media to the All-domain Anomaly Resolution Office (AARO) in 2022. The video contains 2 minutes and 57 secon…

### `dow-153-dow-uap-pr115-unresolved-uap-report-gulf-of-america-2019`
- **family:** `DOW-UAP-PR115`
- **title:** DOW-UAP-PR115, Unresolved UAP Report, Gulf of America, 2019
- **csv:** `2019` -> `2019`
- **title dates:** 2019
- **confirmed date:** `2019` (via csv, title)
- **summary:** The United States Air Force submitted a report of an unidentified anomalous phenomenon to the All-domain Anomaly Resolution Office (AARO) consisting of 8 seconds of video footage from an infrared sen…

### `dow-154-dow-uap-d089-range-fouler-debrief-eastern-united-states-2020`
- **family:** `DOW-UAP-D89`
- **title:** DOW-UAP-D089, Range Fouler Debrief, Eastern United States, 2020
- **csv:** `2020` -> `2020`
- **title dates:** 2020
- **confirmed date:** `2020` (via csv, title)
- **summary:** This document is a Range Fouler Debrief, a standardized reporting form the U.S. Navy uses to record the circumstances surrounding an unauthorized intrusion into controlled airspace during active mili…

### `dow-155-dow-uap-d090-range-fouler-debrief-eastern-united-states-2019`
- **family:** `DOW-UAP-D90`
- **title:** DOW-UAP-D090, Range Fouler Debrief, Eastern United States, 2019
- **csv:** `2019` -> `2019`
- **title dates:** 2019
- **confirmed date:** `2019` (via csv, title)
- **summary:** This document is a Range Fouler Debrief, a standardized reporting form the U.S. Navy uses to record the circumstances surrounding an unauthorized intrusion into controlled airspace during active mili…

### `dow-156-dow-uap-d091-range-fouler-debrief-atlantic-ocean-2020`
- **family:** `DOW-UAP-D91`
- **title:** DOW-UAP-D091, Range Fouler Debrief, Atlantic Ocean, 2020
- **csv:** `2020` -> `2020`
- **title dates:** 2020
- **confirmed date:** `2020` (via csv, title)
- **summary:** This document is a Range Fouler Debrief, a standardized reporting form the U.S. Navy uses to record the circumstances surrounding an unauthorized intrusion into controlled airspace during active mili…

### `dow-157-dow-uap-d092-department-of-the-air-force-committee-to-review`
- **family:** `DOW-UAP-D92`
- **title:** DOW-UAP-D092, Department of the Air Force Committee to Review Project Bluebook, 1966-1967
- **csv:** `4/17/67` -> `1967-04-17`
- **title dates:** 1966; 1967
- **confirmed date:** `1967` (via csv, title)
- **summary:** This file documents the 1966-1967 deliberations and recommendations of the U.S. Air Force (USAF) Scientific Advisory Board’s Ad Hoc Committee to Review Project Blue Book. Project Blue Book was a 1952…

### `dow-158-dow-uap-d093-analysis-of-flying-object-incidents-in-the-unit`
- **family:** `DOW-UAP-D93`
- **title:** DOW-UAP-D093, Analysis of Flying Object Incidents in the United States, 1948
- **csv:** `12/10/48` -> `1948-12-10`
- **title dates:** 1948
- **summary dates:** 1948-12-10
- **confirmed date:** `1948-12-10` (via csv, summary)
- **summary:** This file contains a U.S. Air Force (USAF) Air Intelligence Division study, “Analysis of Flying Object Incidents in the United States,” Study No. 203, dated 12/10/1948. The analysis includes an asses…

### `dow-159-dow-uap-d095-joint-u-s-canadian-aviation-projects-and-ufo-si`
- **family:** `DOW-UAP-D95`
- **title:** DOW-UAP-D095, Joint U.S.-Canadian Aviation Projects and UFO Sighting Reports, 1954-1955
- **csv:** `1955` -> `1955`
- **title dates:** 1954; 1955
- **summary dates:** 1955-07
- **confirmed date:** `1955` (via csv, summary, title)
- **summary:** This file contains reports, memoranda, and correspondence concerning various then-developmental vertical take-off and landing (VTOL) aircraft. The file includes assessments of the experimental potent…

### `dow-160-dow-uap-d096-correspondence-relating-to-project-blue-book-19`
- **family:** `DOW-UAP-D96`
- **title:** DOW-UAP-D096, Correspondence Relating to Project Blue Book, 1955
- **csv:** `1955` -> `1955`
- **title dates:** 1955
- **confirmed date:** `1955` (via csv, title)
- **summary:** This file contains correspondence relating to Project Blue Book, a 1952-1969 U.S. Air Force program to investigate the nature and origin of unidentified flying objects (UFO). The correspondence inclu…

### `dow-161-dow-uap-pr024-unresolved-uap-report-middle-east-2023`
- **family:** `DOW-UAP-PR24`
- **title:** DOW-UAP-PR024, Unresolved UAP Report, Middle East, 2023
- **csv:** `2023` -> `2023`
- **title dates:** 2023
- **confirmed date:** `2023` (via csv, title)
- **summary:** The United States Central Command submitted a report of an unidentified anomalous phenomenon to the All-domain Anomaly Resolution Office (AARO) consisting of 18 seconds of video footage from an infra…

### `dow-162-dow-uap-pr030-unresolved-uap-report-middle-east-2023`
- **family:** `DOW-UAP-PR30`
- **title:** DOW-UAP-PR030, Unresolved UAP Report, Middle East, 2023
- **csv:** `2023` -> `2023`
- **title dates:** 2023
- **confirmed date:** `2023` (via csv, title)
- **summary:** The United States Central Command submitted a report of an unidentified anomalous phenomenon to the All-domain Anomaly Resolution Office (AARO) consisting of 10 seconds of video footage from an infra…

### `dow-163-dow-uap-pr100-unresolved-uap-report-yellow-sea-2023`
- **family:** `DOW-UAP-PR100`
- **title:** DOW-UAP-PR100, Unresolved UAP Report, Yellow Sea, 2023
- **csv:** `2023` -> `2023`
- **title dates:** 2023
- **confirmed date:** `2023` (via csv, title)
- **summary:** The United States Indo-Pacific Command submitted a report of an unidentified anomalous phenomenon to the All-domain Anomaly Resolution Office (AARO) consisting of 4 minutes and 57 seconds of video fo…

### `dow-164-dow-uap-pr101-unresolved-uap-report-south-china-sea-2024`
- **family:** `DOW-UAP-PR101`
- **title:** DOW-UAP-PR101, Unresolved UAP Report, South China Sea, 2024
- **csv:** `2024` -> `2024`
- **title dates:** 2024
- **confirmed date:** `2024` (via csv, title)
- **summary:** The United States Indo-Pacific Command submitted a report of an unidentified anomalous phenomenon to the All-domain Anomaly Resolution Office (AARO) consisting of 1 minute and 46 seconds of video foo…

### `dow-165-dow-uap-pr102-unresolved-uap-report-east-china-sea-2024`
- **family:** `DOW-UAP-PR102`
- **title:** DOW-UAP-PR102, Unresolved UAP Report, East China Sea, 2024
- **csv:** `2024` -> `2024`
- **title dates:** 2024
- **confirmed date:** `2024` (via csv, title)
- **summary:** The United States Indo-Pacific Command submitted a report of an unidentified anomalous phenomenon to the All-domain Anomaly Resolution Office (AARO) consisting of 36 seconds of video footage from an …

### `dow-166-dow-uap-pr103-unresolved-uap-report-east-china-sea-2024`
- **family:** `DOW-UAP-PR103`
- **title:** DOW-UAP-PR103, Unresolved UAP Report, East China Sea, 2024
- **csv:** `2024` -> `2024`
- **title dates:** 2024
- **confirmed date:** `2024` (via csv, title)
- **summary:** The United States Indo-Pacific Command submitted a report of an unidentified anomalous phenomenon to the All-domain Anomaly Resolution Office (AARO) consisting of 1 minute and 16 seconds of video foo…

### `dow-167-dow-uap-pr106-unresolved-uap-report-eastern-united-states-20`
- **family:** `DOW-UAP-PR106`
- **title:** DOW-UAP-PR106, Unresolved UAP Report, Eastern United States, 2020
- **csv:** `2020` -> `2020`
- **title dates:** 2020
- **confirmed date:** `2020` (via csv, title)
- **summary:** The United States Northern Command submitted a report of an unidentified anomalous phenomenon to the All-domain Anomaly Resolution Office (AARO) consisting of 11 seconds of video footage from an infr…

### `dow-168-dow-uap-pr107-unresolved-uap-report-eastern-united-states-20`
- **family:** `DOW-UAP-PR107`
- **title:** DOW-UAP-PR107, Unresolved UAP Report, Eastern United States, 2020
- **csv:** `2020` -> `2020`
- **title dates:** 2020
- **confirmed date:** `2020` (via csv, title)
- **summary:** The United States Northern Command submitted a report of an unidentified anomalous phenomenon to the All-domain Anomaly Resolution Office (AARO) consisting of 28 seconds of video footage from an infr…

### `dow-169-dow-uap-pr108-unresolved-uap-report-western-united-states-20`
- **family:** `DOW-UAP-PR108`
- **title:** DOW-UAP-PR108, Unresolved UAP Report, Western United States, 2020
- **csv:** `2020` -> `2020`
- **title dates:** 2020
- **confirmed date:** `2020` (via csv, title)
- **summary:** The United States Northern Command submitted a report of an unidentified anomalous phenomenon to the All-domain Anomaly Resolution Office (AARO) consisting of 2 minutes and 16 seconds of video footag…

### `dow-170-dow-uap-pr109-unresolved-uap-report-eastern-united-states-20`
- **family:** `DOW-UAP-PR109`
- **title:** DOW-UAP-PR109, Unresolved UAP Report, Eastern United States, 2015
- **csv:** `2015` -> `2015`
- **title dates:** 2015
- **confirmed date:** `2015` (via csv, title)
- **summary:** The United States Navy Unidentified Anomalous Phenomena Task Force (UAPTF) transferred this media to the All-domain Anomaly Resolution Office (AARO) in 2022. The video contains 21 seconds of footage …

### `dow-171-dow-uap-pr110-unresolved-uap-report-eastern-united-states-20`
- **family:** `DOW-UAP-PR110`
- **title:** DOW-UAP-PR110, Unresolved UAP Report, Eastern United States, 2020
- **csv:** `2020` -> `2020`
- **title dates:** 2020
- **confirmed date:** `2020` (via csv, title)
- **summary:** The United States Northern Command submitted a report of an unidentified anomalous phenomenon to the All-domain Anomaly Resolution Office (AARO) consisting of 27 seconds of video footage from an infr…

### `dow-172-dow-uap-pr111-unresolved-uap-report-eastern-united-states-20`
- **family:** `DOW-UAP-PR111`
- **title:** DOW-UAP-PR111, Unresolved UAP Report, Eastern United States, 2020
- **csv:** `2020` -> `2020`
- **title dates:** 2020
- **confirmed date:** `2020` (via csv, title)
- **summary:** The United States Northern Command submitted a report of an unidentified anomalous phenomenon to the All-domain Anomaly Resolution Office (AARO) consisting of 1 minute of video footage from an infrar…

### `dow-173-dow-uap-pr112-unresolved-uap-report-eastern-united-states-20`
- **family:** `DOW-UAP-PR112`
- **title:** DOW-UAP-PR112, Unresolved UAP Report, Eastern United States, 2019
- **csv:** `2019` -> `2019`
- **title dates:** 2019
- **confirmed date:** `2019` (via csv, title)
- **summary:** The United States Navy submitted a report of an unidentified anomalous phenomenon to the All-domain Anomaly Resolution Office (AARO) consisting of 20 seconds of video footage from an infrared sensor …

### `dow-174-dow-uap-pr114-unresolved-uap-report-atlantic-ocean-2016`
- **family:** `DOW-UAP-PR114`
- **title:** DOW-UAP-PR114, Unresolved UAP Report, Atlantic Ocean, 2016
- **csv:** `2016` -> `2016`
- **title dates:** 2016
- **confirmed date:** `2016` (via csv, title)
- **summary:** The United States Northern Command submitted a report of an unidentified anomalous phenomenon to the All-domain Anomaly Resolution Office (AARO) consisting of 39 seconds of video footage from an infr…

### `dow-175-dow-uap-pr116-unresolved-uap-report-atlantic-ocean-2020`
- **family:** `DOW-UAP-PR116`
- **title:** DOW-UAP-PR116, Unresolved UAP Report, Atlantic Ocean, 2020
- **csv:** `2020` -> `2020`
- **title dates:** 2020
- **confirmed date:** `2020` (via csv, title)
- **summary:** The United States Northern Command submitted a report of an unidentified anomalous phenomenon to the All-domain Anomaly Resolution Office (AARO) consisting of 32 seconds of video footage from an infr…

### `fbi-001-65-hs1-834228961-62-hq-83894-section-10`
- **family:** `FBI-Section10`
- **title:** 65_HS1-834228961_62-HQ-83894_Section_10
- **csv:** `N/A` -> `-`
- **summary dates:** 1947-06; 1968-07
- **body dates (filtered):** 1966-10-03; 1966-09-22; 1966-09-19; 1966-05-04; 1966-03-10; 1966-10-19; 1949-03-25; 1947-10-01; 1967-04-27; 1967-07-25; 1967-10-10; 1967-10-09; 1968-01-23; 1967-11-20; 1968-01-17; 1969-05-16; 1969-05-01; 1973-03-20; 1973-03-09; 1963-09-24; 1974-08-22; 1974-08-21; 1977-06-14; 1966-09-06; 1966-08-31; 1964-04-24; 1966-06-04; 1966-06-23; 1966-06-25; 1966-03-05; 1965-10-25; 1966-04-30; 1966-03-29; 1966-07-10; 1968-03-26; 1966-04-04; 1965-12-13; 1965-01-15; 1966-03-25; 1966-05-09; 1966-05-15; 1966-04-18; 1966-03-30; 1966-03-22; 1965-10-24; 1966-10-17; 1966-10-20; 1966-10-16; 1966-10-21; 1965-01-26; 1966-12-21; 1966-12-27; 1966-12-23; 1967-01-23; 1967-01-20; 1967-01-18; 1967-01-17; 1959-07-24; 1961-07-04; 1967-04-26; 1945-03-14; 1951-12-26; 1952-01-07; 1924-05-03; 1967-06-08; 1967-07-28; 1967-08-24; 1967-08-19; 1967-09-12; 1966-09-07; 1967-03-17; 1967-03-10; 1965-08-03; 1966-05-10; 1966-06-27; 1967-01-11; 1967-10-02; 1967-10-19; 1967-08-21; 1962-05-22; 1967-08-06; 1967-08-20; 1987-10-09; 1968-03-19; 1968-03-18; 1969-03-19; 1963-12-07; 1963-12-08; 1964-07-18; 1964-07-28; 1969-04-30; 1969-05-21; 1969-05-14; 1969-10-13; 1969-10-18; 1972-06-20; 1971-08-03; 1972-02-23; 1972-02-15; 1973-10-25; 1974-04-15; 1974-03-31; 1963-09-17; 1969-12-17; 1977-01-24; 1977-01-27; 1977-06-15; 1962-05-10; 1962-05-02; 1971-07-23; 1982-05-10; 1973-07-10; 1965-04; 1966-11
- **confirmed date:** `1968` (via body, summary)
- **summary:** The FBI's 62-HQ-83894 case file includes investigative records, eyewitness testimonies, and public reports concerning Unidentified Flying Objects and flying discs documented between June 1947 and Jul…

### `fbi-002-65-hs1-834228961-62-hq-83894-section-2`
- **family:** `FBI-Section2`
- **title:** 65_HS1-834228961_62-HQ-83894_Section_2
- **csv:** `N/A` -> `-`
- **summary dates:** 1947-06; 1968-07
- **body dates (filtered):** 1947-09-16; 2017-09-17; 1947-07-28; 1947-08-03; 1947-08-04; 1947-08-13; 1930-04-12; 1947-05-29; 1947-08-08; 1947-08-06; 1917-08-01; 1947-08-12; 1964-11-18; 1947-08-25; 1947-08-20; 1947-09-05; 1947-08-15; 1947-08-07; 1947-08-16; 1947-09-08; 1947-08-22; 1947-08-19; 1947-09-25; 1947-09-17; 1947-08-28; 1947-08-30; 1947-09-02; 1947-08-29; 1947-07-07; 1947-09-04; 1947-06-24; 1947-07-21; 1947-10-03; 1947-09-19; 1947-07-10; 1947-07-12; 1915-03-29; 1947-07-30; 1947-08-27; 1947-07-06; 1947-07-09; 1947-07-05; 1947-07-08; 1947-07-16; 1947-06-26; 1947-07-14; 1947-07-15
- **confirmed date:** `1947-06` (via body, summary)
- **summary:** The FBI's 62-HQ-83894 case file includes investigative records, eyewitness testimonies, and public reports concerning Unidentified Flying Objects and flying discs documented between June 1947 and Jul…

### `fbi-003-65-hs1-834228961-62-hq-83894-section-3`
- **family:** `FBI-Section3`
- **title:** 65_HS1-834228961_62-HQ-83894_Section_3
- **csv:** `N/A` -> `-`
- **summary dates:** 1947-06; 1968-07
- **body dates (filtered):** 1947-08-08; 1947-09-04; 1947-08-25; 1947-07-30; 1947-06-24; 1937-09-04; 1947-08-27; 1947-08-30; 1947-07-29; 1947-07-07; 1947-07-18; 1947-08-15; 1904-11-18; 1917-08-01; 1947-07-31; 1947-08-01; 1964-11-18; 1947-08-19; 1947-08-26; 1947-08-18; 1947-08-20; 1947-08-14; 1947-08-21; 1947-08-07; 1947-09-10; 1982-09-12; 1947-08-28; 1947-08-04; 1947-08-12; 1947-06-26; 1947-07-25; 1947-06-21; 1947-07-23; 1947-08-13; 1947-07-24; 1947-07-16; 1915-03-29; 1947-09-20; 1947-08-11; 1947-08-06; 1947-09-18; 1947-09-27; 1947-09-25; 1947-09-03; 1947-09-23; 1910-05-01; 1947-09-02; 1947-09-24; 1947-09-05; 1947-05-05; 1947-08-22; 1947-07-08; 1947-07-11; 1947-07-14; 1947-09-09; 1947-07-12
- **confirmed date:** `1947-06` (via body, summary)
- **summary:** The FBI's 62-HQ-83894 case file includes investigative records, eyewitness testimonies, and public reports concerning Unidentified Flying Objects and flying discs documented between June 1947 and Jul…

### `fbi-004-65-hs1-834228961-62-hq-83894-section-4`
- **family:** `FBI-Section4`
- **title:** 65_HS1-834228961_62-HQ-83894_Section_4
- **csv:** `N/A` -> `-`
- **summary dates:** 1947-06; 1968-07
- **body dates (filtered):** 1947-10-18; 1947-09-25; 1948-03-01; 1948-09-22; 1948-12-28; 1948-12-27; 1948-12-29; 1948-07-25; 1948-07-27; 1947-10-09; 1947-09-13; 1947-09-11; 1964-11-18; 1947-09-12; 1947-09-17; 1947-10-28; 1947-11-05; 1947-11-18; 1947-11-06; 1948-01-05; 1948-01-15; 1948-02-12; 1948-02-04; 1947-10-01; 1948-02-20; 1948-02-19; 1948-03-22; 1948-03-14; 1948-03-24; 1948-08-10; 1948-10-19; 1948-12-06; 1948-12-07; 1948-12-05; 1948-12-13; 1948-12-23; 1949-01-24; 1949-01-31; 1949-03-22; 1949-02-16; 1949-02-14; 1949-02-15; 1949-05-04; 1949-04-16; 1949-04-15; 1949-04-17; 1949-05-02; 1949-04-26; 1949-04-04; 1949-04-03; 1949-03-25; 1949-04-27; 1949-03-31; 1949-05-03; 1949-05-10; 1949-04-29; 1949-05-13; 1949-05-05; 1949-04-25; 1948-07-24; 1949-05-19; 1949-04-21; 1947-08-14; 1949-07-19; 1949-06-06; 1947-09-04; 1947-09-09; 1949-06-30; 1949-06-08; 1949-06-07; 1947-09-03; 1948-09-09; 1949-02-10; 1948-12-16; 1947-07; 1945-07; 1941-08
- **confirmed date:** `1947` (via body, summary)
- **summary:** The FBI's 62-HQ-83894 case file includes investigative records, eyewitness testimonies, and public reports concerning Unidentified Flying Objects and flying discs documented between June 1947 and Jul…

### `fbi-006-65-hs1-834228961-62-hq-83894-section-6`
- **family:** `FBI-Section6`
- **title:** 65_HS1-834228961_62-HQ-83894_Section_6
- **csv:** `N/A` -> `-`
- **summary dates:** 1947-06; 1968-07
- **body dates (filtered):** 1950-09-26; 1950-10-18; 1952-08-07; 2007-05-24; 1950-05-23; 1950-07-19; 1950-05-24; 1950-08-10; 1950-09-08; 1950-08-29; 1950-09-27; 1950-10-09; 1950-08-23; 1950-10-02; 1950-10-13; 1964-11-23; 1949-03-25; 1950-10-20; 1950-11-04; 1950-12-28; 1950-12-19; 1950-12-18; 1951-02-26; 1951-02-14; 1952-03-21; 1952-03-11; 1952-03-06; 1952-03-13; 1952-04-17; 1952-04-07; 1952-05-05; 1952-05-16; 1952-05-13; 1952-05-07; 1952-05-10; 1952-06-10; 1947-08-29; 1947-07-07; 1947-09-04; 1947-08-30; 1950-04-17; 1927-08-30; 1949-06-08; 1952-06-04; 1952-06-08; 1952-06-17; 1952-07-06; 1952-07-08; 1952-07-28; 1952-07-31; 1952-07-27; 1952-07-30; 1952-07-29; 1952-08-08; 1952-08-01; 1952-08-12; 1952-08-18; 1952-08-14; 1952-08-06; 1952-08-13; 1952-08-05; 1952-08-15; 1952-08-11; 1958-07-27; 1950-05-25; 1949-02-17; 1949-10-14; 1950-02-25; 1950-11-15; 1951-01-02; 1951-01-20; 1950-12-20; 1951-12-14; 1950-12-14; 1951-01-16; 1950-01-20; 1951-01-17; 1951-09-10; 1951-09-11; 1952-03-29; 1952-05-09; 1952-05-12; 1946-12; 1948-12
- **confirmed date:** `1947` (via body, summary)
- **summary:** The FBI's 62-HQ-83894 case file includes investigative records, eyewitness testimonies, and public reports concerning Unidentified Flying Objects and flying discs documented between June 1947 and Jul…

### `fbi-007-65-hs1-834228961-62-hq-83894-section-7`
- **family:** `FBI-Section7`
- **title:** 65_HS1-834228961_62-HQ-83894_Section_7
- **csv:** `N/A` -> `-`
- **summary dates:** 1947-06; 1968-07
- **body dates (filtered):** 1947-10-01; 1949-03-25; 1952-08-29; 1953-04-28; 1953-04-27; 1953-04-08; 1954-06-08; 1953-03-31; 1982-08-14; 1952-08-01; 1952-08-12; 1952-07-31; 1952-08-13; 1952-08-05; 1952-08-04; 1952-08-06; 1952-09-02; 1964-11-19; 1952-08-22; 1952-08-15; 1952-08-02; 1952-08-20; 1952-08-25; 1952-08-14; 1952-09-05; 1952-08-26; 1952-09-11; 1952-09-25; 1952-09-20; 1952-10-06; 1952-09-06; 1982-10-29; 1949-12-27; 1948-01-22; 1952-10-28; 1952-09-30; 1952-10-27; 1953-02-11; 1953-01-20; 1953-01-28; 1953-01-19; 1952-10-26; 1952-10-11; 1951-07-06; 1903-12-26; 1940-06-01; 1953-04-01; 1953-02-17; 1953-03-06; 1953-02-14; 1953-03-10; 1953-03-09; 1953-03-12; 1953-03-23; 1953-03-04; 1953-07-09; 1953-06-30; 1953-07-10; 1953-07-28; 1953-07-15; 1954-05-05; 1953-12-20; 1952-03-29; 1954-01-30; 1954-05-18; 1954-04-12; 1954-04-27; 1954-04-21; 1953-03-13; 1954-07-09; 1951-01; 1953-05
- **confirmed date:** `1947` (via body, summary)
- **summary:** The FBI's 62-HQ-83894 case file includes investigative records, eyewitness testimonies, and public reports concerning Unidentified Flying Objects and flying discs documented between June 1947 and Jul…

### `fbi-008-65-hs1-834228961-62-hq-83894-section-9`
- **family:** `FBI-Section9`
- **title:** 65_HS1-834228961_62-HQ-83894_Section_9
- **csv:** `N/A` -> `-`
- **summary dates:** 1947-06; 1968-07
- **body dates (filtered):** 1958-01-06; 1957-12-20; 1958-09-22; 1958-11-18; 1958-11-17; 1958-12-08; 1952-10-26; 1958-12-07; 2025-01-21; 1958-12-16; 1959-01-05; 1958-12-30; 1959-02-12; 1959-01-22; 1959-04-21; 1959-05-05; 1960-03-28; 1960-03-27; 1960-03-09; 1960-03-04; 1960-04-11; 1960-04-06; 1960-04-12; 1960-04-17; 1960-04-19; 1960-04-21; 1962-10-02; 1947-10-01; 1963-10-01; 1963-10-04; 1964-04-27; 1964-04-25; 1964-04-24; 1964-04-26; 1964-05-08; 1963-09-17; 1948-02-02; 1960-06-15; 1958-08-07; 1963-08-08; 1963-07-23; 1963-09-07; 1963-09-27; 1957-11-20; 1957-10-10; 1958-01-23; 1958-01-30; 1958-03-17; 1958-10-02; 1958-07-09; 1958-07-03; 1957-12-05; 1958-10-06; 1947-04-30; 1947-08-30; 1950-04-17; 1958-12-02; 1958-11-22; 1958-12-11; 1958-12-03; 1954-01-01; 1958-12-09; 1958-10-15; 1958-12-17; 1958-12-12; 1958-12-31; 1959-02-09; 1959-02-01; 1952-01-01; 1959-02-10; 1959-04-02; 1959-04-03; 1959-04-22; 1959-04-30; 1959-05-22; 1959-05-25; 1959-08-31; 1959-08-24; 1959-10-07; 1960-03-29; 1960-04-01; 1969-04-13; 1960-03-21; 1960-03-26; 1959-03-21; 1960-04-14; 1960-04-13; 1960-04-26; 1960-05-03; 1960-08-23; 1960-09-30; 1960-10-17; 1960-10-10; 1961-09-25; 1961-10-17; 1961-10-01; 1961-09-10; 1963-06-27; 1963-07-02; 1963-07-17; 1963-07-10; 1968-04-29; 1960-03-13; 1963-10-10; 1959-08-26; 1964-03-09; 1963-10-03; 1964-07-13; 1964-07-05; 1964-11-16; 1965-01-26; 1965-02-26; 1963-02-21; 1965-04-28; 1965-04-30; 1966-04-15; 1966-07-20; 1966-07-21; 1966-07-16; 1966-07-22; 1960-06-06; 1958-06; 1960-02; 1964-02; 1952-12
- **confirmed date:** `1947` (via body, summary)
- **summary:** The FBI's 62-HQ-83894 case file includes investigative records, eyewitness testimonies, and public reports concerning Unidentified Flying Objects and flying discs documented between June 1947 and Jul…

### `fbi-009-65-hs1-834228961-62-hq-83894-serial-130`
- **family:** `FBI-Serial130`
- **title:** 65_HS1-834228961_62-HQ-83894_Serial_130
- **csv:** `N/A` -> `-`
- **summary dates:** 1947-06; 1968-07
- **body dates (filtered):** 1947-07-15; 1947-08-15; 1947-08-13; 1947-08-01; 1947-07-12; 1947-07-28; 1916-09-14; 1947-09-12; 1947-08-12; 1947-08-04; 1947-07-25; 1947-07-06; 1947-07-23; 1947-07-10; 1947-07-11; 1947-07-20; 1947-07-09; 1917-07-20; 1917-07-15; 1947-07-17; 1947-08-25; 1947-07-30; 1947-07-16; 1947-07-01; 1947-06-30; 1947-07-21; 1947-07-29; 1947-07-07; 1947-07-03; 1947-06-27; 1947-07-02; 1947-05-21; 1917-06-26; 1947-07-18; 1947-06-29; 1945-08-15; 1946-08-15; 1927-07; 1947-04
- **confirmed date:** `1947-06` (via body, summary)
- **summary:** The FBI's 62-HQ-83894 case file includes investigative records, eyewitness testimonies, and public reports concerning Unidentified Flying Objects and flying discs documented between June 1947 and Jul…

### `fbi-010-65-hs1-834228961-62-hq-83894-serial-153`
- **family:** `FBI-Serial153`
- **title:** 65_HS1-834228961_62-HQ-83894_Serial_153
- **csv:** `N/A` -> `-`
- **summary dates:** 1947-06; 1968-07
- **body dates (filtered):** 1947-07
- **confirmed date:** `1947` (via body, summary)
- **summary:** The FBI's 62-HQ-83894 case file includes investigative records, eyewitness testimonies, and public reports concerning Unidentified Flying Objects and flying discs documented between June 1947 and Jul…

### `fbi-016-65-hs1-834228961-62-hq-83894-sub-a`
- **title:** 65_HS1-834228961_62-HQ-83894_SUB_A
- **csv:** `N/A` -> `-`
- **summary dates:** 1947-06; 1968-07
- **body dates (filtered):** 2007-05-24; 1960-06-03; 1959-03-03; 1998-08-12; 1957-11-22; 1957-01-28; 1956-08-08; 1956-03-22; 1954-07-14; 1954-01-15; 1954-01-08; 1954-01-12; 1952-03-29; 1959-08-13; 1959-07-31; 1950-07-09; 1950-08-11; 1950-04-20; 1950-04-11; 1950-04-03; 1949-12-27; 1950-03-31; 1950-03-29; 1950-03-26; 1947-06-25; 1950-04-18; 1950-02-27; 1950-02-08; 1949-09-23; 1949-07-17; 1947-07-28; 1947-07-06; 1947-07-12; 1947-07-05; 1951-01
- **confirmed date:** `1947-06` (via body, summary)
- **summary:** The FBI's 62-HQ-83894 case file includes investigative records, eyewitness testimonies, and public reports concerning Unidentified Flying Objects and flying discs documented between June 1947 and Jul…

### `fbi-017-65-hs1-101634279-100-de-18221-serial-844`
- **title:** 65_HS1-101634279_100-DE-18221_Serial_844
- **csv:** `4/17/58` -> `1958-04-17`
- **body dates (filtered):** 2007-05-24; 1958-04-17
- **confirmed date:** `1958-04-17` (via body, csv)
- **summary:** An FBI memo from 1958 reporting a UFO sighting by a Detroit man who described a "circular object with a crystal-type dome," and recommending that the information be forwarded to "proper air force aut…

### `fbi-019-65-hs1-834228961-62-hq-83894-section-1`
- **family:** `FBI-Section1`
- **title:** 65_HS1-834228961_62-HQ-83894_Section_1
- **csv:** `N/A` -> `-`
- **summary dates:** 1947-06; 1968-07
- **body dates (filtered):** 1947-07-10; 1947-07-22; 1947-08-05; 1947-07-11; 1947-07-09; 1947-07-17; 1964-11-18; 1947-07-01; 1947-07-18; 1904-11-18; 1947-07-06; 1947-07-30; 1947-07-14; 1947-08-01; 1947-08-06; 1947-09-13; 1947-08-07; 1947-08-08; 1947-07-08; 1947-08-12; 1947-08-04; 1947-07-05; 1947-07-04; 1947-02
- **confirmed date:** `1947` (via body, summary)
- **summary:** The FBI's 62-HQ-83894 case file includes investigative records, eyewitness testimonies, and public reports concerning Unidentified Flying Objects and flying discs documented between June 1947 and Jul…

### `fbi-054-fbi-september-2023-sighting-composite-sketch`
- **title:** FBI September 2023 Sighting - Composite Sketch
- **csv:** `9/1/23` -> `2023-09-01`
- **title dates:** 2023-09
- **summary dates:** 2023-09
- **confirmed date:** `2023-09` (via csv, summary, title)
- **summary:** Actual site photo with FBI Lab rendered graphic overlay depicting corroborating eyewitness reports from September 2023 of an apparent ellipsoid bronze metallic object materializing out of a bright li…

### `fbi-055-fbi-september-2023-sighting-serial-3`
- **title:** FBI September 2023 Sighting - Serial 3
- **csv:** `9/1/23` -> `2023-09-01`
- **title dates:** 2023-09
- **body dates (filtered):** 2023-09
- **confirmed date:** `2023-09` (via body, csv, title)
- **summary:** This is an FBI 302 interview conducted with a US citizen regarding their first-hand account of a UAP encounter at a US test site. USPER described an object "metallic bronze in color."

### `fbi-056-fbi-september-2023-sighting-serial-4`
- **title:** FBI September 2023 Sighting - Serial 4
- **csv:** `9/1/23` -> `2023-09-01`
- **title dates:** 2023-09
- **body dates (filtered):** 2023-09
- **confirmed date:** `2023-09` (via body, csv, title)
- **summary:** This is an FBI 302 interview conducted with a US citizen regarding their first-hand account of a UAP encounter at a US test site. USPER described an object "metallic/gray in color."

### `fbi-057-fbi-september-2023-sighting-serial-5`
- **title:** FBI September 2023 Sighting - Serial 5
- **csv:** `9/1/23` -> `2023-09-01`
- **title dates:** 2023-09
- **body dates (filtered):** 2023-09
- **confirmed date:** `2023-09` (via body, csv, title)
- **summary:** This is an FBI 302 interview conducted with a US citizen regarding their first-hand account of a UAP encounter at a US test site. USPER described a "bright light over the horizon."

### `fbi-058-fbi-uap-d002-fd-1057-unresolved-uap-report-colorado-springs`
- **title:** FBI-UAP-D002, FD-1057, Unresolved UAP Report, Colorado Springs, 2022
- **csv:** `2022` -> `2022`
- **title dates:** 2022
- **confirmed date:** `2022` (via csv, title)
- **summary:** This document is an FBI FD-1057, a form the Federal Bureau of Investigation (FBI) uses to record investigative activity. This FD-1057 contains a first-hand narrative description of unidentified anoma…

### `fbi-059-fbi-uap-d003-digital-rendering-unresolved-uap-report-colorad`
- **title:** FBI-UAP-D003, Digital Rendering, Unresolved UAP Report, Colorado Springs, 2022
- **csv:** `2022` -> `2022`
- **title dates:** 2022
- **confirmed date:** `2022` (via csv, title)
- **summary:** This image is an artistic interpretation of a 2022 incident potentially involving unidentified anomalous phenomena (UAP) reported near Colorado Springs, Colorado. This image is derived from the first…

### `fbi-060-fbi-uap-d009-fd-302-67-northeastern-orb-sighting-2026`
- **title:** FBI-UAP-D009, FD-302-67, “Northeastern Orb Sighting,” 2026
- **csv:** `2026` -> `2026`
- **title dates:** 2026
- **summary dates:** 2026-02
- **confirmed date:** `2026` (via csv, summary, title)
- **summary:** This document is an FBI FD-302, a form the Federal Bureau of Investigation uses to record interviews. This FD-302 records a February 2026 interview with a U.S. person, in which they described inciden…

### `fbi-061-fbi-uap-d010-fd-302-71-northeastern-orb-sighting-2026`
- **title:** FBI-UAP-D010, FD-302-71, “Northeastern Orb Sighting,” 2026
- **csv:** `2026` -> `2026`
- **title dates:** 2026
- **confirmed date:** `2026` (via csv, title)
- **summary:** This document is an FBI FD-302, a form the Federal Bureau of Investigation uses to record interviews. This FD-302 records an interview with a U.S. person regarding their first-hand account of an inci…

### `fbi-062-fbi-uap-d011-d-fbi-correspondence-referral-1949`
- **title:** FBI-UAP-D011, D/FBI Correspondence Referral, 1949
- **csv:** `1949` -> `1949`
- **title dates:** 1949
- **body dates (filtered):** 1949-01-31
- **confirmed date:** `1949` (via body, csv, title)
- **summary:** This collection of documents contains correspondence between the Director of the Federal Bureau of Investigation (FBI), J. Edgar Hoover, and Rev. Charles Barnes concerning Barnes’ account of an incid…

### `fbi-063-fbi-uap-pr003-orbs-over-the-pond-2024`
- **title:** FBI-UAP-PR003, “Orbs Over the Pond,” 2024
- **csv:** `October, 2024` -> `2024`
- **title dates:** 2024
- **summary dates:** 2024-10
- **confirmed date:** `2024` (via csv, summary, title)
- **summary:** In October 2024, at approximately 1851 local time in the northeastern United States, an eyewitness observed a light source below the horizon, hovering above a pond at an estimated distance of 2,700 f…

### `fbi-064-fbi-uap-pr004-northeastern-orb-sighting-2025`
- **title:** FBI-UAP-PR004, “Northeastern Orb Sighting,” 2025
- **csv:** `July, 2025` -> `2025`
- **title dates:** 2025
- **summary dates:** 2025-07
- **confirmed date:** `2025` (via csv, summary, title)
- **summary:** In July 2025, at approximately 2100 local time in the northeastern United States, an eyewitness observed an intense bright light in their backyard as they parked their car upon returning home from wo…

### `fbi-065-fbi-uap-d001-fd-302-unresolved-uap-report-colorado-springs-2`
- **title:** FBI-UAP-D001, FD-302, Unresolved UAP Report, Colorado Springs, 2022
- **csv:** `February, 2022` -> `2022`
- **title dates:** 2022
- **summary dates:** 2025-03; 2022-02
- **confirmed date:** `2022` (via csv, summary, title)
- **summary:** This document is a Federal Bureau of Investigation (FBI) FD-302, a form the FBI uses to record interviews. This FD-302 contains a summary of an interview with a U.S. military service member in March …

### `fbi-066-fbi-uap-d004-fd-1057-02-northeastern-united-states-2024`
- **title:** FBI-UAP-D004, FD-1057-02, Northeastern United States, 2024
- **csv:** `October, 2024` -> `2024`
- **title dates:** 2024
- **summary dates:** 2024-10
- **body dates (filtered):** 2024-08; 2021-11
- **confirmed date:** `2024` (via body, csv, summary, title)
- **summary:** This document is an FBI FD-1057, a form the Federal Bureau of Investigation (FBI) uses to record investigative activity. This FD-1057 documents the FBI’s contact with a U.S. person in October 2024, d…

### `fbi-067-fbi-uap-d005-fd-1057-04-northeastern-united-states-2024`
- **title:** FBI-UAP-D005, FD-1057-04, Northeastern United States, 2024
- **csv:** `October, 2024` -> `2024`
- **title dates:** 2024
- **summary dates:** 2024-10
- **confirmed date:** `2024` (via csv, summary, title)
- **summary:** This document is an FBI FD-1057, a form the Federal Bureau of Investigation (FBI) uses to record investigative activity. This FD-1057 documents an October 2024 interview with a US person regarding se…

### `fbi-068-fbi-uap-d006-fd-1057-05-northeastern-united-states-2024`
- **title:** FBI-UAP-D006, FD-1057-05, Northeastern United States, 2024
- **csv:** `November, 2024` -> `2024`
- **title dates:** 2024
- **summary dates:** 2024-11
- **confirmed date:** `2024` (via csv, summary, title)
- **summary:** This document is an FBI FD-1057, a form the Federal Bureau of Investigation (FBI) uses to record investigative activity. This FD-1057 documents a November 2024 site survey of a location where a U.S. …

### `fbi-069-fbi-uap-d007-fd-1057-06-northeastern-united-states-2024`
- **title:** FBI-UAP-D007, FD-1057-06, Northeastern United States, 2024
- **csv:** `November, 2024` -> `2024`
- **title dates:** 2024
- **summary dates:** 2024-11
- **confirmed date:** `2024` (via csv, summary, title)
- **summary:** This document is an FBI FD-1057, a form the Federal Bureau of Investigation (FBI) uses to record investigative activity. This FBI FD-1057 documents first-hand observations made by two FBI special age…

### `fbi-070-fbi-uap-d008-fd-1057-07-northeastern-united-states-2024`
- **title:** FBI-UAP-D008, FD-1057-07, Northeastern United States, 2024
- **csv:** `December, 2024` -> `2024`
- **title dates:** 2024
- **summary dates:** 2024-12
- **body dates (filtered):** 2024-12-01
- **confirmed date:** `2024-12` (via body, summary)
- **note:** csv `2024` disagrees
- **summary:** This document is an FBI FD-1057, a form the Federal Bureau of Investigation (FBI) uses to record investigative activity. This FBI FD-1057 documents a December 2024 site survey of a location where two…

### `fbi-071-fbi-uap-d012-newark-field-office-1952-1967`
- **title:** FBI-UAP-D012, Newark Field Office, 1952-1967
- **csv:** `August 1952-1967` -> `1952-08`
- **title dates:** 1952; 1967
- **summary dates:** 1952-08; 1967-01
- **body dates (filtered):** 1957-08-28; 1957-08-27; 1958-02-14; 1958-02-11; 1959-10-28; 1960-02-27; 1961-02-08; 1961-01-16; 1961-02-13; 1966-07-11; 1957-11-05; 1960-01-16
- **confirmed date:** `1952-08` (via csv, summary)
- **summary:** This file details a special inquiry by the Federal Bureau of Investigation’s Newark Field Office of various reported sightings of unidentified flying objects (UFOs) in and near New Jersey between Aug…

### `fbi-072-fbi-uap-d013-washington-state-ufo-investigation-1952-1960`
- **title:** FBI-UAP-D013, Washington State ‘UFO’ Investigation, 1952-1960
- **csv:** `July 1952-1960` -> `1952-07`
- **title dates:** 1952; 1960
- **summary dates:** 1952-07; 1960-08
- **body dates (filtered):** 1954-06-07; 1954-06-06; 1954-06-24
- **confirmed date:** `1952-07` (via csv, summary)
- **summary:** This file details an investigation of various sightings of Unidentified Flying Objects (UFOs) in Washington state between July 1952 and August 1960. This file includes memoranda and correspondence be…

### `fbi-073-fbi-uap-d014-digital-rendering-narrative-statement-1-1-weste`
- **title:** FBI-UAP-D014, Digital Rendering, Narrative Statement 1-1, Western United States Event, 2023
- **csv:** `October, 2023` -> `2023`
- **title dates:** 2023
- **summary dates:** 2023-10
- **confirmed date:** `2023` (via csv, summary, title)
- **summary:** This image is an artistic interpretation of a reported incident near a sensitive national security site in the western United States involving unidentified anomalous phenomena (UAP) over a period of …

### `fbi-074-fbi-uap-d015-digital-rendering-narrative-statement-1-2-weste`
- **title:** FBI-UAP-D015, Digital Rendering, Narrative Statement 1-2, Western United States Event, 2023
- **csv:** `October, 2023` -> `2023`
- **title dates:** 2023
- **summary dates:** 2023-10
- **confirmed date:** `2023` (via csv, summary, title)
- **summary:** This image is an artistic interpretation of a reported incident near a sensitive national security site in the western United States involving unidentified anomalous phenomena (UAP) over a period of …

### `fbi-075-fbi-uap-d016-digital-rendering-narrative-statement-2-1-weste`
- **title:** FBI-UAP-D016, Digital Rendering, Narrative Statement 2-1, Western United States Event, 2023
- **csv:** `October, 2023` -> `2023`
- **title dates:** 2023
- **summary dates:** 2023-10
- **confirmed date:** `2023` (via csv, summary, title)
- **summary:** This image is an artistic interpretation of a reported incident near a sensitive national security site in the western United States involving unidentified anomalous phenomena (UAP) over a period of …

### `fbi-076-fbi-uap-d017-digital-rendering-narrative-statement-2-2-weste`
- **title:** FBI-UAP-D017, Digital Rendering, Narrative Statement 2-2, Western United States Event, 2023
- **csv:** `October, 2023` -> `2023`
- **title dates:** 2023
- **summary dates:** 2023-10
- **confirmed date:** `2023` (via csv, summary, title)
- **summary:** This image is an artistic interpretation of a reported incident near a sensitive national security site in the western United States involving unidentified anomalous phenomena (UAP) over a period of …

### `fbi-077-fbi-uap-d018-digital-rendering-narrative-statement-2-3-weste`
- **title:** FBI-UAP-D018, Digital Rendering, Narrative Statement 2-3, Western United States Event, 2023
- **csv:** `October, 2023` -> `2023`
- **title dates:** 2023
- **summary dates:** 2023-10
- **confirmed date:** `2023` (via csv, summary, title)
- **summary:** This image is an artistic interpretation of a reported incident near a sensitive national security site in the western United States involving unidentified anomalous phenomena (UAP) over a period of …

### `fbi-078-fbi-uap-d019-digital-rendering-narrative-statement-2-4-weste`
- **title:** FBI-UAP-D019, Digital Rendering, Narrative Statement 2-4, Western United States Event, 2023
- **csv:** `October, 2023` -> `2023`
- **title dates:** 2023
- **summary dates:** 2023-10
- **confirmed date:** `2023` (via csv, summary, title)
- **summary:** This image is an artistic interpretation of a reported incident near a sensitive national security site in the western United States involving unidentified anomalous phenomena (UAP) over a period of …

### `fbi-079-fbi-uap-d020-digital-rendering-narrative-statement-2-5-weste`
- **title:** FBI-UAP-D020, Digital Rendering, Narrative Statement 2-5, Western United States Event, 2023
- **csv:** `October, 2023` -> `2023`
- **title dates:** 2023
- **summary dates:** 2023-10
- **confirmed date:** `2023` (via csv, summary, title)
- **summary:** This image is an artistic interpretation of a reported incident near a sensitive national security site in the western United States involving unidentified anomalous phenomena (UAP) over a period of …

### `fbi-080-fbi-uap-d021-digital-rendering-narrative-statement-1-3-weste`
- **title:** FBI-UAP-D021, Digital Rendering, Narrative Statement 1-3, Western United States Event, 2023
- **csv:** `October, 2023` -> `2023`
- **title dates:** 2023
- **summary dates:** 2023-10
- **confirmed date:** `2023` (via csv, summary, title)
- **summary:** This image is an artistic interpretation of a reported incident near a sensitive national security site in the western United States involving unidentified anomalous phenomena (UAP) over a period of …

### `fbi-081-fbi-uap-d022-digital-rendering-narrative-statement-2-6-weste`
- **title:** FBI-UAP-D022, Digital Rendering, Narrative Statement 2-6, Western United States Event, 2026
- **csv:** `October, 2023` -> `2023`
- **title dates:** 2026
- **summary dates:** 2023-10
- **confirmed date:** `2023` (via csv, summary)
- **summary:** This image is an artistic interpretation of a reported incident near a sensitive national security site in the western United States involving unidentified anomalous phenomena (UAP) over a period of …

### `fbi-082-fbi-uap-d023-digital-rendering-narrative-statement-2-7-weste`
- **title:** FBI-UAP-D023, Digital Rendering, Narrative Statement 2-7, Western United States Event, 2023
- **csv:** `October, 2023` -> `2023`
- **title dates:** 2023
- **summary dates:** 2023-10
- **confirmed date:** `2023` (via csv, summary, title)
- **summary:** This image is an artistic interpretation of a reported incident near a sensitive national security site in the western United States involving unidentified anomalous phenomena (UAP) over a period of …

### `fbi-083-fbi-uap-pr001-triangle-orbs-northeastern-united-states-2021`
- **title:** FBI-UAP-PR001, “Triangle Orbs,” Northeastern United States, 2021
- **csv:** `November, 2021` -> `2021`
- **title dates:** 2021
- **summary dates:** 2021-11
- **confirmed date:** `2021` (via csv, summary, title)
- **summary:** In November 2021, at approximately 0500 local time in the northeastern United States, an eyewitness observed a bright light source near the horizon at an estimated distance of 2,000 feet. The light s…

### `fbi-084-fbi-uap-pr002-red-orb-rotation-northeastern-united-states-20`
- **title:** FBI-UAP-PR002, “Red Orb Rotation,” Northeastern United States, 2022
- **csv:** `March, 2022` -> `2022`
- **title dates:** 2022
- **summary dates:** 2022-03
- **confirmed date:** `2022` (via csv, summary, title)
- **summary:** In March 2022, at approximately 1920 local time in the northeastern United States, an eyewitness observed two bright red luminous light sources hovering near the horizon at an estimated distance of 2…

### `fbi-085-fbi-uap-pr005-digital-recreation-narrative-statement-3-1-wes`
- **title:** FBI-UAP-PR005, Digital Recreation, Narrative Statement 3-1, Western United States Event, 2023
- **csv:** `October, 2023` -> `2023`
- **title dates:** 2023
- **summary dates:** 2023-10
- **confirmed date:** `2023` (via csv, summary, title)
- **summary:** This video is an artistic interpretation of a reported incident near a sensitive national security site in the western United States involving unidentified anomalous phenomena (UAP) over a period of …

### `fbi-086-fbi-uap-pr006-digital-recreation-narrative-statement-3-2-wes`
- **title:** FBI-UAP-PR006, Digital Recreation, Narrative Statement 3-2, Western United States Event, 2023
- **csv:** `October, 2023` -> `2023`
- **title dates:** 2023
- **summary dates:** 2023-10
- **confirmed date:** `2023` (via csv, summary, title)
- **summary:** This video is an artistic interpretation of a reported incident near a sensitive national security site in the western United States involving unidentified anomalous phenomena (UAP) over a period of …

### `fbi-087-fbi-uap-d014-correspondence-relating-to-ufo-sightings-1967-1`
- **title:** FBI-UAP-D014, Correspondence Relating to UFO Sightings, 1967, 1974
- **csv:** `10/10/74` -> `1974-10-10`
- **title dates:** 1967; 1974
- **summary dates:** 1967-09-22; 1974-09-30; 1974-10-10; 1954-04-08
- **confirmed date:** `1974-10-10` (via csv, summary)
- **summary:** This file contains two pieces of correspondence. The first, dated 9/22/1967, relays a description of an incident provided by an eleven-year-old child in which they heard a “weird” noise and saw a “fl…

### `ica-001-ica-uap-d001-analysis-colorado-springs-uap-incident-2022`
- **title:** ICA-UAP-D001, Analysis: Colorado Springs UAP Incident, 2022
- **csv:** `2022` -> `2022`
- **title dates:** 2022
- **summary dates:** 2026-06
- **body dates (filtered):** 2022-02-15
- **confirmed date:** `2022` (via body, csv, title)
- **summary:** This document contains analysis by an All-domain Anomaly Resolution Office (AARO) Intelligence Community (IC) partner to account for a 2022 incident involving an airborne object near Colorado Springs…

### `nasa-002-nasa-uap-d3-gemini-7-transcript-1965`
- **family:** `NASA-UAP-D3`
- **title:** NASA-UAP-D3, Gemini 7 Transcript, 1965
- **csv:** `12/5/65` -> `1965-12-05`
- **title dates:** 1965
- **confirmed date:** `1965` (via csv, title)
- **summary:** Gemini 7 was the tenth crewed American spaceflight. This document is a transcript of communications between the flight crew, Astronauts James “Jim” Lovell and Frank Borman, and the Manned Flight Cent…

### `nasa-003-nasa-uap-d3a-gemini-7-audio-excerpt-1965`
- **family:** `NASA-UAP-D3`
- **title:** NASA-UAP-D003A, Gemini 7 Audio Excerpt, 1965
- **csv:** `12/5/65` -> `1965-12-05`
- **title dates:** 1965
- **summary dates:** 1965-12-05
- **body dates (filtered):** 1965-12-05
- **confirmed date:** `1965-12-05` (via body, csv, summary)
- **summary:** This audio recording contains air to ground communications and the NASA Public Affairs audio feed with commentary, recorded during the flight of the Gemini 7 mission. In this excerpted segment of aud…

### `nasa-004-nasa-uap-d1-apollo-12-transcript-1969`
- **family:** `NASA-UAP-D1`
- **title:** NASA-UAP-D1, Apollo 12 Transcript, 1969
- **csv:** `1969` -> `1969`
- **title dates:** 1969
- **summary dates:** 1969-11
- **confirmed date:** `1969` (via csv, summary, title)
- **summary:** Apollo 12 was the fourth crewed U.S. mission to the Moon and the second to land astronauts on the lunar surface. This document is an excerpt from the Apollo 12 Technical Air-to-Ground Voice Transcrip…

### `nasa-005-nasa-uap-d2-apollo-17-transcript-1972`
- **family:** `NASA-UAP-D2`
- **title:** NASA-UAP-D2, Apollo 17 Transcript, 1972
- **csv:** `1972` -> `1972`
- **title dates:** 1972
- **summary dates:** 1972-12
- **confirmed date:** `1972` (via csv, summary, title)
- **summary:** Apollo 17 was the ninth crewed U.S. mission to the Moon, and the sixth to land astronauts on the lunar surface. This document is an excerpt from the Apollo 17 Technical Air-to-Ground Voice Transcript…

### `nasa-006-nasa-uap-d4-apollo-11-technical-crew-debriefing-1969`
- **family:** `NASA-UAP-D4`
- **title:** NASA-UAP-D4, Apollo 11 Technical Crew Debriefing, 1969
- **csv:** `1969` -> `1969`
- **title dates:** 1969
- **summary dates:** 1969-07-31
- **body dates (filtered):** 1969-07-31
- **confirmed date:** `1969-07-31` (via body, summary)
- **note:** csv `1969` disagrees
- **summary:** Apollo 11 was the third crewed mission to the Moon and the first to land Astronauts on the lunar surface. This document is an excerpt from the Apollo 11 Technical Crew Debriefing (Volumes 1 and 2) fr…

### `nasa-007-nasa-uap-d5-apollo-17-crew-debriefing-for-science-1973`
- **family:** `NASA-UAP-D5`
- **title:** NASA-UAP-D5, Apollo 17 Crew Debriefing for Science, 1973
- **csv:** `1973` -> `1973`
- **title dates:** 1973
- **summary dates:** 1973-01-08
- **body dates (filtered):** 1973-01-08
- **confirmed date:** `1973-01-08` (via body, summary)
- **note:** csv `1973` disagrees
- **summary:** Apollo 17 was the ninth crewed U.S. mission to the Moon, and the sixth to land Astronauts on the lunar surface. This document is an excerpt from the Apollo 17 Crew Debriefing for Science on January 8…

### `nasa-008-nasa-uap-d6-apollo-17-technical-crew-debriefing-1973`
- **family:** `NASA-UAP-D6`
- **title:** NASA-UAP-D6, Apollo 17 Technical Crew Debriefing, 1973
- **csv:** `1973` -> `1973`
- **title dates:** 1973
- **summary dates:** 1973-01-04
- **body dates (filtered):** 1973-01-04
- **confirmed date:** `1973-01-04` (via body, summary)
- **note:** csv `1973` disagrees
- **summary:** Apollo 17 was the ninth crewed U.S. mission to the Moon, and the sixth to land Astronauts on the lunar surface. This document is an excerpt from the Apollo 17 Technical Crew Debriefing on January 4, …

### `nasa-009-nasa-uap-d7-skylab-techincal-crew-debriefing-1973`
- **family:** `NASA-UAP-D7`
- **title:** NASA-UAP-D7, Skylab Techincal Crew Debriefing 1973
- **csv:** `1973` -> `1973`
- **title dates:** 1973
- **summary dates:** 1973-05-14; 1973-06-30; 1973-10-04; 1974-02-22
- **body dates (filtered):** 1973-06-30; 1973-10-04; 1974-02-22
- **confirmed date:** `1973-06-30` (via body, summary)
- **note:** csv `1973` disagrees
- **summary:** Launched on May 14, 1973, Skylab was the United States’ first laboratory in space. From 1973 to 1974, the station was visited by three crews. This document contains excerpts from all three crews to v…

### `nasa-010-nasa-uap-vm1-apollo-12-1969`
- **title:** NASA-UAP-VM1, Apollo 12, 1969
- **csv:** `1969` -> `1969`
- **title dates:** 1969
- **confirmed date:** `1969` (via csv, title)
- **summary:** This archival photograph depicts the lunar surface as viewed from the landing site of Apollo 12. This image features a highlighted area of interest slightly to the right of the vertical axis of the f…

### `nasa-011-nasa-uap-vm2-apollo-12-1969`
- **title:** NASA-UAP-VM2, Apollo 12, 1969
- **csv:** `1969` -> `1969`
- **title dates:** 1969
- **confirmed date:** `1969` (via csv, title)
- **summary:** This archival photograph depicts the lunar surface as viewed from the landing site of Apollo 12. This image features two highlighted areas of interest, labeled “Area 1” and “Area 2,” slightly to the …

### `nasa-012-nasa-uap-vm3-apollo-12-1969`
- **title:** NASA-UAP-VM3, Apollo 12, 1969
- **csv:** `1969` -> `1969`
- **title dates:** 1969
- **confirmed date:** `1969` (via csv, title)
- **summary:** This archival photograph depicts the lunar surface as viewed from the landing site of Apollo 12. This image features a highlighted area of interest near the right edge of the frame, above the horizon…

### `nasa-013-nasa-uap-vm4-apollo-12-1969`
- **title:** NASA-UAP-VM4, Apollo 12, 1969
- **csv:** `1969` -> `1969`
- **title dates:** 1969
- **confirmed date:** `1969` (via csv, title)
- **summary:** This archival photograph depicts the lunar surface as viewed from the landing site of Apollo 12. This image features a highlighted area of interest slightly to the left of the vertical axis of the fr…

### `nasa-014-nasa-uap-vm5-apollo-12-1969`
- **title:** NASA-UAP-VM5, Apollo 12, 1969
- **csv:** `1969` -> `1969`
- **title dates:** 1969
- **confirmed date:** `1969` (via csv, title)
- **summary:** This archival photograph depicts the lunar surface as viewed from the landing site of Apollo 12. This image features five highlighted areas of interest, labeled “Area 1” through “Area 5,” above the h…

### `nasa-015-nasa-uap-vm6-apollo-17-1972`
- **title:** NASA-UAP-VM6, Apollo 17, 1972
- **csv:** `1972` -> `1972`
- **title dates:** 1972
- **summary dates:** 1972-12
- **confirmed date:** `1972` (via csv, summary, title)
- **summary:** As part of the review of historical UAP materials under PURSUE, DOW has opened a case to investigate the accompanying NASA photograph from the Apollo 17 mission, taken December 1972. The image contai…

### `nasa-016-nasa-uap-d008-apollo-12-medical-debriefing-tape-12-1969`
- **family:** `NASA-UAP-D8`
- **title:** NASA-UAP-D008, Apollo 12 Medical Debriefing - Tape 12, 1969
- **csv:** `1969` -> `1969`
- **title dates:** 1969
- **confirmed date:** `1969` (via csv, title)
- **summary:** During a medical debriefing of the crew of the Apollo 12 mission, Commander Charles “Pete” Conrad, Command Module Pilot Richard “Dick” F. Gordon, and Lunar Module Pilot Alan L. Bean describe their ob…

### `nasa-017-nasa-uap-d009-apollo-17-audio-excerpt-december-7-1972`
- **family:** `NASA-UAP-D9`
- **title:** NASA-UAP-D009, Apollo 17 Audio Excerpt, December 7, 1972
- **csv:** `12/7/72` -> `1972-12-07`
- **title dates:** 1972-12-07
- **confirmed date:** `1972-12-07` (via csv, title)
- **summary:** During the eleventh and final crewed mission in the Apollo program, Apollo 17 Commander Gene Cernan, Lunar Module Pilot Harrison Schmitt, and Command Module Pilot Ronald Evans report seeing small lig…

### `nasa-018-nasa-uap-d010-mercury-atlas-9-audio-excerpt-may-15-1963`
- **family:** `NASA-UAP-D10`
- **title:** NASA-UAP-D010, Mercury Atlas 9 Audio Excerpt, May 15, 1963
- **csv:** `5/15/63` -> `1963-05-15`
- **title dates:** 1963-05-15
- **confirmed date:** `1963-05-15` (via csv, title)
- **summary:** Approximately one hour and 41 minutes into the final and longest flight of Project Mercury, Mercury-Atlas 9 mission (MA-9) Faith 7 Pilot L. Gordon Cooper Jr. notes that he sees “John’s fireflies,” re…

### `nasa-019-nasa-uap-d011-mercury-atlas-9-audio-excerpt-may-15-1963`
- **family:** `NASA-UAP-D11`
- **title:** NASA-UAP-D011, Mercury Atlas 9 Audio Excerpt, May 15, 1963
- **csv:** `5/15/63` -> `1963-05-15`
- **title dates:** 1963-05-15
- **confirmed date:** `1963-05-15` (via csv, title)
- **summary:** During the final and longest flight of Project Mercury, Mercury-Atlas 9 mission (MA-9) Faith 7 Pilot L. Gordon Cooper Jr. describes the brilliant blue of sunrise beneath the haze layer of the Earth’s…

### `nasa-020-nasa-uap-d012-mercury-atlas-8-audio-excerpt-october-3-1962`
- **family:** `NASA-UAP-D12`
- **title:** NASA-UAP-D012, Mercury Atlas 8 Audio Excerpt, October 3, 1962
- **csv:** `10/3/62` -> `1962-10-03`
- **title dates:** 1962-10-03
- **confirmed date:** `1962-10-03` (via csv, title)
- **summary:** During the Mercury Atlas 8 mission, Sigma 7 pilot Walter M. “Wally” Schirra Jr. describes observing “little white objects that tend to come from the capsule itself and drift off.” Schirra later also …

### `nasa-021-nasa-uap-d013-mercury-atlas-7-may-24-1962`
- **family:** `NASA-UAP-D13`
- **title:** NASA-UAP-D013, Mercury Atlas 7, May 24, 1962
- **csv:** `5/24/62` -> `1962-05-24`
- **title dates:** 1962-05-24
- **confirmed date:** `1962-05-24` (via csv, title)
- **summary:** During the fourth crewed spaceflight and second orbital flight of Project Mercury, Mercury-Atlas 7 (MA-7), Aurora 7 pilot Scott Carpenter describes white particles in view that appear to move at “ran…

### `nasa-022-nasa-uap-d014-mercury-redstone-4-july-21-1961`
- **family:** `NASA-UAP-D14`
- **title:** NASA-UAP-D014, Mercury-Redstone 4, July 21, 1961
- **csv:** `7/21/61` -> `1961-07-21`
- **title dates:** 1961-07-21
- **confirmed date:** `1961-07-21` (via csv, title)
- **summary:** During the recovery of the fourth launch and second crewed spaceflight of Project Mercury, Mercury-Redstone 4 (MR-4) Liberty Bell 7, the recovery team discusses a dye pack in the water that did not a…

### `nasa-023-nasa-uap-d015-astronaut-scientific-debriefings-1962-1963`
- **family:** `NASA-UAP-D15`
- **title:** NASA-UAP-D015, Astronaut Scientific Debriefings, 1962-1963
- **csv:** `1962-1963` -> `1962`
- **title dates:** 1962; 1963
- **body dates (filtered):** 1962-07-13; 1963-03-12; 1963-12-20; 1962-07-29; 1962-02-21; 1962-05-24; 1963-11-15
- **confirmed date:** `1962` (via body, csv, title)
- **summary:** This file contains memoranda, correspondence, reports, and other materials relating to contemporary scientific interest in investigating the nature of luminous phenomena reported by astronauts John G…

### `nasa-024-nasa-uap-d016-preliminary-gemini-4-crew-debriefing-part-i-19`
- **family:** `NASA-UAP-D16`
- **title:** NASA-UAP-D016, Preliminary Gemini 4 Crew Debriefing, Part I, 1965
- **csv:** `6/9/65` -> `1965-06-09`
- **title dates:** 1965
- **summary dates:** 1965-06-09
- **body dates (filtered):** 1965-06-09; 1965-06-23
- **confirmed date:** `1965-06-09` (via body, csv, summary)
- **summary:** This document is a preliminary transcript (Part I) derived from voice recordings of the Gemini 4 flight crew debriefing taken aboard the recovery ship, USS Wasp, on June 9, 1965. Astronaut Ed White r…

### `nasa-025-nasa-uap-d017-preliminary-gemini-4-crew-debriefing-part-ii-1`
- **family:** `NASA-UAP-D17`
- **title:** NASA-UAP-D017, Preliminary Gemini 4 Crew Debriefing, Part II, 1965
- **csv:** `6/9/65` -> `1965-06-09`
- **title dates:** 1965
- **summary dates:** 1965-06-09
- **body dates (filtered):** 1965-06-12
- **confirmed date:** `1965-06-09` (via csv, summary)
- **summary:** This document is a preliminary transcript (Part II) derived from voice recordings of the Gemini 4 flight crew debriefing taken aboard the recovery ship, USS Wasp, on June 9, 1965. Part II of this doc…

### `nasa-026-nasa-uap-d018-gemini-4-experiment-debriefing-1967`
- **family:** `NASA-UAP-D18`
- **title:** NASA-UAP-D018, Gemini 4 Experiment Debriefing, 1967
- **csv:** `June 3-7, 1965` -> `1965`
- **title dates:** 1967
- **summary dates:** 1965-06-07; 1967-06-25
- **body dates (filtered):** 1965-07-16; 1963-08-15; 1929-06-10; 1930-11-14; 1928-03-14; 1928-03-25; 1957-03-15; 1965-07-14; 1965-06-17; 1965-06-03; 1965-07-02; 1965-06-24; 1962-09; 1942-05
- **confirmed date:** `1965-06` (via body, summary)
- **note:** csv `1965` disagrees
- **summary:** Gemini IV was the second crewed mission of the Gemini series. Astronauts James McDivitt and Edward White successfully completed the four-day flight between June 3 and June 7, 1965. The mission includ…

### `nasa-027-nasa-uap-d019-gemini-5-technical-debriefing-part-i-1965`
- **family:** `NASA-UAP-D19`
- **title:** NASA-UAP-D019, Gemini 5 Technical Debriefing, Part I, 1965
- **csv:** `August 2 - September 2, 1965` -> `1965-09-02`
- **title dates:** 1965
- **summary dates:** 1965-08-30; 1965-09-02
- **body dates (filtered):** 1965-08-30; 1965-09-01; 1965-09-03
- **confirmed date:** `1965-09-02` (via csv, summary)
- **summary:** This document is a preliminary transcript (Part I) derived from voice recordings of the Gemini 5 flight crew technical debriefing. NASA conducted this debriefing between August 30, 1965, and Septembe…

### `nasa-028-nasa-uap-d020-gemini-5-technical-debriefing-part-ii-1965`
- **family:** `NASA-UAP-D20`
- **title:** NASA-UAP-D020, Gemini 5 Technical Debriefing, Part II, 1965
- **csv:** `August 30 - September 2, 1965` -> `1965-09-02`
- **title dates:** 1965
- **summary dates:** 1965-08-30; 1965-09-02
- **body dates (filtered):** 1965-09-02; 1965-08-30; 1965-09-01
- **confirmed date:** `1965-09-02` (via body, csv, summary)
- **summary:** This document is a preliminary transcript (Part II) derived from voice recordings of the Gemini 5 flight crew technical debriefing. NASA conducted this debriefing between August 30, 1965, and Septemb…

### `nasa-029-nasa-uap-d021-gemini-7-technical-debriefing-1965`
- **family:** `NASA-UAP-D21`
- **title:** NASA-UAP-D021, Gemini 7 Technical Debriefing, 1965
- **csv:** `December 19-21, 1965` -> `1965`
- **title dates:** 1965
- **body dates (filtered):** 1965-12-23
- **confirmed date:** `1965` (via body, csv, title)
- **summary:** This document is a preliminary transcript derived from voice recordings of the Gemini 7 flight crew debriefing conducted December 19-21, 1965, at the Crew Quarters, Cape Kennedy, Florida. Lights and …

### `nasa-030-nasa-uap-d022-gemini-9-debriefing-1966`
- **family:** `NASA-UAP-D22`
- **title:** NASA-UAP-D022, Gemini 9 Debriefing, 1966
- **csv:** `June 3-6, 1966` -> `1966`
- **title dates:** 1966
- **summary dates:** 1966-06-03; 1966-06-16
- **body dates (filtered):** 1966-05-27; 1966-05-31; 1966-06-10; 1966-01-19; 1966-03-31; 1966-06-02; 1964-12-21; 1957-03-15; 1966-05-20; 1966-03-04; 1966-06-21
- **confirmed date:** `1966-06` (via body, summary)
- **note:** csv `1966` disagrees
- **summary:** Gemini IX (renamed Gemini IX-A) was the seventh crewed flight of the Gemini series, launched on June 3, 1966. The mission’s primary objectives included a spacewalk and multiple scientific and medical…

### `nasa-031-nasa-uap-d023-interview-excerpt-with-astronaut-gordon-cooper`
- **family:** `NASA-UAP-D23`
- **title:** NASA-UAP-D023, Interview Excerpt with Astronaut Gordon Cooper, 1962
- **csv:** `November, 1962` -> `1962`
- **title dates:** 1962
- **summary dates:** 1962-11
- **confirmed date:** `1962` (via csv, summary, title)
- **summary:** In November 1962, journalist Walter Cronkite interviewed astronaut Gordon Cooper. In this excerpt from that interview, Cronkite asks Cooper about his views regarding the nature of unidentified flying…

### `nasa-034-nasa-uap-d030-sts-80-unidentified-object-image-1-1996`
- **family:** `NASA-UAP-D30`
- **title:** NASA-UAP-D030, STS-80 Unidentified Object Image 1, 1996
- **csv:** `1996` -> `1996`
- **title dates:** 1996
- **summary dates:** 1996-12-07
- **confirmed date:** `1996` (via csv, summary, title)
- **summary:** During STS-80, between November 19 and December 7, 1996, astronauts aboard Space Shuttle Columbia captured a series of three images of an unidentified object in low-Earth orbit. In the first photogra…

### `nasa-035-nasa-uap-d031-sts-80-unidentified-object-image-2-1996`
- **family:** `NASA-UAP-D31`
- **title:** NASA-UAP-D031, STS-80 Unidentified Object Image 2, 1996
- **csv:** `1996` -> `1996`
- **title dates:** 1996
- **summary dates:** 1996-12-07
- **confirmed date:** `1996` (via csv, summary, title)
- **summary:** During STS-80, between November 19 and December 7, 1996, astronauts aboard Space Shuttle Columbia captured a series of three images of an unidentified object in low-Earth orbit. In the second photogr…

### `nasa-036-nasa-uap-d032-sts-80-unidentified-object-image-3-1996`
- **family:** `NASA-UAP-D32`
- **title:** NASA-UAP-D032, STS-80 Unidentified Object Image 3, 1996
- **csv:** `1996` -> `1996`
- **title dates:** 1996
- **summary dates:** 1996-12-07
- **confirmed date:** `1996` (via csv, summary, title)
- **summary:** During STS-80, between November 19 and December 7, 1996, astronauts aboard Space Shuttle Columbia captured a series of three images of an unidentified object in low-Earth orbit. In the third photogra…

### `nasa-037-nasa-uap-d026-apollo-14-debriefing-1971`
- **family:** `NASA-UAP-D26`
- **title:** NASA-UAP-D026, Apollo 14 Debriefing, 1971
- **csv:** `2/18/71` -> `1971-02-18`
- **title dates:** 1971
- **confirmed date:** `1971` (via csv, title)
- **summary:** This file contains segment 1 of 2 of the Apollo 14 post-mission crew debriefing at the Manned Spacecraft Center (now Johnson Space Center), Houston, Texas. In the recording, crew members and debriefe…

### `nasa-038-nasa-uap-d027-apollo-14-debriefing-continued-1971`
- **family:** `NASA-UAP-D27`
- **title:** NASA-UAP-D027, Apollo 14 Debriefing (Continued), 1971
- **csv:** `2/18/71` -> `1971-02-18`
- **title dates:** 1971
- **confirmed date:** `1971` (via csv, title)
- **summary:** This file contains segment 2 of 2 of the Apollo 14 post-mission crew debriefing at the Manned Spacecraft Center (now Johnson Space Center), Houston, Texas. In this continued segment, crew members and…

### `nasa-039-nasa-uap-d028-apollo-17-crew-medical-debriefing-1972`
- **family:** `NASA-UAP-D28`
- **title:** NASA-UAP-D028, Apollo 17 Crew Medical Debriefing, 1972
- **csv:** `12/21/72` -> `1972-12-21`
- **title dates:** 1972
- **confirmed date:** `1972` (via csv, title)
- **summary:** This file contains segment 1 of 2 of the Apollo 17 post-mission medical debriefing at the Manned Spacecraft Center (now Johnson Space Center), Houston, Texas. In the recording, crew members discuss t…

### `nasa-040-nasa-uap-d029-apollo-17-crew-medical-debriefing-continued-19`
- **family:** `NASA-UAP-D29`
- **title:** NASA-UAP-D029, Apollo 17 Crew Medical Debriefing (Continued), 1972
- **csv:** `12/21/72` -> `1972-12-21`
- **title dates:** 1972
- **confirmed date:** `1972` (via csv, title)
- **summary:** This file contains segment 2 of 2 of the Apollo 17 post-mission medical debriefing at the Manned Spacecraft Center (now Johnson Space Center), Houston, Texas. In this continued segment, crew members …

### `state-001-59-214434-sp-16-7-18-1963`
- **title:** 59_214434_SP 16 [7.18.1963]
- **csv:** `7/18/63` -> `1963-07-18`
- **title dates:** 1963
- **summary dates:** 1963-07-18
- **body dates (filtered):** 1963-07-18
- **confirmed date:** `1963-07-18` (via body, csv, summary)
- **summary:** This memorandum, dated July 18, 1963, from the Executive Office of the President, National Aeronautics and Space Council, relates to thoughts on the space alien race question. Included are details re…

### `state-002-59-64634-711-5612-7-2852`
- **title:** 59_64634_711.5612[7-2852
- **csv:** `7/18/52` -> `1952-07-18`
- **summary dates:** 1952-07-18
- **body dates (filtered):** 1963-07-18
- **confirmed date:** `1952-07-18` (via csv, summary)
- **summary:** This two page memorandum, dated July 18, 1952, relates to increased reports of unidentified flying objects (UFOs). Included in the record are possible explanations of increased sightings, such as tec…

### `state-003-state-department-uap-cable-1-papua-new-guinea-january-28-198`
- **family:** `State-Cable1`
- **title:** State Department UAP Cable 1, Papua New Guinea, January 28, 1985
- **csv:** `1/24/85` -> `1985-01-24`
- **title dates:** 1985-01-28
- **summary dates:** 1985-01-28; 1985-01-24
- **body dates (filtered):** 2026-12-25; 2026-03-02; 2020-03-02; 1985-01-28
- **confirmed date:** `1985-01-28` (via body, summary, title)
- **note:** csv `1985-01-24` disagrees
- **summary:** This document is a U.S. Department of State diplomatic cable from the U.S. Embassy in Port Moresby, Papua New Guinea to USCINCPAC (United States Indo-Pacific Command) at Honolulu, HI on January 28, 1…

### `state-004-state-department-uap-cable-2-kazakhstan-january-31-1994`
- **family:** `State-Cable2`
- **title:** State Department UAP Cable 2, Kazakhstan, January 31, 1994
- **csv:** `1/27/94` -> `1994-01-27`
- **title dates:** 1994-01-31
- **summary dates:** 1994-01-31; 1994-01-27
- **body dates (filtered):** 2026-03-02; 2026-02-25; 2020-03-02
- **confirmed date:** `1994-01-27` (via csv, summary)
- **summary:** This document is a U.S. Department of State diplomatic cable from the U.S. Embassy in Dushanbe, Tajikistan to the Secretary of State in Washington, D.C. on January 31, 1994. On January 27, 1994 one T…

### `state-005-state-department-uap-cable-3-tbilisi-georgia-october-30-2001`
- **family:** `State-Cable3`
- **title:** State Department UAP Cable 3, Tbilisi, Georgia, October 30, 2001
- **csv:** `10/28/2001-10/29/2001` -> `2001-10-28`
- **title dates:** 2001-10-30
- **body dates (filtered):** 2026-02-25; 2021-10-29; 2001-10-30
- **confirmed date:** `2001-10-30` (via body, title)
- **note:** csv `2001-10-28` disagrees
- **summary:** On October 28-29, there was an incident alleged by the Georgian Foreign Ministry that Russian aircraft had violated Georgian airspace and bombed areas of the Kodori Gorge. Russians denied any of the …

### `state-006-state-department-uap-cable-4-ashgabat-turkmenistan-november`
- **family:** `State-Cable4`
- **title:** State Department UAP Cable 4, Ashgabat, Turkmenistan, November 5, 2004
- **csv:** `11/5/04` -> `2004-11-05`
- **title dates:** 2004-11-05
- **body dates (filtered):** 2026-02-25; 2004-11-12
- **confirmed date:** `2004-11-05` (via csv, title)
- **summary:** UFOlogists of Turkmenistan has gained a positive reputation as a reliable partner for the United States in Turkmenistan to the bemusement of the cable’s author in the build up of civil society organi…

### `state-007-state-department-uap-cable-5-mexico-september-16-2003`
- **family:** `State-Cable5`
- **title:** State Department UAP Cable 5, Mexico, September 16, 2003
- **csv:** `9/12/03` -> `2003-09-12`
- **title dates:** 2003-09-16
- **body dates (filtered):** 2026-02-25; 2023-09-16; 2024-06; 2024-09
- **confirmed date:** `2003-09` (via csv, title)
- **note:** csv day 12 differs from title day 16
- **summary:** On September 12, 20023 the Mexican Congress heard testimony on UAP from experts related to the debate about an Aerial Space Protection Law, which, if approved, would make Mexico the first country to …

### `state-008-59-64634-711-5612-7-2852`
- **title:** 59_64634_711.5612[7-2852
- **csv:** `7/28/52` -> `1952-07-28`
- **summary dates:** 1952-07-28
- **body dates (filtered):** 1952-07-28
- **confirmed date:** `1952-07-28` (via body, csv, summary)
- **summary:** This two page memorandum, dated July 28, 1952, relates to increased reports of unidentified flying objects (UFOs). Included in the record are possible explanations of increased sightings, such as tec…

### `usg-001-usg-uap-d001-congressional-white-house-ufo-related-constitue`
- **title:** USG-UAP-D001, Congressional, White House, UFO-related Constituent Correspondence, 1998
- **csv:** `1998` -> `1998`
- **title dates:** 1998
- **body dates (filtered):** 1998-05-18; 1998-06-24; 1998-06-18; 1998-08-03; 1998-09-04; 1998-09-10; 1998-08-22; 1998-05-17; 1998-06-26; 1998-07-15; 1998-06-04; 1998-07-06; 1998-03-16; 1998-05-28; 1998-05-13; 1998-04-23; 1965-06-03; 1976-03-05; 1965-07-01; 1965-12-04; 1976-04-12; 1969-07-19; 1976-05-10; 1973-10-18; 1970-01-29; 1997-08-10; 1963-05-15; 1962-07-17; 1962-05-11; 1998-06-09; 1969-12-17; 1997-02-14; 1969-07-21; 1970-05; 1969-06; 1992-10; 1993-10
- **confirmed date:** `1998` (via body, csv, title)
- **summary:** This collection of documents, primarily from 1998, contains draft and final correspondence from the White House and the offices of members of Congress responding to constituent inquiries about Uniden…
