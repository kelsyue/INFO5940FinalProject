# BigRedRoutes — User Stories

**Status:** APPROVED. Exact user response “Approve & Continue”, recorded 2026-11-24T17:13:46Z in `../../audit.md`. No implementation or acceptance-test success is implied.
**Baseline:** `../requirements/requirements.md`; personas in `personas.md`.
**Organization:** Traveler journey, with persona/feature tags and stable requirement mappings. All stories implement approved MVP obligations; ordering is narrative, not a sprint sequence or an implementation schedule.

Each numbered criterion is an acceptance specification, not a passing test result. Examples involving schedules are synthetic test inputs unless backed by a reviewed genuine source. “Unknown”, “estimate”, “user-provided”, “reference-link” and “published-schedule” remain distinct throughout every journey.

## Journey 1 — Choose mode, express constraints and confirm windows

### US-01 — Choose the appropriate planning mode
**Personas:** P-01, P-02, P-03, P-04. **Feature:** Mode selection. **Requirements:** FR-01, FR-02.

As a traveler, I want General or Cornell mode so that I see only relevant planning questions and information.

1. **Given** Riley chooses General/DC, **when** completing the form, **then** no campus origin, Cornell login or Ithaca transport is required or added to the plan.
2. **Given** Avery chooses Cornell/NYC, **when** continuing without an origin, **then** North/West/Central selection is required before Cornell planning proceeds.
3. **Given** a populated Cornell form, **when** switching to General, **then** incompatible campus inputs are cleared or explicitly flagged for correction and cannot influence General output.

### US-02 — Submit valid trip preferences, including historical dates
**Personas:** P-01–04. **Feature:** Structured input. **Requirements:** FR-02, FR-03, NFR-03, NFR-06.

As a traveler, I want validated dates and preferences so that I can correct unsupported requests before planning.

1. **Given** NYC/DC, one to five inclusive consecutive days, one to four adults, one to four supported interests and a supported pace, **when** submitting a $25–$300/person/day budget, **then** the request is accepted subject to other confirmed constraints.
2. **Given** a reversed date range, six days, zero/five adults, unsupported city or out-of-range budget, **when** submitting, **then** the app identifies the invalid field and does not silently coerce it into a different trip.
3. **Given** a past, current or future valid date range, **when** planning, **then** past dates are labeled historical and every source is still checked for that requested date; historical mode cannot expose synthetic transit as real service.

### US-03 — Turn conversational intent into inspectable constraints
**Personas:** P-01–04. **Feature:** LLM preference interpretation. **Requirements:** FR-15, FR-16, NFR-06.

As a traveler, I want the local model to interpret my preferences so that I can describe priorities naturally while retaining control of actual constraints.

1. **Given** a healthy model and “three relaxed days in DC focused on history and food”, **when** interpretation finishes, **then** the app shows typed candidate fields for DC, three days, relaxed pace and supported interest values, asking for missing dates/windows rather than inventing them.
2. **Given** ambiguous dates or an unsupported destination, **when** interpretation cannot resolve a valid contract, **then** the app asks for confirmation/correction and does not silently choose a city or date.
3. **Given** model-proposed venue IDs, fares or departures not supported by trusted tools, **when** validating the response, **then** those values cannot become confirmed itinerary facts and the structured form remains usable.

### US-04 — Confirm usable first/last-day windows
**Personas:** P-01–04. **Feature:** Activity boundaries. **Requirements:** FR-09, FR-10, NFR-03.

As a traveler, I want to confirm when sightseeing may start and end so that a plan does not assume an unverified transport arrival.

1. **Given** unknown intercity times, **when** generating the trip, **then** first/last-day scheduling waits for user-confirmed activity windows; intermediate days may use the disclosed 09:00–18:00 default.
2. **Given** confirmed arrival at 12:00 and departure at 17:00, **when** applying default buffers, **then** timed sightseeing starts no earlier than 13:00 and finishes no later than 15:30; user increases narrow, never silently widen, the window.
3. **Given** a one-day trip or incompatible first/last-day bounds, **when** evaluating windows, **then** the app uses their intersection and reports an empty window as infeasible/pending rather than scheduling outside it. User-confirmed windows remain user-provided, not a verified transport schedule.

## Journey 2 — Inspect academic and transport evidence

