# BigRedRoutes — Component Methods and Contracts

**Status:** APPROVED. Exact user response “Approve & Continue”, recorded 2026-11-24T17:34:08Z in `../../audit.md`. No implementation, OS configuration or test success is implied.
**Notation:** Signatures describe typed interfaces only. Detailed algorithms, schema validators and failure/transaction implementation belong to per-unit Functional Design/Construction.

## Shared records

| Type | Fields and meaning |
|---|---|
| Principal | Stable owner ID, session ID, permitted capabilities, server-derived expiry; never trusted from browser payload |
| RequestContext | Correlation ID, accepted instant, deadline, owner/session, job ID if applicable, cancellation/revocation guard |
| SourceStamp | Source URL, captured instant, applicable dates, source version/hash where available, status published-schedule/reference-link/user-provided/estimate/unavailable |
| TripRequest | Mode, city, dates, 1–4 adults, $25–$300/person/day budget, food allowance, interests, pace, campus area only for Cornell, confirmed day windows/anchors and venue constraints |
| EvidenceBundle | Typed academic/provider/catalog/GTFS results with source stamps; missing values explicit, never zero/free/confirmed by default |
| PlanDraft | Plan ID if saved, expected/current version, structured days/visits/constraints, costs with completeness flag, warnings, provenance, unscheduled requests |
| PlanResult | Completeness complete/partial/pending-confirmation; execution normal/fallback; candidate plan, diff, unmet constraints, confirmation proposal, warnings/provenance; no persistence success implied |
| JobTicket | Opaque job ID, server epoch, accepted/deadline instants and safe poll/cancel references; not raw input or a bearer credential |
| JobView | queued/running/succeeded/failed/cancelled/expired, current epoch, optional typed PlanResult or safe error, result expiry; no other-owner information |
| Confirmation | Owner/session-bound proposal ID, expected plan version, exact changes confirmed and expiry; not an arbitrary boolean accepting unseen changes |
| CommitGuard | Valid principal, expected plan version, job/session cancellation and deadline state, deletion epoch; rechecked at mutation boundary |
| SaveReceipt | Plan ID/version, commit outcome, snapshot current/failed/pending status and safe warning; committed state and backup success separate |
| DeleteReceipt | Complete only after authoritative tombstone and purge/fencing of all recoverable copies; otherwise safe incomplete/failure, never false success |
| DomainIssue | Stable code, affected field/constraint, safe explanation and proposed next action, without internal paths/secrets |

All travel instants are timezone-aware; local service date is retained separately from UTC comparisons. Identifiers are opaque, never secret authorization substitutes. Monetary calculation uses exact decimal/minor units; unknown remains null. A user's confirmation changes provenance to user-provided, not published-schedule.

## Public API / browser contracts (C01–C03)

Every route has schema, owner/capability checks unless explicitly public, bounded payloads and safe error mapping. These are proposed route contracts, replacing the original synchronous illustrative generation endpoint behavior without changing product outcomes.

| Method/path | Input → output | Policy |
|---|---|---|
| GET `/` and bundled assets | None → static UI shell | Explicitly public shell; no private embedded data, model HTML or CDN scripts |
| GET `/api/v1/health/live` | None → minimal live/not-live | Public, no dependency versions/paths/details |
| POST `/api/v1/session/bootstrap` | One-use launch token → session cookie + safe owner context | Credential-gated public entry, same-origin/rate-limited; token never URL query/logged/stored in browser persistence |
| DELETE `/api/v1/session` | Auth + CSRF/origin → invalidated | Cancels unfinished session jobs, clears transient results and cookie |
| GET `/api/v1/health` | Auth → aggregate readiness | No raw logs, credentials or private prompts |
| GET `/api/v1/academic-events` | DateRange → stamped events/issues | Protected typed lookup |
| GET `/api/v1/transport-options` | Cornell context/date → stamped options/issues | No live inventory; invalid unsupported corridor explicit |
| GET `/api/v1/attractions` | City/interests → stamped catalog | No invented IDs/hours |
| POST `/api/v1/planning-jobs` | TripRequest plus optional transient natural language → 202 JobTicket | Queue admission and deadline established at acceptance |
| POST `/api/v1/itineraries/{id}/revision-jobs` | Expected version, target, transient instruction → 202 JobTicket | Ownership and current version checked at submit and any eventual save |
| GET `/api/v1/jobs/{id}` | Auth + epoch → JobView | Owner/session guard; status/result polling |
| DELETE `/api/v1/jobs/{id}` | Auth + mutation guard → cancellation outcome | Cannot claim rollback of an already completed commit |
| POST `/api/v1/itineraries` | Candidate reference + Confirmation/validated structured plan → SaveReceipt | Explicit save, revalidate candidate ownership/version/expiry and all invariants |
| GET `/api/v1/itineraries/{id}` | Auth → saved PlanDraft | Read applies current deletion ledger |
| DELETE `/api/v1/itineraries/{id}` | Expected version + auth → DeleteReceipt | Cancel affected jobs and purge/fence recoverable copies |
| POST `/api/v1/local-plans/reset` | Current reset confirmation + auth → DeleteReceipt | Explicit reset-all confirmation, owner-scoped data only |

