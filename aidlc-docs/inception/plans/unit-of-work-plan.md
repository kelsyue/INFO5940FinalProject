# BigRedRoutes — Unit of Work Plan

**Status:** PART 1 APPROVED at 2026-11-24T17:36:53Z; explicit 1A/2A/3A/4A choices and approval recorded in audit. Part 2 unit documentation separately approved; Inception complete and stopped before Construction.
**Prerequisites:** Approved requirements, stories/personas, execution plan and all five Application Design artifacts. See actual approvals in `../../audit.md`.
**Boundary:** Generate and approve unit documentation, then STOP before Construction. No application files, OS setup or tests are created by this plan.

## 1. Decomposition principles and applicability

Use the installed v1.0.1 terminology: a unit is a logical grouping of stories for development; a modular monolith may be one application unit with internal modules. A module is not automatically a separately deployable service. The approved product is a React UI plus one modular FastAPI runtime with process-local background jobs, Ollama and supporting local protected log collection, all on one laptop.

The purpose is manageable work with complete ownership, dependencies and acceptance outcomes, not maximizing the count of units. If there is one application unit, its module work packages still need explicit responsibilities, sequencing and story coverage. A genuinely independently packaged collector may justify its own delivery unit if the team chooses that boundary below; this does not make the business application a distributed microservice system.

| Required question category | Evidence / treatment |
|---|---|
| Story grouping | Q1 selects application-unit versus independently packaged collector; logical modules group approved capability stories |
| Dependencies | Q2 selects contract-first module checkpoints versus journey-slice delivery; both preserve approved runtime boundaries |
| Team alignment | Q3 confirms role-aligned module ownership or shared pairing; all major gates remain team decisions |
| Technical considerations | Q1 addresses independent local packaging; Q2 retains owner/version/deadline/data ownership boundaries. Cloud/scale requirements already fixed out of scope, not reopened |
| Business domain | Q1's capability modules preserve destination planning, Cornell transport/evidence and local plan/trust lifecycle without inventing new product domains |
| Greenfield code organization | Q4 selects a concrete root-relative layout consistent with the unit choice and installed code-generation patterns |

## 2. Planning checklist
- [x] Load approved design and its requirements/story coverage; confirm Units Generation is included in the execution plan.
- [x] Read installed Units rules and greenfield structure patterns from Code Generation without starting Construction.
- [x] Evaluate all six required decomposition categories and propose context-specific options.
- [x] Include unit definitions, dependency matrix/story map and greenfield code organization artifacts in generation checklist.
- [x] Receive and validate all four actual answers.
- [x] Resolve any contradictory boundaries/ownership choices using targeted questions if needed.
- [x] Obtain explicit unit-plan approval before generation.

## 3. Questions

All product/design constraints remain approved. Select letters and any requested specifics; other is available. You may answer and approve the plan in one reply. Do not assume the suggested response below has been given.

## Question 1 — Story grouping, domain boundaries and delivery units
How should delivery units reflect the approved modular application and supporting collector?

A) One application unit, U01 BigRedRoutes, containing all 24 stories and supporting local runtime integration. Define explicit logical work packages for contracts/identity/runtime, reviewed sources/TCAT, deterministic planning, owned jobs/model/tools, plan lifecycle/backup, browser UI and protected observability. The independently owned collector remains a supporting process delivered/configured within that unit, not a fabricated per-feature service. Modules and their acceptance/checkpoints make the single unit manageable.

B) Two local delivery units: U01 BigRedRoutes application (UI/modular API/its data) and U02 ProtectedLogCollector (independently installable local collector/aggregate interface under its separate OS identity). The collector has no business-plan dependency; define a neutral safe-event contract first. Assign each user story one primary application unit, with supporting collector obligations explicitly mapped instead of duplicating story ownership. No additional cloud service or remote multi-user scope.

X) Other (please describe after [Answer]: tag below; specify genuine deployable/unit boundaries and logical modules rather than naming each component a service)

[Answer]: A — One U01 application unit with explicit logical work packages; collector is a supporting process.

## Question 2 — Dependencies and integration checkpoints
How should logical work be sequenced while keeping the approved architecture intact?

A) Contract-first module checkpoints: shared typed records/guard/event interfaces first; establish local trust and data/lifecycle boundaries; build source/domain/job capabilities against those ports; then integrate UI/end-to-end acceptance. Document a dependency matrix distinguishing prerequisites from runtime calls and supporting parallel human work after contracts stabilize. Only PlanLifecycle may mutate SQLite; model/tools remain read/validate-only. These are checkpoints within the chosen unit(s), not new AI-DLC stages.

B) Journey-slice checkpoints: after shared security/contracts are defined, integrate General planning, Cornell transport context, revisions and local save/delete/recovery slices in turn. Keep the same module interfaces, sole lifecycle writer and complete cross-cutting security/test obligations; do not defer required protections until the end. Distinguish slice checkpoints from unit identities and runtime dependencies.

X) Other (please describe after [Answer]: tag below)

[Answer]: A — Contract-first module checkpoints and explicit dependency/data ownership rules.

## Question 3 — Team ownership and review
How should module responsibility align with the roles already agreed in the README?

A) Preserve role-aligned responsibility: Ananya leads repository/local runtime and protected collector integration; Sarah leads browser UX/accessibility; Dyllan leads source/TCAT permissions and data verification; Kelly leads typed architecture, domain/job/lifecycle consistency and tests. Ananya and Kelly jointly review identity/encryption/deletion boundaries. Every member still participates in major AI-DLC approvals; no claim is made that later work has already happened.

B) Shared pairing rather than fixed module leads: keep README review specialties, but assign implementation pairs at Construction planning and require one teammate's review before integration. All four still share product and gate decisions; do not invent pair assignments now.

