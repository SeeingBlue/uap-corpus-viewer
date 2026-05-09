# Location Data Audit

**Reports inspected:** 161  
**Flagged for review:** 82  
**HIGH severity:** 28 · **MEDIUM:** 5 · **LOW:** 49

Method: each report's `incident_location` field was compared against (a) place names found in the report's title, (b) place names found in the description and extracted body text via a 80+-pattern regex dictionary, and (c) sibling reports in the same case-file group. Severity is heuristic — a HIGH flag means the field appears to contradict the title or body, not necessarily that the data is wrong (the underlying PDF may legitimately span many places).

---

## HIGH severity (28 reports)

### dow-004-341-110448-records-relating-to-the-collection-and-disseminat

- **Title:** 341_110448_Records_Relating_to_the_Collection_and_Dissemination_of_Intelligence_1948-1955-TS_CONT_No.2_2-5300-2-5399
- **Declared location:** `Netherlands`  ·  **Declared date:** `11/8/48`  ·  **Agency:** DoW
- **Places named in body/description:** Netherlands, Washington (state)
- ⚠ **TITLE_DATE_VS_DECLARED_DATE** — title year=1955, declared=11/8/48
- File: `extracted/dow-004-341-110448-records-relating-to-the-collection-and-disseminat.md`

### dow-010-dow-uap-d10-mission-report-middle-east-may-2022

- **Title:** DOW-UAP-D10, Mission Report, Middle East, May 2022
- **Declared location:** `Iraq`  ·  **Declared date:** `5/6/22`  ·  **Agency:** DoW
- **Places named in title:** Middle East
- **Places named in body/description:** Iraq, Middle East
- ⚠ **TITLE_BODY_DISAGREES_WITH_DECLARED** — title/body=Middle East, declared=Iraq
- File: `extracted/dow-010-dow-uap-d10-mission-report-middle-east-may-2022.md`

### dow-012-dow-uap-d14-mission-report-iraq-may-2022

- **Title:** DOW-UAP-D14, Mission Report, Iraq, May 2022
- **Declared location:** `Syria`  ·  **Declared date:** `5/29/22`  ·  **Agency:** DoW
- **Places named in title:** Iraq
- **Places named in body/description:** Iraq, Syria, Israel, Lebanon, Mediterranean Sea, New Mexico, Florida
- ⚠ **TITLE_BODY_DISAGREES_WITH_DECLARED** — title/body=Iraq, declared=Syria
- File: `extracted/dow-012-dow-uap-d14-mission-report-iraq-may-2022.md`

### dow-017-dow-uap-d23-mission-report-united-arab-emirates-october-2023

- **Title:** DOW-UAP-D23, Mission Report, United Arab Emirates, October 2023
- **Declared location:** `Persian Gulf`  ·  **Declared date:** `10/31/23`  ·  **Agency:** DoW
- **Places named in title:** United Arab Emirates
- **Places named in body/description:** United Arab Emirates, Persian Gulf
- ⚠ **TITLE_BODY_DISAGREES_WITH_DECLARED** — title/body=United Arab Emirates, declared=Persian Gulf
- File: `extracted/dow-017-dow-uap-d23-mission-report-united-arab-emirates-october-2023.md`

### dow-018-dow-uap-d23-mission-report-united-arab-emirates-october-2023

- **Title:** DOW-UAP-D23, Mission Report, United Arab Emirates, October 2023
- **Declared location:** `Persian Gulf`  ·  **Declared date:** `10/31/23`  ·  **Agency:** DoW
- **Places named in title:** United Arab Emirates
- **Places named in body/description:** United Arab Emirates, Persian Gulf
- ⚠ **TITLE_BODY_DISAGREES_WITH_DECLARED** — title/body=United Arab Emirates, declared=Persian Gulf
- File: `extracted/dow-018-dow-uap-d23-mission-report-united-arab-emirates-october-2023.md`

### dow-019-dow-uap-d25-mission-report-greece-january-2024

- **Title:** DOW-UAP-D25, Mission Report, Greece, January 2024
- **Declared location:** `Mediterranean Sea`  ·  **Declared date:** `1/25/24`  ·  **Agency:** DoW
- **Places named in title:** Greece
- **Places named in body/description:** Mediterranean Sea, Greece, CENTCOM
- ⚠ **TITLE_BODY_DISAGREES_WITH_DECLARED** — title/body=Greece, declared=Mediterranean Sea
- File: `extracted/dow-019-dow-uap-d25-mission-report-greece-january-2024.md`

### dow-020-dow-uap-d27-mission-report-united-arab-emirates-october-2023

- **Title:** DOW-UAP-D27, Mission Report, United Arab Emirates, October 2023
- **Declared location:** `Gulf of Oman`  ·  **Declared date:** `6/7/24`  ·  **Agency:** DoW
- **Places named in title:** United Arab Emirates
- **Places named in body/description:** Oman, United Arab Emirates, Gulf of Oman, CENTCOM
- ⚠ **TITLE_BODY_DISAGREES_WITH_DECLARED** — title/body=United Arab Emirates, declared=Oman
- File: `extracted/dow-020-dow-uap-d27-mission-report-united-arab-emirates-october-2023.md`

### dow-026-dow-uap-d33-mission-report-greece-october-2023

- **Title:** DOW-UAP-D33, Mission Report, Greece, October 2023
- **Declared location:** `Aegean Sea`  ·  **Declared date:** `10/27/23`  ·  **Agency:** DoW
- **Places named in title:** Greece
- **Places named in body/description:** Aegean Sea, Greece
- ⚠ **TITLE_BODY_DISAGREES_WITH_DECLARED** — title/body=Greece, declared=Aegean Sea
- File: `extracted/dow-026-dow-uap-d33-mission-report-greece-october-2023.md`

### dow-027-dow-uap-d35-mission-report-greece-october-2023

- **Title:** DOW-UAP-D35, Mission Report, Greece, October 2023
- **Declared location:** `Aegean Sea`  ·  **Declared date:** `10/29/23`  ·  **Agency:** DoW
- **Places named in title:** Greece
- **Places named in body/description:** Aegean Sea, Greece
- ⚠ **TITLE_BODY_DISAGREES_WITH_DECLARED** — title/body=Greece, declared=Aegean Sea
- File: `extracted/dow-027-dow-uap-d35-mission-report-greece-october-2023.md`

### dow-028-dow-uap-d38-range-fouler-debrief-middle-east-may-2020

- **Title:** DOW-UAP-D38, Range Fouler Debrief, Middle East, May 2020
- **Declared location:** `Persian Gulf`  ·  **Declared date:** `5/14/20`  ·  **Agency:** DoW
- **Places named in title:** Middle East
- **Places named in body/description:** Persian Gulf, Middle East
- ⚠ **TITLE_BODY_DISAGREES_WITH_DECLARED** — title/body=Middle East, declared=Persian Gulf
- File: `extracted/dow-028-dow-uap-d38-range-fouler-debrief-middle-east-may-2020.md`

### dow-030-dow-uap-d42-range-fouler-debrief-japan-2023

