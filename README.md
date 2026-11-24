# BigRedRoutes — Travel Planning for Cornell and Beyond

> **AI-DLC Mid-semester Milestone | November 24, 2026, 11:59 PM ET | 150 points**  
> **Workflow version:** AWS AI-DLC **v1.0.1** only (not v2)  
> **Project status:** AI-DLC Inception complete. All required artifacts and final units are approved; stopped before Construction. No application implementation or Construction started.  
> **Coding agent:** OpenAI Codex; **planned product LLM:** Qwen3 4B through Ollama. These are separate roles.

## Team and collaboration

**Team members and responsibilities:** The team confirmed whole-team input review and agreement to these roles in its Requirements Analysis answers. All four members report reviewing together online via Zoom on November 24, 2026. Ananya is the designated workflow operator; who operates this particular session remains unreported.

| Full name | Cornell NetID | Responsibility |
|---|---|---|
| Ananya Jajodia | aj477 | Repository maintenance, AI-DLC session operator |
| Sarah Park | sp2227 | Product/UX, user stories, accessibility |
| Dyllan Hofflich | drh253 | Transport integrations and data verification |
| Kelly Yue | ky387 | Architecture, test plans, consistency review |

**Agreed collaboration plan:** All members attend major AI-DLC Inception approval sessions, review AI-generated material and question unsupported choices before approval. The team agreed to two 45-minute synchronous meetings per week, plus asynchronous GitHub Issues/PR comments. Synchronous meetings are online via Zoom; the team reports all four members attended on November 24, 2026. Agreement to the recurring plan does not imply every future meeting has already occurred. Each member owns a review area; the session operator records agreed answers in the coding agent. Only one member submits the public GitHub URL on Canvas.

## Project overview — five paragraphs

Travel planning is challenging for everyone, but Cornell students in Ithaca face an extra hurdle before the vacation even begins: figuring out **when** to travel around academic commitments and **how** to get from campus to a bus stop, the airport, or another city without a car. Travel details are scattered across Cornell's academic calendar, TCAT, OurBus, Cornell Campus-to-Campus, airline/airport sites, and destination guides. A student planning a weekend in New York City must piece together departure location, campus-to-terminal connection, boarding buffer, estimated cost, and a workable arrival-day schedule. General-purpose itinerary applications typically focus on the destination rather than this campus-specific first and last mile. **BigRedRoutes** provides one understandable journey, from Cornell to destination activities and back.

BigRedRoutes serves two audiences through **two explicit modes**. In **General Travel Mode**, any traveler can enter their destination, travel dates, interests, budget and preferred pace to build a personalized destination itinerary. In **Cornell Travel Mode**, a traveler additionally selects a campus departure area (North, West or Central Campus), receives official Cornell academic-break context, and explores transport options from Ithaca: scheduled TCAT connections where supported by valid feed data, Cornell Campus-to-Campus service, OurBus provider links and Ithaca Tompkins International Airport (ITH) information. Cornell Mode adds useful local context without restricting the whole product to students. MVP destination activity catalogs will cover **New York City and Washington, DC**, with NYC as the full transportation-coordination demo and DC as a general itinerary demo.

A large language model is useful because requests combine nuanced intent and multiple constraints: “I have February Break, live on North Campus, want a cheap, low-stress NYC weekend, and prefer museums and food.” The proposed **Qwen3 4B model running locally through Ollama** will interpret conversational preferences, call a controlled set of tools (get academic-break dates, look up supported transit data, retrieve bus-provider metadata and curated attractions, check draft plans), and explain alternative travel plans. **Deterministic application code**, not the LLM, enforces schedule order, connection buffers, feed validity, budget arithmetic and exclusion of unsupported transport claims. A model response cannot create a fake departure, live fare, available seat or operating hour. Unknown facts are identified as unknown, and users are directed to official provider pages to confirm and book.

