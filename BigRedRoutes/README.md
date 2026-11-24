# BigRedRoutes — Travel Planning for Cornell and Beyond

> **AI-DLC Mid-semester Milestone | November 24, 2026, 11:59 PM ET | 150 points**  
> **Workflow version:** AWS AI-DLC **v1.0.1** only (not v2)  
> **Project status:** Proposed inputs ready for actual team review. The official rule files and genuine AI-DLC Inception outputs are **not included** until your team runs the workflow.  
> **Proposed coding agent:** OpenAI Codex; **planned product LLM:** Qwen3 4B through Ollama. These are separate roles.

## Team and collaboration

**Team members and proposed responsibilities:** Roles remain subject to team confirmation.

| Full name | Cornell NetID | Proposed responsibility (confirm) |
|---|---|---|
| Ananya Jajodia | aj477 | Repository maintenance, AI-DLC session operator |
| Sarah Park | sp2227 | Product/UX, user stories, accessibility |
| Dyllan Hofflich | drh253 | Transport integrations and data verification |
| Kelly Yue | ky387 | Architecture, test plans, consistency review |

**Proposed collaboration arrangement:** All members attend major AI-DLC Inception approval sessions, review AI-generated material and question unsupported choices before approval. Two 45-minute synchronous meetings per week, plus asynchronous GitHub Issues/PR comments, is a starting proposal, not a claim about the team's actual meetings. Each member owns a review area; the session operator records agreed answers in the coding agent. If the team chooses another cadence, record the agreed plan here. Only one member submits the public GitHub URL on Canvas.

## Project overview — five paragraphs

Travel planning is challenging for everyone, but Cornell students in Ithaca face an extra hurdle before the vacation even begins: figuring out **when** to travel around academic commitments and **how** to get from campus to a bus stop, the airport, or another city without a car. Travel details are scattered across Cornell's academic calendar, TCAT, OurBus, Cornell Campus-to-Campus, airline/airport sites, and destination guides. A student planning a weekend in New York City must piece together departure location, campus-to-terminal connection, boarding buffer, estimated cost, and a workable arrival-day schedule. General-purpose itinerary applications typically focus on the destination rather than this campus-specific first and last mile. **BigRedRoutes** provides one understandable journey, from Cornell to destination activities and back.

BigRedRoutes serves two audiences through **two explicit modes**. In **General Travel Mode**, any traveler can enter their destination, travel dates, interests, budget and preferred pace to build a personalized destination itinerary. In **Cornell Travel Mode**, a traveler additionally selects a campus departure area (North, West or Central Campus), receives official Cornell academic-break context, and explores transport options from Ithaca: scheduled TCAT connections where supported by valid feed data, Cornell Campus-to-Campus service, OurBus provider links and Ithaca Tompkins International Airport (ITH) information. Cornell Mode adds useful local context without restricting the whole product to students. MVP destination activity catalogs will cover **New York City and Washington, DC**, with NYC as the full transportation-coordination demo and DC as a general itinerary demo.

A large language model is useful because requests combine nuanced intent and multiple constraints: “I have February Break, live on North Campus, want a cheap, low-stress NYC weekend, and prefer museums and food.” The proposed **Qwen3 4B model running locally through Ollama** will interpret conversational preferences, call a controlled set of tools (get academic-break dates, look up supported transit data, retrieve bus-provider metadata and curated attractions, check draft plans), and explain alternative travel plans. **Deterministic application code**, not the LLM, enforces schedule order, connection buffers, feed validity, budget arithmetic and exclusion of unsupported transport claims. A model response cannot create a fake departure, live fare, available seat or operating hour. Unknown facts are identified as unknown, and users are directed to official provider pages to confirm and book.

For the **final-course MVP**, a user chooses 1–5 consecutive travel days, one of two supported cities, preferred activities and a per-person daily activities budget in **USD**; Cornell Mode adds campus origin, transport type and an optional outbound/return journey. The application generates chronological day cards with attraction IDs from a curated local catalog, indicative activity fees, travel-time buffers, rationale, and a separate transportation panel showing data source and freshness. In the full NYC demo, the user can compare available *types* of travel (OurBus, Campus-to-Campus or flying via ITH) without treating any option as booked. OurBus and airline links open the provider's actual availability and price search. A user can ask “Make day two cheaper” or “Leave more time after arriving,” and the agent revises a draft and reruns validity checks. A Cornell calendar event is informative, not proof of a specific student's free time.