- **Title:** DOW-UAP-D42, Range Fouler Debrief, Japan, 2023
- **Declared location:** `Arabian Gulf`  ·  **Declared date:** `8/31/20`  ·  **Agency:** DoW
- **Places named in title:** Japan
- **Places named in body/description:** Arabian Gulf, Japan, Florida
- ⚠ **TITLE_BODY_DISAGREES_WITH_DECLARED** — title/body=Japan, declared=Arabian Gulf
- ⚠ **TITLE_DATE_VS_DECLARED_DATE** — title year=2023, declared=8/31/20
- File: `extracted/dow-030-dow-uap-d42-range-fouler-debrief-japan-2023.md`

### dow-031-dow-uap-d44-range-fouler-reporting-form-gulf-of-aden-october

- **Title:** DOW-UAP-D44, Range Fouler Reporting Form, Gulf of Aden, October 2020
- **Declared location:** `Arabian Sea`  ·  **Declared date:** `10/15/20`  ·  **Agency:** DoW
- **Places named in title:** Gulf of Aden
- **Places named in body/description:** Gulf of Aden, Arabian Sea
- ⚠ **TITLE_BODY_DISAGREES_WITH_DECLARED** — title/body=Gulf of Aden, declared=Arabian Sea
- File: `extracted/dow-031-dow-uap-d44-range-fouler-reporting-form-gulf-of-aden-october.md`

### dow-034-dow-uap-d5-mission-report-arabian-gulf-2020

- **Title:** DOW-UAP-D5, Mission Report, Arabian Gulf, 2020
- **Declared location:** `Mediterranean Sea`  ·  **Declared date:** `N/A`  ·  **Agency:** DoW
- **Places named in title:** Arabian Gulf
- **Places named in body/description:** Arabian Gulf, Mediterranean Sea
- ⚠ **TITLE_BODY_DISAGREES_WITH_DECLARED** — title/body=Arabian Gulf, declared=Mediterranean Sea
- ⚠ **DECLARED_DATE_NA_TITLE_HAS_YEAR** — title year=2020
- File: `extracted/dow-034-dow-uap-d5-mission-report-arabian-gulf-2020.md`

### dow-036-dow-uap-d51-email-correspondence-pacific-time-zone-march-202

- **Title:** DOW-UAP-D51, Email Correspondence, Pacific Time Zone, March 2023
- **Declared location:** `Pacific Time Zone`  ·  **Declared date:** `3/23/26`  ·  **Agency:** DoW
- **Places named in title:** Pacific Ocean
- **Places named in body/description:** Pacific Ocean
- ⚠ **TITLE_DATE_VS_DECLARED_DATE** — title year=2023, declared=3/23/26
- File: `extracted/dow-036-dow-uap-d51-email-correspondence-pacific-time-zone-march-202.md`

### dow-043-dow-uap-d6-mission-report-arabian-gulf-2020

- **Title:** DOW-UAP-D6, Mission Report, Arabian Gulf, 2020
- **Declared location:** `Pacific Ocean`  ·  **Declared date:** `N/A`  ·  **Agency:** DoW
- **Places named in title:** Arabian Gulf
- **Places named in body/description:** Arabian Gulf, Pacific Ocean
- ⚠ **TITLE_BODY_DISAGREES_WITH_DECLARED** — title/body=Arabian Gulf, declared=Pacific Ocean
- ⚠ **DECLARED_DATE_NA_TITLE_HAS_YEAR** — title year=2020
- File: `extracted/dow-043-dow-uap-d6-mission-report-arabian-gulf-2020.md`

### dow-053-dow-uap-d8-mission-report-djibouti-2025

- **Title:** DOW-UAP-D8, Mission Report, Djibouti, 2025
- **Declared location:** `Mediterranean Sea`  ·  **Declared date:** `N/A`  ·  **Agency:** DoW
- **Places named in title:** Djibouti
- **Places named in body/description:** Djibouti, Mediterranean Sea
- ⚠ **TITLE_BODY_DISAGREES_WITH_DECLARED** — title/body=Djibouti, declared=Mediterranean Sea
- ⚠ **DECLARED_DATE_NA_TITLE_HAS_YEAR** — title year=2025
- File: `extracted/dow-053-dow-uap-d8-mission-report-djibouti-2025.md`

### dow-055-dow-uap-pr20-unresolved-uap-report-kuwait-may-2022

- **Title:** DOW-UAP-PR20, Unresolved UAP Report, Kuwait, May 2022
- **Declared location:** `Iraq`  ·  **Declared date:** `N/A`  ·  **Agency:** DoW
- **Places named in title:** Kuwait
- **Places named in body/description:** Iraq, Kuwait
- ⚠ **TITLE_BODY_DISAGREES_WITH_DECLARED** — title/body=Kuwait, declared=Iraq
- ⚠ **DECLARED_DATE_NA_TITLE_HAS_YEAR** — title year=2022
- File: `extracted/dow-055-dow-uap-pr20-unresolved-uap-report-kuwait-may-2022.md`

### dow-062-dow-uap-pr29-unresolved-uap-report-united-arab-emirates-june

- **Title:** DOW-UAP-PR29, Unresolved UAP Report, United Arab Emirates, June 2024
- **Declared location:** `Gulf of Oman`  ·  **Declared date:** `N/A`  ·  **Agency:** DoW
- **Places named in title:** United Arab Emirates
- **Places named in body/description:** Oman, United Arab Emirates, Gulf of Oman
- ⚠ **TITLE_BODY_DISAGREES_WITH_DECLARED** — title/body=United Arab Emirates, declared=Oman
- ⚠ **DECLARED_DATE_NA_TITLE_HAS_YEAR** — title year=2024
- File: `extracted/dow-062-dow-uap-pr29-unresolved-uap-report-united-arab-emirates-june.md`

### dow-069-dow-uap-pr37-unresolved-uap-report-middle-east-2020

- **Title:** DOW-UAP-PR37, Unresolved UAP Report, Middle East, 2020
- **Declared location:** `Arabian Gulf`  ·  **Declared date:** `N/A`  ·  **Agency:** DoW
- **Places named in title:** Middle East
- **Places named in body/description:** Arabian Gulf, Middle East
- ⚠ **TITLE_BODY_DISAGREES_WITH_DECLARED** — title/body=Middle East, declared=Arabian Gulf
- ⚠ **DECLARED_DATE_NA_TITLE_HAS_YEAR** — title year=2020
- File: `extracted/dow-069-dow-uap-pr37-unresolved-uap-report-middle-east-2020.md`

### dow-071-dow-uap-pr39-unresolved-uap-report-middle-east-2020

- **Title:** DOW-UAP-PR39, Unresolved UAP Report, Middle East, 2020
- **Declared location:** `Arabian Gulf`  ·  **Declared date:** `N/A`  ·  **Agency:** DoW
- **Places named in title:** Middle East
- **Places named in body/description:** Arabian Gulf, Middle East
- ⚠ **TITLE_BODY_DISAGREES_WITH_DECLARED** — title/body=Middle East, declared=Arabian Gulf
- ⚠ **DECLARED_DATE_NA_TITLE_HAS_YEAR** — title year=2020
- File: `extracted/dow-071-dow-uap-pr39-unresolved-uap-report-middle-east-2020.md`

