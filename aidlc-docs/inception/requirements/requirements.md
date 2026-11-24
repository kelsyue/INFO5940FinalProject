# BigRedRoutes — Requirements

**Status:** APPROVED. User explicitly responded “Approved and continue”; approval recorded 2026-11-24T17:04:29Z in `../../audit.md`. Proceed to User Stories planning, subject to that stage’s own gates.
**Workflow:** AWS AI-DLC v1.0.1, Inception / Requirements Analysis, comprehensive depth.

## 1. Intent analysis and evidence

- **Request:** Build BigRedRoutes — Travel Planning for Cornell and Beyond, an LLM-assisted local application with General NYC/DC destination planning and Cornell campus-origin/NYC transport research. Complete Inception including Units Generation and stop before Construction.
- **Request type:** New project; greenfield. Python files in `examples/` are technical-input examples, not an existing application.
- **Scope:** System-wide, multiple components: user interface, local API, catalogs, source adapters, bounded LLM orchestrator, deterministic planner/validators and local persistence.
- **Complexity:** Complex because data provenance, date applicability, scheduling, model failure and two distinct modes must remain consistent.
- **Sources:** `README.md`, `docs/vision.md`, `docs/technical-environment.md`, `docs/data-sources.md`, `docs/demo-scenarios.md`, all three requirements question files and the actual conversation in `aidlc-docs/audit.md`.
- **Team review:** User reports all four members reviewed the inputs and agreed to roles/cadence, and were present online via Zoom on November 24, 2026. Ananya is the agreed designated workflow operator in the README; the person operating this particular session has not been identified and is not inferred.
- **Demo machine:** Kelly Yue's laptop, macOS Tahoe 26.5.2, 16 GB RAM, as reported. User reports `qwen3:4b` works. No independent tool-use, correctness or latency benchmark is claimed.

The team answered the product clarification questions and subsequently approved this requirements document, including its explicitly proposed local backup policy. Proposal/review language retained below describes what was presented for approval; that behavior is now adopted through the recorded approval, not retrospectively attributed to earlier answers. Implementation and downstream artifacts remain unapproved/unbuilt.

## 2. Product objective and stakeholders

Help travelers turn preferences into inspectable, feasible destination itineraries; help Cornell travelers additionally understand public academic dates, campus departure context, official transport providers and source-supported TCAT connections. An LLM interprets conversational intent, selects from bounded tools and explains/revises plans. Deterministic code validates identities, provenance, dates, time windows, transfers and budget arithmetic.

Primary users are Cornell students without cars, Cornell graduate students with individual obligations, general travelers visiting NYC/DC and small adult groups revising shared activity plans. Transport providers are sources, not integration partners. The product is a student project without provider/university affiliation or endorsement.

## 3. MVP boundary and priorities

All requirements marked MUST are MVP obligations by December 16, 2026. A partial itinerary is acceptable when disclosed constraints or the catalog prevent completion; omitting a required feature is not equivalent to returning a partial itinerary.

**In scope:** General NYC/DC planning; Cornell origin areas North/West/Central; Cornell academic snapshot; official OurBus/C2C/ITH links; local GTFS import and service-validity checks; 1–5 day planning; bounded local agent tools; natural-language revision when the model works; structured deterministic fallback; provenance; budgets; local save/reopen/delete/reset; local security and backup protection; accessible interface; tests.

**Out of scope:** Cloud hosting/accounts/regions/availability zones, production uptime SLA, regional failover, remote multi-user operation, Cornell authentication or individual course-calendar access, booking/payments, live fares/seats/flights, OurBus inventory API, C2C seat inventory, GTFS-RT, live traffic/maps, hotels, weather, unlimited cities and compulsory Docker/Kubernetes. No account signup is required; a local session identity for resource authorization is in scope under the accepted security baseline.

**Stretch only:** Automatic source refresh, C2C timetable ingestion and richer comparisons based on manually confirmed travel times/fares. These cannot displace MUST requirements or turn provider links into live inventory.

## 4. Functional requirements and acceptance conditions

