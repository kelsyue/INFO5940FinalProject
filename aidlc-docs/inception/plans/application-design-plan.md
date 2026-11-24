# BigRedRoutes — Application Design Plan

**Status:** UPDATED PLAN APPROVED at 2026-11-24T17:26:04Z; exact user input “Approve the updated application-design plan” (including quotation marks in the raw audit record). Design documentation generated; generated artifacts separately approved; Application Design complete.
**Prerequisites:** Requirements, stories/personas and execution plan approved. See actual approvals in `../../audit.md`.
**Scope:** High-level components, responsibilities, interfaces, orchestration and dependencies. Detailed algorithms, exact package pins, code and tests remain Construction work. One laptop, no cloud.

## 1. Context and design objectives

Preserve the approved 22 FRs, 14 NFRs and 24 user stories. General NYC/DC planning and Cornell campus-origin/NYC research share a deterministic planning core. The local model interprets/narrates through a restricted tool interface; it cannot manufacture source data or change the trusted saved state directly. Confirmed activity windows, applicable GTFS service, truthful cost/source status, scoped revisions and explicit fallback are hard boundaries.

Local authorization, encrypted persistence/backups, secure serving, protected centralized logs and deletion-safe recovery are already accepted requirements. This gate chooses a reviewable architecture to satisfy them; it does not silently replace them with unprotected HTTP, plaintext SQLite or an application-writable audit log. All options are local; none introduce cloud hosting or a Cornell account.

## 2. Planning checklist
- [x] Load approved requirements, stories/personas and execution-plan decisions.
- [x] Review component, interface, orchestration, dependency and architectural-pattern concerns.
- [x] Identify unresolved local identity, persistence/logging and recovery boundaries.
- [x] Include all mandatory design artifacts and an explicit verification checklist.
- [x] Receive five actual answers and validate consistency with approved requirements.
- [x] Validate the explicit background-job choice; provide concrete proposed job semantics below for plan review. No conflicting answer requires another question file.
- [x] Receive explicit approval of this design approach before generation.

## 3. Proposed component inventory for review

Candidate responsibilities, not final design decisions:

- Browser UI: mode/input forms, confirmed windows, day cards, provenance/budget, revision diff/confirmation, saved-plan controls and textual readiness.
- API boundary: schema validation, local session/object authorization, deadlines, safe errors and correlation identifiers.
- Planning orchestration: local owned background jobs for generation/revision, typed polling/cancellation, bounded model tools, deterministic plan validation and explicit plan completeness/fallback status. Request orchestration and job states are distinct from itinerary states.
- Source adapters: academic snapshot, provider directory, attraction catalog and locally imported TCAT; typed source records with applicability/status.
- Deterministic domain services: input/window, service-date/transfer, schedule, budget and provenance validation.
- Plan lifecycle boundary: versioned save/revise/read/delete/reset, encrypted persistence, serialized mutation and deletion-safe snapshot/restore.
- Local runtime trust boundary: secure loopback serving, protected keys/identity, independent protected log collection and local operational/security status.

Exact names/method contracts, service/module distinction and dependency directions will be generated after approval. This list is not a unit-of-work decomposition or a reason to create distributed services.

## 4. Design questions

Choose a letter for each. Options A form a coherent proposed local architecture; alternatives are available where the trade-off matters. You may answer in the conversation, and can approve this plan in the same reply if the answers are complete and consistent.

## Question 1 — Component boundaries and architecture style
How should the application be organized on the laptop?

A) React frontend plus one modular FastAPI application. Keep source adapters, bounded LLM orchestration, deterministic planning/validation and plan lifecycle as explicit internal modules behind typed interfaces. Ollama and the separately protected local log collector are supporting processes, not one microservice per feature.

B) React frontend plus separately running local planning and data/persistence services, with typed local API contracts and explicit failure handling between them. Still one laptop and no cloud, accepting extra local deployment/integration complexity.

X) Other (please describe after [Answer]: tag below)

[Answer]: A) React frontend plus one modular FastAPI application. Keep source adapters, bounded LLM orchestration, deterministic planning/validation and plan lifecycle as explicit internal modules behind typed interfaces. Ollama and the separately protected local log collector are supporting processes, not one microservice per feature

## Question 2 — Orchestration and interface results
Which request/response coordination model should planning and revision use? Both retain validated typed results and a single overall 150-second budget, six tool calls, 15 seconds per tool and one repair maximum.