For the **final-course MVP**, a user chooses 1–5 consecutive travel days, one of two supported cities, preferred activities and a per-person daily activities budget in **USD**; Cornell Mode adds campus origin, transport type and an optional outbound/return journey. The application generates chronological day cards with attraction IDs from a curated local catalog, indicative activity fees, travel-time buffers, rationale, and a separate transportation panel showing data source and freshness. In the full NYC demo, the user can compare available *types* of travel (OurBus, Campus-to-Campus or flying via ITH) without treating any option as booked. OurBus and airline links open the provider's actual availability and price search. A user can ask “Make day two cheaper” or “Leave more time after arriving,” and the agent revises a draft and reruns validity checks. A Cornell calendar event is informative, not proof of a specific student's free time.

The bounded scope makes this an ambitious but implementable multi-component project: a React/TypeScript frontend, Python/FastAPI backend, structured attraction/provider catalogs, a versioned Cornell calendar snapshot, a **TCAT GTFS importer with service-date checks**, an Ollama client, deterministic validation and pytest/Vitest tests. Inception documented third-party integration limits and an **offline fallback** using reviewed local data; synthetic transport fixtures remain test-only rather than rider schedules. We will *not* promise live OurBus inventory or prices, airline booking, real-time flight status integration, personalized Cornell course timetable access, student login, purchases, or guaranteed transit connections. The team completed the requirements, user-story, workflow-planning, application-design and unit-generation gates, revised deployment/job assumptions through the workflow, preserved the actual `aidlc-docs/audit.md` and `aidlc-docs/aidlc-state.md`, and **stopped before Construction** for this milestone.

## Design at a glance

| | General Travel Mode | Cornell Travel Mode |
|---|---|---|
| Trip preferences | Dates, destination, interests, pace, daily activity budget | Same + North/West/Central Campus origin and transport preference |
| Calendar | User-entered travel dates | Published academic breaks and caution about individual obligations |
| Transport | Arrival/departure supplied or assumed by user | TCAT scheduled service **only within GTFS validity**; OurBus/C2C/ITH information and official booking links |
| Destination | NYC or Washington, DC curated catalog | NYC complete corridor demo; DC activity catalog (transport information limited to supported data) |
| AI | Preference parsing, tool-based candidate selection, plan explanation/revision | Same + explain Ithaca departure trade-offs, boarding buffers, unsupported/freshness gaps |
| Schedule rules | Activity non-overlap, budget checks, arrival-time boundaries | Same + connection and timezone validation |

## Documents and examples

