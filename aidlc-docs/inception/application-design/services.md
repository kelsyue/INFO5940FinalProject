# BigRedRoutes — Services and Orchestration

**Status:** APPROVED. Exact user response “Approve & Continue”, recorded 2026-11-24T17:34:08Z in `../../audit.md`. No implementation, OS configuration or test success is implied.

## S01 — Local session and secured request service

C14 verifies encrypted paths/key access, loopback bindings, local HTTPS certificate configuration and collector isolation before stateful startup. C01 obtains its one-use bootstrap credential through the operator-controlled launch flow, submits it as an HTTPS request body (never a query/fragment/history/log entry), and C03 exchanges it for a server-side opaque session. Draft defaults are a 60-second bootstrap, 30-minute idle/eight-hour absolute session expiry and Secure/HttpOnly/SameSite=Strict cookie. Token material is random, OS-protected or transient as appropriate, never hardcoded or stored in browser local storage.

C02 applies validation, rate limits, explicit-origin and CSRF checks, and C03 authorization to every protected route. Static shell and minimal liveness are explicitly public; they contain no user data. Readiness/details, jobs and plans are protected. Logout/expiry revokes the session, cancels unfinished session jobs and clears result access. Stable local owner identity persists without reactivating any old session/job. No password, Cornell login, browser administrator or remote account feature is added. Privileged setup/import/restore is a local OS-authorized operator action, not a browser admin role.

## S02 — Owned local background-job service

C04 is a bounded process-local registry/worker within the modular API runtime. No cloud queue, external broker, durable raw job transcript or automatic restart replay. At most one compute job is active and one waiting; excess submissions receive explicit busy/retry status. Direct catalog/readiness/saved-plan reads do not queue behind model inference; the worker must not block the API event loop.

1. Authenticate/validate submission and bind owner/session/epoch, optional plan ID/version and an opaque job ID.
2. Establish the 150-second deadline at accepted submission, including queue wait, tools, model repair and result publication. The queue cannot restart this budget.
3. Transition queued to running only if deadline/session/deletion guards remain valid; invoke S03 with the same budget.
4. Publish a typed terminal result only if guards still permit it. Job states are queued/running/succeeded/failed/cancelled/expired; a succeeded job may have complete, partial or pending-confirmation itinerary outcome and normal/fallback execution mode.
5. Owner-scoped polling cannot reveal another principal's inputs/results. Cancellation atomically establishes a no-future-publish/no-future-commit fence. If a short protected save finished first, return its actual receipt instead of claiming to undo it.

Raw input and job results stay in bounded memory. Drop prompt text once interpretation no longer requires it. Completed results expire after at most five minutes or earlier on logout, related deletion/reset or shutdown. Session/deletion invalidation discards affected drafts too, including new proposals derived from a now-deleted plan. No result is written into browser persistence, SQLite, backup or logs as a raw chat transcript.

After API restart, a new epoch makes old handles unavailable; no jobs resume. UI explains interruption and checks saved plan/version before explicit resubmission. Previously committed structured plans remain readable under a new valid local session. A result existing in job memory is never represented as a durable saved plan.

## S03 — Planning and bounded-agent service

For General mode, C05 obtains C08 destination data without Cornell fields. For Cornell mode, it additionally retrieves public academic context, official provider links and C09 TCAT data where requested/valid. Cornell/DC destination planning does not assert an unsupported transport corridor. Missing first/last-day anchors require confirmed activity windows; they do not trigger inferred provider departures.

C06 proposes typed intent/tool steps; C07 validates the registered call/arguments and dispatches only academic/provider/GTFS/attraction/constraint/validation tools. The same six-call maximum, 15-second per-tool limit and one malformed-output repair apply across the job, not separately per component. Model output size is capped before parsing. Missing tools/invalid IDs or external instructions cannot widen permissions.

