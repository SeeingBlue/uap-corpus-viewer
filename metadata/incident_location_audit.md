# Incident Location audit

Records audited: **161**

Verdict counts:

- `confirmed`: 97
- `single-source`: 41
- `no-evidence`: 10
- `disagree`: 8
- `csv-vs-title`: 5

**CSV disagreements flagged:** 7

**Confirmation rules.** A location is `confirmed` when 2+ of {csv, title, summary, body} agree on a place — either by exact match or via containment (a CSV value of `Middle East` agrees with a title of `Iraq`). A location is `confirmed-by-sequence` when the record sits in a numbered family (e.g. DOW-UAP-D{N}) where prev/next neighbors agree on a location AND the current record's title or body matches them, with the CSV disagreeing.


## Disagreements (multiple sources, none corroborate) (8)

### `dow-003-331-120752-numeric-files-1944-1945-37153-german-armament-equ`
- **title:** 331_120752_Numeric_Files_1944–1945_37153_German_Armament_Equipment_Documents
- **csv:** `Germany` -> `Germany`
- **body locations (top 8):** California
- **note:** body=California; csv=Germany
- **summary:** This file contains SHAEF messages and memorandums related to "night phenomena (foofighters)," flak rockets, unidentified cylindrical objects, and blinking lights. The documents include multiple refer…

### `dow-004-341-110448-records-relating-to-the-collection-and-disseminat`
- **title:** 341_110448_Records_Relating_to_the_Collection_and_Dissemination_of_Intelligence_1948-1955-TS_CONT_No.2_2-5300-2-5399
- **csv:** `Netherlands` -> `Netherlands`
- **body locations (top 8):** Washington (state)
- **note:** body=Washington (state); csv=Netherlands
- **summary:** An Air Force intelligence report from November 1948 relating to unidentified flying objects and flying saucers.

### `dow-022-dow-uap-d3-mission-report-arabian-gulf-2020`
- **family:** `DOW-UAP-D3`
- **title:** DOW-UAP-D3, Mission Report, Arabian Gulf, 2020
- **csv:** `N/A` -> `-`
- **title locations:** Persian Gulf
- **body locations (top 8):** United States
- **note:** body=United States; title=Persian Gulf
- **summary:** This document is a Mission Report (MISREP), a standardized reporting form the U.S. Military uses to record the circumstances surrounding its operations. U.S. military services often use MISREPs to re…

### `dow-075-dow-uap-pr43-unresolved-uap-report-africa-2025`
- **family:** `DOW-UAP-PR43`
- **title:** DOW-UAP-PR43, Unresolved UAP Report, Africa, 2025
- **csv:** `Djibouti` -> `Djibouti`
- **summary locations:** United States
- **note:** csv=Djibouti; summary=United States
- **summary:** The United States Africa Command submitted a report of an unidentified anomalous phenomenon to the All-domain Anomaly Resolution Office (AARO) consisting of two seconds of video footage from an infra…

### `fbi-013-65-hs1-834228961-62-hq-83894-serial-403`
- **family:** `FBI-Serial403`
- **title:** 65_HS1-834228961_62-HQ-83894_Serial_403
- **csv:** `N/A` -> `-`
- **summary locations:** Oak Ridge, TN
- **body locations (top 8):** New York
- **note:** body=New York; summary=Oak Ridge, TN
- **summary:** The FBI's 62-HQ-83894 case file includes investigative records, eyewitness testimonies, and public reports concerning Unidentified Flying Objects and flying discs documented between June 1947 and Jul…

### `fbi-014-65-hs1-834228961-62-hq-83894-serial-438`
- **family:** `FBI-Serial438`
- **title:** 65_HS1-834228961_62-HQ-83894_Serial_438
- **csv:** `N/A` -> `-`
- **summary locations:** Oak Ridge, TN
- **body locations (top 8):** New Mexico; Mexico; Jordan
- **note:** body=Jordan; body=Mexico; body=New Mexico; summary=Oak Ridge, TN
- **summary:** The FBI's 62-HQ-83894 case file includes investigative records, eyewitness testimonies, and public reports concerning Unidentified Flying Objects and flying discs documented between June 1947 and Jul…

### `nasa-002-nasa-uap-d3-gemini-7-transcript-1965`
- **family:** `NASA-UAP-D3`
- **title:** NASA-UAP-D3, Gemini 7 Transcript, 1965
- **csv:** `Low Earth Orbit` -> `Low Earth Orbit`
- **summary locations:** Texas
- **note:** csv=Low Earth Orbit; summary=Texas
- **summary:** Gemini 7 was the tenth crewed American spaceflight. This document is a transcript of communications between the flight crew, Astronauts James “Jim” Lovell and Frank Borman, and the Manned Flight Cent…

### `nasa-007-nasa-uap-d5-apollo-17-crew-debriefing-for-science-1973`
- **family:** `NASA-UAP-D5`
- **title:** NASA-UAP-D5, Apollo 17 Crew Debriefing for Science, 1973
- **csv:** `N/A` -> `-`
- **summary locations:** Moon
- **body locations (top 8):** Texas
- **note:** body=Texas; summary=Moon
- **summary:** Apollo 17 was the ninth crewed U.S. mission to the Moon, and the sixth to land Astronauts on the lunar surface. This document is an excerpt from the Apollo 17 Crew Debriefing for Science on January 8…


## Single-source (no corroboration) (41)

### `dow-001-18-100754-general-1946-7-vol-2`
- **title:** 18_100754_ General 1946-7_Vol_2
- **csv:** `N/A` -> `-`
- **body locations (top 8):** Washington (state); California; United States; Spain; Germany; North America; New Mexico; Mexico
- **confirmed location:** `Washington (state)` (via body)
- **summary:** This file contains memorandums and correspondence related to flying disc/saucer sightings and that those are a matter of concern for the Air Materiel Command.

### `dow-002-18-6369445-general-1948-vol-1`
- **title:** 18_6369445_General_1948_Vol_1
- **csv:** `N/A` -> `-`
- **body locations (top 8):** Washington (state); Wright-Patterson AFB; New York; United States; Florida; California; Pacific Ocean; Texas
- **confirmed location:** `Washington (state)` (via body)
- **summary:** This file contains memorandums, correspondence, and forms related to the reporting of information on flying discs and investigations into sightings.

### `dow-005-341-110677-numerical-file-5-2500`
- **title:** 341_110677_Numerical_File,_5-2500
- **csv:** `Azerbaijan` -> `Azerbaijan`
- **confirmed location:** `Azerbaijan` (via csv)
- **summary:** Air Intelligence Information Report, 14 October 1955, Report of eye witness account of the ascent and flight of a unconventional aircraft in the trans-Caucasus region on the USSR.

### `dow-007-38-143685-box-incident-summaries-101-172`
- **title:** 38_143685_box_Incident_Summaries_101-172
- **csv:** `N/A` -> `-`
- **body locations (top 8):** Moon; United Kingdom; California; Pacific Ocean; New Mexico; Mexico; Jordan; United States
- **confirmed location:** `United Kingdom` (via body)
- **summary:** Each of these incident summaries includes a "Check-List - Unidentified Flying Objects" that contains details about the incident. Many summaries also include witness lists or statements and other narr…

### `dow-008-38-143685-box-incident-summaries-173-233`
- **title:** 38_143685_box_Incident_Summaries_173-233
- **csv:** `N/A` -> `-`
- **body locations (top 8):** Mexico; Florida; Moon; Wright-Patterson AFB; Germany; Texas; Washington (state); Andrews AFB
- **confirmed location:** `Mexico` (via body)
- **summary:** Each of these incident summaries includes a "Check-List - Unidentified Flying Objects" that contains details about the incident. Many summaries also include witness lists or statements and other narr…

### `dow-009-38-143685-box7-incident-summaries-1-100`
- **title:** 38_143685_box7_Incident_Summaries_1-100
- **csv:** `N/A` -> `-`
- **body locations (top 8):** California; Florida; Moon; Washington (state); Arizona; New Mexico; Nevada; Texas
- **confirmed location:** `California` (via body)
- **summary:** Each of these incident summaries includes a "Check-List - Unidentified Flying Objects" that contains details about the incident. Many summaries also include witness lists or statements and other narr…

### `dow-029-dow-uap-d4-mission-report-arabian-gulf-2020`
- **family:** `DOW-UAP-D4`
- **title:** DOW-UAP-D4, Mission Report, Arabian Gulf, 2020
- **csv:** `N/A` -> `-`
- **title locations:** Persian Gulf
- **confirmed location:** `Persian Gulf` (via title)
- **summary:** This document is a Mission Report (MISREP), a standardized reporting form the U.S. Military uses to record the circumstances surrounding its operations. U.S. military services often use MISREPs to re…

### `dow-032-dow-uap-d48-department-of-the-air-force-report-1996`
- **family:** `DOW-UAP-D48`
- **title:** DOW-UAP-D48, Department of the Air Force Report, 1996
- **csv:** `N/A` -> `-`
- **body locations (top 8):** Florida; Vandenberg AFB; California; Washington (state); Atlantic Ocean; New Mexico; Moon; Japan
- **confirmed location:** `Florida` (via body)
- **summary:** This report describes the Modeling of Unlikely Space-Booster Failures in Risk Calculations, documenting historical launch failure modes and recommending corrective actions to address them using novel…

### `dow-050-dow-uap-d7-mission-report-arabian-gulf-2020`
- **family:** `DOW-UAP-D7`
- **title:** DOW-UAP-D7, Mission Report, Arabian Gulf, 2020
- **csv:** `N/A` -> `-`
- **title locations:** Persian Gulf
- **confirmed location:** `Persian Gulf` (via title)
- **summary:** This document is a Mission Report (MISREP), a standardized reporting form the U.S. Military uses to record the circumstances surrounding its operations. U.S. military services often use MISREPs to re…

### `dow-081-dow-uap-pr49-unresolved-uap-report-department-of-the-army-20`
- **family:** `DOW-UAP-PR49`
- **title:** DOW-UAP-PR49, Unresolved UAP Report, Department of the Army, 2026
- **csv:** `North America` -> `North America`
- **confirmed location:** `North America` (via csv)
- **summary:** The Department of the Army submitted a report of an unidentified anomalous phenomenon to the All-domain Anomaly Resolution Office (AARO) consisting of one minute and 49 seconds of video from an infra…

