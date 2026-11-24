# BigRedRoutes — Unit, Story and Requirement Map

**Status:** APPROVED. Exact user response “Approve units and stop before Construction”, recorded 2026-11-24T17:44:20Z in `../../audit.md`. Inception complete; Construction not started.
**Primary unit:** U01 BigRedRoutes for every approved user story. Modules/work packages are internal contributions, not extra units or duplicate story ownership. The 72 numbered criteria in the approved [stories](../user-stories/stories.md) remain the acceptance baseline; this map does not replace or weaken them.

## Primary story ownership and supporting contributions

| Story | User outcome | Primary unit | Primary package | Supporting packages / key obligation |
|---|---|---|---|---|
| US-01 | Choose General/Cornell mode | U01 | M06 | M01 request boundary, M03 mode/input rules; no Cornell requirements in General |
| US-02 | Submit valid trip and historical dates | U01 | M03 | M01 schemas, M06 fields; valid range/party/budget, historical label and source applicability |
| US-03 | Interpret conversational preferences | U01 | M04 | M01 typed contracts, M03 validation, M06 confirmation; no invented fields/facts |
| US-04 | Confirm activity-day windows | U01 | M03 | M06 confirmation, M02 evidence; first/last-day confirmation and one-day intersection |
| US-05 | Public academic context | U01 | M02 | M04/M06 display; not individual course availability |
| US-06 | Official transport research | U01 | M02 | M04/M06 explanation; links are not live seats/fares/flights or booking |
| US-07 | Import permitted local TCAT data | U01 | M02 | M01 encrypted paths/operator boundary, M07 safe import events; bounded validated source, synthetic tests never runtime truth |
| US-08 | Date/path-applicable TCAT schedules | U01 | M02 | M03 temporal/domain checks, M04/M06 outcomes; exceptions/24+ times/unavailable honest |
| US-09 | Boarding-buffer feasibility | U01 | M03 | M02 real source applicability, M06 display; exact margin, unknown stays unknown |
| US-10 | Sourced city venues and usable hours | U01 | M02 | M03 scheduling, M06 suggestions; ≥12/city, unknown hours unscheduled until confirmed |
| US-11 | Valid chronological day cards | U01 | M03 | M02 evidence, M04 orchestration, M06 cards; city/pace/window/non-overlap invariants |
| US-12 | Honest food/admission costs | U01 | M03 | M06 per-person/group labels; unknown fees incomplete, travel/lodging excluded |
| US-13 | Partial-plan constraint choices | U01 | M03 | M04 result/confirmation, M06 interaction; no silent relaxation |
| US-14 | Inspect evidence/status | U01 | M06 | M02 stamps, M03 validation, M04 narration; no model status upgrade |
| US-15 | Targeted revision and diff | U01 | M04 | M03 invariants, M05 current version/authorized save, M06 review; preserve other days |
| US-16 | Confirm broader revision | U01 | M04 | M01 proposal/owner contracts, M05 guard, M06 confirmation; no unconfirmed anchor change |
| US-17 | Structured fallback on model failure | U01 | M04 | M03 deterministic path, M06 label, M07 status; all security/source constraints retained |
| US-18 | Bounded safe tool-assisted work | U01 | M04 | M01 budgets/input/owner guards, M03 validation, M07 counters; queue wait in deadline, no arbitrary tools |
| US-19 | Authorized local save/reopen | U01 | M05 | M01 identity/encrypted paths, M04 candidate validation, M06 UI, M07 safe events; no raw chats |
| US-20 | Delete/reset without resurrection | U01 | M05 | M01 confirmation/session, M04 invalidation, M06 controls, M07 events; purge/fence all app-managed copies |
| US-21 | Latest-state encrypted restore | U01 | M05 | M01 protected keys/operator maintenance, M04 job quiescence, M07 backup/restore status; current ledger never rolled back |
| US-22 | Secured local application | U01 | M01 | M05 storage/lifecycle, M07 collector isolation/retention, M06 safe UI; local identity/HTTPS, no external accounts |
| US-23 | Readiness and safe failure | U01 | M07 | M01 error boundaries, M02 source status, M04 jobs/model, M05 store/backup; no secrets/internal-path leakage |
| US-24 | Accessible complete journey | U01 | M06 | M01 semantics, M03/04/05/07 readable results; keyboard, screen-reader-oriented and non-color-only statuses |

Each story appears once as a primary row. Every supporting package contribution remains required; primary ownership does not exclude cross-cutting review. All four traveler personas and the supporting local operator retain their approved story associations in `../user-stories/personas.md`.

## Requirement coverage inherited through U01