| ID | Requirement | Observable acceptance conditions |
|---|---|---|
| FR-01 | MUST provide two explicit modes. | General planning completes without Cornell fields or Ithaca transport. Cornell mode requires North/West/Central campus area. Switching modes clears incompatible inputs or flags them for correction. |
| FR-02 | MUST validate the trip contract. | Destination is NYC or DC; inclusive date span is 1–5 consecutive days; party size 1–4 adults; daily budget $25–$300 per person; 1–4 supported interests; pace relaxed/balanced/packed. Invalid data yields field-specific errors. |
| FR-03 | MUST allow past, today and future dates. | Past itineraries are labeled historical; applicability is evaluated for the requested date. Historical dates never bypass service/calendar/venue checks or expose synthetic test times as genuine. |
| FR-04 | MUST display public academic context in Cornell mode. | Versioned source-supported events show dates, official URL and captured date. Explain that university dates do not establish personal freedom from classes, research, exams or work. Missing coverage is unknown. |
| FR-05 | MUST provide a Cornell NYC transport directory. | OurBus and C2C official schedule/search/booking links and ITH airline/airport reference links carry verification/source information. Fares, departures, flights and seats are not fabricated. DC destination planning does not imply a supported Cornell–DC transport corridor. |
| FR-06 | MUST import genuine TCAT static GTFS locally. | A documented command accepts a user-downloaded official archive, validates required structures and reports errors safely. No raw archive is committed without confirmed permission. Missing/unusable feed leaves reference information usable and schedules unavailable. |
| FR-07 | MUST evaluate TCAT service applicability. | Check actual feed/service range, weekday/calendar and exception rules, correct trip direction and stop sequence, verified campus/terminal mapping and after-midnight service times. Reject uncovered dates, absent paths and ambiguous data. `feed_info` is optional; absent optional metadata is not fabricated. |
| FR-08 | MUST distinguish scheduled transfers from unknown transfers. | Only a source-valid feeder leg plus user-confirmed intercity departure can produce a feasibility calculation. Require feeder arrival plus at least the selected boarding margin to be no later than departure. Equality passes; one minute short fails. Missing times yield unknown, not feasible. |
| FR-09 | MUST honor confirmed activity-day windows. | Without confirmed travel anchors, ask for first/last-day activity windows before scheduling those days. Intermediate days may default to 09:00–18:00. For a one-day trip use the intersection of first/last-day constraints. Missing windows leave those days pending rather than inventing times. |
| FR-10 | MUST apply disclosed planning buffers. | Default intercity bus boarding margin is 15 minutes; sightseeing starts at least 60 minutes after confirmed arrival and ends at least 90 minutes before confirmed departure. Users may increase margins. Activity travel uses curated zone estimates, explicitly labeled estimates; no live-routing/connection guarantee. |
| FR-11 | MUST provide at least 12 sourced venues per city. | Catalog entries have stable city-specific IDs, tags, source URLs, checked dates, visit durations and known/unknown fees/hours. Diverse interests are represented. Unknown/inapplicable hours produce unscheduled suggestions unless the user confirms an activity window. |
| FR-12 | MUST generate deterministic-valid day cards. | Every timed venue belongs to the selected catalog/city, fits valid or user-confirmed hours and day/travel windows, has positive duration and does not overlap another visit or its travel allowance. No duplicate venue within a day. Relaxed/balanced/packed caps are 2/3/4 scheduled attraction stops per day. |
| FR-13 | MUST disclose budget completeness. | Daily food allowance is chosen within the food-plus-admission budget. Show known estimated admission plus food per person/day; group totals are separately labeled. Unknown admission stays null and prevents an unqualified within-budget claim. Transport and lodging are excluded and clearly separate. |
| FR-14 | MUST return explained partial plans for infeasibility. | Identify unmet constraints and unscheduled requested venues; retain feasible portions and ask which constraints the user wants to change. Never silently exceed a hard limit or apply proposed changes without confirmation. A partial response is distinguishable from a complete plan and from invalid input. |
| FR-15 | MUST interpret natural-language preferences through the local model. | Convert intent into typed, validated constraints; unsupported/ambiguous fields require user confirmation. Natural language cannot create catalog IDs, opening hours, confirmed services or budget facts. The structured form remains available. |
| FR-16 | MUST support bounded agentic tool use. | Only registered academic, provider, TCAT, attraction, constraint and validation tools are callable. Backend validates arguments and tool results. No shell execution, arbitrary URL fetch, scraping, provider transaction or file write is available to the model. |
| FR-17 | MUST support targeted natural-language revisions. | Show changed activities/constraints and rerun validators before save. Preserve unaffected days and confirmed travel anchors; if broader changes are needed, propose them and obtain confirmation before applying. Failed/rejected revisions preserve the saved plan. |
| FR-18 | MUST degrade when model inference fails. | After at most one malformed-output repair, offer explicitly labeled deterministic planning from structured inputs. Natural-language interpretation/revision is unavailable until the model recovers. Existing plans and references remain readable. Validators remain mandatory in fallback. |
| FR-19 | MUST preserve provenance throughout output. | Relevant observations carry official/source URL, captured date, applicability and `published-schedule`, `reference-link`, `user-provided`, `estimate` or `unavailable`. Model explanations cannot upgrade a status. User confirmations remain labeled user-provided. |
| FR-20 | MUST save, reopen and remove local plans. | SQLite stores structured itinerary, constraints, source metadata and necessary revision metadata, not raw chats. Saved-plan operations require local authorization. Delete-plan and confirmed reset-all remove associated persisted plan data and prevent backup restoration from resurrecting deleted plans. |
| FR-21 | MUST explain unsupported requests. | Requests for purchases, live prices, guaranteed connections or unavailable sources receive a clear limitation and an appropriate official link. No purchase confirmation, fake price or fake departure is returned. |
| FR-22 | MUST expose readiness and safe errors. | Health information distinguishes app/model/data status. Validation, not-found, infeasibility, source-unavailable and model-unavailable cases are machine-distinguishable and human-readable. No stack trace, secret or internal filesystem path is exposed. |