### dow-072-dow-uap-pr40-unresolved-uap-report-middle-east-2020

- **Title:** DOW-UAP-PR40, Unresolved UAP Report, Middle East, 2020
- **Declared location:** `Arabian Gulf`  ·  **Declared date:** `N/A`  ·  **Agency:** DoW
- **Places named in title:** Middle East
- **Places named in body/description:** Arabian Gulf, Middle East
- ⚠ **TITLE_BODY_DISAGREES_WITH_DECLARED** — title/body=Middle East, declared=Arabian Gulf
- ⚠ **DECLARED_DATE_NA_TITLE_HAS_YEAR** — title year=2020
- File: `extracted/dow-072-dow-uap-pr40-unresolved-uap-report-middle-east-2020.md`

### dow-073-dow-uap-pr41-unresolved-uap-report-middle-east-2020

- **Title:** DOW-UAP-PR41, Unresolved UAP Report, Middle East, 2020
- **Declared location:** `Arabian Gulf`  ·  **Declared date:** `N/A`  ·  **Agency:** DoW
- **Places named in title:** Middle East
- **Places named in body/description:** Arabian Gulf, Middle East
- ⚠ **TITLE_BODY_DISAGREES_WITH_DECLARED** — title/body=Middle East, declared=Arabian Gulf
- ⚠ **DECLARED_DATE_NA_TITLE_HAS_YEAR** — title year=2020
- File: `extracted/dow-073-dow-uap-pr41-unresolved-uap-report-middle-east-2020.md`

### dow-074-dow-uap-pr42-unresolved-uap-report-middle-east-2020

- **Title:** DOW-UAP-PR42, Unresolved UAP Report, Middle East, 2020
- **Declared location:** `Arabian Gulf`  ·  **Declared date:** `N/A`  ·  **Agency:** DoW
- **Places named in title:** Middle East
- **Places named in body/description:** Arabian Gulf, Middle East
- ⚠ **TITLE_BODY_DISAGREES_WITH_DECLARED** — title/body=Middle East, declared=Arabian Gulf
- ⚠ **DECLARED_DATE_NA_TITLE_HAS_YEAR** — title year=2020
- File: `extracted/dow-074-dow-uap-pr42-unresolved-uap-report-middle-east-2020.md`

### dow-076-dow-uap-pr44-unresolved-uap-report-middle-east-2020

- **Title:** DOW-UAP-PR44, Unresolved UAP Report, Middle East, 2020
- **Declared location:** `Arabian Gulf`  ·  **Declared date:** `N/A`  ·  **Agency:** DoW
- **Places named in title:** Middle East
- **Places named in body/description:** Arabian Gulf, Middle East
- ⚠ **TITLE_BODY_DISAGREES_WITH_DECLARED** — title/body=Middle East, declared=Arabian Gulf
- ⚠ **DECLARED_DATE_NA_TITLE_HAS_YEAR** — title year=2020
- File: `extracted/dow-076-dow-uap-pr44-unresolved-uap-report-middle-east-2020.md`

### dow-077-dow-uap-pr45-unresolved-uap-report-middle-east-2020

- **Title:** DOW-UAP-PR45, Unresolved UAP Report, Middle East, 2020
- **Declared location:** `Southern United States`  ·  **Declared date:** `N/A`  ·  **Agency:** DoW
- **Places named in title:** Middle East
- **Places named in body/description:** Middle East
- ⚠ **TITLE_BODY_DISAGREES_WITH_DECLARED** — title/body=Middle East, declared=Southern United States
- ⚠ **DECLARED_DATE_NA_TITLE_HAS_YEAR** — title year=2020
- File: `extracted/dow-077-dow-uap-pr45-unresolved-uap-report-middle-east-2020.md`

### dow-078-dow-uap-pr46-unresolved-uap-report-indopacom-2024

- **Title:** DOW-UAP-PR46, Unresolved UAP Report, INDOPACOM, 2024
- **Declared location:** `East China Sea`  ·  **Declared date:** `N/A`  ·  **Agency:** DoW
- **Places named in title:** Indo-PACOM
- **Places named in body/description:** East China Sea, Pacific Ocean, China, Indo-PACOM
- ⚠ **TITLE_BODY_DISAGREES_WITH_DECLARED** — title/body=Indo-PACOM, declared=East China Sea
- ⚠ **DECLARED_DATE_NA_TITLE_HAS_YEAR** — title year=2024
- File: `extracted/dow-078-dow-uap-pr46-unresolved-uap-report-indopacom-2024.md`

### dow-079-dow-uap-pr47-unresolved-uap-report-indopacom-2023

- **Title:** DOW-UAP-PR47, Unresolved UAP Report, INDOPACOM, 2023
- **Declared location:** `Japan`  ·  **Declared date:** `N/A`  ·  **Agency:** DoW
- **Places named in title:** Indo-PACOM
- **Places named in body/description:** Pacific Ocean, Japan, Indo-PACOM
- ⚠ **TITLE_BODY_DISAGREES_WITH_DECLARED** — title/body=Indo-PACOM, declared=Japan
- ⚠ **DECLARED_DATE_NA_TITLE_HAS_YEAR** — title year=2023
- File: `extracted/dow-079-dow-uap-pr47-unresolved-uap-report-indopacom-2023.md`

### state-006-state-department-uap-cable-4-ashgabat-turkmenistan-november

- **Title:** State Department UAP Cable 4, Ashgabat, Turkmenistan, November 5, 2004
- **Declared location:** `Turkmenistan`  ·  **Declared date:** `11/5/04`  ·  **Agency:** State
- **Places named in title:** Turkmenistan, Ashgabat
- **Places named in body/description:** Turkmenistan, Ashgabat, Texas, Florida
- ⚠ **TITLE_BODY_DISAGREES_WITH_DECLARED** — title/body=Ashgabat, declared=Turkmenistan
- File: `extracted/state-006-state-department-uap-cable-4-ashgabat-turkmenistan-november.md`

## MEDIUM severity (5 reports)

### dow-022-dow-uap-d3-mission-report-arabian-gulf-2020

- **Title:** DOW-UAP-D3, Mission Report, Arabian Gulf, 2020
- **Declared location:** `N/A`  ·  **Declared date:** `N/A`  ·  **Agency:** DoW
- **Places named in title:** Arabian Gulf
- **Places named in body/description:** Arabian Gulf
- ⚠ **TITLE_HAS_PLACE_DECLARED_NA** — Arabian Gulf
- ⚠ **DECLARED_NA_BUT_BODY_HAS_PLACES** — Arabian Gulf
- ⚠ **DECLARED_DATE_NA_TITLE_HAS_YEAR** — title year=2020
- File: `extracted/dow-022-dow-uap-d3-mission-report-arabian-gulf-2020.md`

### dow-029-dow-uap-d4-mission-report-arabian-gulf-2020