| Requirement | Unit | Accountable packages | Acceptance story/reference |
|---|---|---|---|
| FR-01 | U01 | M01, M03, M06 | US-01, US-24 |
| FR-02 | U01 | M01, M03, M06 | US-01, US-02, US-12 |
| FR-03 | U01 | M02, M03, M06 | US-02 |
| FR-04 | U01 | M02, M04, M06 | US-05 |
| FR-05 | U01 | M02, M04, M06 | US-06 |
| FR-06 | U01 | M01, M02, M07 | US-07 |
| FR-07 | U01 | M02, M03 | US-08 |
| FR-08 | U01 | M02, M03 | US-09 |
| FR-09 | U01 | M03, M04, M06 | US-04, US-11 |
| FR-10 | U01 | M02, M03 | US-04, US-09, US-11 |
| FR-11 | U01 | M02, M03, M06 | US-10 |
| FR-12 | U01 | M03, M04 | US-11, US-15 |
| FR-13 | U01 | M03, M06 | US-12, US-15 |
| FR-14 | U01 | M03, M04, M06 | US-13, US-15, US-16 |
| FR-15 | U01 | M01, M03, M04 | US-03 |
| FR-16 | U01 | M01, M03, M04 | US-03, US-18 |
| FR-17 | U01 | M01, M03, M04, M05, M06 | US-15, US-16 |
| FR-18 | U01 | M03, M04, M06, M07 | US-17, US-18 |
| FR-19 | U01 | M02, M03, M04, M06 | US-05, US-06, US-08, US-10, US-14 |
| FR-20 | U01 | M01, M04, M05, M06, M07 | US-19–22 |
| FR-21 | U01 | M02, M04, M06 | US-06, US-14 |
| FR-22 | U01 | M01, M03, M04, M07 | US-13, US-17, US-23 |
| NFR-01 | U01 | M01, M06, M07 | US-21, US-22; one laptop, no cloud |
| NFR-02 | U01 | M01, M04, M07 | US-18, US-23; CC-05, measure target/deadlines during Construction |
| NFR-03 | U01 | M02, M03 | US-02, US-04, US-08, US-09, US-11; temporal/GTFS algorithm and boundary verification |
| NFR-04 | U01 | M06 | US-24; keyboard/screen-reader-oriented/narrow-view checks |
| NFR-05 | U01 | M01–M07 | US-11, US-17, US-23; module boundaries, no model/storage shortcut |
| NFR-06 | U01 | M01, M02, M03, M04 | US-02, US-03, US-07, US-18, US-22; CC-01 |
| NFR-07 | U01 | M01, M04, M05, M06 | US-19, US-20, US-22; CC-02 |
| NFR-08 | U01 | M01, M05, M07 | US-19–22; CC-02, private plan lifecycle versus protected security-event retention |
| NFR-09 | U01 | M01 | US-22; local HTTPS trust and actual required headers |
| NFR-10 | U01 | M01 with all package leads | US-07, US-22; CC-03, exact pins/lockfiles/integrity/scanning/pipeline controls |
| NFR-11 | U01 | M01–M07 | US-07, US-15, US-17–19, US-23; safe cleanup, rollback and preserved state |
| NFR-12 | U01 | M01, M05, M07 | US-20, US-21; latest-state snapshot/current-ledger restore, no numeric guarantee |
| NFR-13 | U01 | M03, M05 with M02/M04/M01 | CC-04; property identification and full applicable PBT at later gates |
| NFR-14 | U01 | All leads; Kelly coordinates tests | US-01–24, CC-04/05; meaningful examples plus PBT, ≥80% pure planner/validator coverage target |

CC-01–06 refer to the approved shared acceptance obligations in `stories.md`. All live-source/model/OS/performance/restore/accessibility test results remain future evidence, not facts inferred from this map.

## Cross-cutting extension accountability and later verification

All rules remain enabled as configured in state. “Carried” means responsibility is assigned, not implemented/passing. N/A/deferred scope below follows the approved design; unit decomposition does not introduce new exceptions.

