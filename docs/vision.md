# BigRedRoutes — Product Vision and Scope

**Input for AWS AI-DLC v1.0.1 Inception · team input review reported November 24, 2026; reconciled below through actual requirements answers. Generated requirements and all Inception artifacts subsequently approved through the recorded workflow; implementation remains future work.**  
**Product:** BigRedRoutes — Travel Planning for Cornell and Beyond  
**Core user context:** Cornell University, Ithaca, NY; **general itinerary cities:** New York City and Washington, DC  
**Guiding rule:** A model may recommend and explain; source-grounded tools and deterministic validators decide whether schedule and budget claims are supported.

## 1. Vision and problem

People can quickly find lists of attractions but struggle to transform preferences into realistic schedules. Cornell students have another layer: school breaks, getting from North/West/Central Campus to a terminal, deciding between OurBus and Cornell's C2C bus, using TCAT for first-mile connections, and knowing whether flights out of ITH are an option. Unconnected webpages create uncertainty and last-minute rushing. A free-form chatbot might invent a bus departure, misleading price or impossible transfer. BigRedRoutes makes the full journey inspectable and separates **published schedules** from **provider links** and **user assumptions**.

**Vision statement:** Help travelers make personalized, grounded trip plans; give Cornell travelers one campus-aware starting point that respects academic dates, local transport limitations, and their preferences without impersonating a booking engine.

**Why an LLM:** Conversational inputs contain flexible priorities ("keep costs low, don't rush between stops, save a museum for the rainy day"). LLM tools can translate intent into typed constraints, retrieve the right published data/catalog items, compare options and explain the impact of changes. Domain algorithms handle time, source validity, routes, cost and identity, and all model outputs go through validation.

## 2. Audiences and personas

| Persona | Situation and needs | Success criterion |
|---|---|---|
| **Avery — Cornell first-year** | Lives on North Campus, no car, wants to go to NYC for a long weekend without missing class; unfamiliar with campus bus stops | Understands break dates, campus-origin options, official booking links, realistic departure/arrival buffers |
| **Jordan — Cornell graduate student** | Has irregular course/research obligations; compares C2C/OurBus/ITH; limited budget | Can plan around personally chosen free dates and compare transport assumptions without fabricated fares or availability |
| **Riley — non-Cornell traveler** | Wants 3 relaxed days in DC with history and food on a budget | Can get a coherent, adjustable itinerary without seeing Cornell-only fields |
| **Morgan — friend-group planner** | Plans NYC activities for two adults and needs to change one afternoon | Sees explicit costs, revisions, and preserved unaffected activities |

**Primary stakeholders:** Students and travelers; course team implementing application; transport providers are *information sources*, not integration partners. The app is **not affiliated with or endorsed by Cornell, TCAT, OurBus, C2C, or the airport**.

## 3. Experience: two modes, one planning pipeline

### General Travel Mode

1. Choose NYC or Washington, DC, travel dates (1–5 days), interests, pace (relaxed/balanced/packed), daily activities budget per person (USD), party size, optional must-see/avoid attractions.
2. Optionally enter known arrival and departure times (in destination local time). If omitted, require user-confirmed first/last-day activity windows before scheduling those days; intermediate days may default to 09:00–18:00. No fake transport leg is created.
3. Planner retrieves candidate destinations from versioned catalog, schedules non-overlapping visits with zone-based travel-time allowances, checks admission and food budget, and explains its selections.
4. Display a daily timeline, source assumptions, estimated cost and warnings; revise using natural language (for example, "switch day 2 to more outdoor attractions").

### Cornell Travel Mode

1. Choose campus origin **North, West or Central Campus**, dates, destination, interests and budget. Campus origin is an area selection, **not live location tracking**.
2. Show official Cornell 2026–27 break dates relevant to requested travel; say *"University break / no classes"* only when supported, and remind students to confirm personal exam/work commitments.
3. Offer **transport options** for the supported corridor: OurBus Ithaca–NYC official search link, Cornell Campus-to-Campus official schedule/booking link, ITH flight-status/airline pages, and TCAT campus-to-terminal connections **only when a GTFS feed covers that service date** and a routing result exists. The app labels this screen as 'transport research/options,' not real-time booking availability.
4. If a user provides/chooses a scheduled departure/arrival time, check campus-to-terminal transfer buffers. Otherwise show *"departure time to confirm with provider"*; do not schedule a fictitious concrete transfer.
5. Make destination-day activities respect user-confirmed arrival/departure times (plus configurable post-arrival/pre-departure buffer). Offer safe alternative plan when service is unknown or no feasible connection exists.