### US-05 — View public academic context without inferring personal availability
**Personas:** P-01, P-02. **Feature:** Academic events. **Requirements:** FR-04, FR-19.

As a Cornell traveler, I want relevant public academic dates so that I can consider university context alongside my own obligations.

1. **Given** a reviewed snapshot covering the requested dates, **when** viewing academic context, **then** event name, applicable dates, official URL and captured date are visible.
2. **Given** a published no-classes event, **when** Jordan considers travel, **then** the app explains that individual work/research/exam commitments still need confirmation and never claims access to a personal course calendar.
3. **Given** missing/out-of-coverage records, **when** context is requested, **then** the result is unknown with an official source link; the model cannot extrapolate a break from a different year.

### US-06 — Research transport through honest provider links
**Personas:** P-01, P-02. **Feature:** Transport directory. **Requirements:** FR-05, FR-19, FR-21.

As a Cornell traveler, I want official transport options so that I can verify departures and book directly with providers.

1. **Given** Cornell/NYC, **when** opening transport options, **then** OurBus and C2C official pages and ITH airline/airport reference pages show source details and reference-link status, with unknown date-specific fares, flights and seats.
2. **Given** “book a seat” or “cheapest flight right now”, **when** the request is evaluated, **then** the app explains the unsupported operation and provides an approved official link without confirming a transaction, fare or seat.
3. **Given** a DC destination itinerary, **when** viewing its transport context, **then** the app does not imply a supported Cornell–DC corridor or invent a flight/intercity route; General mode adds no Cornell transport.

### US-07 — Import local TCAT data without unsafe redistribution
**Role:** O-01. **Feature:** Local source preparation. **Requirements:** FR-06, NFR-06, NFR-10, NFR-11.

As the local operator, I want to import a user-downloaded official GTFS archive so that the app can evaluate scheduled connections from a permitted local source.

1. **Given** a permitted genuine archive, **when** using the documented local import command, **then** the app validates required data, records source/version/applicability information and makes valid imported data available locally without committing the raw feed to Git.
2. **Given** a corrupt archive, unsafe archive path, oversized content or missing essential structure, **when** importing, **then** safe bounded validation fails, no arbitrary filesystem write occurs and previously usable data is preserved.
3. **Given** no valid imported archive or unreviewed redistribution permission, **when** preparing the demo, **then** the app reports schedule-unavailable while provider links remain usable; synthetic test fixtures cannot be selected as genuine rider schedules.

### US-08 — See only date- and path-applicable TCAT schedules
**Personas:** P-01, P-02. **Supporting role:** O-01. **Feature:** Static transit lookup. **Requirements:** FR-07, FR-19, NFR-03.

As a Cornell traveler, I want TCAT suggestions tied to the requested service date and verified stops so that stale or unrelated data does not become a departure claim.

1. **Given** imported data with an applicable service date and stop path, **when** searching, **then** weekday/calendar rules, added/removed exceptions, trip direction and stop sequence are checked before publishing scheduled times with source details.
2. **Given** an uncovered date, a removed service, a missing campus/terminal mapping or no usable path, **when** searching, **then** no confirmed trip is returned; the app shows unavailable and the official TCAT link.
3. **Given** a synthetic service record containing 25:00:00 or a DST-boundary case, **when** resolving the trip, **then** service date is retained and the resulting aware instants are compared correctly. Missing optional `feed_info` is handled from actual service records, not fabricated metadata.

### US-09 — Understand transfer feasibility and its limits
**Personas:** P-01, P-02. **Feature:** Connection check. **Requirements:** FR-08, FR-10, NFR-03.

As a Cornell traveler, I want an explicit boarding-buffer check so that I can spot an impossible campus-to-terminal connection.

1. **Given** a source-valid feeder arriving 09:10, user-confirmed intercity departure 09:25 and 15-minute margin in a synthetic acceptance fixture, **when** checking, **then** the calculation passes exactly at the boundary; arrival at 09:11 fails.
2. **Given** missing departure confirmation or invalid/uncovered feeder data, **when** checking, **then** feasibility is unknown, not true and not an invented replacement departure.
3. **Given** naive timestamps, changed dates or incompatible instants, **when** validating, **then** invalid input is rejected or a corrected confirmation is requested. A passing calculation is labeled scheduled feasibility with a planning heuristic, never guaranteed vehicle reliability or seat availability.