C10 computes/validates windows, catalog selections, source-date applicability, transfers, non-overlap, pace, admission/food arithmetic and provenance. C05 returns structured plan/diff/issues. Narration is only an explanation of trusted typed results and cannot upgrade an estimate/reference/user entry to published evidence. Unknown venue hours remain unscheduled until user confirmation; unknown fees never become zero or a complete-budget claim. Infeasibility returns partial/pending outcomes with unscheduled requests and a question about which constraint to change, never a silently relaxed limit.

If the local model fails, use the approved deterministic path from structured inputs with fallback label; natural-language operations remain unavailable. Saved reads and references remain independent. Missing encrypted store/authorization/collector controls are security failures, not reasons to bypass controls under “fallback”. No fake provider data fills a gap.

## S04 — Source and evidence service

C08 returns versioned reviewed academic/provider/attraction records with SourceStamp, applicability and unknowns. At least 12 sourced venues per city are a catalog acceptance condition. Input documents' calendar/feed dates are historical claims; Dyllan must verify actual sources before importing/using them. There is no claim that the current design run fetched or certified a live feed.

C09 accepts only an operator-selected local official GTFS archive after permission review. It validates bounded extraction, schema/relationships, service/calendar exceptions, stop mapping/direction and after-midnight aware time handling before publishing a new local source version. Reject unsafe paths/oversized content and preserve the last good version on failure. Synthetic fixtures belong only to tests and cannot be used as genuine scheduled runtime data. Missing feed/service/path returns unavailable plus official link; never an invented departure. Exact routing/DST algorithms remain Functional Design work.

All app-owned runtime source files/caches, including imported feeds and extraction staging, use the encrypted private location. Public reviewed seed documents may remain in the repository as non-sensitive inputs; raw downloaded feeds/keys/runtime plans are excluded. Source access is read-only to the model; it cannot choose arbitrary file paths or URLs.

## S05 — Versioned saved-plan lifecycle service

C11 is the sole mutation/restore boundary. Planning jobs produce candidates; saving is an explicit authorized action using a current candidate/confirmation. Revisions cannot silently save broader changes. Existing plan ID/version and exact confirmable changes are bound to the principal; stale versions return conflict and never overwrite newer state.

For each save, C11 rechecks input/domain validation, session/owner permission, current version, deadline/cancellation if executing within an active job, deletion epoch and protected-store/collector readiness. Serialize the final protected check/commit decision with delete/reset/cancel fences; never rely on stale checks taken before inference. C12 uses parameterized SQLite transactions under verified encrypted paths. Close connections/rollback on error. Emit only safe structured audit metadata (pseudonymous actor/resource references, action, timestamp, version/state hashes) to C15, not before/after itinerary contents.

After a committed save, create/verify an encrypted latest-state snapshot before replacing the previous known-good copy. SaveReceipt separates actual committed plan version from current/failed/pending snapshot status. An interrupted snapshot cannot be labeled backed-up; preserve the prior valid snapshot and surface a safe retry/failure state. Persistence success is not inferred from a completed generation job.

### Delete/reset and no-resurrection invariant

Before acknowledging deletion, establish a durable ledger fence that is not part of a replaceable plan snapshot; cancel/invalidate all affected jobs/results; remove live data; purge/rewrite every app-managed recoverable copy containing removed plan data, including SQLite side files and transient restore staging; verify the resulting retained state. Reset requires explicit confirmation and applies the same protections to all owner plans. Record only opaque deleted identifiers/epochs, not recoverable itineraries, in the protected ledger.

If purge/rewrite cannot finish, return incomplete/failure and keep access/restore fenced; never claim deletion complete while a retained copy can restore the data. Repeated deletion cannot recreate state. Future saves based on pre-deletion jobs/versions are rejected, including a “new plan” candidate derived from deleted data. Current deletion/owner fences survive restart and are never rolled back by restoring an older snapshot.

This design defines the required trust/consistency invariant, not a proven crash protocol or secure forensic erasure guarantee. Functional Design must define ordering, locking, failure recovery and purge handling for all file copies; Construction must test interrupt points. Unmanaged OS backups, malicious root/OS compromise and deleted bytes outside app-controlled encrypted storage are not claimed under the application guarantee.

