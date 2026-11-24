# BigRedRoutes — Consolidated Application Design

**Status:** APPROVED. Exact user response “Approve & Continue”, recorded 2026-11-24T17:34:08Z in `../../audit.md`. No implementation, OS configuration or test success is implied.
**Authority:** Approved requirements, stories/personas, execution plan and updated application-design plan. Choices: 1A modular backend, 2B background jobs, 3A local bootstrap/session, 4A encrypted local volume and independent protected logs, 5A serialized versioned lifecycle/deletion ledger.

## 1. Architecture and document map

One laptop hosts a React UI, one modular FastAPI runtime, Ollama and supporting secure local serving/log collection. Source/catalog and deterministic domain logic are internal modules; there is no per-feature microservice, cloud broker, remote account system or cloud availability topology.

- [Components](components.md): C01–C15 purposes, responsibilities, interfaces/trust boundaries and local criticality.
- [Methods/contracts](component-methods.md): shared types, API routes, internal typed ports, safe errors and bounded design defaults.
- [Services](services.md): S01–S07 sessions, background jobs, planning/source orchestration, versioned mutation, recovery and protected observability.
- [Dependencies](component-dependency.md): allowed-call matrix, planning/deletion/restore flows and text alternatives.

These files together are the Application Design artifact. This consolidated document records decisions, traceability, extension review and outstanding verification so no single diagram is mistaken for a full design.

## 2. Decisions and rationale

| Decision | Adopted mechanism | Trade-off / consequence |
|---|---|---|
| AD-01 Local modular application | One FastAPI runtime with explicit source/model/domain/lifecycle modules and React UI | Avoids distributed application setup; internal interfaces and tests still enforce boundaries |
| AD-02 Background jobs | Process-local owned queue, one active/one waiting compute job, typed poll/cancel, memory-only results | Keeps UI responsive; restart interrupts transient jobs and requires explicit resubmission, not durable replay |
| AD-03 Honest independent states | Job lifecycle separate from itinerary completeness and fallback mode | A successful job can return a partial/pending plan; UI cannot infer persistence or feasibility from job success |
| AD-04 Bounded agent | Restricted tools, six calls/one repair, 15-second tool cap and 150-second accepted-job total budget including queue wait | Slow requests degrade/fail safely; 95%-within-120-second performance still needs a benchmark |
| AD-05 Local identity | OS-protected stable owner config; one-use bootstrap, expiring opaque server session, secure cookies and origin/CSRF checks | No public signup/password/admin account; OS-controlled setup/restore is separate from browser identity |
| AD-06 Encrypted runtime | Standard SQLite/cache/ledger/snapshot/temp paths inside verified OS-encrypted private storage; collector has its own protected encrypted store | Extra local setup/key/unlock feasibility work; missing protection blocks affected stateful startup |
| AD-07 Independent safe logs | Separate OS identity, restricted local IPC, protected append/tamper-evident store, ≥90-day security retention and aggregate alerts | App cannot rewrite/delete its own retained audit; no private prompt/itinerary bodies logged. OS/root compromise not covered |
| AD-08 Sole mutation boundary | C11 owner/version/domain/guard checks and serialized mutation; explicit save, no model/tool repository writes | Stale jobs and unconfirmed broader edits cannot overwrite current plans; mutation concurrency needs formal crash/lock design |
| AD-09 Latest-state recovery | Verified encrypted snapshot after saves, separate current deletion ledger, purge/fence retained copies, maintenance restore | No deleted-plan resurrection through app-managed restore; no numeric RTO/RPO or total-laptop-loss guarantee |
| AD-10 Source status authority | Immutable referenced source versions/stamps plus deterministic checks, unknown explicit | No invented GTFS applicability, venue hours, costs or bookings; historical source claims require actual review |

The five-minute job result retention, queue size and job restart behavior were explicitly included in the approved updated plan. Additional session/input bounds in the method document are design defaults offered in this generated design for review, not retrospective user-supplied facts.