## Journey 3 — Create and inspect a useful destination plan

### US-10 — Select sourced venues with usable hours
**Personas:** P-01–04. **Supporting role:** O-01. **Feature:** Catalog trust. **Requirements:** FR-11, FR-19.

As a traveler, I want city-specific venues with source information so that my itinerary uses places and visit windows I can verify.

1. **Given** the MVP catalog, **when** browsing either city, **then** at least 12 sourced venues per city represent varied interests and expose stable IDs, tags, source URLs, checked dates and estimated visit durations.
2. **Given** unknown or date-inapplicable opening hours, **when** considering a venue, **then** it appears only as an unscheduled suggestion with an official verification link until a user confirms a usable activity window.
3. **Given** source-supported hours or a user-confirmed window, **when** scheduling, **then** the visit fits that window and its status remains published-schedule or user-provided respectively; a NYC venue cannot appear as a DC catalog entry.

### US-11 — Receive a chronological day plan that respects constraints
**Personas:** P-01–04. **Feature:** Deterministic scheduling. **Requirements:** FR-09–12, NFR-03, NFR-05.

As a traveler, I want chronological day cards so that I can follow a schedule consistent with my confirmed windows and pace.

1. **Given** valid city venues and confirmed activity windows, **when** generating a day, **then** each visit has positive duration, belongs to the selected city, fits applicable hours/windows and does not overlap another visit or its travel allowance.
2. **Given** relaxed, balanced or packed pace, **when** scheduling, **then** the day contains at most 2, 3 or 4 attraction stops respectively, without duplicating a venue within that day or filling space with fabricated places.
3. **Given** travel between zones or confirmed arrival/departure anchors, **when** displaying the schedule, **then** curated travel estimates and 60/90-minute default anchor buffers are disclosed and enforced; infeasible days follow US-13 instead of violating constraints.

### US-12 — Understand daily food/admission costs and unknown fees
**Personas:** P-01–04, especially P-04. **Feature:** Budget completeness. **Requirements:** FR-02, FR-13.

As a traveler, I want separately labeled per-person and group cost estimates so that unknown fees and excluded travel costs do not mislead my budget decisions.

1. **Given** a $75/person/day budget, $25 food allowance and $40 known estimated admission total, **when** summarizing the day, **then** the known estimate is $65/person/day and $130 for two adults, clearly labeled as estimates rather than a total-trip guarantee.
2. **Given** one unknown admission fee, **when** calculating costs, **then** that fee stays null, known estimated costs are shown separately and the day cannot claim complete within-budget status.
3. **Given** food allowance exceeds the daily budget, or known admissions plus food exceed it, **when** planning, **then** invalid allowance is corrected or infeasibility is explained; transport/lodging are excluded and unknown transport fares are never $0.

### US-13 — Resolve an incomplete plan without hidden constraint changes
**Personas:** P-01–04. **Feature:** Infeasibility decisions. **Requirements:** FR-14, FR-22.

As a traveler, I want a partial plan with reasons and alternatives so that I can choose which constraints to change.

1. **Given** must-see venues, hours, catalog capacity or budget cannot all be satisfied, **when** planning, **then** feasible portions remain visible, the result is labeled partial and unscheduled requests have specific reasons.
2. **Given** proposed changes to cost, pace, dates or visit preferences, **when** viewing alternatives, **then** the app asks which constraints the user wants to change and applies none until confirmation.
3. **Given** no confirmed window or a rejected change proposal, **when** continuing, **then** pending days remain pending and prior saved state remains intact; partial/infeasible is distinct from malformed input or source-unavailable.

### US-14 — Inspect evidence behind the plan
**Personas:** P-01–04. **Feature:** Provenance inspection. **Requirements:** FR-19, FR-21.

As a traveler, I want inspectable source/status information so that I can distinguish facts, assumptions and unavailable data.

1. **Given** an academic, venue or transport observation, **when** inspecting it, **then** its source URL, capture/check date, applicability and semantic status are available beside or through the relevant card.
2. **Given** model-generated explanation text, **when** rendering, **then** user-provided values stay user-provided, estimates stay estimates and provider links never become published timetables or availability confirmation.
3. **Given** a missing source or unsupported claim, **when** validating/displaying it, **then** the app labels it unavailable or omits the unsupported fact and supplies an appropriate approved verification link instead of inventing evidence.