## 5. Non-functional requirements

| ID | Requirement and verification target |
|---|---|
| NFR-01 | MUST run on one laptop with local browser UI, FastAPI, SQLite and Ollama. No cloud dependency or remote failover. Local HTTPS/security controls below supersede illustrative HTTP-only setup snippets in the original inputs. |
| NFR-02 | Target 95% of warmed-model generation/revision requests within 120 seconds on the declared demo laptop. Hard overall request deadline 150 seconds; at most six tool calls, each at most 15 seconds; at most one output repair within the same deadline. Non-LLM lookup target two seconds. Benchmark during Construction; current report of model success does not establish these targets. |
| NFR-03 | MUST preserve aware timestamps and IANA zone `America/New_York`; normalize instant comparisons appropriately and retain GTFS local service dates. Test DST transitions, after-midnight service, reversed ranges and exact transfer boundaries. Never compare naive travel timestamps. |
| NFR-04 | MUST provide keyboard-operable forms, mode selection, timeline, warnings, source links and deletion controls, readable labels/focus states, mobile-responsive cards and status text independent of color. Include keyboard and screen-reader-oriented checks. |
| NFR-05 | MUST isolate model, source-adapter, planning, persistence and authorization concerns so model/source failures cannot bypass invariants. Local data reads and deterministic validation must not require model availability. |
| NFR-06 | MUST validate bounded payloads, strings, arrays, IDs, enums and dates at API/tool/import boundaries; parameterize SQLite access, treat external/model text as data, escape displayed text and restrict provider URLs to approved sources. Design will specify exact size limits before implementation. |
| NFR-07 | MUST keep app/model listeners on loopback, use explicitly allowed browser origins, protect against unauthorized local/cross-origin mutations, enforce object-level saved-plan permissions and provide an HTTPS-capable local demo configuration. No Cornell credentials or public signup. Session/credential mechanisms require design review. |
| NFR-08 | MUST protect persistent stores and backups with encryption and OS-managed or equivalent key protection. Use protected centralized local structured logs with timestamp, request ID, severity and message, without raw chat, credentials or private itinerary content. Protect audit integrity and separate application write access from log modification/deletion. Apply the security baseline's 90-day minimum security-log retention; plan backups and security logs have different retention/deletion policies. |
| NFR-09 | MUST set restrictive CSP, HSTS with one-year minimum max-age, content-type protection, anti-framing and referrer headers on HTML-serving endpoints in the secured local setup. Do not claim HTTP loopback alone supplies TLS or HSTS protection. |
| NFR-10 | MUST pin resolved dependencies/lockfiles, use trusted registries and integrity checks, document vulnerability scanning and restrict/audit pipeline changes. No secrets, databases, downloaded unlicensed feeds or real-user prompts in Git. Exact runtime pins will be validated during Construction; broad version ranges in the initial input are not final pins. |
| NFR-11 | MUST fail safely on database, filesystem, import, model and network errors: bounded waits, cleanup/rollback, safe user messages and preserved prior saved state. Fallback must not relax validation, access control, encryption or provenance. Model-produced instructions in source data must not be executed. |
| NFR-12 | MUST retain automated encrypted local backups and a tested local restore procedure, without claiming a production availability or laptop-loss guarantee. The draft policy in section 6 is for review; it is not a previously agreed numeric RTO/RPO commitment. |
| NFR-13 | MUST complement scenario tests with full property-based testing where properties exist: generated scheduling/cost/provenance invariants, serialization round trips, idempotent deletion and stateful save/revise/delete sequences. Identify properties in Functional Design; propose Hypothesis for Python and fast-check for applicable TypeScript logic. Configure shrinking, reproducible seeds and CI coverage during Construction. |
| NFR-14 | MUST test both modes, missing windows/hours, historical/source-date mismatch, GTFS calendar exceptions/24+ times, model malformed output/tool abuse, unknown fees, unauthorized saved-plan access, revision preservation, backup restore and deletion persistence. Target at least 80% coverage on pure planner/validator modules. No test result or coverage is claimed until implementation. |

