# BigRedRoutes — Requirement Verification Questions

**Stage:** Requirements Analysis, comprehensive depth.
**Status:** All 16 initial answers received in the conversation and recorded by the agent. Product selections are clear; original Q1/Q3/Q9 requested details remain incomplete. Enabled extensions introduce additional decisions. See `requirements-clarification-questions.md`; the answer gate is not yet passed.

Fill each `[Answer]:` with a letter and any requested specifics, then tell the agent when done. Alternatively, provide numbered answers in the conversation and the agent will record them here and in the audit. Select Other when needed. Proposed defaults below are proposals, not team decisions or approvals.

Already established by the initiating request: greenfield application; General NYC/DC planning; Cornell campus-origin/NYC transport options; public academic dates; valid-date static TCAT only; OurBus/C2C/ITH official links without live fares, seats, flights or booking; bounded local LLM tools; deterministic validators; all Inception stages through Units Generation; no Construction. These constraints are not reopened below.

## Question 1 — Actual team review and collaboration
What is the actual status of whole-team input review and the proposed collaboration arrangement in the README?

A) All four listed members have reviewed and agreed to the inputs and proposed roles/cadence. Add the actual review date, session operator, and meeting format/platform or location.

B) Whole-team agreement is still pending. Identify who is participating now and the session operator; add the intended meeting format/platform or location and any proposed role/cadence changes. We will record pending review honestly.

X) Other (please describe after [Answer]: tag below)

[Answer]: A) All four listed members have reviewed and agreed to the inputs and proposed roles/cadence. Add the actual review date, session operator, and meeting format/platform or location.

## Question 2 — Catalog size and deliverable commitment
How large a curated attraction catalog will the MVP commit to, covering varied interests and a five-day itinerary without requiring invented venues?

A) At least 12 sourced attractions per city; longer or constrained trips may return a clearly labeled partial plan if the catalog cannot fill them.

B) At least 20 sourced attractions per city, with explicit partial-plan behavior when constraints still make a full schedule infeasible.

X) Other (please describe after [Answer]: tag below)

[Answer]: A) At least 12 sourced attractions per city; longer or constrained trips may return a clearly labeled partial plan if the catalog cannot fill them.

## Question 3 — TCAT ingestion and source ownership
How should genuine TCAT data reach the local app? Synthetic fixtures remain test-only, and data without confirmed redistribution permission will not be committed.

A) Provide a local import command for a user-downloaded official GTFS archive; commit only importer instructions and clearly labeled synthetic tests. Without an imported valid feed, show unavailable.

B) Bundle a vetted official snapshot only after confirming redistribution permission and attribution; retain a local import path and unavailable behavior if no permitted snapshot can be obtained.

X) Other (please describe after [Answer]: tag below)

For either option, name the team member responsible for reviewing source permissions, verifying the Registrar/provider records and checking coverage before the demo. The existing source document's dated feed range must not be treated as permanently current.

[Answer]: A) Provide a local import command for a user-downloaded official GTFS archive; commit only importer instructions and clearly labeled synthetic tests. Without an imported valid feed, show unavailable.

## Question 4 — Missing arrival/departure times
When no user-confirmed intercity arrival/departure time exists, how should destination-day planning work?

A) Generate a provisional itinerary using a disclosed 09:00–18:00 daily sightseeing window, requiring user acknowledgment of first/last-day assumptions; transfer feasibility remains unknown.

B) Require user-confirmed first/last-day activity windows before generating those days; intermediate days may use 09:00–18:00. Transfer feasibility remains unknown until a confirmed departure and valid feeder trip exist.

X) Other (please describe after [Answer]: tag below)

[Answer]: B) Require user-confirmed first/last-day activity windows before generating those days; intermediate days may use 09:00–18:00. Transfer feasibility remains unknown until a confirmed departure and valid feeder trip exist.

## Question 5 — Buffers and travel-time assumptions
Which concrete scheduling defaults should requirements adopt? These are planning heuristics, not provider guarantees.

A) Use the proposed 15-minute intercity bus boarding margin, 60 minutes after destination arrival, and 90 minutes before destination departure. Use curated zone-to-zone activity travel estimates, displaying assumptions and permitting user increases.

B) Make users enter boarding and arrival/departure margins before evaluating travel anchors; use curated zone-to-zone activity travel estimates with displayed assumptions.

X) Other (please describe after [Answer]: tag below)

[Answer]: A) Use the proposed 15-minute intercity bus boarding margin, 60 minutes after destination arrival, and 90 minutes before destination departure. Use curated zone-to-zone activity travel estimates, displaying assumptions and permitting user increases.