A) One bounded API response per operation, using asynchronous I/O internally but no durable background job system. Return a typed result containing plan/diff, complete/partial/pending/fallback status, unmet constraints and provenance. Domain/source interfaces use explicit input/result types; model output cannot call persistence or bypass validators.

B) Submit a local background job and poll a typed progress/result endpoint. Jobs have explicit owner, deadline, cancellation/expiry and bounded resource use; the same result/provenance and validation boundaries apply. Accept the extra job-state API and failure/restart semantics.

X) Other (please describe after [Answer]: tag below)

[Answer]: B — Background job system selected; typed plan/diff/status, unmet constraints, provenance and validated interfaces retained. Original response: background job system. Return a typed result containing plan/diff, complete/partial/pending/fallback status, unmet constraints and provenance. Domain/source interfaces use explicit input/result types; model output cannot call persistence or bypass validators.

## Question 3 — Local identity without external accounts
How should the approved saved-plan authorization work without Cornell login or public signup?

A) Single local owner identity tied to the laptop user's protected app configuration. A short-lived single-use launch/bootstrap token establishes an expiring same-origin local HTTPS session, then is invalidated; it is not stored in browser local storage or logs. Cookies are Secure/HttpOnly/SameSite=Strict, mutations use origin/CSRF protection, saved plans are owner-scoped, session logout/expiry invalidates access, and bootstrap/session endpoints are rate-limited. Key material is OS-protected. No new password/admin account feature.

B) Explicit local passphrase login for the laptop owner, accepting a new local authentication feature and its full applicable credential protections (adaptive password hashing, breached-password checks, brute-force protection, session expiry/logout, secure cookies and any administrative-role/MFA applicability). Still no external identity provider.

X) Other (please describe after [Answer]: tag below; no-auth access to saved IDs would change an approved requirement)

[Answer]: A) Single local owner identity tied to the laptop user's protected app configuration. A short-lived single-use launch/bootstrap token establishes an expiring same-origin local HTTPS session, then is invalidated; it is not stored in browser local storage or logs. Cookies are Secure/HttpOnly/SameSite=Strict, mutations use origin/CSRF protection, saved plans are owner-scoped, session logout/expiry invalidates access, and bootstrap/session endpoints are rate-limited. Key material is OS-protected. No new password/admin account feature.

## Question 4 — Local storage, secure serving and protected logs
Which trust-boundary mechanism should design target for the accepted local security requirements? These are proposals requiring feasibility verification during Construction, not claims that the laptop is already configured.

A) Keep standard SQLite inside a dedicated OS-encrypted private storage volume/container with OS-protected key/unlock handling; all app-owned persistent source caches and plan snapshots live in protected storage. Refuse stateful startup when required protection is unavailable. Serve the browser/API through one local HTTPS origin with the required headers; keep internal model calls loopback/private and evaluate their TLS applicability explicitly. A separate local collector under a distinct OS identity owns protected append-only/tamper-evident security logs with 90-day retention; app code can submit events but cannot rewrite/delete retained logs. Include a safe aggregate local status/alert view, not raw sensitive logs. Accept additional operator setup/permissions to establish that boundary.

B) Use a vetted encrypted SQLite-compatible storage adapter plus separately encrypted cache/snapshot files with OS-protected keys. Keep the same single HTTPS browser origin and separately owned local log collector/status view as A, accepting an additional database-encryption dependency to validate and pin.

X) Other (please describe after [Answer]: tag below; specify how encryption, key handling, HTTPS/headers and log modification isolation remain satisfied)

[Answer]: A) Keep standard SQLite inside a dedicated OS-encrypted private storage volume/container with OS-protected key/unlock handling; all app-owned persistent source caches and plan snapshots live in protected storage. Refuse stateful startup when required protection is unavailable. Serve the browser/API through one local HTTPS origin with the required headers; keep internal model calls loopback/private and evaluate their TLS applicability explicitly. A separate local collector under a distinct OS identity owns protected append-only/tamper-evident security logs with 90-day retention; app code can submit events but cannot rewrite/delete retained logs. Include a safe aggregate local status/alert view, not raw sensitive logs. Accept additional operator setup/permissions to establish that boundary.

## Question 5 — Consistency, snapshots and deletion-safe recovery
Which high-level lifecycle boundary should coordinate saves, targeted revisions, deletion and restore? Both preserve the approved latest-state encrypted snapshot policy and no resurrection of deleted plans; detailed transaction/crash algorithms belong to Functional Design.