- [`aidlc-docs/aidlc-state.md`](aidlc-docs/aidlc-state.md) — current stage and pending gates.
- [`aidlc-docs/inception/application-design/unit-of-work.md`](aidlc-docs/inception/application-design/unit-of-work.md) — U01, seven work packages, responsibilities and planned code layout.
- [`aidlc-docs/inception/application-design/unit-of-work-dependency.md`](aidlc-docs/inception/application-design/unit-of-work-dependency.md) — dependency matrix and integration checkpoints.
- [`aidlc-docs/inception/application-design/unit-of-work-story-map.md`](aidlc-docs/inception/application-design/unit-of-work-story-map.md) — full story/requirement/extension ownership map.
- [`aidlc-docs/inception/plans/unit-of-work-plan.md`](aidlc-docs/inception/plans/unit-of-work-plan.md) — approved decomposition and completed generation/final-approval checklist.
- [`aidlc-docs/inception/application-design/application-design.md`](aidlc-docs/inception/application-design/application-design.md) — approved consolidated design, links to all five design artifacts, traceability and extension review.
- [`aidlc-docs/inception/plans/application-design-plan.md`](aidlc-docs/inception/plans/application-design-plan.md) — approved design choices/background-job approach and generation checklist.
- [`aidlc-docs/inception/plans/execution-plan.md`](aidlc-docs/inception/plans/execution-plan.md) — approved lifecycle stage decisions, remaining artifacts and the stop before Construction.
- [`aidlc-docs/inception/plans/story-generation-plan.md`](aidlc-docs/inception/plans/story-generation-plan.md) — approved story approach and completed generation/approval checklist.
- [`aidlc-docs/inception/user-stories/stories.md`](aidlc-docs/inception/user-stories/stories.md) — 24 stories with acceptance scenarios and requirement coverage.
- [`aidlc-docs/inception/user-stories/personas.md`](aidlc-docs/inception/user-stories/personas.md) — four traveler archetypes and supporting local-operator role.
- [`aidlc-docs/inception/plans/user-stories-assessment.md`](aidlc-docs/inception/plans/user-stories-assessment.md) — why this project needs stories and personas.
- [`aidlc-docs/inception/requirements/requirements.md`](aidlc-docs/inception/requirements/requirements.md) — approved requirements, including the local encrypted latest-state backup policy.
- [`aidlc-docs/audit.md`](aidlc-docs/audit.md) — actual workflow request, actions and subsequent decisions.
- [`aidlc-docs/inception/requirements/requirement-verification-questions.md`](aidlc-docs/inception/requirements/requirement-verification-questions.md) — initial team verification answers.
- [`aidlc-docs/inception/requirements/requirements-clarification-questions.md`](aidlc-docs/inception/requirements/requirements-clarification-questions.md) — recorded follow-up details and enabled-extension decisions.
- [`aidlc-docs/inception/requirements/requirements-final-clarification-questions.md`](aidlc-docs/inception/requirements/requirements-final-clarification-questions.md) — recorded meeting/model responses and explicit single-laptop scope change.
- [`docs/vision.md`](docs/vision.md) — product vision, users, requirements seed, feature scope, scenarios and risks.
- [`docs/technical-environment.md`](docs/technical-environment.md) — languages/frameworks, data models, bounded LLM tool use, source-refresh policy, prohibited libraries, security, tests, sample API design.
- [`docs/data-sources.md`](docs/data-sources.md) — **source-by-source feasibility matrix** and official source links for Cornell, TCAT, OurBus, C2C, ITH and places.
- [`docs/demo-scenarios.md`](docs/demo-scenarios.md) — NYC, DC, February Break and missing-schedule examples with expected safe behavior.
- [`docs/team-review-worksheet.md`](docs/team-review-worksheet.md) — real meeting questions; **not an AI-DLC audit**.
- [`docs/ai-dlc-runbook.md`](docs/ai-dlc-runbook.md) — official v1.0.1 setup, suggested first prompt, review gates and GitHub submission.
- [`docs/rubric-checklist.md`](docs/rubric-checklist.md) — 150-point completeness checklist.
- [`examples/`](examples/) — endpoint, deterministic function and pytest examples required by the technical-environment input. **Illustrative, not a built app.**
- [`scripts/install-aidlc-v1.0.1.sh`](scripts/install-aidlc-v1.0.1.sh) — installer for **official** AWS v1.0.1 rules on macOS/Linux (Codex by default).

## Submission steps remaining

Inception is complete and the final unit artifacts are approved. Construction has not started.

1. Review the final repository changes and commit/push the root-level rules, input documents, generated `aidlc-docs/` artifacts and records. Include the move from the old nested project directory. Keep private runtime data, credentials, keys and unlicensed raw feeds out of Git.
2. Verify the final GitHub repository URL opens without signing in (private/incognito window), and that teammates have the required repository access.
3. Submit one team GitHub repository URL on Canvas by November 24, 2026, 11:59 PM ET.

These delivery steps are not marked complete by the workflow. A new instruction is required to begin the final project's Construction phase.

## Official links

- [AWS AI-DLC v1.0.1 release](https://github.com/awslabs/aidlc-workflows/releases/tag/v1.0.1) and [v1.0.1 instructions](https://github.com/awslabs/aidlc-workflows/blob/v1.0.1/README.md)
- [Cornell Registrar 2026–27 calendar](https://registrar.cornell.edu/calendars-exams/academic-calendar/2026-2027)
- [TCAT GTFS feed listing](https://www.transit.land/data/feeds/f-dr997-tompkinsconsolidatedareatransit)
- [OurBus Ithaca–NYC](https://www.ourbus.com/routes/ithaca-to-nyc)
- [Cornell C2C official schedules](https://www.fcs.cornell.edu/departments/transportation-delivery-services/campus-campus-bus-service/c2c-departure-schedule-stop-locations)
- [Ithaca Airport flight status](https://www.flyithaca.com/flights)

**Integrity note:** Inception approvals and the explicit stop before Construction are recorded in the audit. The examples are illustrative; no product code, OS security setup or runtime verification was performed. Commit/push, unauthenticated GitHub access and Canvas submission remain separate unverified delivery tasks.