## Question 6 — Unverified attraction hours
May an attraction with unknown or date-inapplicable opening hours occupy a specific itinerary time slot?

A) No. Show it as an unscheduled suggestion with an official verification link; use only date-applicable hours or user-confirmed windows for timed visits.

B) Yes, in an explicitly provisional slot with an unverified-hours warning; the itinerary cannot be labeled fully verified until the user confirms the hours.

X) Other (please describe after [Answer]: tag below)

[Answer]: A) No. Show it as an unscheduled suggestion with an official verification link; use only date-applicable hours or user-confirmed windows for timed visits.

## Question 7 — Infeasible constraints
If must-see venues, opening windows, pace or budget cannot all be satisfied, what should the planner return?

A) A labeled partial plan with structured reasons, unscheduled requested venues and proposed changes; never silently exceed hard constraints or mutate them without confirmation.

B) No saved new plan; return a structured infeasibility response and ask the user which constraint to change, retaining any existing plan.

X) Other (please describe after [Answer]: tag below)

[Answer]: X) Return a labeled partial plan with structured reasons, unscheduled requested venues and proposed changes; never silently exceed hard constraints or mutate them without confirmation. but ask the user which constraints to change to make a feasible plan

## Question 8 — Date handling and reproducible demos
How should real-user dates differ from fixed historical test/demo dates?

A) Allow today and future dates in normal mode; permit past dates only in an explicitly labeled replay/demo mode that preserves original source applicability and never presents synthetic schedules as genuine.

B) Allow today, past and future dates in the ordinary planner, explicitly labeling historical planning; source validity checks still apply to every requested date.

X) Other (please describe after [Answer]: tag below)

[Answer]: B) Allow today, past and future dates in the ordinary planner, explicitly labeling historical planning; source validity checks still apply to every requested date.

## Question 9 — Local model and fallback
What should happen if the planned Ollama `qwen3:4b` model is unavailable or cannot produce valid tool/JSON output after one repair attempt?

A) Offer deterministic planning from structured form inputs with a visible fallback status. Natural-language interpretation/revision remains unavailable until the model works; preserve existing plans.

B) Return a clear model-unavailable error for new generation and natural-language revisions; keep saved plans and reference information readable.

X) Other (please describe after [Answer]: tag below)

Also identify the intended demo laptop owner, OS, RAM, and whether this model has actually been tried. “Not tested yet” is acceptable and will remain a Construction feasibility task, not a fabricated result.

[Answer]: A) Offer deterministic planning from structured form inputs with a visible fallback status. Natural-language interpretation/revision remains unavailable until the model works; preserve existing plans.

## Question 10 — Measurable performance and agent bounds
What local performance target and request limits are acceptable for the course MVP?

A) Target 95% of warmed-model generation/revision requests within 60 seconds on the declared demo laptop; a 90-second overall deadline, at most 6 tool calls, 15 seconds per tool call, and one malformed-output repair within the same overall budget. Non-LLM lookups target 2 seconds. Benchmark during Construction.

B) Target 95% of warmed-model generation/revision requests within 120 seconds; a 150-second overall deadline, at most 6 tool calls, 15 seconds per tool call, and one malformed-output repair within the same overall budget. Non-LLM lookups target 2 seconds. Benchmark during Construction.

X) Other (please describe after [Answer]: tag below)

[Answer]: B) Target 95% of warmed-model generation/revision requests within 120 seconds; a 150-second overall deadline, at most 6 tool calls, 15 seconds per tool call, and one malformed-output repair within the same overall budget. Non-LLM lookups target 2 seconds. Benchmark during Construction.

## Question 11 — Budget meaning and unknown fees
Should the input's proposed $25–$300 per-person daily budget cover food plus activity admission, with transportation/lodging excluded?

A) Yes. Let the user set a daily food allowance within that budget; unknown admission prices produce an incomplete-cost warning, so the app cannot claim the day is within budget until costs are confirmed.

B) No. Make it an admission-only budget; show food separately as an estimate and flag unknown admission prices as incomplete. Update the input documents and field labels accordingly.

X) Other (please describe after [Answer]: tag below)

[Answer]: A) Yes. Let the user set a daily food allowance within that budget; unknown admission prices produce an incomplete-cost warning, so the app cannot claim the day is within budget until costs are confirmed.

## Question 12 — Revision scope and confirmation
How should a targeted revision behave if satisfying it would require changing another day or a confirmed travel anchor?

A) Preserve unaffected days and confirmed anchors; propose broader changes and require user confirmation before applying them. Return a diff and rerun all validators before saving.

B) Allow automatic changes to other activity days with a visible diff, but require confirmation before changing any confirmed travel anchor. Rerun all validators before saving.