A) One plan lifecycle coordinator owns every mutation and restore, serializes writers and uses plan-version checks so stale revisions cannot overwrite newer state. It creates/verifies/replaces the encrypted latest-state database snapshot after successful saves. A durable deletion ledger is enforced during reads/restores; retained copies containing removed data are purged/rewritten before deletion/reset is reported complete. Interrupted operations fail closed; a restore cannot bypass ownership or deletion decisions. Backup failure is explicitly reported and never falsely labeled fully saved-and-backed-up.

B) Separate per-plan lifecycle aggregates with version checks and per-plan encrypted latest-state recovery records, coordinated by an owner-scoped manifest. Delete/reset removes all affected recovery material and records durable deletion decisions before any restore can expose records. Accept the extra manifest/key/recovery consistency work; no historical plan-version archive is introduced.

X) Other (please describe after [Answer]: tag below)

[Answer]: A) One plan lifecycle coordinator owns every mutation and restore, serializes writers and uses plan-version checks so stale revisions cannot overwrite newer state. It creates/verifies/replaces the encrypted latest-state database snapshot after successful saves. A durable deletion ledger is enforced during reads/restores; retained copies containing removed data are purged/rewritten before deletion/reset is reported complete. Interrupted operations fail closed; a restore cannot bypass ownership or deletion decisions. Backup failure is explicitly reported and never falsely labeled fully saved-and-backed-up.

## 5. Generation steps — execute after validated answers and approval

- [x] Load the approved plan/answers; document architectural decisions and actual trade-offs without inventing validations or approvals.
- [x] Generate `../application-design/components.md`.
  - [x] Define each component's purpose, high-level responsibility, trust boundary, inputs/outputs and public interface.
  - [x] Classify local workload criticality and describe user impact of model/source/API/storage unavailability.
- [x] Generate `../application-design/component-methods.md`.
  - [x] Define typed interface signatures and result/error shapes for request interpretation, source lookup, deterministic validation, revision and plan lifecycle.
  - [x] Preserve complete/partial/pending/fallback semantics and version/owner/provenance fields; no detailed scheduling/GTFS/security algorithms or implementation code.
- [x] Generate `../application-design/services.md`.
  - [x] Describe background-job submission/poll/cancel/restart behavior for both modes, model/tool limits and fallback; data/source and persistence dependencies are explicit.
  - [x] Describe secured local session flow, encrypted storage/snapshot boundary, log collection/status and deletion/restore coordination at a high level.
- [x] Generate `../application-design/component-dependency.md`.
  - [x] Include a dependency matrix, permitted communication patterns and data-flow diagrams with text alternatives.
  - [x] Show model/source text entering validation as untrusted data; prevent UI/model bypass of owner checks or persistent mutation boundaries.
- [x] Generate `../application-design/application-design.md` consolidating the design and key decisions.
  - [x] Include requirement/story coverage and explicit local deployment/no-cloud scope.
  - [x] Record future feasibility checks and deferred stage-specific decisions; do not present mechanisms as proven working.
- [x] Verify every FR/NFR and US-01–24 maps to designed responsibility/interface/service or an explicit future verification obligation.
- [x] Review each enabled Security/Resiliency/PBT rule as compliant at this design stage, non-compliant/blocking or N/A with rationale. Resolve actual blocking findings before presenting approval.
- [x] Validate Markdown, type/identifier consistency, diagrams and links; update plan checkboxes, state and append actual actions/review prompt to audit.
- [x] Present generated design for separate approval.
- [x] Receive explicit generated-design approval before Units Generation.

## 6. Deferred work and extension coverage

- Application Design supplies architectural feasibility and trust-boundary choices, not package installation, certificates, key creation, OS account changes or application code. None of those external/system changes are performed merely by approving a document.
- SECURITY-01/03/04/08/12/14 are substantive local design concerns addressed by Q3–Q5; remaining Security rules are reviewed against the generated artifact responsibilities and approved acceptance obligations. Cloud-only resources remain N/A only where absent.
- RESILIENCY-01 workload/dependency classification and RESILIENCY-05–07/10/12–13 local health/failure/restore responsibilities are included in the design checklist. Production regional availability/scaling remain N/A. CI/release/rollback, incident-process and resiliency-test-process questions permitted at NFR Design remain at that later gate; no existing organizational process is invented.
- Full PBT stays enabled. High-level interfaces must support test isolation and preserve domain invariants; formal property identification, generators, shrinking/seeds, dependency configuration and tests occur at their applicable per-unit Construction stages.
- Units/count/story assignment are decided at Units Generation after this design is approved. One modular backend does not automatically mean a separately deployable service per internal module.