### Example prompts

- "I'm on North Campus and want to visit NYC during February Break, February 13–16, 2027. Keep things affordable, and don't overpack the first day."
- "I can leave Cornell after 4 PM Friday. How would that affect a weekend plan?"
- "Show me C2C versus OurBus as ways to get to NYC, but mark fares and seats unverified."
- "Plan 3 days in DC with museums and food, under $75/person/day for activities."

## 4. MVP input contract

| Input | Proposed validation | Notes |
|---|---|---|
| `mode` | `general` or `cornell` | Cornell-only inputs hidden in general mode |
| `destination` | `new-york-city` or `washington-dc` | NYC full Cornell corridor; DC activity planning |
| `start_date`, `end_date` | 1–5 consecutive days, valid local calendar dates | Past, today and future dates allowed; historical plans labeled; source applicability always enforced |
| `campus_area` | North/West/Central required only in Cornell mode | Do not infer residence from identity |
| `budget_usd_per_person_day` | $25–$300; activities/food allowance only | Separately display transport cost as unknown unless user supplies fare |
| `party_size` | 1–4 adults | No child-specific suggestions in MVP |
| `interests` | 1–4 from history, art, food, architecture, nature, shopping, pop culture | Typed list, no LLM-generated categories |
| `pace` | relaxed 2 stops/day; balanced 3; packed up to 4 | Not guaranteed if constraints conflict |
| `mode_preferences` | Optional bus/flight/any and accessibility preferences | Accessibility not guaranteed by routing algorithm; point to provider details |
| `departure_anchor` | Optional **user-confirmed** provider, stop, departure/arrival times, timezones | Without confirmation require first/last-day activity windows; transfer remains unknown, not a verified departure |
| `must_see_ids`, `avoid_ids` | IDs from local attraction catalog | Conflicts flagged, never silently ignored |
| `revision` | Typed targeted/global change; max length | Revalidate fully and show differences |

**Timezone:** Ithaca, NYC, Washington DC use `America/New_York` during DST changes. Store aware timestamps, IANA time zones, UTC if persisted, and source-local dates for GTFS calendar lookups; never compare naive datetimes.

## 5. MVP features with acceptance expectations

| ID | Feature | Acceptance conditions |
|---|---|---|
| BRR-01 | Two explicit modes | General users can complete planning without Cornell inputs; Cornell mode asks origin area |
| BRR-02 | Cornell academic context | App displays accurately sourced 2026–27 break dates, link and snapshot date; never claims a user's individual classes are canceled beyond university listing |
| BRR-03 | Ithaca transport directory | NYC options include OurBus and C2C provider links; ITH flights information is clearly an external lookup, not a flight inventory |
| BRR-04 | TCAT static GTFS adapter | Ingests standard `stops`, `routes`, `trips`, `stop_times`, `calendar`, `calendar_dates` and optional `feed_info`; rejects uncovered dates and does not claim service is live |
| BRR-05 | Campus to terminal transfer check | If source-valid trip leg(s) and confirmed departure exist, require arrival + boarding buffer <= departure; otherwise mark `unknown`/`unverified` instead of false certainty |
| BRR-06 | LLM preference interpretation | Converts natural-language request to typed fields; rejects ambiguous/unsupported fields and asks for confirmation |
| BRR-07 | Tool-mediated lookup | LLM can call bounded academic-calendar, transport-catalog, GTFS and attraction tools; no unrestricted provider scraping |
| BRR-08 | Destination day plans | 1–5 days in NYC/DC with venue IDs only from catalog, no overlapping activity windows, appropriate city/timezone |
| BRR-09 | Budget display | Activity/food budget in USD per person per day; unknown fees not treated as zero; transport fares not silently included |
| BRR-10 | Arrival/day boundary | First and last day activity schedule honors confirmed travel times and explicit buffers; unknown times appear as assumptions |
| BRR-11 | Natural-language revision | Revises relevant day or preference, revalidates constraints and preserves unaffected days when possible |
| BRR-12 | Provenance & freshness | Academic/GTFS/provider data shows source link, as-of date, applicability, and one of `published-schedule`, `reference-link`, `user-provided`, `estimate`, `unavailable` |
| BRR-13 | Local persistence | Save/reopen/delete/reset locally with local session authorization; no Cornell login or account signup; no raw chat persistence |
| BRR-14 | Accessible UI | Text labels/status, keyboard navigation and non-color-only warning distinction; mobile-responsive travel cards |