X) Other (please describe after [Answer]: tag below)

[Answer]: A) Preserve unaffected days and confirmed anchors; propose broader changes and require user confirmation before applying them. Return a diff and rerun all validators before saving.

## Question 13 — Local persistence and deletion
What should the MVP retain locally, and how can a user remove it?

A) Save structured itinerary, constraints and provenance in SQLite; do not persist raw chat transcripts. Add delete-plan and reset-all-local-plans controls with confirmation for reset-all.

B) Save structured itinerary, constraints, provenance and revision messages in SQLite with clear disclosure; add delete-plan and reset-all controls, deleting associated messages too.

X) Other (please describe after [Answer]: tag below)

[Answer]: A) Save structured itinerary, constraints and provenance in SQLite; do not persist raw chat transcripts. Add delete-plan and reset-all-local-plans controls with confirmation for reset-all.

## Question 14 — Security Extensions
Should security extension rules be enforced for this project?

A) Yes — enforce all SECURITY rules as blocking constraints (recommended for production-grade applications)

B) No — skip all SECURITY rules (suitable for PoCs, prototypes, and experimental projects)

X) Other (please describe after [Answer]: tag below)

[Answer]: A) Yes — enforce all SECURITY rules as blocking constraints (recommended for production-grade applications)

## Question 15 — Resiliency Extensions
Should the resiliency baseline be applied to this project?

**What this extension is.** Enabling it applies a set of **directional, design-time best practices** for building resilient systems, derived from the **AWS Well-Architected Framework (Reliability Pillar)** and resilience-review guidance. It steers requirements, design, and code toward fault tolerance, high availability, observability, and recoverability — covering 15 practice areas across business goals, change management, observability, high availability, disaster recovery, and continuous improvement.

**What this extension is NOT.** Enabling it does **not** make your workload production-ready, nor does it certify or guarantee any availability, RTO, or RPO target. It is a **starting point** that scaffolds good resiliency decisions early — it is not a substitute for a formal **AWS Well-Architected Review** of the built system.

Treat the output as a well-grounded **first draft of your resiliency posture** to build on and validate — not a finished, production-certified result.

A) Yes — apply the resiliency baseline as directional best practices and design-time guidance (recommended for business-critical workloads, as an informed starting point that you can validate and harden before go-live)

B) No — skip the resiliency baseline (suitable for PoCs, prototypes, and experimental projects where rapid iteration matters more than reliability)

X) Other (please describe after [Answer]: tag below)

[Answer]: A) Yes — apply the resiliency baseline as directional best practices and design-time guidance (recommended for business-critical workloads, as an informed starting point that you can validate and harden before go-live)

## Question 16 — Property-Based Testing Extension
Should property-based testing (PBT) rules be enforced for this project?

A) Yes — enforce all PBT rules as blocking constraints (recommended for projects with business logic, data transformations, serialization, or stateful components)

B) Partial — enforce PBT rules only for pure functions and serialization round-trips (suitable for projects with limited algorithmic complexity)

C) No — skip all PBT rules (suitable for simple CRUD applications, UI-only projects, or thin integration layers with no significant business logic)

X) Other (please describe after [Answer]: tag below)

[Answer]: A) Yes — enforce all PBT rules as blocking constraints (recommended for projects with business logic, data transformations, serialization, or stateful components)

---

Declining an optional extension does not remove security, reliability or testing requirements explicitly agreed for BigRedRoutes. After these answers are validated, the agent will generate requirements for a separate review and approval gate. No team approval is implied by the existence of this file.


## Agent validation of received answers

Option text without a letter was mapped to its exact corresponding option; raw input is preserved in the append-only audit. Q7 remains the team’s custom answer, including asking the traveler which constraints to change. Product decisions do not conflict with one another. Q8 intentionally supersedes the input vision’s future-only restriction, and Q4/Q6 select stricter scheduling behavior than the input defaults. Those changes must be reconciled through this workflow after clarification; no previous input or stage approval is inferred. Q1 confirms whole-team input review/roles/cadence as reported by the user, but does not supply a date/operator/meeting format. Q3 lacks a named source owner and Q9 lacks a declared machine/test status. These are addressed in the follow-up file.


## Subsequent clarification outcome

See `requirements-final-clarification-questions.md` and the audit: the team reports the November 24 Zoom review, Qwen3 working on Kelly’s laptop, and explicitly requires a single-laptop/no-cloud MVP. This supersedes the earlier cloud multi-zone selection. All supplied answers remain preserved above; no approval of generated requirements is inferred. See the draft `requirements.md` for reconciled requirements and explicitly proposed local backup behavior.
