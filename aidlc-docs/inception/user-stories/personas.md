# BigRedRoutes — Personas

**Status:** APPROVED. Exact user response “Approve & Continue”, recorded 2026-11-24T17:13:46Z in `../../audit.md`. No implementation or acceptance-test success is implied.
**Evidence:** Archetypes from the team-reviewed vision and approved requirements. These are illustrative design personas, not interview participants or claims of validated user research. No invented age, disability, income or demographic findings.

## P-01 — Avery, Cornell first-year without a car

- **Context:** Starts from North Campus and is unfamiliar with Ithaca terminals and first-mile transit. Wants an affordable, relaxed NYC weekend around university dates.
- **Goal:** Understand what must be confirmed before leaving campus and obtain realistic destination-day activities.
- **Pain points:** Fragmented provider pages, unfamiliar stops, confusion between academic breaks and personal availability, and itineraries that assume unverified arrival times.
- **Behavior:** Chooses Cornell mode, campus area and dates; checks official providers; supplies known travel times or confirms sightseeing windows.
- **Trust needs:** No invented TCAT departure, fare or seat; source/date applicability visible; unknown transfers clearly differentiated from calculated feasibility. Public university dates never imply access to a personal schedule.
- **Access/usability needs:** Clear field labels, keyboard navigation, readable status text and focused next actions. These are product access requirements, not a claimed individual diagnosis.
- **Success:** Can explain which departure facts are known, why an uncovered TCAT date is unavailable, and when first-day activities may begin.
- **Primary stories:** US-01–06, US-08–09, US-11–14, US-17–18, US-22–24.

## P-02 — Jordan, Cornell graduate student with individual obligations

- **Context:** Has research/work obligations that may not align with university no-classes dates. Compares OurBus, C2C and airport information without requiring live inventory.
- **Goal:** Fit travel around personally confirmed availability and revise a plan without losing trusted constraints.
- **Pain points:** A chatbot treating a public break as free time, conflating provider links with schedules, and quietly changing confirmed departure anchors.
- **Behavior:** Supplies personal travel/activity windows, compares official links and requests targeted revisions with explicit trade-offs.
- **Trust needs:** User-provided times remain labeled as such; default buffers are disclosed heuristics; no guarantee of vehicle reliability or seat availability.
- **Access/usability needs:** Inspectable timeline, clear warnings, revision diffs and preserved existing plan on failure.
- **Success:** Can reject a proposed broader change while keeping an existing itinerary and confirmed travel anchors intact.
- **Primary stories:** US-01–06, US-08–09, US-12–19, US-22–24.

## P-03 — Riley, general DC traveler

- **Context:** Wants three relaxed days in Washington, DC focused on history/art/food, without Cornell or Ithaca travel context.
- **Goal:** Receive a city-specific, adjustable itinerary with understandable hours and costs.
- **Pain points:** Irrelevant university questions, generic invented venues, unknown hours treated as confirmed, and food/transport spending hidden inside a misleading total.
- **Behavior:** Uses General mode, selects DC, dates, interests, pace and budget, confirms first/last-day activity windows and checks venue sources.
- **Trust needs:** Only catalog-supported venues; uncertain hours unscheduled; unknown fees prevent a complete-budget claim. Historical plans must be identified as historical.
- **Access/usability needs:** Can complete the form and inspect daily cards using a keyboard and textual statuses; no university credentials required.
- **Success:** Gets an understandable DC-only plan, or a partial plan with useful reasons and a choice of which constraints to change.
- **Primary stories:** US-01–04, US-10–20, US-22–24.

## P-04 — Morgan, small adult-group planner

- **Context:** Coordinates activities for two adults in NYC and wants to revise one afternoon while preserving the rest. Supported party sizes are one to four adults, not shared remote accounts.
- **Goal:** Understand per-person versus group costs, keep revisions limited and manage locally stored plans.
- **Pain points:** Group totals confused with per-person budgets, silent cross-day edits, lost plans after a failed revision and deleted trips reappearing after restore.
- **Behavior:** Selects party size and food allowance, reviews day cards, requests targeted changes and saves/reopens/deletes plans on the local laptop.
- **Trust needs:** Unknown fees are never zero; confirmation before broader changes; only authorized local access; raw conversations not stored.
- **Access/usability needs:** Readable budget labels and confirmation/diff controls, without color-only warnings or hidden focus.
- **Success:** Can make day two cheaper without silently changing days one/three and can delete a plan without later restoration resurrecting it.
- **Primary stories:** US-01–04, US-10–24.

## O-01 — Supporting local operator

This is a supporting acceptance role, not a fifth traveler persona and not an added administrator-account product.

- **Context:** A team member prepares the single-laptop demo, imports a user-downloaded TCAT archive, reviews curated sources, checks local readiness and verifies restoration.
- **Goal:** Prepare reproducible local data and a recoverable saved-plan state without cloud hosting or redistributing unlicensed feeds.
- **Ownership:** Dyllan Hofflich owns source permissions/verification/coverage review; Kelly Yue owns the declared demo laptop. These responsibilities do not prove who operates the current AI-DLC session.
- **Trust needs:** Synthetic fixtures remain test-only; import failures preserve usable state; encryption/authorization/log protections remain intact in fallback and recovery.
- **Success:** Can identify why a source is unavailable, demonstrate a safe local restore and show that delete/reset cannot be undone by an old retained backup.
- **Primary stories:** US-07–08, US-10, US-18–23.

## Persona-to-journey map

| Journey | Primary travelers | Supporting role | Story IDs |
|---|---|---|---|
| Choose mode, express constraints and confirm windows | P-01–04 | None | US-01–04 |
| Inspect academic/transport evidence | P-01–02 | O-01 for import/service data | US-05–09 |
| Inspect catalog and create a valid affordable plan | P-01–04 | O-01 for catalog review | US-10–14 |
| Revise safely and survive model failure | P-01–04 | O-01 for diagnostics | US-15–18 |
| Save, remove and recover local plans | P-01–04 | O-01 for restore | US-19–21 |
| Use a private, understandable and accessible local app | P-01–04 | O-01 for setup/readiness | US-22–24 |

All applicable personas inherit the common privacy, accessibility and provenance requirements. Persona examples do not override supported cities, source coverage, group-size limits or the one-laptop scope.