### `fbi-029-fbi-photo-b1`
- **title:** FBI Photo B1
- **csv:** `Western United States` -> `Western United States`
- **confirmed location:** `Western United States` (via csv)
- **summary:** The Federal Bureau of Investigation (FBI) submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of a still image derived from …

### `fbi-030-fbi-photo-b10`
- **title:** FBI Photo B10
- **csv:** `Western United States` -> `Western United States`
- **confirmed location:** `Western United States` (via csv)
- **summary:** The Federal Bureau of Investigation (FBI) submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of a still image derived from …

### `fbi-031-fbi-photo-b11`
- **title:** FBI Photo B11
- **csv:** `Western United States` -> `Western United States`
- **confirmed location:** `Western United States` (via csv)
- **summary:** The Federal Bureau of Investigation (FBI) submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of a still image derived from …

### `fbi-032-fbi-photo-b12`
- **title:** FBI Photo B12
- **csv:** `Western United States` -> `Western United States`
- **confirmed location:** `Western United States` (via csv)
- **summary:** The Federal Bureau of Investigation (FBI) submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of a still image derived from …

### `fbi-033-fbi-photo-b13`
- **title:** FBI Photo B13
- **csv:** `Western United States` -> `Western United States`
- **confirmed location:** `Western United States` (via csv)
- **summary:** The Federal Bureau of Investigation (FBI) submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of a still image derived from …

### `fbi-034-fbi-photo-b14`
- **title:** FBI Photo B14
- **csv:** `Western United States` -> `Western United States`
- **confirmed location:** `Western United States` (via csv)
- **summary:** The Federal Bureau of Investigation (FBI) submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of a still image derived from …

### `fbi-035-fbi-photo-b15`
- **title:** FBI Photo B15
- **csv:** `Western United States` -> `Western United States`
- **confirmed location:** `Western United States` (via csv)
- **summary:** The Federal Bureau of Investigation (FBI) submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of a still image derived from …

### `fbi-036-fbi-photo-b16`
- **title:** FBI Photo B16
- **csv:** `Western United States` -> `Western United States`
- **confirmed location:** `Western United States` (via csv)
- **summary:** The Federal Bureau of Investigation (FBI) submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of a still image derived from …

### `fbi-037-fbi-photo-b17`
- **title:** FBI Photo B17
- **csv:** `Western United States` -> `Western United States`
- **confirmed location:** `Western United States` (via csv)
- **summary:** The Federal Bureau of Investigation (FBI) submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of a still image derived from …

### `fbi-038-fbi-photo-b18`
- **title:** FBI Photo B18
- **csv:** `Western United States` -> `Western United States`
- **confirmed location:** `Western United States` (via csv)
- **summary:** The Federal Bureau of Investigation (FBI) submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of a still image derived from …

### `fbi-039-fbi-photo-b19`
- **title:** FBI Photo B19
- **csv:** `Western United States` -> `Western United States`
- **confirmed location:** `Western United States` (via csv)
- **summary:** The Federal Bureau of Investigation (FBI) submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of a still image derived from …

### `fbi-040-fbi-photo-b2`
- **title:** FBI Photo B2
- **csv:** `Western United States` -> `Western United States`
- **confirmed location:** `Western United States` (via csv)
- **summary:** The Federal Bureau of Investigation (FBI) submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of a still image derived from …

### `fbi-041-fbi-photo-b20`
- **title:** FBI Photo B20
- **csv:** `Western United States` -> `Western United States`
- **confirmed location:** `Western United States` (via csv)
- **summary:** The Federal Bureau of Investigation (FBI) submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of a still image derived from …

### `fbi-042-fbi-photo-b21`
- **title:** FBI Photo B21
- **csv:** `Western United States` -> `Western United States`
- **confirmed location:** `Western United States` (via csv)
- **summary:** The Federal Bureau of Investigation (FBI) submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of a still image derived from …

### `fbi-043-fbi-photo-b22`
- **title:** FBI Photo B22
- **csv:** `Western United States` -> `Western United States`
- **confirmed location:** `Western United States` (via csv)
- **summary:** The Federal Bureau of Investigation (FBI) submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of a still image derived from …

### `fbi-044-fbi-photo-b23`
- **title:** FBI Photo B23
- **csv:** `Western United States` -> `Western United States`
- **confirmed location:** `Western United States` (via csv)
- **summary:** The Federal Bureau of Investigation (FBI) submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of a still image derived from …

### `fbi-045-fbi-photo-b24`
- **title:** FBI Photo B24
- **csv:** `Western United States` -> `Western United States`
- **confirmed location:** `Western United States` (via csv)
- **summary:** The Federal Bureau of Investigation (FBI) submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of a still image derived from …

### `fbi-046-fbi-photo-b3`
- **title:** FBI Photo B3
- **csv:** `Western United States` -> `Western United States`
- **confirmed location:** `Western United States` (via csv)
- **summary:** The Federal Bureau of Investigation (FBI) submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of a still image derived from …

### `fbi-047-fbi-photo-b4`
- **title:** FBI Photo B4
- **csv:** `Western United States` -> `Western United States`
- **confirmed location:** `Western United States` (via csv)
- **summary:** The Federal Bureau of Investigation (FBI) submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of a still image derived from …

### `fbi-048-fbi-photo-b5`
- **title:** FBI Photo B5
- **csv:** `Western United States` -> `Western United States`
- **confirmed location:** `Western United States` (via csv)
- **summary:** The Federal Bureau of Investigation (FBI) submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of a still image derived from …

### `fbi-049-fbi-photo-b6`
- **title:** FBI Photo B6
- **csv:** `Western United States` -> `Western United States`
- **confirmed location:** `Western United States` (via csv)
- **summary:** The Federal Bureau of Investigation (FBI) submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of a still image derived from …

### `fbi-050-fbi-photo-b7`
- **title:** FBI Photo B7
- **csv:** `Western United States` -> `Western United States`
- **confirmed location:** `Western United States` (via csv)
- **summary:** The Federal Bureau of Investigation (FBI) submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of a still image derived from …

### `fbi-051-fbi-photo-b8`
- **title:** FBI Photo B8
- **csv:** `Western United States` -> `Western United States`
- **confirmed location:** `Western United States` (via csv)
- **summary:** The Federal Bureau of Investigation (FBI) submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of a still image derived from …

### `fbi-052-fbi-photo-b9`
- **title:** FBI Photo B9
- **csv:** `Western United States` -> `Western United States`
- **confirmed location:** `Western United States` (via csv)
- **summary:** The Federal Bureau of Investigation (FBI) submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of a still image derived from …

### `fbi-053-usper-statement-about-uap-sighting`
- **title:** USPER Statement about UAP Sighting
- **csv:** `United States` -> `United States`
- **confirmed location:** `United States` (via csv)
- **summary:** This is an FBI 302 interview conducted with a senior US intelligence official regarding his first-hand account of a UAP encounter at a US military facility. USPER relayed to FBI agents that he and ot…

### `fbi-054-fbi-september-2023-sighting-composite-sketch`
- **title:** FBI September 2023 Sighting - Composite Sketch
- **csv:** `United States` -> `United States`
- **confirmed location:** `United States` (via csv)
- **summary:** Actual site photo with FBI Lab rendered graphic overlay depicting corroborating eyewitness reports from September 2023 of an apparent ellipsoid bronze metallic object materializing out of a bright li…

### `fbi-055-fbi-september-2023-sighting-serial-3`
- **title:** FBI September 2023 Sighting - Serial 3
- **csv:** `United States` -> `United States`
- **confirmed location:** `United States` (via csv)
- **summary:** This is an FBI 302 interview conducted with a US citizen regarding their first-hand account of a UAP encounter at a US test site. USPER described an object "metallic bronze in color."

### `fbi-057-fbi-september-2023-sighting-serial-5`
- **title:** FBI September 2023 Sighting - Serial 5
- **csv:** `United States` -> `United States`
- **confirmed location:** `United States` (via csv)
- **summary:** This is an FBI 302 interview conducted with a US citizen regarding their first-hand account of a UAP encounter at a US test site. USPER described a "bright light over the horizon."

### `nasa-001-255-413270-ufo-s-and-defense-what-should-we-prepare-for`
- **title:** 255_413270_UFO's_and_Defense_What_Should_we_Prepare_For
- **csv:** `N/A` -> `-`
- **body locations (top 8):** California; France; United Kingdom; United States; Mexico; Texas; Moon; Russia
- **confirmed location:** `California` (via body)
- **summary:** This file contains an independent report on UFOs written by the French association COMETA (previously published in the French magazine VDS in 1999), which details the results of a study by the Instit…

### `state-001-59-214434-sp-16-7-18-1963`
- **title:** 59_214434_SP 16 [7.18.1963]
- **csv:** `N/A` -> `-`
- **body locations (top 8):** Washington (state); Moon
- **confirmed location:** `Washington (state)` (via body)
- **summary:** This memorandum, dated July 18, 1963, from the Executive Office of the President, National Aeronautics and Space Council, relates to thoughts on the space alien race question. Included are details re…