## 6. Integration tiers and explicit exclusions

**MVP / strong commitment:** Published Cornell dates in versioned local JSON; user-downloaded official TCAT GTFS imported locally **with feed/service-date checks**; synthetic fixtures are test-only; static official OurBus/C2C/ITH links and explanatory metadata; curated NYC/DC attractions; planner, validation and revisions.

**Stretch, only with evidence and time:** Controlled periodic refresh of GTFS, richer C2C published timetable parsing with human verification, transport comparison after user manually enters dates/times/fares, optional static airport service guide.

**Explicitly OUT:** Cornell NetID authentication, importing a student's personal course calendar or Google Calendar (separate consent/OAuth project), live OurBus API/ticket inventory/fare guarantee, live C2C seat availability, automated ticketing/payment, searching or booking actual flights, real-time flight status/feed API, real-time GTFS-RT reliability guarantees, weather, hotel reservations, live maps/turn-by-turn navigation, inaccessible-route certification, unlimited worldwide destination catalogs, scraped or copyrighted timetable redistribution, remote user tracking. The interface can **link** to providers.

**Why this scope works:** The product generalizes the destination planning pipeline while introducing one high-value, verifiable campus departure workflow. A provider's absence of a public API does not force mock 'live' data or unauthorised scraping.

## 7. Proposed agentic workflow and tool boundaries

1. Parse the request into `TripRequest` + `CornellDepartureContext?` with the local LLM.
2. If dates may intersect Cornell breaks, call `get_academic_events(start_date,end_date)` from a **versioned** official calendar snapshot.
3. In Cornell mode, call `list_transport_options(origin_area,destination,date)` returning official provider links/metadata and coverage limits, **not ticket availability**.
4. When needed and supported, call `lookup_tcat_connections(origin_stop,terminal_stop,service_date)` using static GTFS; reject result on unsupported feed dates and missing calendar/exception coverage. Keep departure date local and resolve time zones.
5. Call `get_attraction_candidates(city,interests,excluded_ids)` to return authoritative IDs/metadata; rank and select with bounded preferences.
6. Deterministic planner generates activity blocks subject to traveler-confirmed travel anchors, windows, buffers, attraction opening windows (only if documented) and estimated meal/admission budget.
7. `validate_plan` checks all invariants and outputs structured warnings; LLM can explain **only** grounded results. One bounded retry is allowed; deterministic fallback yields a partial plan or safe error.
8. The revision tool updates selected constraints and re-runs retrieval/validation. No autonomous purchases or external submissions.

## 8. Safety, reliability and user trust

- **Never show invented schedule, fare, seat availability, flight time, campus class exemption, or verified transfer.** Unknown is distinct from false and from estimated.
- **Freshness:** The TCAT static feed listed in November 2026 covers service **Sept 22–Dec 19, 2026**. A **February 2027** request cannot use it as a confirmed trip schedule. Show link to TCAT and `schedule unavailable for date` until a new valid source is obtained.
- **Calendar:** Published university breaks are not individualized course/research obligations. For February 2027, Cornell Registrar shows **Feb 13–16** as February Break/No Classes, but this does not certify free time.
- **Connections:** Require source-valid arrival at departure stop plus a configurable boarding margin (15 minutes for bus *as a planning heuristic*, not a provider mandate); never guarantee a connection based solely on heuristics.
- **Costs:** Separate admission/food estimates from transportation costs. Unknown fares and fees remain `null`, not $0.
- **Privacy:** No Cornell credentials required. Do not store addresses, actual course schedules, full PNRs, API keys, or personal calendar tokens. Local plan data only; deletion path required.
- **Branding:** State that BigRedRoutes is a student project and is not affiliated with the providers.

## 9. User journeys for demonstration