## 3. Invariants and failure boundaries

1. Model/source/browser text is never authorization or truth authority. Typed constraints/evidence cross validation before output or save.
2. General mode is destination-only; Cornell mode adds public academic/origin/NYC transport context. No Cornell–DC transport guarantee or personal course access.
3. A confirmed TCAT result needs actual service/date/path applicability. An activity window is not proof of an intercity departure. Unknown hours remain unscheduled; unknown fees remain incomplete.
4. A job has at most six tool calls, one repair and 150 seconds from accepted submission including queueing. Cancellation/session expiry/deletion prevents future publication/commit; a prior committed save cannot be falsely undone by a cancellation receipt.
5. Explicit saved-plan mutations require current owner/session, expected version, valid exact confirmation and domain checks. Raw browser submission cannot claim it was a trusted validated job result.
6. A delete/reset is not complete until current durable fences and app-managed recoverable-copy purge/rewrite prevent resurrection. Restore cannot roll back current ledger, identity/session revocation or epoch state. Missing ledger/keys fails closed.
7. Model fallback is permitted; missing authorization/encryption/log integrity is not a fallback permission. Component failure cannot silently drop safeguards.
8. No raw chats persist in browser storage, job database, saved plans, snapshots or logs. Structured preferences necessarily retained in a saved itinerary remain private owner-scoped data.

## 4. Requirement and story coverage

All story IDs below refer to the approved `../user-stories/stories.md`; mapping identifies responsibility, not a claim of completed acceptance tests.

| Requirement | Responsible components / services | Stories |
|---|---|---|
| FR-01 | C01/C02/C05, S03 | US-01, US-24 |
| FR-02 | C01/C02/C10 | US-01, US-02, US-12 |
| FR-03 | C01/C08/C09/C10 | US-02 |
| FR-04 | C08/C05, S04 | US-05 |
| FR-05 | C08/C05, S04 | US-06 |
| FR-06 | C09/C14, S04 | US-07 |
| FR-07 | C09/C10, S04 | US-08 |
| FR-08 | C09/C10 | US-09 |
| FR-09 | C01/C10/C05 | US-04, US-11 |
| FR-10 | C09/C10 | US-04, US-09, US-11 |
| FR-11 | C08/C10 | US-10 |
| FR-12 | C10/C05 | US-11, US-15 |
| FR-13 | C10/C01 | US-12, US-15 |
| FR-14 | C10/C05/C01 | US-13, US-15, US-16 |
| FR-15 | C06/C07/C10/C05 | US-03 |
| FR-16 | C04/C05/C06/C07/C10, S02/S03 | US-03, US-18 |
| FR-17 | C01/C04/C05/C10/C11 | US-15, US-16 |
| FR-18 | C04/C05/C10/C13 | US-17, US-18 |
| FR-19 | C08/C09/C10/C05/C01 | US-05, US-06, US-08, US-10, US-14 |
| FR-20 | C02/C03/C04/C11/C12/C14, S05/S06 | US-19, US-20, US-21, US-22 |
| FR-21 | C01/C05/C07/C08 | US-06, US-14 |
| FR-22 | C02/C04/C13/C15 | US-13, US-17, US-23 |
| NFR-01 | C01/C02/C14, S01 | US-21, US-22 |
| NFR-02 | C04/C05/C06/C07/C13, S02/S03 | US-18, US-23 |
| NFR-03 | C09/C10; temporal algorithms at Functional Design | US-02, US-04, US-08, US-09, US-11 |
| NFR-04 | C01; accessibility acceptance at Construction | US-24 |
| NFR-05 | C03–C12 separation, S02/S03/S05 | US-11, US-17, US-23 |
| NFR-06 | C02/C07/C09/C10; bounded contract defaults and import limits before code | US-02, US-03, US-07, US-18, US-22 |
| NFR-07 | C02/C03/C04/C11/C14, S01/S05 | US-19, US-20, US-22 |
| NFR-08 | C11/C12/C14/C15, S05–S07 | US-19, US-20, US-21, US-22 |
| NFR-09 | C02/C14, secure HTML serving in S01 | US-22 |
| NFR-10 | C14/setup/build boundary; exact pins/integrity/scanning/pipeline controls at Construction | US-07, US-22; CC-03 |
| NFR-11 | C02/C04/C05/C09/C11/C12/C15 | US-07, US-15, US-17, US-18, US-19, US-23 |
| NFR-12 | C11/C12/C14, S05/S06 | US-20, US-21 |
| NFR-13 | Pure C10 and typed C08/C09/C11/C12 ports support isolation; full property identification/configuration at Construction | US-08–13, US-15–21; CC-04 |
| NFR-14 | All component failure/acceptance boundaries, later scenario/PBT/coverage checks | US-01–24; CC-04/05 |