## Journey 4 — Revise safely and handle model failure

### US-15 — Revise one day and inspect the diff
**Personas:** P-01–04, especially P-04. **Feature:** Targeted revision. **Requirements:** FR-17, FR-12–14.

As a traveler, I want to make day two cheaper or more relaxed so that I can improve it without silently changing other days.

1. **Given** a three-day plan and “reduce day two to two activities”, **when** revising, **then** changed catalog-backed visits are shown in a diff and days one/three and confirmed travel anchors remain unchanged.
2. **Given** a proposed revision, **when** validating, **then** hours, windows, non-overlap, city, provenance, pace and cost completeness are rechecked before a valid revised plan can be saved.
3. **Given** malformed/failed model output, invalid revision or rejected proposal, **when** processing ends, **then** no invalid plan overwrites the original; the user sees a safe explanation or fallback state.

### US-16 — Confirm changes that reach beyond the target
**Personas:** P-01–04, especially P-02, P-04. **Feature:** Revision scope. **Requirements:** FR-14, FR-17.

As a traveler, I want to approve broader changes separately so that a local revision cannot move trusted days or travel anchors without my consent.

1. **Given** day-two constraints can only be satisfied by changing another day or anchor, **when** proposing a revision, **then** the app identifies the additional changes and asks for confirmation before applying them.
2. **Given** the user declines or does not confirm, **when** returning to the plan, **then** all affected saved values remain unchanged and the unsatisfied constraint remains visible.
3. **Given** explicit confirmation, **when** applying broader changes, **then** the app reruns every applicable validator and displays the full diff; a failed validation still cannot overwrite valid saved state.

### US-17 — Keep planning when the local model is unavailable
**Personas:** P-01–04. **Feature:** Degraded mode. **Requirements:** FR-18, FR-22, NFR-05, NFR-11.

As a traveler, I want a clearly labeled structured-input fallback so that model failure does not erase or block access to my useful local plans.

1. **Given** Ollama is unavailable, times out or produces invalid output after at most one repair, **when** a model-dependent action ends, **then** the app offers deterministic planning from structured inputs with explicit fallback status.
2. **Given** fallback is active, **when** interacting, **then** natural-language interpretation/revision is visibly unavailable while saved-plan reads and references remain usable subject to authorization.
3. **Given** fallback planning runs, **when** producing a result, **then** all source, scheduling, budget and security checks remain enforced; an unavailable model cannot make an unknown transfer feasible.

### US-18 — Receive bounded tool-assisted results
**Personas:** P-01–04. **Supporting role:** O-01. **Feature:** Agent boundaries and responsiveness. **Requirements:** FR-16, FR-18, NFR-02, NFR-06, NFR-11.

As a traveler, I want tool-assisted planning to stop predictably and safely so that an untrusted instruction or looping model cannot consume unbounded resources or act outside planning.

1. **Given** a healthy model request, **when** tools execute, **then** only registered tools with validated arguments/results can run; no shell, arbitrary URL, booking, scraping or model-controlled file writing is permitted.
2. **Given** injected provider text, an invented tool name/ID or repeated requests, **when** processing, **then** untrusted instructions are treated as data and invalid calls cannot bypass constraints; at most six tool calls and one repair occur within the total budget.
3. **Given** a slow call, **when** its deadline is reached, **then** the tool ends within 15 seconds and the overall request within 150 seconds, returning safe fallback/error without changing prior saved state. A Construction benchmark must assess the separate 95%-within-120-second warmed-model target; non-LLM lookups target two seconds.

## Journey 5 — Save, remove and recover local plans

### US-19 — Save and reopen an authorized local plan
**Personas:** P-01–04. **Feature:** Local persistence. **Requirements:** FR-20, NFR-07–08, NFR-11.

As a traveler, I want to save/reopen a local itinerary so that I can return to the same constraints and evidence without an external account.