- **Title:** DOW-UAP-D4, Mission Report, Arabian Gulf, 2020
- **Declared location:** `N/A`  ·  **Declared date:** `N/A`  ·  **Agency:** DoW
- **Places named in title:** Arabian Gulf
- **Places named in body/description:** Arabian Gulf
- ⚠ **TITLE_HAS_PLACE_DECLARED_NA** — Arabian Gulf
- ⚠ **DECLARED_NA_BUT_BODY_HAS_PLACES** — Arabian Gulf
- ⚠ **DECLARED_DATE_NA_TITLE_HAS_YEAR** — title year=2020
- File: `extracted/dow-029-dow-uap-d4-mission-report-arabian-gulf-2020.md`

### dow-033-dow-uap-d49-launch-summary-vandenberg-afb-2000

- **Title:** DOW-UAP-D49, Launch Summary, Vandenberg AFB, 2000
- **Declared location:** `N/A`  ·  **Declared date:** `2/3/00`  ·  **Agency:** DoW
- **Places named in title:** Vandenberg AFB
- **Places named in body/description:** United Kingdom, Korea, Georgia (country), Vandenberg AFB, Edwards AFB, California, Florida, Moon
- ⚠ **TITLE_HAS_PLACE_DECLARED_NA** — Vandenberg AFB
- ⚠ **DECLARED_NA_BUT_BODY_HAS_PLACES** — United Kingdom, Korea, Georgia (country), Vandenberg AFB, Edwards AFB
- File: `extracted/dow-033-dow-uap-d49-launch-summary-vandenberg-afb-2000.md`

### dow-035-dow-uap-d50-email-correspondence-indopacom-april-2025

- **Title:** DOW-UAP-D50, Email Correspondence, INDOPACOM, April 2025
- **Declared location:** `N/A`  ·  **Declared date:** `4/10/2025-4/11/2025`  ·  **Agency:** DoW
- **Places named in title:** Indo-PACOM
- **Places named in body/description:** Indo-PACOM
- ⚠ **TITLE_HAS_PLACE_DECLARED_NA** — Indo-PACOM
- File: `extracted/dow-035-dow-uap-d50-email-correspondence-indopacom-april-2025.md`

### dow-050-dow-uap-d7-mission-report-arabian-gulf-2020

- **Title:** DOW-UAP-D7, Mission Report, Arabian Gulf, 2020
- **Declared location:** `N/A`  ·  **Declared date:** `N/A`  ·  **Agency:** DoW
- **Places named in title:** Arabian Gulf
- **Places named in body/description:** Arabian Gulf
- ⚠ **TITLE_HAS_PLACE_DECLARED_NA** — Arabian Gulf
- ⚠ **DECLARED_NA_BUT_BODY_HAS_PLACES** — Arabian Gulf
- ⚠ **DECLARED_DATE_NA_TITLE_HAS_YEAR** — title year=2020
- File: `extracted/dow-050-dow-uap-d7-mission-report-arabian-gulf-2020.md`

## LOW severity (49 reports)

### dow-001-18-100754-general-1946-7-vol-2

- **Title:** 18_100754_ General 1946-7_Vol_2
- **Declared location:** `N/A`  ·  **Declared date:** `12/30/47`  ·  **Agency:** DoW
- **Places named in body/description:** Germany, Spain, Mexico, California, New Mexico, Washington (state), North America
- ⚠ **DECLARED_NA_BUT_BODY_HAS_PLACES** — Germany, Spain, Mexico, California, New Mexico
- File: `extracted/dow-001-18-100754-general-1946-7-vol-2.md`

### dow-002-18-6369445-general-1948-vol-1

- **Title:** 18_6369445_General_1948_Vol_1
- **Declared location:** `N/A`  ·  **Declared date:** `6/15/48`  ·  **Agency:** DoW
- **Places named in body/description:** Pacific Ocean, Canada, Wright-Patterson AFB, Texas, California, Florida, New York, Washington (state)
- ⚠ **DECLARED_NA_BUT_BODY_HAS_PLACES** — Canada, Wright-Patterson AFB, Texas, California, Florida
- File: `extracted/dow-002-18-6369445-general-1948-vol-1.md`

### dow-006-342-hs1-416511228-319-1-flying-discs-1949

- **Title:** 342_HS1-416511228_319.1 Flying Discs 1949
- **Declared location:** `N/A`  ·  **Declared date:** `1/9/50`  ·  **Agency:** DoW
- **Places named in body/description:** Oman, Pacific Ocean, Japan, China, Canada, Wright-Patterson AFB, Texas, California (+4 more)
- ⚠ **DECLARED_NA_BUT_BODY_HAS_PLACES** — Oman, Japan, China, Canada, Wright-Patterson AFB
- File: `extracted/dow-006-342-hs1-416511228-319-1-flying-discs-1949.md`

### dow-007-38-143685-box-incident-summaries-101-172

- **Title:** 38_143685_box_Incident_Summaries_101-172
- **Declared location:** `N/A`  ·  **Declared date:** `N/A`  ·  **Agency:** DoW
- **Places named in body/description:** United Arab Emirates, Jordan, Turkey, Pacific Ocean, Atlantic Ocean, United Kingdom, Norway, Sweden (+10 more)
- ⚠ **DECLARED_NA_BUT_BODY_HAS_PLACES** — United Arab Emirates, Jordan, Turkey, United Kingdom, Norway
- File: `extracted/dow-007-38-143685-box-incident-summaries-101-172.md`

### dow-008-38-143685-box-incident-summaries-173-233

- **Title:** 38_143685_box_Incident_Summaries_173-233
- **Declared location:** `N/A`  ·  **Declared date:** `N/A`  ·  **Agency:** DoW
- **Places named in body/description:** Germany, Mexico, Wright-Patterson AFB, Andrews AFB, Texas, Arizona, New Mexico, Florida (+2 more)
- ⚠ **DECLARED_NA_BUT_BODY_HAS_PLACES** — Germany, Mexico, Wright-Patterson AFB, Andrews AFB, Texas
- File: `extracted/dow-008-38-143685-box-incident-summaries-173-233.md`

### dow-009-38-143685-box7-incident-summaries-1-100

- **Title:** 38_143685_box7_Incident_Summaries_1-100
- **Declared location:** `N/A`  ·  **Declared date:** `N/A`  ·  **Agency:** DoW
- **Places named in body/description:** Pacific Ocean, Atlantic Ocean, Germany, Finland, Texas, California, Arizona, Nevada (+4 more)
- ⚠ **DECLARED_NA_BUT_BODY_HAS_PLACES** — Germany, Finland, Texas, California, Arizona
- File: `extracted/dow-009-38-143685-box7-incident-summaries-1-100.md`

### dow-032-dow-uap-d48-department-of-the-air-force-report-1996

- **Title:** DOW-UAP-D48, Department of the Air Force Report, 1996
- **Declared location:** `N/A`  ·  **Declared date:** `9/10/96`  ·  **Agency:** DoW
- **Places named in body/description:** Atlantic Ocean, Japan, Vandenberg AFB, California, New Mexico, Florida, Washington (state), Moon
- ⚠ **DECLARED_NA_BUT_BODY_HAS_PLACES** — Japan, Vandenberg AFB, California, New Mexico, Florida
- File: `extracted/dow-032-dow-uap-d48-department-of-the-air-force-report-1996.md`

### dow-054-dow-uap-pr19-unresolved-uap-report-middle-east-may-2022