## S06 — Operator-local restoration service

Restore is an OS-authorized maintenance command; stop accepting jobs/mutations and invalidate transient work before staging a candidate snapshot in encrypted storage. Verify snapshot identity/schema/integrity, preserve the current stable owner configuration and non-rollback ledger, and filter/purge tombstoned records before any data is exposed. An unavailable/corrupt ledger fails closed: do not substitute the older ledger in a snapshot or expose potentially deleted plans. Do not restore bootstrap/session secrets or job epochs.

Validate structured plans/provenance after restoration, take a current deletion-safe snapshot and record a safe restore outcome. Failed verification leaves current valid data intact where possible and exposes no partially restored records. Show only an operator-safe failure, not fabricated recovered content. A documented restore check before the final demo is required; no numeric recovery-time/data-loss guarantee or survival of laptop/key loss is promised.

## S07 — Protected local observability service

C15 runs under a distinct OS identity that owns its encrypted store and retention mechanism. The app may submit allowlisted structured events through peer-authorized local IPC and query aggregate metrics, but has no file-write/delete/raw-log-read rights. Retain security logs at least 90 days with append-only/tamper-evident storage. An app-writable hash chain alone is insufficient isolation. C14 verifies the configured identity/permissions; inability to establish it is a Construction blocking finding, not a reason to assert compliance.

Events include timestamp, correlation ID, level, code, pseudonymous actor/resource and non-sensitive state/version hashes. No raw prompts, session/bootstrap tokens, keys, private itinerary details or user calendar/booking credentials. OS permissions/keys protect collection; collector's own failures use a separately protected system/operator diagnostic path, not recursive logging or plaintext files. Logging remains bounded; failure to record a required security mutation event prevents that sensitive mutation from falsely reporting full success.

C13 exposes protected aggregate counters/status for job latency/errors/deadlines, model/data readiness, vault/key state, failed snapshots/restores, collector readiness and security denials. Repeated bootstrap failures or authorization denials, unexpected local peer/permission changes, ledger corruption and backup/log integrity failures produce a local alert indicator visible to the operator. No Slack/email/external notification integration is required or sent. Formal incident process/tool decisions remain at the allowed NFR Design gate.

## Transport and local security applicability

Browser-to-API is local HTTPS (TLS 1.2+), same origin, strict CSP (`default-src 'self'` with only specifically required local allowances), HSTS `max-age=31536000; includeSubDomains`, `nosniff`, anti-framing `DENY` and `strict-origin-when-cross-origin`. Disable directory listing, debug traces and example endpoints in the final demo. Local certificate/key provisioning and browser trust must be verified in Construction.

SQLite/files/snapshots have in-process/local filesystem access, not a network database connection; TLS connection-string requirements are N/A to that access path. Collector uses OS-protected local IPC. Ollama may use private loopback HTTP for inference only: it is not a database/storage network protocol and must never bind publicly or log private prompts. This does not claim HTTP is encrypted. If a networked storage/collector interface is introduced, require TLS rather than inheriting this local-access applicability decision. No cloud secrets manager is required; OS key protection is the accepted local equivalent.

## Verification handoff

All flows are architecture specifications, not observed results. Functional Design must supply job/commit/cancel/delete atomicity, session/token details, GTFS/time and snapshot crash algorithms. NFR Design must decide the deferred release/rollback/incident/testing processes. Code Generation/Build and Test must prove security boundaries, full PBT plus concrete scenarios, seeded reproducibility, ≥80% planner/validator coverage target and actual performance on Kelly's laptop.


### Candidate save timing clarification

Completed candidates may be explicitly saved while their short result lifetime remains valid. C11 verifies that publication originally completed before the job deadline, and rechecks current owner/session, candidate invalidation, deletion epoch and expected plan version. This is a separate bounded user-authorized save operation, not an extension/restart of the inference job. Late active-job writes remain forbidden. Deletion/logout/cancellation invalidation still revokes applicable candidate access immediately.