## 6. Single-laptop reliability and draft backup policy

The latest team answer explicitly supersedes the cloud single-region/multi-zone selection: one laptop only, no cloud. Production regional redundancy, autoscaling, uptime SLA and production recovery guarantees are N/A for this educational MVP. Loss of the laptop and all copies on it can mean total data loss; no model or backup feature can guarantee otherwise.

Local backup protection still applies under the retained security/resiliency baselines. **Draft proposal for this review:** maintain an automated encrypted known-good SQLite snapshot after successful saves, retaining the latest restorable state; preserve a prior valid copy while creating/verifying a replacement atomically. Verify a restore before the final demo. Delete/reset must purge or rewrite every retained copy containing removed plans, or use an equivalent reviewed mechanism that prevents their restoration. Raw chat is never backed up because it is not persisted. Exact encryption, storage path, locking and backup procedures will be designed in Application Design/Construction.

This proposal does not adopt the earlier unselected 30-minute RTO, hourly RPO or seven-day retention policy. No numeric local RTO/RPO or production SLA has been approved. If the team needs numeric guarantees or a different retention policy, request changes explicitly before approving these requirements. A local backup/restore procedure and observable recovery check are required even without a numeric guarantee.

Formal organizational change management is exempt per the team's answer: a local course prototype has no production service/organization release process. Git history and actual AI-DLC stage reviews/approvals still apply. CI tooling, rollback/deployment process, incident handling and resiliency-test process allowed at NFR Design remain decisions for that later gate; this does not start Construction.

## 7. Critical workflows and acceptance scenarios

| Scenario | Required observable outcome | Requirements |
|---|---|---|
| Cornell NYC, three days, academic break | Show only source-supported academic context and provider links. Ask for unconfirmed first/last-day windows. No TCAT departure unless the imported source supports the requested date and path. | FR-01, 04–10, 19 |
| General DC, three days, art/history/food | No Cornell questions. Use DC catalog; show costs, applicable hours and day constraints. At least 12 sourced venues exist; constrained requests may be partial. | FR-01–03, 09–14 |
| Transfer at boundary | Valid feeder 09:10, confirmed departure 09:25 and 15-minute margin passes; 09:11 fails; unknown feeder stays unknown. Synthetic fixtures are test-only. | FR-07–08, NFR-03 |
| Out-of-date or absent feed | Source applicability, not a hard-coded date, determines availability. No data means no claimed departure; reference links and destination planning remain available. | FR-05–07, 19, 21 |
| Venue unknown hours/fee | Hours unknown means unscheduled until user confirms a window. Fee unknown means incomplete cost; never free or unqualified within-budget. | FR-11–14 |
| Targeted cheaper day two | Diff and validation required; day one/three and travel anchors stay unchanged unless broader change is confirmed. Explain infeasibility and ask which constraints to change. | FR-14, 17 |
| Local model unavailable | Structured deterministic planning is visibly labeled; no natural-language operations; existing plans remain intact. | FR-15–18, NFR-11 |
| Prompt injection or fabricated tool output | Unauthorized tool names/IDs and untrusted instructions cannot bypass schema/provenance checks or execute actions. | FR-16, 19, NFR-06–07 |
| Save, delete, restore | Authorized local owner can save/reopen/delete. Another local principal cannot read/mutate by guessing ID. Restore never resurrects deleted plans. Raw chats absent from database/logs/backups. | FR-20, NFR-07–08, 12 |
| Unsupported booking request | Explain limitation and link official provider; no fake purchase, live fare, seat or flight. | FR-05, 21 |

The input documents' specific calendar/feed dates are historical source claims, not newly verified facts. Dyllan owns permissions, Registrar/provider verification and actual feed applicability before the demo. Snapshot acceptance tests must use reviewed source records; this draft does not certify current external source contents.