- **Title:** DOW-UAP-PR19, Unresolved UAP Report, Middle East, May 2022
- **Declared location:** `Middle East`  ·  **Declared date:** `N/A`  ·  **Agency:** DoW
- **Places named in title:** Middle East
- **Places named in body/description:** Middle East
- ⚠ **DECLARED_DATE_NA_TITLE_HAS_YEAR** — title year=2022
- File: `extracted/dow-054-dow-uap-pr19-unresolved-uap-report-middle-east-may-2022.md`

### dow-056-dow-uap-pr21-unresolved-uap-report-iraq-may-2022

- **Title:** DOW-UAP-PR21, Unresolved UAP Report, Iraq, May 2022
- **Declared location:** `Iraq`  ·  **Declared date:** `N/A`  ·  **Agency:** DoW
- **Places named in title:** Iraq
- **Places named in body/description:** Iraq
- ⚠ **DECLARED_DATE_NA_TITLE_HAS_YEAR** — title year=2022
- File: `extracted/dow-056-dow-uap-pr21-unresolved-uap-report-iraq-may-2022.md`

### dow-057-dow-uap-pr22-unresolved-uap-report-syria-july-2022

- **Title:** DOW-UAP-PR22, Unresolved UAP Report, Syria, July 2022
- **Declared location:** `Syria`  ·  **Declared date:** `N/A`  ·  **Agency:** DoW
- **Places named in title:** Syria
- **Places named in body/description:** Syria
- ⚠ **DECLARED_DATE_NA_TITLE_HAS_YEAR** — title year=2022
- File: `extracted/dow-057-dow-uap-pr22-unresolved-uap-report-syria-july-2022.md`

### dow-058-dow-uap-pr23-unresolved-uap-report-iraq-december-2022

- **Title:** DOW-UAP-PR23, Unresolved UAP Report, Iraq, December 2022
- **Declared location:** `Iraq`  ·  **Declared date:** `N/A`  ·  **Agency:** DoW
- **Places named in title:** Iraq
- **Places named in body/description:** Iraq
- ⚠ **DECLARED_DATE_NA_TITLE_HAS_YEAR** — title year=2022
- File: `extracted/dow-058-dow-uap-pr23-unresolved-uap-report-iraq-december-2022.md`

### dow-059-dow-uap-pr26-unresolved-uap-report-united-arab-emirates-octo

- **Title:** DOW-UAP-PR26, Unresolved UAP Report, United Arab Emirates, October 2023
- **Declared location:** `United Arab Emirates`  ·  **Declared date:** `N/A`  ·  **Agency:** DoW
- **Places named in title:** United Arab Emirates
- **Places named in body/description:** United Arab Emirates
- ⚠ **DECLARED_DATE_NA_TITLE_HAS_YEAR** — title year=2023
- File: `extracted/dow-059-dow-uap-pr26-unresolved-uap-report-united-arab-emirates-octo.md`

### dow-060-dow-uap-pr27-unresolved-uap-report-united-arab-emirates-octo

- **Title:** DOW-UAP-PR27, Unresolved UAP Report, United Arab Emirates, October 2023
- **Declared location:** `United Arab Emirates`  ·  **Declared date:** `N/A`  ·  **Agency:** DoW
- **Places named in title:** United Arab Emirates
- **Places named in body/description:** United Arab Emirates
- ⚠ **DECLARED_DATE_NA_TITLE_HAS_YEAR** — title year=2023
- File: `extracted/dow-060-dow-uap-pr27-unresolved-uap-report-united-arab-emirates-octo.md`

### dow-061-dow-uap-pr28-unresolved-uap-report-greece-january-2024

- **Title:** DOW-UAP-PR28, Unresolved UAP Report, Greece, January 2024
- **Declared location:** `Greece`  ·  **Declared date:** `N/A`  ·  **Agency:** DoW
- **Places named in title:** Greece
- **Places named in body/description:** Greece
- ⚠ **DECLARED_DATE_NA_TITLE_HAS_YEAR** — title year=2024
- File: `extracted/dow-061-dow-uap-pr28-unresolved-uap-report-greece-january-2024.md`

### dow-063-dow-uap-pr31-unresolved-uap-report-syria-october-2024

- **Title:** DOW-UAP-PR31, Unresolved UAP Report, Syria, October 2024
- **Declared location:** `Syria`  ·  **Declared date:** `N/A`  ·  **Agency:** DoW
- **Places named in title:** Syria
- **Places named in body/description:** Syria
- ⚠ **DECLARED_DATE_NA_TITLE_HAS_YEAR** — title year=2024
- File: `extracted/dow-063-dow-uap-pr31-unresolved-uap-report-syria-october-2024.md`

### dow-064-dow-uap-pr32-unresolved-uap-report-syria-october-2024

- **Title:** DOW-UAP-PR32, Unresolved UAP Report, Syria, October 2024
- **Declared location:** `Syria`  ·  **Declared date:** `N/A`  ·  **Agency:** DoW
- **Places named in title:** Syria
- **Places named in body/description:** Syria
- ⚠ **DECLARED_DATE_NA_TITLE_HAS_YEAR** — title year=2024
- File: `extracted/dow-064-dow-uap-pr32-unresolved-uap-report-syria-october-2024.md`

### dow-065-dow-uap-pr33-unresolved-uap-report-syria-october-2024

- **Title:** DOW-UAP-PR33, Unresolved UAP Report, Syria, October 2024
- **Declared location:** `Syria`  ·  **Declared date:** `N/A`  ·  **Agency:** DoW
- **Places named in title:** Syria
- **Places named in body/description:** Syria
- ⚠ **DECLARED_DATE_NA_TITLE_HAS_YEAR** — title year=2024
- File: `extracted/dow-065-dow-uap-pr33-unresolved-uap-report-syria-october-2024.md`

### dow-066-dow-uap-pr34-unresolved-uap-report-greece-october-2023

- **Title:** DOW-UAP-PR34, Unresolved UAP Report, Greece, October 2023
- **Declared location:** `Greece`  ·  **Declared date:** `N/A`  ·  **Agency:** DoW
- **Places named in title:** Greece
- **Places named in body/description:** Greece
- ⚠ **DECLARED_DATE_NA_TITLE_HAS_YEAR** — title year=2023
- File: `extracted/dow-066-dow-uap-pr34-unresolved-uap-report-greece-october-2023.md`

### dow-067-dow-uap-pr35-unresolved-uap-report-greece-october-2023

- **Title:** DOW-UAP-PR35, Unresolved UAP Report, Greece, October 2023
- **Declared location:** `Greece`  ·  **Declared date:** `N/A`  ·  **Agency:** DoW
- **Places named in title:** Greece
- **Places named in body/description:** Greece
- ⚠ **DECLARED_DATE_NA_TITLE_HAS_YEAR** — title year=2023
- File: `extracted/dow-067-dow-uap-pr35-unresolved-uap-report-greece-october-2023.md`

### dow-068-dow-uap-pr36-unresolved-uap-report-middle-east-may-2020