1. **Given** an authorized local session and a validated complete or labeled partial plan, **when** saving/reopening, **then** structured itinerary, constraints, provenance and needed revision metadata survive with their original meaning; raw chat transcripts do not persist.
2. **Given** another local principal or no valid permission, **when** requesting a saved ID, **then** the app denies access without leaking the plan; guessing an ID is insufficient authorization.
3. **Given** a database/encryption/write failure, **when** saving, **then** the app gives a safe failure and preserves previous valid saved state, without claiming the new data was durably saved/backed up.

### US-20 — Delete a plan or reset all local plans
**Personas:** P-01–04. **Feature:** Data deletion. **Requirements:** FR-20, NFR-08, NFR-12.

As a traveler, I want deletion and a confirmed reset-all so that removed travel plans do not remain recoverable through app-managed storage.

1. **Given** an authorized plan owner, **when** deleting a plan, **then** associated structured data and all app-managed recoverable copies are removed or rewritten so a later restore cannot resurrect it.
2. **Given** reset-all, **when** the user cancels confirmation, **then** nothing is removed; after confirmation, all locally saved plan data and applicable recoverable copies are removed while the app remains usable.
3. **Given** repeated deletion or an unauthorized request, **when** processing, **then** repetition does not recreate state and unauthorized callers cannot delete another principal's plan. Security logs retain only non-sensitive audit events, not recoverable itinerary content.

### US-21 — Restore the latest valid local saved state
**Personas:** P-01–04 as beneficiaries. **Role:** O-01 for recovery. **Feature:** Local backup/restore. **Requirements:** FR-20, NFR-08, NFR-12, NFR-14.

As the local operator, I want a verified encrypted latest-state backup so that accidental local data failure can be recovered without a cloud service.

1. **Given** a successful plan save, **when** creating the approved automated encrypted snapshot, **then** the latest restorable state is retained and the previous valid copy is protected until replacement is verified/committed safely.
2. **Given** a valid backup and available protected keys, **when** executing the documented restore check before the demo, **then** restored plans preserve constraints/provenance and deleted/reset plans cannot return from any retained copy.
3. **Given** corrupt backup, unavailable keys or loss of the laptop and its copies, **when** recovery cannot complete safely, **then** the app reports failure without fabricating data or bypassing encryption. No numeric RTO/RPO, cloud SLA or laptop-loss guarantee is claimed.

## Journey 6 — Use a private, understandable and accessible local app

### US-22 — Use the secured local application without external credentials
**Personas:** P-01–04. **Role:** O-01 for setup. **Feature:** Local trust boundary. **Requirements:** NFR-01, NFR-06–10, FR-20.

As a local user, I want protected access to my itinerary so that a laptop demo does not expose saved plans or require Cornell/provider credentials.

1. **Given** the approved local setup, **when** launching, **then** required services are local/loopback, local HTTPS and required security headers are available, origins are explicitly restricted and no cloud account, Cornell login or public signup is required.
2. **Given** unauthorized/cross-origin mutation or malicious input, **when** accessing the app, **then** local authorization and schema/size/format checks reject it; rendered text is escaped and untrusted input cannot become SQL, shell or model instruction authority.
3. **Given** saved data/backups and security logging, **when** inspecting the configured controls during Construction, **then** encryption/key protection and protected centralized structured logging with request ID/timestamp/level are present, sensitive content is excluded, and security-log retention is at least 90 days without retaining plan content. Exact mechanisms require later design approval.

### US-23 — Understand readiness and safe errors
**Personas:** P-01–04. **Supporting role:** O-01. **Feature:** Readiness/error communication. **Requirements:** FR-22, NFR-05, NFR-11.

As a local user, I want distinct app, model and source status so that I know whether to correct an input, confirm information or use fallback.

1. **Given** an available API but missing model/feed, **when** viewing readiness, **then** each component's state is distinguished and the app points to the usable fallback/reference behavior rather than claiming complete readiness.
2. **Given** invalid input, unknown plan, infeasibility or source/model failure, **when** responding, **then** a machine-distinguishable safe code and understandable explanation are supplied without stack traces, keys or internal filesystem paths.
3. **Given** failure during a revision/import/save, **when** cleanup finishes, **then** resources are released, invalid intermediate state is not committed and previous valid saved data is preserved wherever the operation promised preservation.

### US-24 — Complete the journey with readable, keyboard-accessible controls
**Personas:** P-01–04. **Feature:** Accessibility. **Requirements:** NFR-04, FR-01, FR-14, FR-17, FR-19, FR-20.