## 8. Traceability to vision and team decisions

| Vision feature / decision | Requirements |
|---|---|
| BRR-01 modes | FR-01–02 |
| BRR-02 academic context | FR-04, 19 |
| BRR-03 provider directory | FR-05, 21 |
| BRR-04 static GTFS | FR-06–07, NFR-03 |
| BRR-05 transfer check | FR-08, 10 |
| BRR-06 preference interpretation | FR-15, 18 |
| BRR-07 bounded tools | FR-16, NFR-02, 06, 11 |
| BRR-08 day plans | FR-02–03, 09–12, 14 |
| BRR-09 budget | FR-13 |
| BRR-10 boundaries | FR-09–10 |
| BRR-11 revision | FR-17 |
| BRR-12 provenance | FR-19 |
| BRR-13 persistence | FR-20, NFR-07–08, 12 |
| BRR-14 accessible UI | NFR-04 |
| Initial Q2–8 | FR-03, 06–14 |
| Initial Q9–13 | FR-13, 17–20, NFR-02 |
| Initial Q14–16 / first follow-up Q4 | NFR-06–14; compliance below |
| Final clarification Q3, single laptop | NFR-01, 12; section 6 |

Stories, components and units are not generated at this gate. Their later artifacts must reference these requirement IDs and preserve the distinctions between confirmed, estimated, user-provided and unavailable data.

## 9. Extension compliance at the requirements-document stage

“Compliant” here means a requirement/applicability decision is captured for this stage. It does not mean an unbuilt app has passed a control or test. Design, configuration and implementation checks remain mandatory at their applicable gates.

### Security compliance

| Rule | Stage status | Requirement or applicability |
|---|---|---|
| SECURITY-01 | Compliant at requirements level | NFR-08 requires encrypted stores/backups and key protection. Store access through in-process SQLite has no separate database network protocol; any network data movement requiring TLS must be secured in design. |
| SECURITY-02 | N/A | No external-traffic load balancer, API gateway or CDN. Reassess if one is introduced; local app logging still applies. |
| SECURITY-03 | Compliant at requirements level | NFR-08, local centralized structured logging; design must resolve collector isolation. |
| SECURITY-04 | Compliant at requirements level | NFR-07/09, secured local HTML serving and required headers. |
| SECURITY-05 | Compliant at requirements level | FR-02/16 and NFR-06, all input boundaries. |
| SECURITY-06 | N/A for cloud IAM | No cloud roles/policies. Local authorization/key permissions required by NFR-07/08. |
| SECURITY-07 | Compliant at requirements level | Loopback-only, explicit origins/listeners; no public cloud subnets/security groups. |
| SECURITY-08 | Compliant at requirements level | FR-20, NFR-07 require local principal and object authorization, with explicitly public routes identified during design. |
| SECURITY-09 | Compliant at requirements level | FR-22/NFR-10/11 require safe errors, supported pinned runtime and hardened local demo; examples are not application endpoints. |
| SECURITY-10 | Compliant at requirements level | NFR-10, pins/scanning/trusted sources. Production SBOM deployment obligation N/A to this non-production local milestone; reconsider for any production deployment. |
| SECURITY-11 | Compliant at requirements level | NFR-05–08, layered controls and explicit abuse scenarios. Internet-public endpoint throttling N/A; bounded local model work still required. |
| SECURITY-12 | Deferred design verification | No password/Cornell/admin account feature required. If session/credential design introduces applicable authentication, expiration/invalidation, safe storage, brute-force controls and cookie protections must be addressed; no unconditional blanket exemption. |
| SECURITY-13 | Compliant at requirements level | NFR-06/10; safe parsing, artifact integrity and auditable pipeline/data changes. SRI N/A if no CDN assets are loaded. |
| SECURITY-14 | Compliant at requirements level | NFR-08, protected local security logs, retention and security-event monitoring; detailed event/alert mechanisms await design. |
| SECURITY-15 | Compliant at requirements level | NFR-11, fail-closed errors/cleanup; deterministic fallback retains protections. |

### Resiliency compliance