- **Title:** DOW-UAP-PR36, Unresolved UAP Report, Middle East, May 2020
- **Declared location:** `Middle East`  ·  **Declared date:** `N/A`  ·  **Agency:** DoW
- **Places named in title:** Middle East
- **Places named in body/description:** Middle East
- ⚠ **DECLARED_DATE_NA_TITLE_HAS_YEAR** — title year=2020
- File: `extracted/dow-068-dow-uap-pr36-unresolved-uap-report-middle-east-may-2020.md`

### dow-070-dow-uap-pr38-unresolved-uap-report-middle-east-2013

- **Title:** DOW-UAP-PR38, Unresolved UAP Report, Middle East, 2013
- **Declared location:** `Middle East`  ·  **Declared date:** `N/A`  ·  **Agency:** DoW
- **Places named in title:** Middle East
- **Places named in body/description:** Middle East
- ⚠ **DECLARED_DATE_NA_TITLE_HAS_YEAR** — title year=2013
- File: `extracted/dow-070-dow-uap-pr38-unresolved-uap-report-middle-east-2013.md`

### dow-075-dow-uap-pr43-unresolved-uap-report-africa-2025

- **Title:** DOW-UAP-PR43, Unresolved UAP Report, Africa, 2025
- **Declared location:** `Djibouti`  ·  **Declared date:** `N/A`  ·  **Agency:** DoW
- **Places named in body/description:** Djibouti
- ⚠ **DECLARED_DATE_NA_TITLE_HAS_YEAR** — title year=2025
- File: `extracted/dow-075-dow-uap-pr43-unresolved-uap-report-africa-2025.md`

### dow-080-dow-uap-pr48-unresolved-uap-report-indopacom-2024

- **Title:** DOW-UAP-PR48, Unresolved UAP Report, INDOPACOM, 2024
- **Declared location:** `Indo-PACOM`  ·  **Declared date:** `N/A`  ·  **Agency:** DoW
- **Places named in title:** Indo-PACOM
- **Places named in body/description:** Pacific Ocean, Indo-PACOM
- ⚠ **DECLARED_DATE_NA_TITLE_HAS_YEAR** — title year=2024
- File: `extracted/dow-080-dow-uap-pr48-unresolved-uap-report-indopacom-2024.md`

### dow-081-dow-uap-pr49-unresolved-uap-report-department-of-the-army-20

- **Title:** DOW-UAP-PR49, Unresolved UAP Report, Department of the Army, 2026
- **Declared location:** `North America`  ·  **Declared date:** `N/A`  ·  **Agency:** DoW
- **Places named in body/description:** North America
- ⚠ **DECLARED_DATE_NA_TITLE_HAS_YEAR** — title year=2026
- File: `extracted/dow-081-dow-uap-pr49-unresolved-uap-report-department-of-the-army-20.md`

### fbi-001-65-hs1-834228961-62-hq-83894-section-10

- **Title:** 65_HS1-834228961_62-HQ-83894_Section_10
- **Declared location:** `N/A`  ·  **Declared date:** `N/A`  ·  **Agency:** FBI
- **Places named in body/description:** Iran, Pacific Ocean, Atlantic Ocean, Germany, Netherlands, Belgium, Italy, United Kingdom (+30 more)
- ⚠ **DECLARED_NA_BUT_BODY_HAS_PLACES** — Iran, Germany, Netherlands, Belgium, Italy
- File: `extracted/fbi-001-65-hs1-834228961-62-hq-83894-section-10.md`

### fbi-002-65-hs1-834228961-62-hq-83894-section-2

- **Title:** 65_HS1-834228961_62-HQ-83894_Section_2
- **Declared location:** `N/A`  ·  **Declared date:** `N/A`  ·  **Agency:** FBI
- **Places named in body/description:** Lebanon, Pacific Ocean, Atlantic Ocean, United Kingdom, Sweden, Oak Ridge, TN, Detroit, MI, Utica (+8 more)
- ⚠ **DECLARED_NA_BUT_BODY_HAS_PLACES** — Lebanon, United Kingdom, Sweden, Oak Ridge, TN, Detroit, MI
- File: `extracted/fbi-002-65-hs1-834228961-62-hq-83894-section-2.md`

### fbi-003-65-hs1-834228961-62-hq-83894-section-3

- **Title:** 65_HS1-834228961_62-HQ-83894_Section_3
- **Declared location:** `N/A`  ·  **Declared date:** `N/A`  ·  **Agency:** FBI
- **Places named in body/description:** Pacific Ocean, Mexico, Oak Ridge, TN, Texas, California, Arizona, New Mexico, Florida (+3 more)
- ⚠ **DECLARED_NA_BUT_BODY_HAS_PLACES** — Mexico, Oak Ridge, TN, Texas, California, Arizona
- File: `extracted/fbi-003-65-hs1-834228961-62-hq-83894-section-3.md`

### fbi-004-65-hs1-834228961-62-hq-83894-section-4

- **Title:** 65_HS1-834228961_62-HQ-83894_Section_4
- **Declared location:** `N/A`  ·  **Declared date:** `N/A`  ·  **Agency:** FBI
- **Places named in body/description:** Pacific Ocean, Germany, Spain, Italy, Sweden, Russia, China, India (+14 more)
- ⚠ **DECLARED_NA_BUT_BODY_HAS_PLACES** — Germany, Spain, Italy, Sweden, Russia
- File: `extracted/fbi-004-65-hs1-834228961-62-hq-83894-section-4.md`

### fbi-005-65-hs1-834228961-62-hq-83894-section-5

- **Title:** 65_HS1-834228961_62-HQ-83894_Section_5
- **Declared location:** `N/A`  ·  **Declared date:** `N/A`  ·  **Agency:** FBI
- **Places named in body/description:** United Arab Emirates, Baltic Sea, Germany, Italy, Sweden, Russia, Georgia (country), Mexico (+11 more)
- ⚠ **DECLARED_NA_BUT_BODY_HAS_PLACES** — United Arab Emirates, Baltic Sea, Germany, Italy, Sweden
- File: `extracted/fbi-005-65-hs1-834228961-62-hq-83894-section-5.md`

### fbi-006-65-hs1-834228961-62-hq-83894-section-6

- **Title:** 65_HS1-834228961_62-HQ-83894_Section_6
- **Declared location:** `N/A`  ·  **Declared date:** `N/A`  ·  **Agency:** FBI
- **Places named in body/description:** Pacific Ocean, Germany, Netherlands, United Kingdom, Ireland, Finland, Russia, Korea (+17 more)
- ⚠ **DECLARED_NA_BUT_BODY_HAS_PLACES** — Germany, Netherlands, United Kingdom, Ireland, Finland
- File: `extracted/fbi-006-65-hs1-834228961-62-hq-83894-section-6.md`

### fbi-007-65-hs1-834228961-62-hq-83894-section-7

- **Title:** 65_HS1-834228961_62-HQ-83894_Section_7
- **Declared location:** `N/A`  ·  **Declared date:** `N/A`  ·  **Agency:** FBI
- **Places named in body/description:** Egypt, Pacific Ocean, Atlantic Ocean, Germany, Netherlands, France, United Kingdom, Norway (+20 more)
- ⚠ **DECLARED_NA_BUT_BODY_HAS_PLACES** — Egypt, Germany, Netherlands, France, United Kingdom
- File: `extracted/fbi-007-65-hs1-834228961-62-hq-83894-section-7.md`