### `state-002-59-64634-711-5612-7-2852`
- **title:** 59_64634_711.5612[7-2852
- **csv:** `N/A` -> `-`
- **body locations (top 8):** Washington (state); Moon
- **confirmed location:** `Washington (state)` (via body)
- **summary:** This two page memorandum, dated July 18, 1952, relates to increased reports of unidentified flying objects (UFOs). Included in the record are possible explanations of increased sightings, such as tec…


## No evidence anywhere (10)

### `dow-037-dow-uap-d52-email-correspondance-na-august-2024`
- **family:** `DOW-UAP-D52`
- **title:** DOW-UAP-D52, Email Correspondance, NA, August 2024
- **csv:** `N/A` -> `-`
- **summary:** This document is email correspondence describing the content of a mission report and requesting clarification on its content. All descriptive and estimative language contained in this report reflects…

### `dow-042-dow-uap-d58-range-fouler-debrief-na-october-2020`
- **family:** `DOW-UAP-D58`
- **title:** DOW-UAP-D58, Range Fouler Debrief, NA, October 2020
- **csv:** `N/A` -> `-`
- **summary:** This document is a Range Fouler Debrief, a standardized reporting form the U.S. Navy uses to record the circumstances surrounding an unauthorized intrusion into controlled airspace during active mili…

### `fbi-021-fbi-photo-a1`
- **title:** FBI Photo A1
- **csv:** `N/A` -> `-`
- **summary:** The Federal Bureau of Investigation (FBI) submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of a still image derived from …

### `fbi-022-fbi-photo-a2`
- **title:** FBI Photo A2
- **csv:** `N/A` -> `-`
- **summary:** The Federal Bureau of Investigation (FBI) submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of a still image derived from …

### `fbi-023-fbi-photo-a3`
- **title:** FBI Photo A3
- **csv:** `N/A` -> `-`
- **summary:** The Federal Bureau of Investigation (FBI) submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of a still image derived from …

### `fbi-024-fbi-photo-a4`
- **title:** FBI Photo A4
- **csv:** `N/A` -> `-`
- **summary:** The Federal Bureau of Investigation (FBI) submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of a still image derived from …

### `fbi-025-fbi-photo-a5`
- **title:** FBI Photo A5
- **csv:** `N/A` -> `-`
- **summary:** The Federal Bureau of Investigation (FBI) submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of a still image derived from …

### `fbi-026-fbi-photo-a6`
- **title:** FBI Photo A6
- **csv:** `N/A` -> `-`
- **summary:** The Federal Bureau of Investigation (FBI) submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of a still image derived from …

### `fbi-027-fbi-photo-a7`
- **title:** FBI Photo A7
- **csv:** `N/A` -> `-`
- **summary:** The Federal Bureau of Investigation (FBI) submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of a still image derived from …

### `fbi-028-fbi-photo-a8`
- **title:** FBI Photo A8
- **csv:** `N/A` -> `-`
- **summary:** The Federal Bureau of Investigation (FBI) submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of a still image derived from …


## Confirmed (>=2 sources agree) (97)

### `dow-006-342-hs1-416511228-319-1-flying-discs-1949`
- **title:** 342_HS1-416511228_319.1 Flying Discs 1949
- **csv:** `N/A` -> `-`
- **summary locations:** Japan
- **body locations (top 8):** Wright-Patterson AFB; Florida; Washington (state); Oman; California; Moon; Texas; United States
- **confirmed location:** `Japan` (via body, summary)
- **summary:** This file primarily contains incident reports on Unidentified Flying Objects (UFOs) written in compliance with the 1948 Flight Service Regulation (FSR) 200-4. The incidents were witnessed by military…

### `dow-010-dow-uap-d10-mission-report-middle-east-may-2022`
- **family:** `DOW-UAP-D10`
- **title:** DOW-UAP-D10, Mission Report, Middle East, May 2022
- **csv:** `Iraq` -> `Iraq`
- **title locations:** Middle East
- **body locations (top 8):** United States
- **confirmed location:** `Iraq` (via csv, title)
- **summary:** This document is a Mission Report (MISREP), a standardized reporting form the U.S. Military uses to record the circumstances surrounding its operations. U.S. military services often use MISREPs to re…

### `dow-011-dow-uap-d12-mission-report-iraq-may-2022`
- **family:** `DOW-UAP-D12`
- **title:** DOW-UAP-D12, Mission Report, Iraq, May 2022
- **csv:** `Iraq` -> `Iraq`
- **title locations:** Iraq
- **body locations (top 8):** United States
- **confirmed location:** `Iraq` (via csv, title)
- **summary:** This document is a Mission Report (MISREP), a standardized reporting form the U.S. Military uses to record the circumstances surrounding its operations. U.S. military services often use MISREPs to re…

### `dow-012-dow-uap-d14-mission-report-iraq-may-2022`
- **family:** `DOW-UAP-D14`
- **title:** DOW-UAP-D14, Mission Report, Iraq, May 2022
- **csv:** `Syria` -> `Syria`
- **title locations:** Iraq
- **body locations (top 8):** Mediterranean Sea; United States; Israel; Lebanon; Syria; Florida; New Mexico
- **confirmed location:** `Syria` (via body, csv)
- **summary:** This document is a Mission Report (MISREP), a standardized reporting form the U.S. Military uses to record the circumstances surrounding its operations. U.S. military services often use MISREPs to re…

### `dow-013-dow-uap-d16-mission-report-syria-july-2022`
- **family:** `DOW-UAP-D16`
- **title:** DOW-UAP-D16, Mission Report, Syria, July 2022
- **csv:** `Syria` -> `Syria`
- **title locations:** Syria
- **body locations (top 8):** United States; Arizona; Florida
- **confirmed location:** `Syria` (via csv, title)
- **summary:** This document is a Mission Report (MISREP), a standardized reporting form the U.S. Military uses to record the circumstances surrounding its operations. U.S. military services often use MISREPs to re…

### `dow-014-dow-uap-d18-mission-report-iraq-december-2022`
- **family:** `DOW-UAP-D18`
- **title:** DOW-UAP-D18, Mission Report, Iraq, December 2022
- **csv:** `Iraq` -> `Iraq`
- **title locations:** Iraq
- **body locations (top 8):** Iraq; United States
- **confirmed location:** `Iraq` (via body, csv, title)
- **summary:** This document is a Mission Report (MISREP), a standardized reporting form the U.S. Military uses to record the circumstances surrounding its operations. U.S. military services often use MISREPs to re…

### `dow-015-dow-uap-d19-mission-report-syria-february-21-2023`
- **family:** `DOW-UAP-D19`
- **title:** DOW-UAP-D19, Mission Report, Syria, February 21, 2023
- **csv:** `Syria` -> `Syria`
- **title locations:** Syria
- **body locations (top 8):** Florida; United States; Turkey
- **confirmed location:** `Syria` (via csv, title)
- **summary:** This document is a Mission Report (MISREP), a standardized reporting form the U.S. Military uses to record the circumstances surrounding its operations. U.S. military services often use MISREPs to re…

### `dow-016-dow-uap-d20-mission-report-iraq-2023`
- **family:** `DOW-UAP-D20`
- **title:** DOW-UAP-D20, Mission Report, Iraq, 2023
- **csv:** `Iraq` -> `Iraq`
- **title locations:** Iraq
- **body locations (top 8):** United States
- **confirmed location:** `Iraq` (via csv, title)
- **summary:** This document is a Mission Report (MISREP), a standardized reporting form the U.S. Military uses to record the circumstances surrounding its operations. U.S. military services often use MISREPs to re…

### `dow-017-dow-uap-d23-mission-report-united-arab-emirates-october-2023`
- **family:** `DOW-UAP-D23`
- **title:** DOW-UAP-D23, Mission Report, United Arab Emirates, October 2023
- **csv:** `Persian Gulf` -> `Persian Gulf`
- **title locations:** United Arab Emirates
- **body locations (top 8):** United States
- **confirmed location:** `United Arab Emirates` (via csv, title)
- **summary:** This document is a Mission Report (MISREP), a standardized reporting form the U.S. Military uses to record the circumstances surrounding its operations. U.S. military services often use MISREPs to re…

### `dow-018-dow-uap-d23-mission-report-united-arab-emirates-october-2023`
- **family:** `DOW-UAP-D23`
- **title:** DOW-UAP-D23, Mission Report, United Arab Emirates, October 2023
- **csv:** `Persian Gulf` -> `Persian Gulf`
- **title locations:** United Arab Emirates
- **body locations (top 8):** United States
- **confirmed location:** `United Arab Emirates` (via csv, title)
- **summary:** This document is a Mission Report (MISREP), a standardized reporting form the U.S. Military uses to record the circumstances surrounding its operations. U.S. military services often use MISREPs to re…

### `dow-019-dow-uap-d25-mission-report-greece-january-2024`
- **family:** `DOW-UAP-D25`
- **title:** DOW-UAP-D25, Mission Report, Greece, January 2024
- **csv:** `Mediterranean Sea` -> `Mediterranean Sea`
- **title locations:** Greece
- **body locations (top 8):** United States; CENTCOM
- **confirmed location:** `Greece` (via csv, title)
- **summary:** This document is a Mission Report (MISREP), a standardized reporting form the U.S. Military uses to record the circumstances surrounding its operations. U.S. military services often use MISREPs to re…

### `dow-020-dow-uap-d27-mission-report-united-arab-emirates-october-2023`
- **family:** `DOW-UAP-D27`
- **title:** DOW-UAP-D27, Mission Report, United Arab Emirates, October 2023
- **csv:** `Gulf of Oman` -> `Oman`
- **title locations:** United Arab Emirates
- **body locations (top 8):** United States; CENTCOM
- **confirmed location:** `Oman` (via body, csv)
- **summary:** This document is a Mission Report (MISREP), a standardized reporting form the U.S. Military uses to record the circumstances surrounding its operations. U.S. military services often use MISREPs to re…

### `dow-021-dow-uap-d28-mission-report-iraq-september-2024`
- **family:** `DOW-UAP-D28`
- **title:** DOW-UAP-D28, Mission Report, Iraq, September 2024
- **csv:** `Iraq` -> `Iraq`
- **title locations:** Iraq
- **body locations (top 8):** United States; CENTCOM
- **confirmed location:** `Iraq` (via body, csv, title)
- **summary:** This document is a Mission Report (MISREP), a standardized reporting form the U.S. Military uses to record the circumstances surrounding its operations. U.S. military services often use MISREPs to re…

### `dow-023-dow-uap-d32-mission-report-syria-october-2024`
- **family:** `DOW-UAP-D32`
- **title:** DOW-UAP-D32, Mission Report, Syria, October 2024
- **csv:** `Syria` -> `Syria`
- **title locations:** Syria
- **body locations (top 8):** United States
- **confirmed location:** `Syria` (via csv, title)
- **summary:** This document is a Mission Report (MISREP), a standardized reporting form the U.S. Military uses to record the circumstances surrounding its operations. U.S. military services often use MISREPs to re…

### `dow-024-dow-uap-d32-mission-report-syria-october-2024`
- **family:** `DOW-UAP-D32`
- **title:** DOW-UAP-D32, Mission Report, Syria, October 2024
- **csv:** `Syria` -> `Syria`
- **title locations:** Syria
- **body locations (top 8):** United States
- **confirmed location:** `Syria` (via csv, title)
- **summary:** This document is a Mission Report (MISREP), a standardized reporting form the U.S. Military uses to record the circumstances surrounding its operations. U.S. military services often use MISREPs to re…

### `dow-025-dow-uap-d32-mission-report-syria-october-2024`
- **family:** `DOW-UAP-D32`
- **title:** DOW-UAP-D32, Mission Report, Syria, October 2024
- **csv:** `Syria` -> `Syria`
- **title locations:** Syria
- **body locations (top 8):** United States
- **confirmed location:** `Syria` (via csv, title)
- **summary:** This document is a Mission Report (MISREP), a standardized reporting form the U.S. Military uses to record the circumstances surrounding its operations. U.S. military services often use MISREPs to re…

### `dow-026-dow-uap-d33-mission-report-greece-october-2023`
- **family:** `DOW-UAP-D33`
- **title:** DOW-UAP-D33, Mission Report, Greece, October 2023
- **csv:** `Aegean Sea` -> `Aegean Sea`
- **title locations:** Greece
- **confirmed location:** `Greece` (via csv, title)
- **summary:** This document is a Mission Report (MISREP), a standardized reporting form the U.S. Military uses to record the circumstances surrounding its operations. U.S. military services often use MISREPs to re…

### `dow-027-dow-uap-d35-mission-report-greece-october-2023`
- **family:** `DOW-UAP-D35`
- **title:** DOW-UAP-D35, Mission Report, Greece, October 2023
- **csv:** `Aegean Sea` -> `Aegean Sea`
- **title locations:** Greece
- **body locations (top 8):** United States
- **confirmed location:** `Greece` (via csv, title)
- **summary:** This document is a Mission Report (MISREP), a standardized reporting form the U.S. Military uses to record the circumstances surrounding its operations. U.S. military services often use MISREPs to re…

### `dow-028-dow-uap-d38-range-fouler-debrief-middle-east-may-2020`
- **family:** `DOW-UAP-D38`
- **title:** DOW-UAP-D38, Range Fouler Debrief, Middle East, May 2020
- **csv:** `Persian Gulf` -> `Persian Gulf`
- **title locations:** Middle East
- **confirmed location:** `Persian Gulf` (via csv, title)
- **summary:** This document is a Range Fouler Debrief, a standardized reporting form the U.S. Navy uses to record the circumstances surrounding an unauthorized intrusion into controlled airspace during active mili…

### `dow-031-dow-uap-d44-range-fouler-reporting-form-gulf-of-aden-october`
- **family:** `DOW-UAP-D44`
- **title:** DOW-UAP-D44, Range Fouler Reporting Form, Gulf of Aden, October 2020
- **csv:** `Arabian Sea` -> `Arabian Sea`
- **title locations:** Gulf of Aden
- **body locations (top 8):** Gulf of Aden
- **confirmed location:** `Gulf of Aden` (via body, title)
- **summary:** This document is a Range Fouler Reporting Form, a standardized reporting form the U.S. Navy uses to record the circumstances surrounding an unauthorized intrusion into controlled airspace during acti…

### `dow-033-dow-uap-d49-launch-summary-vandenberg-afb-2000`
- **family:** `DOW-UAP-D49`
- **title:** DOW-UAP-D49, Launch Summary, Vandenberg AFB, 2000
- **csv:** `N/A` -> `-`
- **title locations:** Vandenberg AFB
- **summary locations:** Vandenberg AFB
- **body locations (top 8):** Vandenberg AFB; California; Florida; Korea; Edwards AFB; Moon; Georgia (country); United Kingdom
- **confirmed location:** `Vandenberg AFB` (via body, summary, title)
- **summary:** This report summarizes the historical record of launches occurring at Vandenberg Air Force Base between 1958 and 2000.

### `dow-035-dow-uap-d50-email-correspondence-indopacom-april-2025`
- **family:** `DOW-UAP-D50`
- **title:** DOW-UAP-D50, Email Correspondence, INDOPACOM, April 2025
- **csv:** `N/A` -> `-`
- **title locations:** Indo-PACOM
- **body locations (top 8):** Indo-PACOM
- **confirmed location:** `Indo-PACOM` (via body, title)
- **summary:** This document is email correspondence describing the content of a mission report and requesting clarification on its content. All descriptive and estimative language contained in this report reflects…

### `dow-036-dow-uap-d51-email-correspondence-pacific-time-zone-march-202`
- **family:** `DOW-UAP-D51`
- **title:** DOW-UAP-D51, Email Correspondence, Pacific Time Zone, March 2023
- **csv:** `Pacific Time Zone` -> `Pacific Ocean`
- **title locations:** Pacific Ocean; Pacific Time Zone
- **body locations (top 8):** Pacific Ocean; Pacific Time Zone
- **confirmed location:** `Pacific Ocean` (via body, csv, title)
- **summary:** This document is email correspondence describing the content of a mission report and requesting clarification on its content. All descriptive and estimative language contained in this report reflects…

### `dow-038-dow-uap-d54-mission-report-mediterranean-sea-na`
- **family:** `DOW-UAP-D54`
- **title:** DOW-UAP-D54, Mission Report, Mediterranean Sea, NA
- **csv:** `Mediterranean Sea` -> `Mediterranean Sea`
- **title locations:** Mediterranean Sea
- **confirmed location:** `Mediterranean Sea` (via csv, title)
- **summary:** This document is a Mission Report (MISREP), a standardized reporting form the U.S. Military uses to record the circumstances surrounding its operations. U.S. military services often use MISREPs to re…

### `dow-039-dow-uap-d55-mission-report-syria-november-2016`
- **family:** `DOW-UAP-D55`
- **title:** DOW-UAP-D55, Mission Report, Syria, November 2016
- **csv:** `Syria` -> `Syria`
- **title locations:** Syria
- **summary locations:** Syria
- **body locations (top 8):** New Mexico; Syria; Mediterranean Sea
- **confirmed location:** `Syria` (via body, csv, summary, title)
- **summary:** This document is a mission briefing summarizing an observation of Unidentified Anomalous Phenomena (UAP) by a U.S. military platform near Latakia, Syria. A U.S. military pilot flying a P-8A aircraft …

### `dow-040-dow-uap-d56-range-fouler-debrief-arabian-sea-august-2020`
- **family:** `DOW-UAP-D56`
- **title:** DOW-UAP-D56, Range Fouler Debrief, Arabian Sea, August 2020
- **csv:** `Arabian Sea` -> `Arabian Sea`
- **title locations:** Arabian Sea
- **summary locations:** Arabian Sea
- **body locations (top 8):** Arabian Sea
- **confirmed location:** `Arabian Sea` (via body, csv, summary, title)
- **summary:** This document is a Range Fouler Debrief Form, a standardized reporting form the U.S. Navy uses to record the circumstances surrounding an unauthorized intrusion into controlled airspace during active…

### `dow-041-dow-uap-d57-range-fouler-reporting-form-gulf-of-aden-septemb`
- **family:** `DOW-UAP-D57`
- **title:** DOW-UAP-D57, Range Fouler Reporting Form, Gulf of Aden, September 2020
- **csv:** `Gulf of Aden` -> `Gulf of Aden`
- **title locations:** Gulf of Aden
- **summary locations:** Gulf of Aden
- **body locations (top 8):** New Mexico
- **confirmed location:** `Gulf of Aden` (via csv, summary, title)
- **summary:** This document is a Range Fouler Reporting Form, a standardized reporting form the U.S. Navy uses to record the circumstances surrounding an unauthorized intrusion into controlled airspace during acti…

### `dow-044-dow-uap-d60-mission-report-persian-gulf-august-2020`
- **family:** `DOW-UAP-D60`
- **title:** DOW-UAP-D60, Mission Report, Persian Gulf, August 2020
- **csv:** `Persian Gulf` -> `Persian Gulf`
- **title locations:** Persian Gulf
- **body locations (top 8):** Persian Gulf; Strait of Hormuz; Gulf of Oman; Oman; United States; Florida
- **confirmed location:** `Persian Gulf` (via body, csv, title)
- **summary:** This document is a Mission Report (MISREP), a standardized reporting form the U.S. Military uses to record the circumstances surrounding its operations. U.S. military services often use MISREPs to re…

### `dow-045-dow-uap-d61-mission-report-persian-gulf-august-2020`
- **family:** `DOW-UAP-D61`
- **title:** DOW-UAP-D61, Mission Report, Persian Gulf, August 2020
- **csv:** `Persian Gulf` -> `Persian Gulf`
- **title locations:** Persian Gulf
- **body locations (top 8):** Strait of Hormuz; Gulf of Oman; Oman; United States; Persian Gulf
- **confirmed location:** `Persian Gulf` (via body, csv, title)
- **summary:** This document is a Mission Report (MISREP), a standardized reporting form the U.S. Military uses to record the circumstances surrounding its operations. U.S. military services often use MISREPs to re…

### `dow-046-dow-uap-d62-mission-report-strait-of-hormuz-september-2020`
- **family:** `DOW-UAP-D62`
- **title:** DOW-UAP-D62, Mission Report, Strait of Hormuz, September 2020
- **csv:** `Strait of Hormuz` -> `Strait of Hormuz`
- **title locations:** Strait of Hormuz
- **body locations (top 8):** Persian Gulf; Gulf of Oman; Oman; United States; Florida
- **confirmed location:** `Strait of Hormuz` (via csv, title)
- **summary:** This document is a Mission Report (MISREP), a standardized reporting form the U.S. Military uses to record the circumstances surrounding its operations. U.S. military services often use MISREPs to re…

### `dow-047-dow-uap-d63-mission-report-strait-of-hormuz-october-2020`
- **family:** `DOW-UAP-D63`
- **title:** DOW-UAP-D63, Mission Report, Strait of Hormuz, October 2020
- **csv:** `Strait of Hormuz` -> `Strait of Hormuz`
- **title locations:** Strait of Hormuz
- **body locations (top 8):** Persian Gulf; Strait of Hormuz; Gulf of Oman; Oman; United States; Florida
- **confirmed location:** `Strait of Hormuz` (via body, csv, title)
- **summary:** This document is a Mission Report (MISREP), a standardized reporting form the U.S. Military uses to record the circumstances surrounding its operations. U.S. military services often use MISREPs to re…

### `dow-048-dow-uap-d64-mission-report-iran-november-2020`
- **family:** `DOW-UAP-D64`
- **title:** DOW-UAP-D64, Mission Report, Iran, November 2020
- **csv:** `Iran` -> `Iran`
- **title locations:** Iran
- **body locations (top 8):** Persian Gulf; Strait of Hormuz; Gulf of Oman; Oman; United States; Florida
- **confirmed location:** `Iran` (via csv, title)
- **summary:** This document is a Mission Report (MISREP), a standardized reporting form the U.S. Military uses to record the circumstances surrounding its operations. U.S. military services often use MISREPs to re…

### `dow-049-dow-uap-d65-mission-report-persian-gulf-july-2020`
- **family:** `DOW-UAP-D65`
- **title:** DOW-UAP-D65, Mission Report, Persian Gulf, July 2020
- **csv:** `Persian Gulf` -> `Persian Gulf`
- **title locations:** Persian Gulf
- **body locations (top 8):** Strait of Hormuz; Gulf of Oman; Oman; United States; Persian Gulf; Florida
- **confirmed location:** `Persian Gulf` (via body, csv, title)
- **summary:** This document is a Mission Report (MISREP), a standardized reporting form the U.S. Military uses to record the circumstances surrounding its operations. U.S. military services often use MISREPs to re…

### `dow-051-dow-uap-d74-mission-report-syria-november-2023`
- **family:** `DOW-UAP-D74`
- **title:** DOW-UAP-D74, Mission Report, Syria, November 2023
- **csv:** `Syria` -> `Syria`
- **title locations:** Syria
- **body locations (top 8):** United States; CENTCOM
- **confirmed location:** `Syria` (via body, csv, title)
- **summary:** This document is a Mission Report (MISREP), a standardized reporting form the U.S. Military uses to record the circumstances surrounding its operations. U.S. military services often use MISREPs to re…

### `dow-052-dow-uap-d75-mission-report-gulf-of-aden-july-2024`
- **family:** `DOW-UAP-D75`
- **title:** DOW-UAP-D75, Mission Report, Gulf of Aden, July 2024
- **csv:** `Gulf of Aden` -> `Gulf of Aden`
- **title locations:** Gulf of Aden
- **body locations (top 8):** United States
- **confirmed location:** `Gulf of Aden` (via csv, title)
- **summary:** This document is a Mission Report (MISREP), a standardized reporting form the U.S. Military uses to record the circumstances surrounding its operations. U.S. military services often use MISREPs to re…

### `dow-054-dow-uap-pr19-unresolved-uap-report-middle-east-may-2022`
- **family:** `DOW-UAP-PR19`
- **title:** DOW-UAP-PR19, Unresolved UAP Report, Middle East, May 2022
- **csv:** `Middle East` -> `Middle East`
- **title locations:** Middle East
- **summary locations:** United States
- **body locations (top 8):** Middle East
- **confirmed location:** `Middle East` (via body, csv, title)
- **summary:** The United States Central Command submitted a report of an unidentified anomalous phenomenon to the All-domain Anomaly Resolution Office (AARO) consisting of five seconds of video footage from an inf…

### `dow-056-dow-uap-pr21-unresolved-uap-report-iraq-may-2022`
- **family:** `DOW-UAP-PR21`
- **title:** DOW-UAP-PR21, Unresolved UAP Report, Iraq, May 2022
- **csv:** `Iraq` -> `Iraq`
- **title locations:** Iraq
- **summary locations:** United States
- **body locations (top 8):** Iraq
- **confirmed location:** `Iraq` (via body, csv, title)
- **summary:** The United States Central Command submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of ten seconds of video footage from a…

### `dow-057-dow-uap-pr22-unresolved-uap-report-syria-july-2022`
- **family:** `DOW-UAP-PR22`
- **title:** DOW-UAP-PR22, Unresolved UAP Report, Syria, July 2022
- **csv:** `Syria` -> `Syria`
- **title locations:** Syria
- **summary locations:** United States
- **body locations (top 8):** Syria
- **confirmed location:** `Syria` (via body, csv, title)
- **summary:** The United States Central Command submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of 14 seconds of video footage from an…

### `dow-058-dow-uap-pr23-unresolved-uap-report-iraq-december-2022`
- **family:** `DOW-UAP-PR23`
- **title:** DOW-UAP-PR23, Unresolved UAP Report, Iraq, December 2022
- **csv:** `Iraq` -> `Iraq`
- **title locations:** Iraq
- **summary locations:** United States
- **body locations (top 8):** Iraq; California
- **confirmed location:** `Iraq` (via body, csv, title)
- **summary:** The United States Central Command submitted a report of an unidentified anomalous phenomenon to the All-domain Anomaly Resolution Office (AARO) consisting of ten seconds of video footage from an infr…

### `dow-059-dow-uap-pr26-unresolved-uap-report-united-arab-emirates-octo`
- **family:** `DOW-UAP-PR26`
- **title:** DOW-UAP-PR26, Unresolved UAP Report, United Arab Emirates, October 2023
- **csv:** `United Arab Emirates` -> `United Arab Emirates`
- **title locations:** United Arab Emirates
- **summary locations:** United States
- **body locations (top 8):** United Arab Emirates
- **confirmed location:** `United Arab Emirates` (via body, csv, title)
- **summary:** The United States Central Command submitted a report of an unidentified anomalous phenomenon to the All-domain Anomaly Resolution Office (AARO) consisting of 43 seconds of video footage from an infra…

### `dow-060-dow-uap-pr27-unresolved-uap-report-united-arab-emirates-octo`
- **family:** `DOW-UAP-PR27`
- **title:** DOW-UAP-PR27, Unresolved UAP Report, United Arab Emirates, October 2023
- **csv:** `United Arab Emirates` -> `United Arab Emirates`
- **title locations:** United Arab Emirates
- **summary locations:** United States
- **body locations (top 8):** United Arab Emirates
- **confirmed location:** `United Arab Emirates` (via body, csv, title)
- **summary:** The United States Central Command submitted a report of an unidentified anomalous phenomenon to the All-domain Anomaly Resolution Office (AARO) consisting of four minutes and 57 seconds of video foot…

### `dow-061-dow-uap-pr28-unresolved-uap-report-greece-january-2024`
- **family:** `DOW-UAP-PR28`
- **title:** DOW-UAP-PR28, Unresolved UAP Report, Greece, January 2024
- **csv:** `Greece` -> `Greece`
- **title locations:** Greece
- **summary locations:** United States
- **body locations (top 8):** Greece
- **confirmed location:** `Greece` (via body, csv, title)
- **summary:** The United States Central Command submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of one minute and five seconds of vide…

### `dow-062-dow-uap-pr29-unresolved-uap-report-united-arab-emirates-june`
- **family:** `DOW-UAP-PR29`
- **title:** DOW-UAP-PR29, Unresolved UAP Report, United Arab Emirates, June 2024
- **csv:** `Gulf of Oman` -> `Oman`
- **title locations:** United Arab Emirates
- **summary locations:** United States
- **body locations (top 8):** United Arab Emirates
- **confirmed location:** `United Arab Emirates` (via body, title)
- **note:** csv `Oman` disagrees
- **summary:** The United States Northern Command submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of 21 seconds of video footage from a…

### `dow-063-dow-uap-pr31-unresolved-uap-report-syria-october-2024`
- **family:** `DOW-UAP-PR31`
- **title:** DOW-UAP-PR31, Unresolved UAP Report, Syria, October 2024
- **csv:** `Syria` -> `Syria`
- **title locations:** Syria
- **summary locations:** United States
- **body locations (top 8):** Syria
- **confirmed location:** `Syria` (via body, csv, title)
- **summary:** The United States Central Command submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of five seconds of video footage from …

### `dow-064-dow-uap-pr32-unresolved-uap-report-syria-october-2024`
- **family:** `DOW-UAP-PR32`
- **title:** DOW-UAP-PR32, Unresolved UAP Report, Syria, October 2024
- **csv:** `Syria` -> `Syria`
- **title locations:** Syria
- **summary locations:** United States
- **body locations (top 8):** Syria
- **confirmed location:** `Syria` (via body, csv, title)
- **summary:** The United States Central Command submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of six seconds of video footage from a…

### `dow-065-dow-uap-pr33-unresolved-uap-report-syria-october-2024`
- **family:** `DOW-UAP-PR33`
- **title:** DOW-UAP-PR33, Unresolved UAP Report, Syria, October 2024
- **csv:** `Syria` -> `Syria`
- **title locations:** Syria
- **summary locations:** United States
- **body locations (top 8):** Syria
- **confirmed location:** `Syria` (via body, csv, title)
- **summary:** The United States Central Command submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of five seconds of video footage from …

### `dow-066-dow-uap-pr34-unresolved-uap-report-greece-october-2023`
- **family:** `DOW-UAP-PR34`
- **title:** DOW-UAP-PR34, Unresolved UAP Report, Greece, October 2023
- **csv:** `Greece` -> `Greece`
- **title locations:** Greece
- **summary locations:** United States
- **body locations (top 8):** Greece
- **confirmed location:** `Greece` (via body, csv, title)
- **summary:** The United States Central Command submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of two minutes and 57 seconds of video…

### `dow-067-dow-uap-pr35-unresolved-uap-report-greece-october-2023`
- **family:** `DOW-UAP-PR35`
- **title:** DOW-UAP-PR35, Unresolved UAP Report, Greece, October 2023
- **csv:** `Greece` -> `Greece`
- **title locations:** Greece
- **summary locations:** United States
- **body locations (top 8):** Greece
- **confirmed location:** `Greece` (via body, csv, title)
- **summary:** The United States Central Command submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of 24 seconds of video footage from an…

### `dow-068-dow-uap-pr36-unresolved-uap-report-middle-east-may-2020`
- **family:** `DOW-UAP-PR36`
- **title:** DOW-UAP-PR36, Unresolved UAP Report, Middle East, May 2020
- **csv:** `Middle East` -> `Middle East`
- **title locations:** Middle East
- **summary locations:** United States
- **body locations (top 8):** Middle East
- **confirmed location:** `Middle East` (via body, csv, title)
- **summary:** The United States Central Command submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of two minutes and 17 seconds of video…

### `dow-069-dow-uap-pr37-unresolved-uap-report-middle-east-2020`
- **family:** `DOW-UAP-PR37`
- **title:** DOW-UAP-PR37, Unresolved UAP Report, Middle East, 2020
- **csv:** `Arabian Gulf` -> `Persian Gulf`
- **title locations:** Middle East
- **summary locations:** United States
- **body locations (top 8):** Middle East
- **confirmed location:** `Persian Gulf` (via body, csv, title)
- **summary:** The United States Central Command submitted a report of an unidentified anomalous phenomenon to the All-domain Anomaly Resolution Office (AARO) consisting of nine seconds of video footage from an inf…

### `dow-070-dow-uap-pr38-unresolved-uap-report-middle-east-2013`
- **family:** `DOW-UAP-PR38`
- **title:** DOW-UAP-PR38, Unresolved UAP Report, Middle East, 2013
- **csv:** `Middle East` -> `Middle East`
- **title locations:** Middle East
- **summary locations:** United States
- **body locations (top 8):** Middle East
- **confirmed location:** `Middle East` (via body, csv, title)
- **summary:** The United States Central Command submitted a report of an unidentified anomalous phenomenon to the All-domain Anomaly Resolution Office (AARO) consisting of one minute and 46 seconds of video footag…

### `dow-071-dow-uap-pr39-unresolved-uap-report-middle-east-2020`
- **family:** `DOW-UAP-PR39`
- **title:** DOW-UAP-PR39, Unresolved UAP Report, Middle East, 2020
- **csv:** `Arabian Gulf` -> `Persian Gulf`
- **title locations:** Middle East
- **summary locations:** United States
- **body locations (top 8):** Middle East
- **confirmed location:** `Persian Gulf` (via body, csv, title)
- **summary:** The United States Central Command submitted a report of an unidentified anomalous phenomenon to the All-domain Anomaly Resolution Office (AARO) consisting of five seconds of video footage from an inf…

### `dow-072-dow-uap-pr40-unresolved-uap-report-middle-east-2020`
- **family:** `DOW-UAP-PR40`
- **title:** DOW-UAP-PR40, Unresolved UAP Report, Middle East, 2020
- **csv:** `Arabian Gulf` -> `Persian Gulf`
- **title locations:** Middle East
- **summary locations:** United States
- **body locations (top 8):** Middle East
- **confirmed location:** `Persian Gulf` (via body, csv, title)
- **summary:** The United States Central Command submitted a report of an unidentified anomalous phenomenon to the All-domain Anomaly Resolution Office (AARO) consisting of one minute and three seconds of video foo…

### `dow-073-dow-uap-pr41-unresolved-uap-report-middle-east-2020`
- **family:** `DOW-UAP-PR41`
- **title:** DOW-UAP-PR41, Unresolved UAP Report, Middle East, 2020
- **csv:** `Arabian Gulf` -> `Persian Gulf`
- **title locations:** Middle East
- **summary locations:** United States
- **body locations (top 8):** Middle East
- **confirmed location:** `Persian Gulf` (via body, csv, title)
- **summary:** The United States Central Command submitted a report of an unidentified anomalous phenomenon to the All-domain Anomaly Resolution Office (AARO) consisting of one minute and 34 seconds of video footag…

### `dow-074-dow-uap-pr42-unresolved-uap-report-middle-east-2020`
- **family:** `DOW-UAP-PR42`
- **title:** DOW-UAP-PR42, Unresolved UAP Report, Middle East, 2020
- **csv:** `Arabian Gulf` -> `Persian Gulf`
- **title locations:** Middle East
- **summary locations:** United States
- **body locations (top 8):** Middle East
- **confirmed location:** `Persian Gulf` (via body, csv, title)
- **summary:** The United States Central Command submitted a report of an unidentified anomalous phenomenon to the All-domain Anomaly Resolution Office (AARO) consisting of four minutes and 53 seconds of video foot…

### `dow-076-dow-uap-pr44-unresolved-uap-report-middle-east-2020`
- **family:** `DOW-UAP-PR44`
- **title:** DOW-UAP-PR44, Unresolved UAP Report, Middle East, 2020
- **csv:** `Arabian Gulf` -> `Persian Gulf`
- **title locations:** Middle East
- **summary locations:** United States
- **body locations (top 8):** Middle East
- **confirmed location:** `Persian Gulf` (via body, csv, title)
- **summary:** The United States Central Command submitted a report of an unidentified anomalous phenomenon (UAP) to the All-domain Anomaly Resolution Office (AARO) consisting of five minutes and 11 seconds of vide…

### `dow-077-dow-uap-pr45-unresolved-uap-report-middle-east-2020`
- **family:** `DOW-UAP-PR45`
- **title:** DOW-UAP-PR45, Unresolved UAP Report, Middle East, 2020
- **csv:** `Southern United States` -> `Southern United States`
- **title locations:** Middle East
- **body locations (top 8):** Middle East
- **confirmed location:** `Middle East` (via body, title)
- **note:** csv `Southern United States` disagrees
- **summary:** The Department of the Air Force submitted a report of an unidentified anomalous phenomenon to the All-domain Anomaly Resolution Office (AARO) consisting of 58 seconds of video footage from an infrare…

### `dow-078-dow-uap-pr46-unresolved-uap-report-indopacom-2024`
- **family:** `DOW-UAP-PR46`
- **title:** DOW-UAP-PR46, Unresolved UAP Report, INDOPACOM, 2024
- **csv:** `East China Sea` -> `East China Sea`
- **title locations:** Indo-PACOM
- **summary locations:** Pacific Ocean; United States
- **body locations (top 8):** Indo-PACOM
- **confirmed location:** `East China Sea` (via body, csv, title)
- **summary:** The United States Indo-Pacific Command submitted a report of an unidentified anomalous phenomenon to the All-domain Anomaly Resolution Office (AARO) consisting of nine seconds of video footage from a…

### `dow-079-dow-uap-pr47-unresolved-uap-report-indopacom-2023`
- **family:** `DOW-UAP-PR47`
- **title:** DOW-UAP-PR47, Unresolved UAP Report, INDOPACOM, 2023
- **csv:** `Japan` -> `Japan`
- **title locations:** Indo-PACOM
- **summary locations:** Pacific Ocean; United States
- **body locations (top 8):** Indo-PACOM
- **confirmed location:** `Japan` (via body, csv, title)
- **summary:** The United States Indo-Pacific Command submitted a report of an unidentified anomalous phenomenon to the All-domain Anomaly Resolution Office (AARO) consisting of one minute and 59 seconds of video f…

### `dow-080-dow-uap-pr48-unresolved-uap-report-indopacom-2024`
- **family:** `DOW-UAP-PR48`
- **title:** DOW-UAP-PR48, Unresolved UAP Report, INDOPACOM, 2024
- **csv:** `Indo-PACOM` -> `Indo-PACOM`
- **title locations:** Indo-PACOM
- **summary locations:** Pacific Ocean; United States
- **body locations (top 8):** Indo-PACOM
- **confirmed location:** `Pacific Ocean` (via body, csv, summary, title)
- **summary:** The United States Indo-Pacific Command submitted a report of an unidentified anomalous phenomenon to the All-domain Anomaly Resolution Office (AARO) consisting of one minute and 39 seconds of video f…

### `dow-082-western-us-event`
- **title:** Western US Event
- **csv:** `Western United States` -> `Western United States`
- **summary locations:** Western United States; United States
- **confirmed location:** `Western United States` (via csv, summary)
- **summary:** This document is a summary of statements by seven US PERSONs employed by the federal government who separately reported observing several unidentified anomalous phenomena in the western United States…

### `fbi-001-65-hs1-834228961-62-hq-83894-section-10`
- **family:** `FBI-Section10`
- **title:** 65_HS1-834228961_62-HQ-83894_Section_10
- **csv:** `N/A` -> `-`
- **summary locations:** Oak Ridge, TN
- **body locations (top 8):** Arizona; California; Nevada; Vietnam; United States; China; United Kingdom; Washington (state)
- **confirmed location:** `Oak Ridge, TN` (via body, summary)
- **summary:** The FBI's 62-HQ-83894 case file includes investigative records, eyewitness testimonies, and public reports concerning Unidentified Flying Objects and flying discs documented between June 1947 and Jul…

### `fbi-002-65-hs1-834228961-62-hq-83894-section-2`
- **family:** `FBI-Section2`
- **title:** 65_HS1-834228961_62-HQ-83894_Section_2
- **csv:** `N/A` -> `-`
- **summary locations:** Oak Ridge, TN
- **body locations (top 8):** California; Arizona; Florida; United States; Detroit, MI; New York; Utica, NY; Washington (state)
- **confirmed location:** `Oak Ridge, TN` (via body, summary)
- **summary:** The FBI's 62-HQ-83894 case file includes investigative records, eyewitness testimonies, and public reports concerning Unidentified Flying Objects and flying discs documented between June 1947 and Jul…

### `fbi-003-65-hs1-834228961-62-hq-83894-section-3`
- **family:** `FBI-Section3`
- **title:** 65_HS1-834228961_62-HQ-83894_Section_3
- **csv:** `N/A` -> `-`
- **summary locations:** Oak Ridge, TN
- **body locations (top 8):** California; Washington (state); Florida; Moon; Pacific Ocean; New Mexico; Mexico; United States
- **confirmed location:** `Oak Ridge, TN` (via body, summary)
- **summary:** The FBI's 62-HQ-83894 case file includes investigative records, eyewitness testimonies, and public reports concerning Unidentified Flying Objects and flying discs documented between June 1947 and Jul…

### `fbi-004-65-hs1-834228961-62-hq-83894-section-4`
- **family:** `FBI-Section4`
- **title:** 65_HS1-834228961_62-HQ-83894_Section_4
- **csv:** `N/A` -> `-`
- **summary locations:** Oak Ridge, TN
- **body locations (top 8):** United States; New York; Spain; Washington (state); California; Georgia (country); Wright-Patterson AFB; Arizona
- **confirmed location:** `Oak Ridge, TN` (via body, summary)
- **summary:** The FBI's 62-HQ-83894 case file includes investigative records, eyewitness testimonies, and public reports concerning Unidentified Flying Objects and flying discs documented between June 1947 and Jul…

### `fbi-005-65-hs1-834228961-62-hq-83894-section-5`
- **family:** `FBI-Section5`
- **title:** 65_HS1-834228961_62-HQ-83894_Section_5
- **csv:** `N/A` -> `-`
- **summary locations:** Oak Ridge, TN
- **body locations (top 8):** Texas; New York; United States; California; Washington (state); New Mexico; Mexico; United Arab Emirates
- **confirmed location:** `Oak Ridge, TN` (via body, summary)
- **summary:** The FBI's 62-HQ-83894 case file includes investigative records, eyewitness testimonies, and public reports concerning Unidentified Flying Objects and flying discs documented between June 1947 and Jul…

### `fbi-006-65-hs1-834228961-62-hq-83894-section-6`
- **family:** `FBI-Section6`
- **title:** 65_HS1-834228961_62-HQ-83894_Section_6
- **csv:** `N/A` -> `-`
- **summary locations:** Oak Ridge, TN
- **body locations (top 8):** United States; New Mexico; Mexico; Canada; Washington (state); California; Korea; Low Earth Orbit
- **confirmed location:** `Oak Ridge, TN` (via body, summary)
- **summary:** The FBI's 62-HQ-83894 case file includes investigative records, eyewitness testimonies, and public reports concerning Unidentified Flying Objects and flying discs documented between June 1947 and Jul…

### `fbi-007-65-hs1-834228961-62-hq-83894-section-7`
- **family:** `FBI-Section7`
- **title:** 65_HS1-834228961_62-HQ-83894_Section_7
- **csv:** `N/A` -> `-`
- **summary locations:** Oak Ridge, TN
- **body locations (top 8):** United States; Washington (state); New Mexico; New York; Germany; California; Pacific Ocean; Florida
- **confirmed location:** `Oak Ridge, TN` (via body, summary)
- **summary:** The FBI's 62-HQ-83894 case file includes investigative records, eyewitness testimonies, and public reports concerning Unidentified Flying Objects and flying discs documented between June 1947 and Jul…

### `fbi-008-65-hs1-834228961-62-hq-83894-section-9`
- **family:** `FBI-Section9`
- **title:** 65_HS1-834228961_62-HQ-83894_Section_9
- **csv:** `N/A` -> `-`
- **summary locations:** Oak Ridge, TN
- **body locations (top 8):** United States; Moon; Georgia (country); Florida; Mexico; Wright-Patterson AFB; California; Canada
- **confirmed location:** `Oak Ridge, TN` (via body, summary)
- **summary:** The FBI's 62-HQ-83894 case file includes investigative records, eyewitness testimonies, and public reports concerning Unidentified Flying Objects and flying discs documented between June 1947 and Jul…

### `fbi-009-65-hs1-834228961-62-hq-83894-serial-130`
- **family:** `FBI-Serial130`
- **title:** 65_HS1-834228961_62-HQ-83894_Serial_130
- **csv:** `N/A` -> `-`
- **summary locations:** Oak Ridge, TN
- **body locations (top 8):** New York; Florida; Atlantic Ocean; California; United States; Western United States; Washington (state); Texas
- **confirmed location:** `Oak Ridge, TN` (via body, summary)
- **summary:** The FBI's 62-HQ-83894 case file includes investigative records, eyewitness testimonies, and public reports concerning Unidentified Flying Objects and flying discs documented between June 1947 and Jul…

### `fbi-010-65-hs1-834228961-62-hq-83894-serial-153`
- **family:** `FBI-Serial153`
- **title:** 65_HS1-834228961_62-HQ-83894_Serial_153
- **csv:** `N/A` -> `-`
- **summary locations:** Oak Ridge, TN
- **body locations (top 8):** Oak Ridge, TN; Tennessee
- **confirmed location:** `Oak Ridge, TN` (via body, summary)
- **summary:** The FBI's 62-HQ-83894 case file includes investigative records, eyewitness testimonies, and public reports concerning Unidentified Flying Objects and flying discs documented between June 1947 and Jul…

### `fbi-011-65-hs1-834228961-62-hq-83894-serial-164`
- **family:** `FBI-Serial164`
- **title:** 65_HS1-834228961_62-HQ-83894_Serial_164
- **csv:** `N/A` -> `-`
- **summary locations:** Oak Ridge, TN
- **body locations (top 8):** United States; Washington (state); Wright-Patterson AFB
- **confirmed location:** `Oak Ridge, TN` (via body, summary)
- **summary:** The FBI's 62-HQ-83894 case file includes investigative records, eyewitness testimonies, and public reports concerning Unidentified Flying Objects and flying discs documented between June 1947 and Jul…

### `fbi-012-65-hs1-834228961-62-hq-83894-serial-220`
- **family:** `FBI-Serial220`
- **title:** 65_HS1-834228961_62-HQ-83894_Serial_220
- **csv:** `N/A` -> `-`
- **summary locations:** Oak Ridge, TN
- **body locations (top 8):** United States; North America; New York; Mexico; California
- **confirmed location:** `Oak Ridge, TN` (via body, summary)
- **summary:** The FBI's 62-HQ-83894 case file includes investigative records, eyewitness testimonies, and public reports concerning Unidentified Flying Objects and flying discs documented between June 1947 and Jul…

### `fbi-015-65-hs1-834228961-62-hq-83894-serial-449`
- **family:** `FBI-Serial449`
- **title:** 65_HS1-834228961_62-HQ-83894_Serial_449
- **csv:** `N/A` -> `-`
- **summary locations:** Oak Ridge, TN
- **body locations (top 8):** California; Vietnam; United States; China; United Kingdom; Washington (state); Mexico; Nevada
- **confirmed location:** `Oak Ridge, TN` (via body, summary)
- **summary:** The FBI's 62-HQ-83894 case file includes investigative records, eyewitness testimonies, and public reports concerning Unidentified Flying Objects and flying discs documented between June 1947 and Jul…

### `fbi-016-65-hs1-834228961-62-hq-83894-sub-a`
- **title:** 65_HS1-834228961_62-HQ-83894_SUB_A
- **csv:** `N/A` -> `-`
- **summary locations:** Oak Ridge, TN
- **body locations (top 8):** Washington (state); Moon; New York; Wright-Patterson AFB; New Mexico; United Arab Emirates; Mexico; United States
- **confirmed location:** `Oak Ridge, TN` (via body, summary)
- **summary:** The FBI's 62-HQ-83894 case file includes investigative records, eyewitness testimonies, and public reports concerning Unidentified Flying Objects and flying discs documented between June 1947 and Jul…

### `fbi-017-65-hs1-101634279-100-de-18221-serial-844`
- **title:** 65_HS1-101634279_100-DE-18221_Serial_844
- **csv:** `Detroit, MI` -> `Detroit, MI`
- **summary locations:** Detroit, MI
- **body locations (top 8):** United States; Detroit, MI
- **confirmed location:** `Detroit, MI` (via body, csv, summary)
- **summary:** An FBI memo from 1958 reporting a UFO sighting by a Detroit man who described a "circular object with a crystal-type dome," and recommending that the information be forwarded to "proper air force aut…

### `fbi-018-65-hs1-101634279-100-de-26505`
- **title:** 65_HS1-101634279_100-DE-26505
- **csv:** `Germany` -> `Germany`
- **summary locations:** Germany
- **body locations (top 8):** California; Detroit, MI; Texas; Poland; Germany; United States; New York; Wright-Patterson AFB
- **confirmed location:** `Germany` (via body, csv, summary)
- **summary:** An FBI report from 1957 detailing the interview with Wladyslaw Krasuski, who recounted seeing a large, circular, vertically-rising vehicle in 1944 Germany near a German military compound.

### `fbi-019-65-hs1-834228961-62-hq-83894-section-1`
- **family:** `FBI-Section1`
- **title:** 65_HS1-834228961_62-HQ-83894_Section_1
- **csv:** `N/A` -> `-`
- **summary locations:** Oak Ridge, TN
- **body locations (top 8):** Pacific Ocean; Arizona; California; New York; Washington (state); United States; Texas; Russia
- **confirmed location:** `Oak Ridge, TN` (via body, summary)
- **summary:** The FBI's 62-HQ-83894 case file includes investigative records, eyewitness testimonies, and public reports concerning Unidentified Flying Objects and flying discs documented between June 1947 and Jul…

### `fbi-020-65-hs1-834228961-62-hq-83894-section-8`
- **family:** `FBI-Section8`
- **title:** 65_HS1-834228961_62-HQ-83894_Section_8
- **csv:** `N/A` -> `-`
- **summary locations:** Oak Ridge, TN
- **body locations (top 8):** United Kingdom; New York; California; Nevada; Wright-Patterson AFB; Washington (state); United States; Pacific Ocean
- **confirmed location:** `Oak Ridge, TN` (via body, summary)
- **summary:** The FBI's 62-HQ-83894 case file includes investigative records, eyewitness testimonies, and public reports concerning Unidentified Flying Objects and flying discs documented between June 1947 and Jul…

### `fbi-056-fbi-september-2023-sighting-serial-4`
- **title:** FBI September 2023 Sighting - Serial 4
- **csv:** `United States` -> `United States`
- **body locations (top 8):** United States
- **confirmed location:** `United States` (via body, csv)
- **summary:** This is an FBI 302 interview conducted with a US citizen regarding their first-hand account of a UAP encounter at a US test site. USPER described an object "metallic/gray in color."

### `nasa-003-nasa-uap-d3a-gemini-7-audio-excerpt-1965`
- **family:** `NASA-UAP-D3`
- **title:** NASA-UAP-D3A, Gemini 7 Audio Excerpt, 1965
- **csv:** `Low Earth Orbit` -> `Low Earth Orbit`
- **body locations (top 8):** Low Earth Orbit
- **confirmed location:** `Low Earth Orbit` (via body, csv)
- **summary:** This audio recording contains air to ground communications and the NASA Public Affairs audio feed with commentary, recorded during the flight of the Gemini 7 mission. In this excerpted segment of aud…

### `nasa-004-nasa-uap-d1-apollo-12-transcript-1969`
- **family:** `NASA-UAP-D1`
- **title:** NASA-UAP-D1, Apollo 12 Transcript, 1969
- **csv:** `Moon` -> `Moon`
- **summary locations:** Moon
- **body locations (top 8):** Moon
- **confirmed location:** `Moon` (via body, csv, summary)
- **summary:** Apollo 12 was the fourth crewed U.S. mission to the Moon and the second to land astronauts on the lunar surface. This document is an excerpt from the Apollo 12 Technical Air-to-Ground Voice Transcrip…

### `nasa-005-nasa-uap-d2-apollo-17-transcript-1972`
- **family:** `NASA-UAP-D2`
- **title:** NASA-UAP-D2, Apollo 17 Transcript, 1972
- **csv:** `Moon` -> `Moon`
- **summary locations:** Moon
- **body locations (top 8):** Japan; Vietnam; Australia; Moon
- **confirmed location:** `Moon` (via body, csv, summary)
- **summary:** Apollo 17 was the ninth crewed U.S. mission to the Moon, and the sixth to land astronauts on the lunar surface. This document is an excerpt from the Apollo 17 Technical Air-to-Ground Voice Transcript…

### `nasa-006-nasa-uap-d4-apollo-11-technical-crew-debriefing-1969`
- **family:** `NASA-UAP-D4`
- **title:** NASA-UAP-D4, Apollo 11 Technical Crew Debriefing, 1969
- **csv:** `N/A` -> `-`
- **summary locations:** Moon
- **body locations (top 8):** United States; Moon
- **confirmed location:** `Moon` (via body, summary)
- **summary:** Apollo 11 was the third crewed mission to the Moon and the first to land Astronauts on the lunar surface. This document is an excerpt from the Apollo 11 Technical Crew Debriefing (Volumes 1 and 2) fr…

### `nasa-008-nasa-uap-d6-apollo-17-technical-crew-debriefing-1973`
- **family:** `NASA-UAP-D6`
- **title:** NASA-UAP-D6, Apollo 17 Technical Crew Debriefing, 1973
- **csv:** `N/A` -> `-`
- **summary locations:** Moon
- **body locations (top 8):** Texas; Moon
- **confirmed location:** `Moon` (via body, summary)
- **summary:** Apollo 17 was the ninth crewed U.S. mission to the Moon, and the sixth to land Astronauts on the lunar surface. This document is an excerpt from the Apollo 17 Technical Crew Debriefing on January 4, …

### `nasa-009-nasa-uap-d7-skylab-techincal-crew-debriefing-1973`
- **family:** `NASA-UAP-D7`
- **title:** NASA-UAP-D7, Skylab Techincal Crew Debriefing 1973
- **csv:** `N/A` -> `-`
- **summary locations:** United States
- **body locations (top 8):** Texas; Atlantic Ocean
- **confirmed location:** `Texas` (via body, summary)
- **summary:** Launched on May 14, 1973, Skylab was the United States’ first laboratory in space. From 1973 to 1974, the station was visited by three crews. This document contains excerpts from all three crews to v…

### `nasa-010-nasa-uap-vm1-apollo-12-1969`
- **title:** NASA-UAP-VM1, Apollo 12, 1969
- **csv:** `Moon` -> `Moon`
- **summary locations:** Moon
- **confirmed location:** `Moon` (via csv, summary)
- **summary:** This archival photograph depicts the lunar surface as viewed from the landing site of Apollo 12. This image features a highlighted area of interest slightly to the right of the vertical axis of the f…

### `nasa-011-nasa-uap-vm2-apollo-12-1969`
- **title:** NASA-UAP-VM2, Apollo 12, 1969
- **csv:** `Moon` -> `Moon`
- **summary locations:** Moon
- **confirmed location:** `Moon` (via csv, summary)
- **summary:** This archival photograph depicts the lunar surface as viewed from the landing site of Apollo 12. This image features two highlighted areas of interest, labeled “Area 1” and “Area 2,” slightly to the …

### `nasa-012-nasa-uap-vm3-apollo-12-1969`
- **title:** NASA-UAP-VM3, Apollo 12, 1969
- **csv:** `Moon` -> `Moon`
- **summary locations:** Moon
- **confirmed location:** `Moon` (via csv, summary)
- **summary:** This archival photograph depicts the lunar surface as viewed from the landing site of Apollo 12. This image features a highlighted area of interest near the right edge of the frame, above the horizon…

### `nasa-013-nasa-uap-vm4-apollo-12-1969`
- **title:** NASA-UAP-VM4, Apollo 12, 1969
- **csv:** `Moon` -> `Moon`
- **summary locations:** Moon
- **confirmed location:** `Moon` (via csv, summary)
- **summary:** This archival photograph depicts the lunar surface as viewed from the landing site of Apollo 12. This image features a highlighted area of interest slightly to the left of the vertical axis of the fr…

### `nasa-014-nasa-uap-vm5-apollo-12-1969`
- **title:** NASA-UAP-VM5, Apollo 12, 1969
- **csv:** `Moon` -> `Moon`
- **summary locations:** Moon
- **confirmed location:** `Moon` (via csv, summary)
- **summary:** This archival photograph depicts the lunar surface as viewed from the landing site of Apollo 12. This image features five highlighted areas of interest, labeled “Area 1” through “Area 5,” above the h…

### `nasa-015-nasa-uap-vm6-apollo-17-1972`
- **title:** NASA-UAP-VM6, Apollo 17, 1972
- **csv:** `Moon` -> `Moon`
- **summary locations:** Moon
- **confirmed location:** `Moon` (via csv, summary)
- **summary:** As part of the review of historical UAP materials under PURSUE, DOW has opened a case to investigate the accompanying NASA photograph from the Apollo 17 mission, taken December 1972. The image contai…

### `state-003-state-department-uap-cable-1-papua-new-guinea-january-28-198`
- **family:** `State-Cable1`
- **title:** State Department UAP Cable 1, Papua New Guinea, January 28, 1985
- **csv:** `Papua New Guinea` -> `Papua New Guinea`
- **title locations:** Papua New Guinea
- **summary locations:** Pacific Ocean; Papua New Guinea; Indo-PACOM; United States
- **body locations (top 8):** Papua New Guinea
- **confirmed location:** `Papua New Guinea` (via body, csv, summary, title)
- **summary:** This document is a U.S. Department of State diplomatic cable from the U.S. Embassy in Port Moresby, Papua New Guinea to USCINCPAC (United States Indo-Pacific Command) at Honolulu, HI on January 28, 1…

### `state-004-state-department-uap-cable-2-kazakhstan-january-31-1994`
- **family:** `State-Cable2`
- **title:** State Department UAP Cable 2, Kazakhstan, January 31, 1994
- **csv:** `Kazakhstan` -> `Kazakhstan`
- **title locations:** Kazakhstan
- **summary locations:** Kazakhstan
- **body locations (top 8):** Ashgabat; Kazakhstan
- **confirmed location:** `Kazakhstan` (via body, csv, summary, title)
- **summary:** This document is a U.S. Department of State diplomatic cable from the U.S. Embassy in Dushanbe, Tajikistan to the Secretary of State in Washington, D.C. on January 31, 1994. On January 27, 1994 one T…

### `state-005-state-department-uap-cable-3-tbilisi-georgia-october-30-2001`
- **family:** `State-Cable3`
- **title:** State Department UAP Cable 3, Tbilisi, Georgia, October 30, 2001
- **csv:** `Georgia` -> `Georgia (country)`
- **title locations:** Georgia (country)
- **body locations (top 8):** Georgia (country); New York; Russia; Florida
- **confirmed location:** `Georgia (country)` (via body, csv, title)
- **summary:** On October 28-29, there was an incident alleged by the Georgian Foreign Ministry that Russian aircraft had violated Georgian airspace and bombed areas of the Kodori Gorge. Russians denied any of the …

### `state-006-state-department-uap-cable-4-ashgabat-turkmenistan-november`
- **family:** `State-Cable4`
- **title:** State Department UAP Cable 4, Ashgabat, Turkmenistan, November 5, 2004
- **csv:** `Turkmenistan` -> `Turkmenistan`
- **title locations:** Turkmenistan; Ashgabat
- **summary locations:** Turkmenistan; United States
- **body locations (top 8):** Ashgabat; Texas; Turkmenistan; Florida
- **confirmed location:** `Turkmenistan` (via body, csv, summary, title)
- **summary:** UFOlogists of Turkmenistan has gained a positive reputation as a reliable partner for the United States in Turkmenistan to the bemusement of the cable’s author in the build up of civil society organi…

### `state-007-state-department-uap-cable-5-mexico-september-16-2003`
- **family:** `State-Cable5`
- **title:** State Department UAP Cable 5, Mexico, September 16, 2003
- **csv:** `Mexico` -> `Mexico`
- **title locations:** Mexico
- **summary locations:** Mexico
- **body locations (top 8):** Mexico; Florida
- **confirmed location:** `Mexico` (via body, csv, summary, title)
- **summary:** On September 12, 20023 the Mexican Congress heard testimony on UAP from experts related to the debate about an Aerial Space Protection Law, which, if approved, would make Mexico the first country to …