Restore, source import and key/collector setup are operator-local commands/ports, not browser admin APIs. No application admin account is introduced. Demo product does not serve `examples/` endpoints or debug/directory-listing pages.

Safe status mapping: 202 accepted job; 200 result/read or successful mutation; 401 absent/expired session; 403 origin/CSRF/capability failure; 404 unknown or other-owner resource; 409 stale version/conflicting confirmation or lifecycle failure; 422 invalid contract; 429 bounded queue/rate limit; 503 required dependency/protection unavailable. Job terminal failure uses a safe typed error in JobView; completed partial plans are successful job results, not malformed-request errors. Restart-lost/expired jobs return safe unavailable/404 and never replay automatically.

## Internal component ports

| Component | Interface signature | High-level result/purpose |
|---|---|---|
| C03 LocalIdentity | `issue_bootstrap(operator_context) -> BootstrapHandle` | Local operator entry; one-use short-lived credential |
| C03 | `exchange_bootstrap(token, origin) -> SessionGrant` | Validate one-use credential, create expiring server-side session |
| C03 | `authorize(session, action, resource_owner) -> Principal or SafeError` | Deny by default; validate ownership/capability/expiry on every access |
| C03 | `revoke_session(principal) -> RevocationReceipt` | Invalidate session and notify job guard |
| C04 JobCoordinator | `submit(principal, operation, input, expected_version?) -> JobTicket or Busy` | Admission, owner binding, epoch and deadline |
| C04 | `poll(principal, job_id, epoch) -> JobView` | Typed status/result with no cross-owner leak |
| C04 | `cancel(principal, job_id) -> CancelReceipt` | Set cancellation fence, suppress late result/commit |
| C04 | `invalidate_for_plan(owner, plan_id_or_all) -> InvalidationReceipt` | Delete/reset invalidates work/results before final deletion confirmation |
| C04 | `check_guard(context) -> GuardDecision` | Current deadline/cancel/session/deletion state, not stale cached flags |
| C05 PlanningOrchestrator | `generate(request, context) -> PlanResult` | Retrieve evidence, interpret if needed, plan and validate |
| C05 | `propose_revision(saved, change, context) -> PlanResult` | Scope changes, retain originals, create confirmable diff |
| C06 ModelGateway | `infer(messages_in_memory, allowed_tools, budget) -> ModelStep or ModelFailure` | Bounded untrusted response; no persistence authority |
| C07 ToolRegistry | `invoke(call, context, shared_budget) -> TypedToolResult` | Validate allowlisted call/result and charge same six-call budget |
| C08 SourceCatalog | `academic_events(range) -> SourceResult[AcademicEvent]` | Applicability and university-wide qualifier |
| C08 | `provider_links(cornell_context) -> SourceResult[ProviderOption]` | Reference links, unknown fares/seats/times |
| C08 | `attractions(city, filters) -> SourceResult[Attraction]` | Known/unknown fees/hours, stable IDs |
| C09 TcatAdapter | `import_feed(archive_handle, source_review, operator_context) -> ImportReceipt` | Validated local import, preserve last good source on failure |
| C09 | `connections(stops, service_date, constraints) -> SourceResult[TransitLeg]` | Valid service/path and aware instants or unavailable |
| C10 DomainPlanner | `validate_input(request) -> ValidInput or Issues` | Field and cross-field contract |
| C10 | `activity_windows(request, evidence) -> Windows or Pending` | Confirmed bounds and buffers, one-day intersection |
| C10 | `transfer(leg, confirmed_departure, margin) -> Feasible/Infeasible/Unknown` | Source-valid boundary check |
| C10 | `plan(input, evidence, windows) -> PlanDraft` | Deterministic bounded candidate assembly |
| C10 | `validate_plan(draft, evidence) -> ValidationReport` | Schedule/city/hours/budget/provenance invariants |
| C11 PlanLifecycle | `read(principal, plan_id) -> PlanDraft or SafeError` | Authorized ledger-aware current state |
| C11 | `current_guard(principal, plan_id_or_epoch, version?) -> GuardDecision` | Read-only current owner/version/deletion fence for job publication/candidate access |
| C11 | `save(principal, candidate, confirmation, guard) -> SaveReceipt` | Validated versioned commit; explicit snapshot outcome |
| C11 | `delete(principal, plan_id, version) -> DeleteReceipt` | Durable deletion fence, job invalidation and copy purge |
| C11 | `reset(principal, confirmation) -> DeleteReceipt` | Confirmed owner-scoped reset and recovery-copy cleanup |
| C11 | `restore(operator_context, snapshot_handle) -> RestoreReceipt` | Maintenance-mode restore obeying current owner/ledger, never restore secrets/sessions |
| C12 ProtectedStore | `load/save_transaction/snapshot/purge/restore_candidate(...) -> TypedStorageResult` | Repository port used only through lifecycle; no browser/model calls |
| C13 ReadinessMonitor | `status(principal) -> ReadinessView` | Safe aggregate app/model/feed/vault/backup/collector state |
| C14 RuntimeSecurity | `verify_runtime(operator_context) -> RuntimeReady or Denied` | Encrypted paths, keys, secure origin and collector isolation checks |
| C15 ProtectedLogCollector | `submit(safe_event) -> EventReceipt` | Peer-authorized protected append; sensitive fields excluded |
| C15 | `aggregate_status(peer) -> SafeMetrics` | Read-only counters/alerts, no raw event/plan contents |