### fbi-008-65-hs1-834228961-62-hq-83894-section-9

- **Title:** 65_HS1-834228961_62-HQ-83894_Section_9
- **Declared location:** `N/A`  ·  **Declared date:** `N/A`  ·  **Agency:** FBI
- **Places named in body/description:** Atlantic Ocean, Germany, United Kingdom, Russia, Japan, China, Australia, Georgia (country) (+13 more)
- ⚠ **DECLARED_NA_BUT_BODY_HAS_PLACES** — Germany, United Kingdom, Russia, Japan, China
- File: `extracted/fbi-008-65-hs1-834228961-62-hq-83894-section-9.md`

### fbi-009-65-hs1-834228961-62-hq-83894-serial-130

- **Title:** 65_HS1-834228961_62-HQ-83894_Serial_130
- **Declared location:** `N/A`  ·  **Declared date:** `N/A`  ·  **Agency:** FBI
- **Places named in body/description:** Pacific Ocean, Atlantic Ocean, Germany, United Kingdom, Mexico, Oak Ridge, TN, Texas, California (+6 more)
- ⚠ **DECLARED_NA_BUT_BODY_HAS_PLACES** — Germany, United Kingdom, Mexico, Oak Ridge, TN, Texas
- File: `extracted/fbi-009-65-hs1-834228961-62-hq-83894-serial-130.md`

### fbi-010-65-hs1-834228961-62-hq-83894-serial-153

- **Title:** 65_HS1-834228961_62-HQ-83894_Serial_153
- **Declared location:** `N/A`  ·  **Declared date:** `N/A`  ·  **Agency:** FBI
- **Places named in body/description:** Oak Ridge, TN, Tennessee
- ⚠ **DECLARED_NA_BUT_BODY_HAS_PLACES** — Oak Ridge, TN, Tennessee
- File: `extracted/fbi-010-65-hs1-834228961-62-hq-83894-serial-153.md`

### fbi-011-65-hs1-834228961-62-hq-83894-serial-164

- **Title:** 65_HS1-834228961_62-HQ-83894_Serial_164
- **Declared location:** `N/A`  ·  **Declared date:** `N/A`  ·  **Agency:** FBI
- **Places named in body/description:** Oak Ridge, TN, Wright-Patterson AFB, Washington (state)
- ⚠ **DECLARED_NA_BUT_BODY_HAS_PLACES** — Oak Ridge, TN, Wright-Patterson AFB, Washington (state)
- File: `extracted/fbi-011-65-hs1-834228961-62-hq-83894-serial-164.md`

### fbi-012-65-hs1-834228961-62-hq-83894-serial-220

- **Title:** 65_HS1-834228961_62-HQ-83894_Serial_220
- **Declared location:** `N/A`  ·  **Declared date:** `N/A`  ·  **Agency:** FBI
- **Places named in body/description:** Mexico, Oak Ridge, TN, California, New York, North America
- ⚠ **DECLARED_NA_BUT_BODY_HAS_PLACES** — Mexico, Oak Ridge, TN, California, New York
- File: `extracted/fbi-012-65-hs1-834228961-62-hq-83894-serial-220.md`

### fbi-013-65-hs1-834228961-62-hq-83894-serial-403

- **Title:** 65_HS1-834228961_62-HQ-83894_Serial_403
- **Declared location:** `N/A`  ·  **Declared date:** `N/A`  ·  **Agency:** FBI
- **Places named in body/description:** Oak Ridge, TN, New York
- ⚠ **DECLARED_NA_BUT_BODY_HAS_PLACES** — Oak Ridge, TN, New York
- File: `extracted/fbi-013-65-hs1-834228961-62-hq-83894-serial-403.md`

### fbi-014-65-hs1-834228961-62-hq-83894-serial-438

- **Title:** 65_HS1-834228961_62-HQ-83894_Serial_438
- **Declared location:** `N/A`  ·  **Declared date:** `N/A`  ·  **Agency:** FBI
- **Places named in body/description:** Jordan, Mexico, Oak Ridge, TN, New Mexico
- ⚠ **DECLARED_NA_BUT_BODY_HAS_PLACES** — Jordan, Mexico, Oak Ridge, TN, New Mexico
- File: `extracted/fbi-014-65-hs1-834228961-62-hq-83894-serial-438.md`

### fbi-015-65-hs1-834228961-62-hq-83894-serial-449

- **Title:** 65_HS1-834228961_62-HQ-83894_Serial_449
- **Declared location:** `N/A`  ·  **Declared date:** `N/A`  ·  **Agency:** FBI
- **Places named in body/description:** Pacific Ocean, United Kingdom, Russia, China, Vietnam, Mexico, Canada, Brazil (+10 more)
- ⚠ **DECLARED_NA_BUT_BODY_HAS_PLACES** — United Kingdom, Russia, China, Vietnam, Mexico
- File: `extracted/fbi-015-65-hs1-834228961-62-hq-83894-serial-449.md`

### fbi-016-65-hs1-834228961-62-hq-83894-sub-a

- **Title:** 65_HS1-834228961_62-HQ-83894_SUB_A
- **Declared location:** `N/A`  ·  **Declared date:** `N/A`  ·  **Agency:** FBI
- **Places named in body/description:** United Arab Emirates, Baltic Sea, Pacific Ocean, Atlantic Ocean, Germany, Italy, United Kingdom, Ireland (+20 more)
- ⚠ **DECLARED_NA_BUT_BODY_HAS_PLACES** — United Arab Emirates, Baltic Sea, Germany, Italy, United Kingdom
- File: `extracted/fbi-016-65-hs1-834228961-62-hq-83894-sub-a.md`

### fbi-019-65-hs1-834228961-62-hq-83894-section-1

- **Title:** 65_HS1-834228961_62-HQ-83894_Section_1
- **Declared location:** `N/A`  ·  **Declared date:** `N/A`  ·  **Agency:** FBI
- **Places named in body/description:** United Arab Emirates, Pacific Ocean, Atlantic Ocean, Germany, Italy, United Kingdom, Sweden, Russia (+13 more)
- ⚠ **DECLARED_NA_BUT_BODY_HAS_PLACES** — United Arab Emirates, Germany, Italy, United Kingdom, Sweden
- File: `extracted/fbi-019-65-hs1-834228961-62-hq-83894-section-1.md`

### fbi-020-65-hs1-834228961-62-hq-83894-section-8

- **Title:** 65_HS1-834228961_62-HQ-83894_Section_8
- **Declared location:** `N/A`  ·  **Declared date:** `N/A`  ·  **Agency:** FBI
- **Places named in body/description:** Israel, Lebanon, Egypt, Pacific Ocean, Atlantic Ocean, Germany, Belgium, Spain (+21 more)
- ⚠ **DECLARED_NA_BUT_BODY_HAS_PLACES** — Israel, Lebanon, Egypt, Germany, Belgium
- File: `extracted/fbi-020-65-hs1-834228961-62-hq-83894-section-8.md`

### nasa-001-255-413270-ufo-s-and-defense-what-should-we-prepare-for