As a traveler using keyboard or assistive navigation, I want labeled controls and textual statuses so that I can plan, inspect warnings and manage my itinerary independently.

1. **Given** keyboard-only navigation, **when** choosing mode, entering constraints, confirming windows, inspecting cards and revising/deleting a plan, **then** labels, logical focus and actionable controls are available without a pointer-only step.
2. **Given** unknown data, partial plans, failure or changed activities, **when** presented, **then** status/diff/warnings use readable text, not color alone, and relevant source links have descriptive names.
3. **Given** a narrow viewport and screen-reader-oriented inspection, **when** reviewing day/budget cards and confirmations, **then** controls remain usable, content order is meaningful and essential information is not hidden by layout.

## Cross-cutting acceptance obligations

These are shared obligations attached to the stories above, not extra implementation tasks or replacements for their user-value criteria.

| ID | Applies to | Acceptance / later-stage verification obligation |
|---|---|---|
| CC-01 | All input/model/source stories | Validate API/tool/import bounds and safe parsing; source/model text cannot issue instructions. Exact size limits specified before code generation. |
| CC-02 | US-19–23 | Authorized saved-plan operations, encrypted stores/backups, protected key handling, local secure serving and safe failure must remain enforced in fallback and restore. |
| CC-03 | US-07, US-18–23 | Build/release verification must show exact dependency pins/lockfiles, trusted sources/integrity, vulnerability-scanning instructions and access-controlled auditable pipeline changes. Production cloud resources/SBOM deployment are not introduced. |
| CC-04 | US-08–13, US-15–21 | Functional Design identifies generated properties; Construction adds PBT alongside concrete example tests, reusable domain generators, shrinking, reproducible seeds and CI. No passing result claimed here. |
| CC-05 | US-03, US-15–18, US-23 | Test limits and benchmark warmed-model 95% ≤120 seconds, total deadline ≤150 seconds, tool deadline ≤15 seconds, ≤6 calls/≤1 repair and two-second non-LLM target on declared hardware. A report that Qwen3 works does not establish these measurements. |
| CC-06 | All stories | No cloud hosting, remote multi-user scope, live booking/inventory, guaranteed transport connection, synthetic production timetable or numeric recovery guarantee. Preserve statuses and source applicability. |

## Requirement-to-story traceability

| Requirement | Story coverage | Shared obligation / verification |
|---|---|---|
| FR-01 | US-01, US-24 | Mode isolation |
| FR-02 | US-01–02, US-12 | CC-01 |
| FR-03 | US-02 | Historical labels, source applicability |
| FR-04 | US-05 | Academic context, not personal availability |
| FR-05 | US-06 | CC-06 |
| FR-06 | US-07 | CC-01, CC-03 |
| FR-07 | US-08 | CC-04 |
| FR-08 | US-09 | CC-04 |
| FR-09 | US-04, US-11 | Window intersection and missing-window behavior |
| FR-10 | US-04, US-09, US-11 | Disclosed buffers |
| FR-11 | US-10 | ≥12/city, unknown hours |
| FR-12 | US-11, US-15 | CC-04 |
| FR-13 | US-12, US-15 | CC-04 |
| FR-14 | US-13, US-15–16 | Confirmed constraint changes |
| FR-15 | US-03 | CC-01 |
| FR-16 | US-03, US-18 | CC-01, CC-05 |
| FR-17 | US-15–16 | CC-04 |
| FR-18 | US-17–18 | CC-02, CC-05 |
| FR-19 | US-05–06, US-08, US-10, US-14 | CC-06 |
| FR-20 | US-19–22 | CC-02, CC-04 |
| FR-21 | US-06, US-14 | CC-06 |
| FR-22 | US-13, US-17, US-23 | Safe error classes |
| NFR-01 | US-21–22 | CC-06 |
| NFR-02 | US-18, US-23 | CC-05 |
| NFR-03 | US-02, US-04, US-08–09, US-11 | CC-04 |
| NFR-04 | US-24 | Keyboard/screen-reader-oriented acceptance |
| NFR-05 | US-11, US-17, US-23 | Architecture isolation verified in Application Design |
| NFR-06 | US-02–03, US-07, US-18, US-22 | CC-01 |
| NFR-07 | US-19–20, US-22 | CC-02 |
| NFR-08 | US-19–22 | CC-02; security logs distinct from plan backups |
| NFR-09 | US-22 | CC-02, secured HTML headers |
| NFR-10 | US-07, US-22 | CC-03; build artifacts verified in Construction |
| NFR-11 | US-07, US-15–19, US-23 | CC-01–02 |
| NFR-12 | US-20–21 | CC-02, CC-04 |
| NFR-13 | US-08–13, US-15–21 | CC-04; full PBT at applicable later stages |
| NFR-14 | US-01–24 | CC-04–05; scenario tests plus ≥80% pure planner/validator coverage target during Construction |