US-01–24 are all represented. Dependencies and supporting responsibilities do not change user-story scope or preselect units. No unit-of-work artifacts are generated at this gate.

## 5. Design-stage extension review

“Compliant (design)” means an applicable architectural responsibility/interface/control is defined here; it does not mean a configured control or test has passed. Construction must verify the mechanisms. N/A applies only to the named absent feature or later-stage verification, not wholesale exemption of local security.

### Security compliance

| Rule | Design status | Evidence / later verification |
|---|---|---|
| SECURITY-01 | Compliant (design) | C12/C14 encrypted volume includes SQLite side files/caches/ledger/snapshots; C15 independently protected encrypted log store. Browser HTTPS TLS 1.2+. No network database; filesystem/in-process access has no TLS connection string. Private inference HTTP is explicitly not encrypted and not storage traffic. Verify actual paths/keys/mounts in Construction. |
| SECURITY-02 | N/A external intermediary | No external-traffic load balancer/CDN/API gateway. Local HTTPS endpoint events still use C15. If a local reverse proxy is selected, its sanitized access events must also feed C15. |
| SECURITY-03 | Compliant (design) | C15 structured central collector and peer-authorized IPC; timestamp/correlation/level/code, sensitive-field allowlist exclusion. All entry points route safe events; collector has separately protected diagnostics. |
| SECURITY-04 | Compliant (design) | S01 secure HTML serving; S07 transport section enumerates CSP/HSTS/nosniff/DENY/referrer headers. Construction must verify browser trust and actual responses. |
| SECURITY-05 | Compliant (design) | C02/C07/C09/C10 schemas/bounds/escape/parameterization. Explicit browser/text/model limits; archive limits must be set against actual feed at Functional Design before code. |
| SECURITY-06 | N/A cloud IAM; local least privilege designed | No cloud roles. C15 separate identity, C12 mutation-only lifecycle access, C03 owner capability checks and OS-authorized operator commands constrain local privileges. |
| SECURITY-07 | Compliant (design) | C14 loopback-only listeners, explicit origin/local peers, no public/LAN model or DB listener. No cloud subnets/routes/security groups exist. |
| SECURITY-08 | Compliant (design) | C03 guards every protected API and owner/session job/plan ID. Static shell/liveness explicitly public; bootstrap credential-gated/rate-limited. Restore/import are OS-authorized local commands, not unchecked browser admin routes. |
| SECURITY-09 | Compliant (design) | C02 safe errors, no directory/debug/example endpoint serving, no default credentials; C14 supported pinned runtime configuration verified later. |
| SECURITY-10 | Compliant design obligation; build checks deferred | Pin lockfiles/exact versions, trusted registry integrity, vulnerability scanning and no unused dependencies in Construction; no `latest` CI/base images. Production SBOM deployment obligation N/A to this non-production local prototype; reconsider if scope changes. |
| SECURITY-11 | Compliant (design) | Auth/key/lifecycle/domain separation, input+authorization+encryption layers; queue/bootstrap/session admission limits and misuse scenarios below. |
| SECURITY-12 | Compliant applicable session design | Expiring opaque server sessions, logout revocation, Secure/HttpOnly/Strict cookies, one-use bootstrap and rate limits; OS-protected keys, no hardcoded credentials. Password policy/hashing N/A without passwords; MFA for admin accounts N/A because there is no application admin account. OS operator privilege is not an invented browser role. |
| SECURITY-13 | Compliant (design) | Validated untrusted JSON/archives, reviewed source hashes/versioning; safe actor/timestamp/action/version-state hashes for mutation events rather than private before/after values. Dependency checksums and access-controlled/auditable pipeline changes verified in Construction. CDN SRI N/A: bundled local assets only. |
| SECURITY-14 | Compliant (design) | C15 independent OS ownership/append integrity, ≥90-day retention, alert counters for failed bootstrap/authorization, unexpected peers/permissions, backup/ledger/log errors; C13 aggregate dashboard, no private contents. Verify identity enforcement/retention at Construction. |
| SECURITY-15 | Compliant (design) | Typed safe external-call failures, deadline guards, global API error boundary, transaction rollback/resource cleanup; fail closed on identity/vault/ledger/log integrity errors. Detailed failure/crash ordering verified later. |