## Design defaults and unresolved implementation details

Draft defaults for this design review: bootstrap lifetime 60 seconds; session idle expiry 30 minutes and absolute expiry eight hours; one active/one queued compute job; completed results at most five minutes. All jobs share accepted-time deadline 150 seconds, tool deadline 15 seconds, six tool calls and one repair. A session's revocation invalidates its work; owner identity can persist across new sessions without reviving old jobs.

Bound browser JSON bodies to 32 KiB, natural-language fields to 2,000 characters and model step output to a configured 32 KiB ceiling before parsing; stop accumulating beyond the bound. Archive entry count, decompressed-byte and row limits are mandatory import configuration, set against the actual reviewed feed during Functional Design before implementation. No unbounded archive extraction, SQL construction or output accumulation is permitted. Typed safe errors cover size failures. These are reviewable design defaults, not measurements of the selected model/feed.

Plan versions, current deletion epoch and session guards must be atomic with mutation permission checks. HTTP retry/idempotency details, ledger/crash protocol, scheduling/GTFS algorithms, concrete OS mechanisms and exact dependency pins are deferred to Construction; they cannot weaken these interfaces or acceptance outcomes.


### Completed candidate versus active job deadline

A job must compute and publish its result before its accepted-time deadline. A later explicit browser save is a new short authorized operation, not a resumed inference job: require that the candidate was validly published before that deadline, remains within its at-most-five-minute result lifetime, belongs to the current authorized owner/session and is not cancelled/invalidated/stale/deleted. Recheck the current plan version, confirmation and deletion fences. The new save has its own bounded API/transaction context; it never extends or restarts the original inference budget. While a job is active, no commit/publication can outlive its deadline. This distinction avoids treating retained completed results as permission for late background writes.