## Persona-to-story traceability

| Persona / role | Primary applicable stories |
|---|---|
| P-01 Avery | US-01–06, US-08–14, US-15–20, US-22–24; US-21 as recovery beneficiary |
| P-02 Jordan | US-01–06, US-08–09, US-10–20, US-22–24; US-21 as recovery beneficiary |
| P-03 Riley | US-01–04, US-10–20, US-22–24; US-21 as recovery beneficiary |
| P-04 Morgan | US-01–04, US-10–24 |
| O-01 local operator | US-07–08, US-10, US-18–23 |

## INVEST review and genuine dependencies

- **Independent:** Each story describes an independently reviewable outcome and can be accepted using controlled prerequisite state. Shared catalogs, confirmed inputs and saved plans are genuine dependencies, not claims that every feature can be implemented in isolation.
- **Negotiable:** Acceptance outcomes are fixed to the approved product baseline; UI layout, component boundaries and mechanisms remain negotiable at their design gates. Removing approved scope requires an actual change request.
- **Valuable:** Each narrative states traveler benefit or, for the supporting operator, a data/readiness/recovery outcome needed by travelers. No story is simply “create a table” or “write a module”.
- **Estimable:** Inputs, statuses and failure outcomes are explicit. Architectural effort estimates and unit decomposition belong to later gates, not invented story-point estimates here.
- **Small:** Happy-path revision (US-15), broader-change confirmation (US-16), fallback (US-17) and tool limits (US-18) are separate outcomes. Save, delete and restore likewise have separate stories. Security/accessibility have shared obligations to prevent copying a large checklist into every story.
- **Testable:** Every story has three numbered Given/When/Then scenarios with meaningful boundary, error or unknown behavior. Coverage tables identify all 22 FRs and 14 NFRs; no criterion is asserted to have passed.

| Dependency | Meaning without prescribing unit order |
|---|---|
| US-03 → US-02/04 | Model interpretation must produce valid fields and obtain missing windows. Structured inputs need no model. |
| US-08 → US-07 | Genuine scheduled lookup needs a valid imported feed; unavailable behavior works without it. |
| US-09 → US-08/04 | Transfer needs supported feeder data and confirmed departure; activity windows alone are not intercity departure proof. |
| US-11 → US-04/10/12 | A valid plan needs usable windows, catalog data and honest budget handling. |
| US-15/16 → US-11/13 | Revision needs an existing plan/constraints; partial-plan behavior may preserve infeasible requests. |
| US-20/21 → US-19 | Deletion and restore operate on saved states; deleted-plan protection constrains every retained copy. |
| US-22/24 across all | Security and accessibility are acceptance constraints, not optional end-of-project extras. |

## Extension coverage at the story stage

This is a documentation/acceptance review. Rule coverage below preserves approved obligations; security controls, backup restoration, property tests and performance have not been implemented or tested.