## 7. Validated choices and revised background-job proposal

Recorded choices are **1A, 2B, 3A, 4A, 5A**. Q2 says “background job system”; it is mapped to B rather than recorded as A or silently ignored. Its typed results and trust boundaries remain intact. The proposal below makes that choice concrete for approval; resource/retention values are proposed design defaults, not values the user already supplied.

- **Local job coordinator:** A bounded worker/job registry within the modular FastAPI runtime; no external broker, cloud queue or new separately deployed planning service. Generation and natural-language revision use jobs; ordinary reference/readiness/saved-plan reads remain direct bounded API requests.
- **Submit/poll/cancel:** Authenticated owner-scoped submit returns an accepted job ID; typed status/result polling and cancellation check the same local principal, expiry and permissions. Exact routes/signatures are generated after approval. Unknown/other-owner IDs cannot reveal inputs/results.
- **Separate states:** Job lifecycle is queued/running/succeeded/failed/cancelled/expired. Itinerary outcome is complete/partial/pending-confirmation, with normal/fallback execution mode separately identified. A successful job may produce a partial itinerary; a queued job is not the same as an itinerary awaiting user input.
- **Bounded workload:** Proposed default is one active planning/revision job and at most one waiting job on the 16 GB demo laptop; reject excess submissions with an explicit busy/retry response, not an unbounded queue. The 150-second overall deadline begins when submission is accepted, including queue wait, all tools and the one allowed repair. No tool exceeds 15 seconds and no job exceeds six tool calls. The 120-second warmed-model performance target remains unmeasured.
- **Cancellation and deadline:** Cancelled/expired jobs cannot save or overwrite plans or publish late results. Guard every persistent commit with current job permission/deadline/cancellation and expected plan version through the selected lifecycle coordinator. If a short protected commit already finished before cancellation was accepted, report that actual committed result; do not falsely claim cancellation undid it.
- **Transient jobs:** Keep raw natural-language input and job results in bounded process memory only; never in SQLite/backups/security logs. Proposed completed-result retention is five minutes or until owner logout, deletion/reset or shutdown, whichever occurs first. Erase request text as soon as interpretation no longer needs it. A saved itinerary persists only as structured authorized plan data under the already approved lifecycle rules.
- **Restart behavior:** Do not resume jobs automatically after API restart. Transient jobs/results are lost; the UI explains interruption/unavailability and allows an explicit resubmission. Previously committed structured plans survive. A client must check saved state/current version before resubmitting a revision so work is not blindly replayed.
- **Deletion/logout/reset:** Invalidate/cancel affected jobs, discard their transient results and prevent late writes or resurrection. The durable deletion ledger and serialized plan lifecycle remain authoritative across job restarts and snapshot restores. Session expiry/logout revokes job access and cancels the session's unfinished work.
- **Fallback and failure:** Model failures may produce the same visibly labeled deterministic fallback from structured inputs. Failed jobs retain safe structured error categories, not stack traces/private prompts; prior saved state remains intact. Queue/job metadata and safe aggregate counters can be observed without exposing raw travel content.

### Requirements and story compatibility

This selects an interface coordination mechanism, not a change to the 22 FRs, 14 NFRs or 24 story outcomes. FR-16/18 and NFR-02 limits now apply to the entire accepted job, not just the initial HTTP response. FR-20/NFR-07 ownership also applies to jobs. US-15–23 acceptance behavior extends to polling/cancellation, late results and restart without weakening saved-state, privacy or deletion guarantees. A raw job transcript is never made into a persistent chat history.

## 8. Approval instructions

Review the five recorded choices and the concrete job proposal above. Reply **“Approve the updated application-design plan”** to authorize generation, or request changes to a specific choice/default. Your answers have been recorded; no need to paste them again.

Generated design artifacts will require their own subsequent review. Plan approval does not authorize Construction, certificates, OS changes or implementation.


## Generation and validation result

Generated all five mandatory design artifacts. Checked 15 component IDs, typed contracts and dependency rows; mapped all 22 FRs, 14 NFRs and 24 stories; reviewed all 40 extension rule IDs; checked table/Markdown/link consistency and both diagram graphs using basic grammar validation with text alternatives. No full renderer or implementation verification claimed. Review prompt recorded 2026-11-24T17:33:06Z; generated-design approval pending.

Generated design approved 2026-11-24T17:34:08Z; exact response “Approve & Continue”. Unit planning is next, not Construction.