X) Other (please describe after [Answer]: tag below)

[Answer]: A — Role-aligned responsibilities; Ananya/Kelly joint trust-boundary review; all-member gates.

## Question 4 — Greenfield code organization
Which proposed root-relative structure should unit documentation describe? This is a documentation choice only; do not create implementation directories now.

A) Use the installed conventional patterns. If Q1=A: `src/frontend/`, `src/backend/`, `src/collector/` for application-delivered collector code/configuration, mirrored `tests/` subdirectories, `tests/fixtures/`, and root `config/`/existing `scripts/`. If Q1=B: `application/src/frontend/`, `application/src/backend/`, `application/tests/`, `collector/src/`, `collector/tests/`, each unit's non-secret config, and root orchestration scripts. Shared event/schema contract is versioned without either unit importing business code from the other. Existing input docs/examples/rules stay at root; runtime private data/keys/logs/archives remain outside Git and outside `aidlc-docs/`.

B) Use the same single-unit versus independent-unit root patterns, with a namespaced code layer: for Q1=A, `src/bigredroutes/frontend/`, `src/bigredroutes/backend/`, `src/bigredroutes/collector/` and mirrored tests; for Q1=B, `application/src/bigredroutes/` and `collector/src/protected_logs/` with their own tests/config. Preserve the same private-data and documentation separation.

X) Other (please describe after [Answer]: tag below; provide concrete code/test/config paths consistent with the approved local deployment)

[Answer]: A — Conventional single-unit src/frontend, src/backend, src/collector, mirrored tests, config and existing scripts.

## 4. Generation checklist — after validated answers and explicit approval

- [x] Load the approved plan/answers; record unit choice, module grouping, dependencies, team alignment and directory conventions.
- [x] Generate `../application-design/unit-of-work.md`.
  - [x] Define each unit's purpose, responsibilities, component/module boundary, interfaces, owned data, supporting role obligations and completion criteria.
  - [x] Define manageable logical work packages without confusing modules/checkpoints with independently deployed services or AI-DLC stages.
  - [x] Document greenfield root-relative code/test/config strategy using the installed rules; preserve root `aidlc-docs/` for documentation only.
  - [x] Carry all security/source/deadline/cancellation/backup/deletion and accessibility acceptance obligations; no approved scope reduction.
- [x] Generate `../application-design/unit-of-work-dependency.md`.
  - [x] Include unit-level and logical work-package dependency matrices, integration/checkpoint order and data ownership rules.
  - [x] Distinguish construction prerequisites from runtime calls/events and shared support contracts; a single-unit matrix explicitly states no inter-unit dependency, not a fake multi-service diagram.
  - [x] Provide validated dependency diagrams and text alternatives where useful, with no unaddressed cyclic construction prerequisites.
- [x] Generate `../application-design/unit-of-work-story-map.md`.
  - [x] Assign US-01–24 exactly one primary unit each; map logical module contributions and supporting unit/process obligations without duplicate ownership.
  - [x] Carry all 22 FRs and 14 NFRs through story/cross-cutting mappings; no orphan or dropped acceptance obligation.
- [x] Validate unit/module boundaries against all five approved design artifacts and the chosen directory strategy.
- [x] Review enabled-extension applicability and map future Functional/NFR/Code/Build verification obligations to the chosen unit(s); do not execute those stages now.
- [x] Validate files, story coverage, matrices/graphs, IDs/links and all answered question markers; update checkboxes/state and append actual actions to audit.
- [x] Present the generated units/dependency/story-map files for explicit team approval.
- [x] On actual artifact approval, mark Inception complete and STOP before Construction; log that stop explicitly.

## 5. Extension and final-product handoff

Security, Resiliency and full PBT remain enabled. All chosen unit(s) must preserve the approved local identity/HTTPS/encryption/collector and deletion-safe snapshot architecture. Cloud-only infrastructure/production guarantees remain N/A; actual OS controls and crash algorithms still need Construction verification. Full PBT property identification, generators, shrinking/seeds and scenario tests remain later applicable-stage obligations. Assign cross-cutting work explicitly even when only one primary application unit owns a traveler story.

Construction will apply AI-DLC's per-unit lifecycle to the approved unit(s), with internal module checkpoints for manageability. It is not authorized by this milestone plan. Any question about release/rollback, incident response or resiliency test processes permitted at NFR Design remains a future user decision; this plan does not invent those answers.

## 6. Plan approval prompt

**Unit of work plan complete. Review the plan in `aidlc-docs/inception/plans/unit-of-work-plan.md`. Ready to proceed to generation?**

Answer Q1–Q4 and explicitly approve the plan, or request changes. If all A choices fit, you may reply **“1A, 2A, 3A, 4A. Approve the unit-of-work plan.”** That example is not an actual answer or approval.

The generated units will require a separate approval. At that final milestone gate, the continuation is **approve units and stop before Construction**, overriding the generic rule prompt that offers Construction.


No contradictory answer detected. All four explicit selections are recorded; no follow-up clarification required. Actual approval applies to the plan only.


## Generation result

All three artifacts generated and checked: U01 with seven logical work packages, all 15 components assigned once, all 24 stories assigned once to U01 and a primary package, all 36 requirements and 40 extension responsibilities mapped; construction-prerequisite graph acyclic. Final artifact approval received and explicit Inception stop recorded. Documentation checks recorded 2026-11-24T17:42:08Z; no runtime results inferred.


## Final approval and stop

Recorded 2026-11-24T17:44:20Z; exact user response: “Approve units and stop before Construction”. All Units planning/generation/review checklist items complete. Inception complete. STOPPED BEFORE CONSTRUCTION. Submission delivery tasks remain separate and unverified.