### Resiliency compliance

| Rule | Design status | Evidence / applicability |
|---|---|---|
| RESILIENCY-01 | Compliant (design) | Components table assigns local criticality and failure impact; matrix/flows define upstream/downstream dependencies and fallback. |
| RESILIENCY-02 | N/A production guarantees | Explicit single-laptop educational scope, no production uptime SLA/numeric RTO/RPO. Honest local restore behavior specified without a guarantee. |
| RESILIENCY-03 | Compliant exemption | User-selected formal-process exemption for local course prototype; Git history and AI-DLC reviews remain. |
| RESILIENCY-04 | Deferred to permitted NFR Design gate | No cloud/IaC deployment. Ask user CI/release/rollback choices there; document exact local startup/config verification during Construction. |
| RESILIENCY-05 | Compliant (design) | C13/C15 latency/error/queue/model/source/vault/backup/collector metrics/logs and local alerts. Correlation ID carries job/tool events; no separate distributed-app topology requiring cloud tracing. |
| RESILIENCY-06 | Compliant (design) | Minimal liveness separate from protected deep readiness for store/key/model/source/log dependencies. Load-balancer routing and external canaries N/A. |
| RESILIENCY-07 | Compliant local design; cloud portions N/A | Explicit degraded-state/backup/log integrity and queue saturation indicators. Continuous external resiliency tooling is future improvement, not required cloud integration; no autoscaling/replication indicators without those resources. |
| RESILIENCY-08 | N/A | No cloud regions/zones or zone-failure guarantee. |
| RESILIENCY-09 | N/A production autoscaling | One laptop; queue/payload/output/deadline bounds prevent unbounded local work. Resource limits/latency validated later. |
| RESILIENCY-10 | Compliant (design) | Shared request budget; per-tool/model/file/DB bounded operation design, bounded compute queue, source/model fallback. Explicit failed model state short-circuits new model calls until readiness/retry; separate short-lived DB access does not wait through inference. Detailed busy/timeouts/circuit behavior at Functional Design. |
| RESILIENCY-11 | N/A production regional DR | Local latest-state restore only; no regional failover or numeric target. |
| RESILIENCY-12 | Compliant (design) | Automated encrypted latest-state snapshot after committed saves, old good copy protected until verified replacement; deletion ledger and purge semantics, restore check required. No cross-region copies or seven-day/hourly policy inferred. |
| RESILIENCY-13 | Compliant (design) | Maintenance restore flow stages/validates before visibility and preserves current fences; shutdown/invalidate jobs first. Concrete operator runbook and recovery tests at Construction; no regional failback. |
| RESILIENCY-14 | Deferred process choice | Failure/restore/cancel acceptance scenarios identified; formal resiliency testing approach must be asked at NFR Design as the rule allows. |
| RESILIENCY-15 | Deferred process choice | Local diagnostic/alert channel specified; user incident-response process selection remains at NFR Design. No existing organizational process invented. |