The bounded scope makes this an ambitious but implementable multi-component project: a React/TypeScript frontend, Python/FastAPI backend, structured attraction/provider catalogs, a versioned Cornell calendar snapshot, a **TCAT GTFS importer with service-date checks**, an Ollama client, deterministic validation and pytest/Vitest tests. Inception will explicitly document third-party integration limits and an **offline fixture fallback** so the team can demo without live network access. We will *not* promise live OurBus inventory or prices, airline booking, real-time flight status integration, personalized Cornell course timetable access, student login, purchases, or guaranteed transit connections. During Inception, the team will complete all requirements, user-story, workflow-planning, application-design and unit-generation gates; challenge any inaccurate live-data assumptions; preserve the real `aidlc-docs/audit.md` and `aidlc-docs/aidlc-state.md`; and **stop before Construction** for this milestone.

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

- [`docs/vision.md`](docs/vision.md) — product vision, users, requirements seed, feature scope, scenarios and risks.
- [`docs/technical-environment.md`](docs/technical-environment.md) — languages/frameworks, data models, bounded LLM tool use, source-refresh policy, prohibited libraries, security, tests, sample API design.
- [`docs/data-sources.md`](docs/data-sources.md) — **source-by-source feasibility matrix** and official source links for Cornell, TCAT, OurBus, C2C, ITH and places.
- [`docs/demo-scenarios.md`](docs/demo-scenarios.md) — NYC, DC, February Break and missing-schedule examples with expected safe behavior.
- [`docs/team-review-worksheet.md`](docs/team-review-worksheet.md) — real meeting questions; **not an AI-DLC audit**.
- [`docs/ai-dlc-runbook.md`](docs/ai-dlc-runbook.md) — official v1.0.1 setup, suggested first prompt, review gates and GitHub submission.
- [`docs/rubric-checklist.md`](docs/rubric-checklist.md) — 150-point completeness checklist.
- [`examples/`](examples/) — endpoint, deterministic function and pytest examples required by the technical-environment input. **Illustrative, not a built app.**
- [`scripts/install-aidlc-v1.0.1.sh`](scripts/install-aidlc-v1.0.1.sh) — installer for **official** AWS v1.0.1 rules on macOS/Linux (Codex by default).

## To finish the actual assignment

1. Confirm the two-mode scope, demo laptop, team details and approvals; adjust the proposed decisions rather than assuming they are final.
2. In the repository root, run `bash scripts/install-aidlc-v1.0.1.sh codex` (or follow the official v1.0.1 guide for another agent). **Commit** `AGENTS.md` and all `.aidlc-rule-details/` rules, including hidden files/directories.
3. Open the project with that coding agent, confirm it recognizes AI-DLC, and give it the exact starter prompt in [`docs/ai-dlc-runbook.md`](docs/ai-dlc-runbook.md).
4. Review, challenge when justified, answer actual generated verification questions and approve each stage as a team: Requirements Analysis → User Stories → Workflow Planning → Application Design → Units Generation.
5. Verify all genuine generated artifacts under `aidlc-docs/inception/`, plus the conversation-backed `aidlc-docs/audit.md` and `aidlc-docs/aidlc-state.md`. **Do not hand-create or pretend these are AI-DLC outputs. Stop before Construction.**
6. Commit/push and submit **one publicly accessible GitHub repository URL** before the course deadline.

## Official links

- [AWS AI-DLC v1.0.1 release](https://github.com/awslabs/aidlc-workflows/releases/tag/v1.0.1) and [v1.0.1 instructions](https://github.com/awslabs/aidlc-workflows/blob/v1.0.1/README.md)
- [Cornell Registrar 2026–27 calendar](https://registrar.cornell.edu/calendars-exams/academic-calendar/2026-2027)
- [TCAT GTFS feed listing](https://www.transit.land/data/feeds/f-dr997-tompkinsconsolidatedareatransit)
- [OurBus Ithaca–NYC](https://www.ourbus.com/routes/ithaca-to-nyc)
- [Cornell C2C official schedules](https://www.fcs.cornell.edu/departments/transportation-delivery-services/campus-campus-bus-service/c2c-departure-schedule-stop-locations)
- [Ithaca Airport flight status](https://www.flyithaca.com/flights)

**Integrity note:** This is a documented **Inception starter**, not a representation that AWS rules have already been installed, the team has approved the design, or a complete working product or AI-DLC audit exists.