| Rule | U01 accountable package(s) | Applicability / later checkpoint |
|---|---|---|
| SECURITY-01 | M01, M05, M07 | Carried: encrypted runtime/store/cache/backup/log paths, keys and local HTTPS; actual OS/key/TLS verification during Construction |
| SECURITY-02 | M01, M07 | External intermediaries N/A; any selected local HTTPS proxy emits sanitized protected access events |
| SECURITY-03 | M01, M07 | Carried: structured centralized safe logs for all entry points |
| SECURITY-04 | M01 | Carried: CSP/HSTS/nosniff/anti-frame/referrer headers, verify actual responses |
| SECURITY-05 | M01, M02, M03, M04 | Carried: bounded schemas/import/tools, safe rendering and parameterized queries |
| SECURITY-06 | M01, M07 | Cloud IAM N/A; OS local least-privilege identity/key/collector boundary retained |
| SECURITY-07 | M01 | Carried: loopback listeners, explicit origins/peers; cloud network resources N/A |
| SECURITY-08 | M01, M04, M05 | Carried: principal/session/object/job authorization and explicit public route policy |
| SECURITY-09 | M01, M06 | Carried: safe errors, no debug/default/example serving; supported runtime checked at Construction |
| SECURITY-10 | M01 with all leads | Carried: exact dependency pins, integrity, vulnerability checks and no unused dependencies; production SBOM obligation N/A to current local prototype |
| SECURITY-11 | M01, M03, M04, M05 | Carried: separated validation/auth/lifecycle, bounded work and misuse coverage |
| SECURITY-12 | M01, M04 | Carried applicable sessions/bootstrap/expiry/revocation/rate limits; password/admin-MFA N/A without those features; OS operator boundary retained |
| SECURITY-13 | M01, M02, M05, M07 | Carried: source/software integrity, safe parsing, auditable non-sensitive state hashes and restricted pipeline changes; CDN SRI N/A for bundled assets |
| SECURITY-14 | M07 | Carried: independent collector permissions, ≥90-day protected security-event retention, aggregate alerts; no raw private data |
| SECURITY-15 | M01–M07 | Carried: bounded errors/cleanup/rollback/fail-closed controls; no unprotected fallback |
| RESILIENCY-01 | All package leads | Carried local criticality/dependency map from approved design; final integrated failure checks |
| RESILIENCY-02 | M01, M05 | Production SLA/numeric RTO/RPO N/A; honest local recovery behavior retained |
| RESILIENCY-03 | Ananya / all reviewers | Approved formal-process exemption; Git and AI-DLC gates still required |
| RESILIENCY-04 | M01 / team | Deferred user CI/release/rollback decisions at NFR Design; no cloud/IaC assumed |
| RESILIENCY-05 | M07, M04 | Carried local metrics/logs/correlation/status, actual monitoring verification later |
| RESILIENCY-06 | M01, M07 | Carried liveness versus deep readiness; external load-balancer/canary N/A |
| RESILIENCY-07 | M07 | Carried degraded model/source/backup/log states; absent cloud scaling/replication portions N/A |
| RESILIENCY-08 | M01 | Cloud zones/regions N/A to one laptop |
| RESILIENCY-09 | M01, M04 | Production autoscaling N/A; local admission/queue/resource bounds retained |
| RESILIENCY-10 | M01, M04, M05 | Carried shared deadlines, bounded I/O/DB operations and model/source fallback |
| RESILIENCY-11 | M05 | Regional DR N/A; local maintenance restore retained |
| RESILIENCY-12 | M05, M01 | Carried encrypted verified latest-state snapshots and deletion-safe copies |
| RESILIENCY-13 | M05, M07 | Carried safe restore/runbook/validation; no regional failback |
| RESILIENCY-14 | Kelly / team | Failure/recovery examples retained; user testing-process choice at NFR Design |
| RESILIENCY-15 | Ananya / team | Local diagnostics retained; user incident-process choice at NFR Design |
| PBT-01 | M03, M05 with M02/M04 | Functional Design must identify properties per applicable component |
| PBT-02 | M01, M05 | Later structured plan/provenance serialization/restore round trips |
| PBT-03 | M02, M03, M04 | Later schedule/cost/source/date/queue/deadline invariants over domain inputs |
| PBT-04 | M03, M05 | Later normalization/deletion idempotence where claimed |
| PBT-05 | M02, M03 | Later simple oracle/reference applicability evaluation |
| PBT-06 | M04, M05 | Later stateful save/revise/cancel/delete/reset/restore reference-model sequences |
| PBT-07 | Kelly with domain leads | Later reusable valid/boundary domain generators |
| PBT-08 | Kelly / Ananya | Later shrinking, logged reproducible seeds and actual CI execution |
| PBT-09 | Kelly / Sarah | Later Hypothesis/fast-check dependency configuration for applicable Python/TypeScript logic |
| PBT-10 | All package leads | Concrete critical-path examples complement generated properties; capture counterexamples as regressions |

No unit/story/requirement or enabled-extension responsibility is orphaned. The single-unit decision preserves the separately owned collector and all local trust boundaries; it does not permit the business app to modify its own audit store. Full implementation verification remains required at applicable Construction gates.

## Final Inception review boundary

Review this map with `unit-of-work.md` and `unit-of-work-dependency.md`. Request changes if ownership, boundaries or dependencies are wrong. On explicit approval of all three artifacts, mark Units Generation and Inception complete and **stop before Construction**. Do not interpret the generic continuation wording in upstream rules as authorization to implement now.