| Scenario | User request | Necessary demonstrated behavior |
|---|---|---|
| C1 NYC Cornell weekend | North Campus, Feb 13–16 2027, relaxed, under $80/day activities, ask for OurBus/C2C comparison | Show February Break, transport provider links, **no fabricated 2027 TCAT departure**, NYC itinerary with separate budget estimate |
| C2 NYC true connection check | Fixed, in-feed-range TCAT fixture and user-entered intercity departure time | Accept only when arrival + margin <= boarding; flag missed connections and uncovered feed days |
| C3 General DC | General mode, DC, 3 days, art/history, $70/day | Itinerary generated without Cornell fields or fictitious Ithaca transport leg |
| C4 Revision | "Reduce day 2 to two activities" | Original day 1/3 preserved where constraints allow; new schedule validated and differences visible |
| C5 Unsupported | Ask for live OurBus ticket price or guaranteed flight | Explain unsupported live lookup; provide official booking/status link; no invented answer |

## 10. Success measures

| Measure | Goal |
|---|---|
| Hallucinated venue/provider departures | **0** in automated validator tests and demos |
| Plans with overlapping activities | **0** in planner tests |
| False-confirmed TCAT schedules outside feed dates | **0**; explicit unknown with official link |
| Academic dates with incorrect source attribution | **0** in snapshot test fixtures |
| Feasible transport transfer accepted incorrectly | **0** in boundary/boarding buffer unit tests |
| Cornell versus General mode separation | All required Cornell fields absent from General request flow |
| Unknown prices treated as zero | **0**; unknown prominently labeled |
| End-to-end student and general demos | At least three scenarios including an invalid/unknown transport scenario |
| Revision effects | Changes explicitly diffed, unaffected days preserved where feasible |
| Accessibility/basic UX | Keyboard flow and readable source-status labels validated in UI review |

## 11. Decisions reconciled through requirements Q&A

- Codex with installed AWS AI-DLC v1.0.1; all Inception stages through Units Generation, then stop before Construction.
- Local-only single-laptop MVP; no cloud deployment, production SLA or regional redundancy. Kelly Yue's reported demo machine: macOS Tahoe 26.5.2, 16 GB RAM. User reports Qwen3 4B works; benchmark and bounded-tool validation remain future checks.
- Dyllan Hofflich owns permissions, Registrar/provider verification and feed coverage review. Import user-downloaded GTFS locally; no unlicensed raw feed in Git. C2C remains links-only for MVP.
- At least 12 sourced attractions per city. Unknown/inapplicable hours mean unscheduled suggestions until a user confirms a window. Unknown fees prevent an unqualified within-budget claim.
- Food plus admission budget $25–$300/person/day, with user-selected food allowance; transport/lodging excluded. Boarding/arrival/departure margins default to 15/60/90 minutes and can increase.
- Missing first/last-day travel anchors require confirmed activity windows. Infeasibility produces partial plans and asks which constraints to change; never silently relax constraints.
- Targeted revisions preserve unrelated days/anchors and require confirmation for broader changes. Model failure exposes structured deterministic planning; natural-language operations remain unavailable until recovery.
- Team reports all four members reviewed online via Zoom November 24, 2026 and accepted roles/cadence. Current session operator identity remains an administrative follow-up, not an invented fact.
- Security, Resiliency and full PBT extensions enabled. Extra local encryption, protected logging, HTTPS/security headers and saved-plan authorization accepted; detailed mechanisms await design. Formal change management exempt for local course prototype; Git/AI-DLC records still apply.
- Local backup/restore details are proposed for review in `../aidlc-docs/inception/requirements/requirements.md`, not a prior team commitment. No numeric recovery targets were selected.

These changes reconcile actual user answers; they do not replace approval of generated requirements. Exact dependency pins, local security mechanisms, CI/release process and implementation checks remain later-stage decisions.

## 12. Primary source links to preserve

Full feasibility and freshness analysis: [`data-sources.md`](data-sources.md). Official links: [Cornell Registrar](https://registrar.cornell.edu/calendars-exams/academic-calendar/2026-2027), [TCAT GTFS](https://www.transit.land/data/feeds/f-dr997-tompkinsconsolidatedareatransit), [OurBus](https://www.ourbus.com/routes/ithaca-to-nyc), [C2C](https://www.fcs.cornell.edu/departments/transportation-delivery-services/campus-campus-bus-service/c2c-departure-schedule-stop-locations), [ITH airport](https://www.flyithaca.com/flights).