- **Title:** 255_413270_UFO's_and_Defense_What_Should_we_Prepare_For
- **Declared location:** `N/A`  ·  **Declared date:** ``  ·  **Agency:** NASA
- **Places named in body/description:** Iran, Egypt, Pacific Ocean, Atlantic Ocean, Indian Ocean, Germany, Belgium, France (+21 more)
- ⚠ **DECLARED_NA_BUT_BODY_HAS_PLACES** — Iran, Egypt, Indian Ocean, Germany, Belgium
- File: `extracted/nasa-001-255-413270-ufo-s-and-defense-what-should-we-prepare-for.md`

### nasa-006-nasa-uap-d4-apollo-11-technical-crew-debriefing-1969

- **Title:** NASA-UAP-D4, Apollo 11 Technical Crew Debriefing, 1969
- **Declared location:** `N/A`  ·  **Declared date:** `1969`  ·  **Agency:** NASA
- **Places named in body/description:** Moon
- ⚠ **DECLARED_NA_BUT_BODY_HAS_PLACES** — Moon
- File: `extracted/nasa-006-nasa-uap-d4-apollo-11-technical-crew-debriefing-1969.md`

### nasa-007-nasa-uap-d5-apollo-17-crew-debriefing-for-science-1973

- **Title:** NASA-UAP-D5, Apollo 17 Crew Debriefing for Science, 1973
- **Declared location:** `N/A`  ·  **Declared date:** `1973`  ·  **Agency:** NASA
- **Places named in body/description:** Texas, Moon
- ⚠ **DECLARED_NA_BUT_BODY_HAS_PLACES** — Texas, Moon
- File: `extracted/nasa-007-nasa-uap-d5-apollo-17-crew-debriefing-for-science-1973.md`

### nasa-008-nasa-uap-d6-apollo-17-technical-crew-debriefing-1973

- **Title:** NASA-UAP-D6, Apollo 17 Technical Crew Debriefing, 1973
- **Declared location:** `N/A`  ·  **Declared date:** `1973`  ·  **Agency:** NASA
- **Places named in body/description:** Texas, Moon
- ⚠ **DECLARED_NA_BUT_BODY_HAS_PLACES** — Texas, Moon
- File: `extracted/nasa-008-nasa-uap-d6-apollo-17-technical-crew-debriefing-1973.md`

### nasa-009-nasa-uap-d7-skylab-techincal-crew-debriefing-1973

- **Title:** NASA-UAP-D7, Skylab Techincal Crew Debriefing 1973
- **Declared location:** `N/A`  ·  **Declared date:** `1973`  ·  **Agency:** NASA
- **Places named in body/description:** Atlantic Ocean, Texas
- ⚠ **DECLARED_NA_BUT_BODY_HAS_PLACES** — Texas
- File: `extracted/nasa-009-nasa-uap-d7-skylab-techincal-crew-debriefing-1973.md`

### state-001-59-214434-sp-16-7-18-1963

- **Title:** 59_214434_SP 16 [7.18.1963]
- **Declared location:** `N/A`  ·  **Declared date:** `7/18/63`  ·  **Agency:** State
- **Places named in body/description:** Washington (state), Moon
- ⚠ **DECLARED_NA_BUT_BODY_HAS_PLACES** — Washington (state), Moon
- File: `extracted/state-001-59-214434-sp-16-7-18-1963.md`

### state-002-59-64634-711-5612-7-2852

- **Title:** 59_64634_711.5612[7-2852
- **Declared location:** `N/A`  ·  **Declared date:** `7/18/52`  ·  **Agency:** State
- **Places named in body/description:** Washington (state), Moon
- ⚠ **DECLARED_NA_BUT_BODY_HAS_PLACES** — Washington (state), Moon
- File: `extracted/state-002-59-64634-711-5612-7-2852.md`

---
## Case-group consistency

Most reports in this archive belong to a small number of large case files (FBI 62-HQ-83894, the DoW Incident Summaries box, the DOW D/PR series). When a single PDF's declared location is `N/A` but it actually compiles many incidents at named places, that's a CSV-modeling choice — not a bug — and explains most LOW flags.

### DOW/D-series  (44 reports)
- Declared locations: {'Iraq': 5, 'Syria': 8, 'Persian Gulf': 6, 'Mediterranean Sea': 4, 'Oman': 1, 'N/A': 8, 'Aegean Sea': 2, 'Arabian Gulf': 1, 'Arabian Sea': 2, 'Pacific Ocean': 2, 'Gulf of Aden': 2, 'Strait of Hormuz': 2, 'Iran': 1}
- Top places mentioned in bodies: Arabian Gulf(12), Florida(11), Syria(8), Oman(7), Gulf of Oman(7), Iraq(6), Mediterranean Sea(6), Persian Gulf(6)

### DOW/PR-series  (28 reports)
- Declared locations: {'Middle East': 3, 'Iraq': 3, 'Syria': 4, 'United Arab Emirates': 2, 'Greece': 3, 'Oman': 1, 'Arabian Gulf': 6, 'Djibouti': 1, 'Southern United States': 1, 'East China Sea': 1, 'Japan': 1, 'Indo-PACOM': 1, 'North America': 1}
- Top places mentioned in bodies: Middle East(10), Arabian Gulf(6), Syria(4), Iraq(3), United Arab Emirates(3), Greece(3), Pacific Ocean(3), Indo-PACOM(3)

### DoW/Incident-Summaries-143685  (3 reports)
- Declared locations: {'N/A': 3}
- Top places mentioned in bodies: New Mexico(3), Washington (state)(3), Moon(3), Pacific Ocean(2), Atlantic Ocean(2), Mexico(2), California(2), Germany(2)

### FBI/62-HQ-83894  (18 reports)
- Declared locations: {'N/A': 18}
- Top places mentioned in bodies: Oak Ridge, TN(18), New York(15), Mexico(14), California(14), Washington (state)(14), New Mexico(13), Florida(12), Pacific Ocean(11)

### NASA/mission-docs  (15 reports)
- Declared locations: {'N/A': 5, 'Low Earth Orbit': 2, 'Moon': 8}
- Top places mentioned in bodies: Moon(12), Texas(5), Atlantic Ocean(2), Germany(2), Japan(2), Australia(2), Low Earth Orbit(2), Iran(1)

### State/cables  (7 reports)
- Declared locations: {'N/A': 2, 'Papua New Guinea': 1, 'Kazakhstan': 1, 'Georgia (country)': 1, 'Turkmenistan': 1, 'Mexico': 1}
- Top places mentioned in bodies: Florida(3), Washington (state)(2), Moon(2), Ashgabat(2), Pacific Ocean(1), Papua New Guinea(1), Indo-PACOM(1), Kazakhstan(1)

### other  (46 reports)
- Declared locations: {'N/A': 11, 'Germany': 2, 'Netherlands': 1, 'Azerbaijan': 1, 'Western United States': 25, 'Detroit, MI': 1, 'United States': 5}
- Top places mentioned in bodies: California(5), Washington (state)(4), Germany(3), Wright-Patterson AFB(3), Texas(3), Pacific Ocean(2), Canada(2), Florida(2)
