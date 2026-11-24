# Data Sources, Integration Feasibility, and Freshness

**As researched:** November 19, 2026 · **Purpose:** keep Inception grounded. A link to a booking website is not an API or proof of seats, fares or departures.

## Source matrix

| Source | Confirmed public information | MVP ingestion | Status in UI | Constraints and official link |
|---|---|---|---|---|
| **Cornell University Registrar** | 2026–27 academic calendar lists fall and spring breaks and university academic dates. **February Break: Feb 13–16, 2027**; **Spring Break: Mar 27–Apr 4, 2027**. | Manually verified, versioned JSON event snapshot with as-of date and link. | `published-schedule` for university dates, not student's personalized calendar. | [Registrar 2026–27](https://registrar.cornell.edu/calendars-exams/academic-calendar/2026-2027) |
| **TCAT** | A **static GTFS** feed URL is indexed with service validity **Sept 22–Dec 19, 2026** in the current listing. There is also a GTFS-RT provider endpoint indexed publicly, but not required for MVP. | Import date-valid static GTFS and test service exceptions/stop matching; local fixture if redistribution restricted. | `published-schedule` **only within applicable service range after matching**; otherwise `unavailable`. No real-time promise. | [Feed listing and validity](https://www.transit.land/data/feeds/f-dr997-tompkinsconsolidatedareatransit), [TCAT official](https://tcatbus.com/) |
| **OurBus** | Public Ithaca–NYC route page with stops including Cornell **West** and **North** Campus; booking workflow and variable fare/date. | Static provider/route metadata + official link; no public documented timetable/availability API verified for this project. | `reference-link`, **time/seat/price unknown** until checked on provider. | [Official Ithaca–NYC page](https://www.ourbus.com/routes/ithaca-to-nyc) |
| **Cornell Campus-to-Campus (C2C)** | Official campus/NYC stop and weekly schedule page. A **new online reservation system launched Nov 4, 2026**, with different links for 2026 vs 2027 travel. | Official schedule link; optionally reviewed timetable snapshot as stretch, with calendar applicability and source date. | `reference-link` by default; any manually ingested timetable must be marked `published-schedule`, not seat availability. | [Official timetable](https://www.fcs.cornell.edu/departments/transportation-delivery-services/campus-campus-bus-service/c2c-departure-schedule-stop-locations), [reservation system announcement](https://www.fcs.cornell.edu/announcements/2026-10-22/new-campus-campus-reservation-system-launches-november-4) |
| **Ithaca Tompkins International Airport (ITH)** | Official arrivals/departures/status page and airline overview; current airline connection information available on official site. | Official flight status and airline links; *not* a date-specific inventory feed. | `reference-link`; **no guaranteed departures/fares**. | [Flights/status](https://www.flyithaca.com/flights), [Airlines](https://www.flyithaca.com/airlines) |
| **NYC and DC attractions** | Official museum/park/attraction pages can provide venue identifiers and publicly described hours/fees. | Hand-curated seed JSON with sources and as-of date; small enough to verify. | `published-schedule` for source-supported hours *only if confirmed*, `estimate` for typical visit duration, `unavailable` for unknown fees/hours. | Use primary official venue pages when implementing catalog |

## Academic dates are not personal availability

The registrar calendar says **February 13–16, 2027** is February Break/No Classes. It does **not** establish that a given student has no work, exams, research duties, extracurricular obligations or personal conflicts. The interface must ask for **user-confirmed availability** if that matters.

## TCAT feed time validity and algorithm

At research time the publicly indexed feed version covers **2026-09-22 through 2026-12-19**. As a result, an Ithaca-to-NYC itinerary dated February 2027 **cannot** claim a confirmed TCAT feeder trip using this snapshot. Show `No verified TCAT service data for this date` and a [TCAT official schedule link](https://tcatbus.com/). A developer may refresh a newer licensed feed later and retest validity before using its records.

A proper static GTFS query is more than looking up `stop_times.txt`:

1. Check `feed_info`/feed-version service coverage and the date selected.
2. Map campus departure area to a verified stop ID and destination terminal to a verified stop ID; no invented stops/nearby walking connection.
3. Evaluate `calendar.txt` weekdays/date range and `calendar_dates.txt` addition/removal exceptions for the target date.
4. Follow `trips`/`stop_times` in direction and chronological sequence. GTFS timestamps may be **25:00:00** for next-day service; preserve the service date and convert correctly.
5. Convert to aware time in **America/New_York** with DST considerations and verify transfer buffers.
6. Return `published-schedule` with source URL, feed version, valid service date, stops and times only if all checks pass; otherwise `unavailable` or `reference-link`.

This is **scheduled data**, not proof that a vehicle arrived on time. Optional GTFS-RT support, including delays, is out of scope.

## OurBus, C2C and flight policy

- A route page may mention sample times/frequency, but current *date-specific* service and ticket price **must be rechecked** on provider booking pages.
- Do not scrape booking or login forms. Do not use internal/undocumented APIs.
- A sample NYC comparison is appropriate: "OurBus: see provider; Cornell C2C: see provider; ITH flights: see airline; TCAT first-mile: schedule coverage may be missing." Avoid ranking them by cost without comparable observed data.
- C2C's Nov 2026 reservation update introduced distinct links for departure year; link to the current official C2C page so the user chooses the correct reservation system.
- **Air travel scenario:** ITH route/flight status page helps decide whether to investigate a flight. It does not enable making a real flight booking inside BigRedRoutes.

## Snapshot schema and governance

Each source/snapshot record should have `provider_id`, `source_url`, `captured_at` (offset-aware), `valid_start`, `valid_end`, `source_type`, `license_or_permissions_reviewed`, `attribution`, `status`, `notes`, and optional `content_hash`. Curated academic events include each event's actual inclusive dates and a displayed label. Attraction records include official URL, fee in USD or null, opening window or null and verification date. **Do not commit raw TCAT data if its license/redistribution terms are not confirmed**; commit small synthetic (explicitly labeled test-only) fixtures and a repeatable local importer.

## Known constraints and decisions to ask the team

- How many NYC/DC attractions can the team verify with primary links by Construction?
- Is the TCAT GTFS feed included as permitted snapshot or downloaded locally at runtime?
- Is a C2C timetable snapshot worthwhile or only official link for MVP?
- Are user-confirmed intercity arrival/departure times part of MVP, or only estimated planning windows?
- What minimum buffer makes the UX useful without claiming transit reliability?
- Who is responsible for checking whether service-date source snapshots changed?