| Rules | Story-stage treatment |
|---|---|
| SECURITY-01 | US-19/21/22 and CC-02 retain encryption and key-protection obligations. |
| SECURITY-02 | N/A: no external-traffic load balancer/API gateway/CDN. Local logging remains required. |
| SECURITY-03 | US-22/23 retain protected structured centralized local logs without sensitive content. |
| SECURITY-04 | US-22 retains secured local serving and all headers from NFR-09; mechanisms verified later. |
| SECURITY-05 | US-02/03/07/18/22 and CC-01 cover validated bounded input. |
| SECURITY-06 | Cloud IAM N/A; US-19/22 retains local permission/key boundaries. |
| SECURITY-07 | US-22 retains loopback, allowed origins and restricted local exposure. |
| SECURITY-08 | US-19/20/22 cover local object authorization and unauthorized mutation. |
| SECURITY-09 | US-22/23 and CC-03 retain hardening, pinned supported runtime and safe errors; verify configuration later. |
| SECURITY-10 | CC-03 retains pins/scanning/trusted sources. Production deployment SBOM obligation N/A to this local prototype; reassess if scope changes. |
| SECURITY-11 | US-18/22 cover misuse and layered boundaries; public Internet throttling N/A, bounded local work still required. |
| SECURITY-12 | Local credential/session design verification deferred; US-19/22 cannot bypass applicable expiry/invalidation/secure credential protections if introduced. No password or Cornell-login feature added. |
| SECURITY-13 | US-07/18/22 and CC-03 retain safe parsing, source/software integrity and auditable changes; CDN SRI N/A without CDN assets. |
| SECURITY-14 | US-22 retains protected security logs/retention; local event-alert/monitoring design remains a later obligation, not a passing result. |
| SECURITY-15 | US-07/15/17/19/23 retain safe errors, cleanup and preserved state. |
| RESILIENCY-01 | Travelers depend on planning/UI/storage; model and imported sources can degrade visibly. Detailed dependency map/classification verified at Application Design. |
| RESILIENCY-02 | Production SLA/numeric RTO/RPO N/A per approved single-laptop scope; US-21 covers honest local recovery behavior. |
| RESILIENCY-03 | Formal change-management exemption approved; Git and AI-DLC gates retained. |
| RESILIENCY-04 | CI/release/rollback selection deferred to the permitted NFR Design gate; CC-03 preserves verification needs. |
| RESILIENCY-05 | US-18/22/23 retain performance, structured logs and readiness. Local dashboard/monitoring mechanisms await design. |
| RESILIENCY-06 | US-23 distinguishes process/model/data health; load-balancer/public-canary infrastructure N/A. |
| RESILIENCY-07 | US-17/21/23 cover model/source/backup degradation; assessment tool and local monitoring applicability assessed later. |
| RESILIENCY-08 | Cloud multi-zone/multi-region N/A to explicitly approved one-laptop scope. |
| RESILIENCY-09 | Production autoscaling N/A; US-18 retains bounded local requests. |
| RESILIENCY-10 | US-17/18/23 retain bounded failure/degradation; pool/circuit-breaker design applicability later. |
| RESILIENCY-11 | Production regional DR N/A; US-21 retains local restore with no guaranteed recovery time. |
| RESILIENCY-12 | US-20/21 retain automated encrypted snapshots and deletion-safe retention; no backup exists yet. |
| RESILIENCY-13 | US-21 requires documented local restore and observed validation at Construction; no regional failback. |
| RESILIENCY-14 | US-17/21/23 and CC-04 preserve failure/recovery scenario needs; formal process choice at NFR Design. |
| RESILIENCY-15 | Safe diagnostic outcomes captured in US-23; incident-process decision deferred to NFR Design. |
| PBT-01 | N/A at story generation; CC-04 carries Functional Design property identification forward. |
| PBT-02 | N/A at story generation; CC-04/US-19/21 identify serialization/restore round-trip outcomes for later tests. |
| PBT-03 | N/A at story generation; US-08–13/15–18 identify schedule/cost/provenance/bounds invariants. |
| PBT-04 | N/A at story generation; US-20 identifies repeat-deletion observable-state invariance. |
| PBT-05 | N/A at story generation; later Functional Design must assess oracle/reference applicability. |
| PBT-06 | N/A at story generation; US-19–21 provide save/revise/delete/restore state outcomes. |
| PBT-07 | N/A at story generation; CC-04 retains domain generators and boundary coverage. |
| PBT-08 | N/A at story generation; CC-04 retains shrinking/seeds/CI requirements. |
| PBT-09 | N/A at story generation; Hypothesis/fast-check remain approved requirement-stage proposals for later configuration. |
| PBT-10 | N/A at story generation; the 72 concrete scenarios complement, not replace, future generated-property tests. |

No blocking story-level inconsistency was identified in this review. Later design/implementation checks may identify findings and must not be marked passing merely because an acceptance criterion exists.