| Rule | Stage status | Requirement or applicability |
|---|---|---|
| RESILIENCY-01 | Compliant at requirements level | Planner/validators/API/storage are High for demo success; UI High for interaction; model Medium because fallback exists; source imports Medium because unknown/reference handling exists. No safety-critical or production service. Dependency map awaits Application Design. |
| RESILIENCY-02 | N/A for production SLA/guarantees | Team requires a single-laptop educational MVP. No production availability SLA or guaranteed RTO/RPO; no numeric values inferred. Local recovery behavior remains in NFR-12/section 6. |
| RESILIENCY-03 | Compliant exemption | Team selected exemption for local course prototype; Git/AI-DLC record still applies. |
| RESILIENCY-04 | Deferred | CI/release/rollback choices permitted at NFR Design. No production deployment or IaC required now. |
| RESILIENCY-05 | Compliant at requirements level | FR-22, NFR-02/08 require readiness, performance/error observations and centralized local logs. Dashboard and local monitoring design later. |
| RESILIENCY-06 | Compliant at requirements level | FR-22, process/model/data readiness; load-balancer routing and public canaries N/A without those systems. |
| RESILIENCY-07 | Deferred local design | Monitor model/source/backup failure; cloud scaling/replication monitoring N/A. No continuous posture tool claimed. |
| RESILIENCY-08 | N/A | Latest user scope replaces cloud multi-zone answer: one laptop, no region/zone infrastructure or zone-failure guarantee. |
| RESILIENCY-09 | N/A for production autoscaling | One local demo operator; explicit request/tool bounds remain required by NFR-02/11. |
| RESILIENCY-10 | Compliant at requirements level | FR-18/NFR-02/11, timeouts, resource bounds and graceful failure; connection pools/circuit-breaker applicability assessed in design. |
| RESILIENCY-11 | N/A for production regional DR | Single-laptop scope; local restore procedure in NFR-12/section 6, no regional failover. |
| RESILIENCY-12 | Compliant draft requirement | Automated encrypted snapshots, latest-state retention, restore check and deletion protection proposed in section 6, subject to this review. No backup currently exists. |
| RESILIENCY-13 | Deferred design verification | Local restore instructions and recovery validation required; no region failback infrastructure. |
| RESILIENCY-14 | Deferred | Testing-process decision is permitted at NFR Design; NFR-14 already captures recovery/degraded-mode test needs. |
| RESILIENCY-15 | Deferred | Incident-response process decision permitted at NFR Design; do not invent an existing organization process. |

### Property-based testing compliance

| Rule | Stage status | Planned obligation |
|---|---|---|
| PBT-01 | N/A at Requirements; required later | Functional Design must identify properties per relevant component. |
| PBT-02 | N/A at Requirements; required later | Round-trip tests for plans, constraints and provenance serialization. |
| PBT-03 | N/A at Requirements; required later | General scheduling, cost, city/provenance and source-date invariants. |
| PBT-04 | N/A at Requirements; required later | Idempotent normalization/deletion where promised. |
| PBT-05 | N/A at Requirements; required later | Evaluate a simple reference schedule/service lookup oracle. |
| PBT-06 | N/A at Requirements; required later | Evaluate save/revise/delete/restore state sequences against a model. |
| PBT-07 | N/A at Requirements; required later | Reusable domain-valid generators including temporal/service boundaries. |
| PBT-08 | N/A at Requirements; required later | Shrinking, seeded reproducibility and CI inclusion. |
| PBT-09 | N/A at Requirements; required later | Hypothesis/fast-check are draft framework choices; configure actual dependencies at Construction. |
| PBT-10 | N/A at Requirements; required later | Complement generated properties with explicit critical-scenario tests. |

No blocking finding is asserted against nonexistent implementation. Deferred stage-specific verification is not evidence of implementation compliance. Any design unable to satisfy an applicable enabled rule must raise a finding rather than silently weaken it.

## 10. Review focus and remaining administrative follow-up

Review the complete MVP, particularly strict first/last-day windows, unknown attraction hours/fees, partial-plan constraint questions, local security workload and section 6's **proposed automated latest-state backup policy without numeric recovery guarantees**. Request changes if that policy does not match your intended local recovery expectations. Approval would adopt this requirements draft, including its explicitly proposed behavior; it is not a claim of implementation or test success.

The current session operator's identity remains unreported; record it when known without inventing attendance/operator history. Exact dependency pins, security mechanisms, CI/release process and accepted stage-specific design choices remain future workflow decisions. Source claims must be checked against actual source records before use.


## 11. Approval record

- Recorded at: 2026-11-24T17:04:29Z.
- Exact user response: “Approved and continue”.
- Approved scope: all requirements in this document, including automated encrypted latest-state local snapshots after successful saves and a restore check, without numeric recovery guarantees or cloud deployment.
- Next authorized step: User Stories planning; its approach/answer/approval gates remain required.