### Property-based testing compliance

| Rule | Application Design status | Handoff |
|---|---|---|
| PBT-01 | N/A at this stage | Per-unit Functional Design must identify formal properties; pure C10 and typed source/lifecycle ports make isolation possible. |
| PBT-02 | N/A at this stage | Test serialization/restore of structured plan/provenance round trips later. |
| PBT-03 | N/A at this stage | Test scheduling/cost/source-status/service-date invariants over generated domain inputs. |
| PBT-04 | N/A at this stage | Test deletion/normalization idempotence where promised. |
| PBT-05 | N/A at this stage | Assess simplified routing/scheduling oracle in Functional Design. |
| PBT-06 | N/A at this stage | Model save/revise/delete/reset/restore/cancel command sequences against current ledger/version state. |
| PBT-07 | N/A at this stage | Reusable domain generators for aware dates, trips, catalogs and operation sequences. |
| PBT-08 | N/A at this stage | Shrinking, reproducible seeds and CI inclusion during Construction. |
| PBT-09 | N/A at this stage | Hypothesis/fast-check selection/configuration verified at NFR Requirements/Construction as applicable. |
| PBT-10 | N/A at this stage | Pair generated properties with all concrete business-critical scenarios; no property tests generated in Inception. |

No unresolved architectural contradiction or blocking design-coverage finding identified. This conclusion is limited to the documents and the approved constraints. A later inability to configure OS identity/key/log protection or prove crash/restore invariants is a blocking implementation finding, not permission to claim control success here.

## 6. Misuse/failure review

| Trigger | Required defense/outcome |
|---|---|
| Another origin, missing session or guessed plan/job ID | C02/C03 deny; no data leak; safe denial event |
| Prompt injection or invented source/tool | C07/C10 reject invalid authority/IDs, no arbitrary action or source-status upgrade |
| Unbounded job flood/oversized input/archive | Admission/body/output/archive limits; explicit busy/invalid response; no resource-exhaustion queue |
| Session expires, job cancelled or plan deleted during inference | Current authoritative guards prevent late publish/save; transient result cleanup and ledger fencing |
| Stale revision or confirmation | Expected-version/proposal guard returns conflict; current saved plan unchanged |
| Crash while saving snapshot/deleting/restoring | Preserve/fence current valid state and fail closed; never expose deleted plan or claim unverified backup success; formal protocol/tests later |
| Log collector or encrypted volume unavailable | Report security-unready; no sensitive mutation through unprotected fallback |
| Laptop/key loss | Safe unrecoverable state; no false cloud recovery or guaranteed surviving backup |

## 7. Construction verification and later decisions

Before implementing relevant units, settle the concrete OS volume/key/certificate/collector setup and verify privilege/retention enforcement; no OS changes have been made in this Inception run. Verify the local model's tool/schema handling and actual latency on Kelly's reported 16 GB laptop. Define archive size/row limits from a reviewed valid source, temporal/GTFS algorithms, session/token internals, crash-safe cancellation/commit/deletion/restore ordering, and exact dependency pins.

At allowed NFR Design gates, ask the deferred CI/release/rollback, incident-process and resiliency-test-process questions. Functional Design identifies testable properties; Code Generation/Build and Test provide actual scenario/PBT/security/accessibility/performance results. These remain required, not optional merely because this design is approved.

## 8. Review and next gate

Review all five linked design artifacts and request changes or approve the generated design. On actual approval, proceed to Units Generation planning/questions; do not start Construction. Unit count, story assignment and directory organization are decided in that next stage using this approved architecture, not silently preselected here.
