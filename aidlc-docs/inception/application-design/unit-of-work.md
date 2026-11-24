# BigRedRoutes — Unit of Work

**Status:** APPROVED. Exact user response “Approve units and stop before Construction”, recorded 2026-11-24T17:44:20Z in `../../audit.md`. Inception complete; Construction not started.

## U01 — BigRedRoutes local application

**Purpose:** Deliver the approved single-laptop General NYC/DC and Cornell campus-origin/NYC travel planner with honest evidence, bounded local LLM jobs, deterministic validation and protected local plan lifecycle.

**Unit boundary:** One application delivery/construction unit contains the React UI, modular FastAPI runtime and all required supporting local integration/configuration. Ollama is a local dependency; the protected collector is a separately owned OS process delivered/configured within this unit, not an invented feature microservice or a second application unit. All 24 stories have exactly one primary unit: U01.

**Owned responsibilities/data:** Typed trip/window/anchor/provenance contracts; reviewed source catalogs and local GTFS import; deterministic planner/validators; owned transient background jobs; local session/object authorization; structured saved plans, current deletion ledger and encrypted latest-state snapshots; safe aggregate readiness/log integration; UI/accessibility. Current identities/keys, source caches, database side files, snapshots and collector logs use their approved protected runtime locations outside Git.

**Public interfaces:** Approved local HTTPS routes and operator-local commands in `component-methods.md`. Safe event IPC/schema is a neutral contract between the app and the independently owned collector, not permission for the collector to import business code or for the app to rewrite logs.

**Constraints:** No cloud, live inventory/booking, personal Cornell calendar, unlimited destinations, raw-chat persistence, automatic job replay or guaranteed recovery time. All approved requirements and extension obligations remain in U01. One unit does not mean one undifferentiated task: use the following work packages and their dependency/acceptance checkpoints throughout its later per-unit lifecycle.

## Logical implementation work packages

These are internal modules/work packages, not separately deployable business services or additional AI-DLC stages. Component ownership is unique; other packages consume their typed ports.

| Package | Components owned | Responsibilities and owned boundary | Lead / review | Observable acceptance checkpoint |
|---|---|---|---|---|
| M01 Contracts, identity and runtime trust | C02 ApiBoundary, C03 LocalIdentity, C14 RuntimeSecurity | Shared types/event/guard contracts; validation/error/auth/origin boundaries; stable owner/bootstrap/session; verified loopback/HTTPS/encrypted-path/key readiness. Safe event contract in neutral config/schema, no collector dependency on backend business imports | Ananya; Kelly reviews security/contracts | Typed boundaries reject invalid/unauthorized access; secured setup readiness is explicit. Contract fixtures can be used before collector integration; full stateful acceptance waits for M07 |
| M02 Reviewed sources and TCAT | C08 SourceCatalog, C09 TcatAdapter | Academic/provider/venue source records, ≥12 sourced venues/city, GTFS importer/service/date/path checks, provenance/unknown semantics | Dyllan; Kelly reviews temporal/data contracts | Valid/invalid/out-of-range/exception/after-midnight sources tested; no synthetic runtime schedule, no raw unlicensed feed committed; no guessed venue hours/prices |
| M03 Deterministic planning and validation | C10 DomainPlanner | Input/window/transfer/schedule/cost/provenance submodules, partial outcomes and constraint-change proposals. No I/O/model/identity ownership | Kelly; Dyllan reviews transit semantics, Sarah reviews user outcomes | Confirmed windows/buffers/pace/city/non-overlap/cost completeness hold, exact transfer boundary works, unknowns never promoted; pure logic supports generated properties |
| M04 Owned jobs, model and tools | C04 JobCoordinator, C05 PlanningOrchestrator, C06 ModelGateway, C07 ToolRegistry | Process-local one-active/one-waiting jobs; owner/session/version/deadline/cancel guards; local model interpretation/typed tools; both-mode orchestration/revisions/fallback; transient result retention and restart epoch | Kelly; Ananya reviews lifecycle/session integration | Typed poll/cancel/result distinguishes job/itinerary/fallback state; 150-second budget includes queue wait; six calls/one repair; no raw-chat persistence/late writes/automatic replay |
| M05 Plan lifecycle, storage and recovery | C11 PlanLifecycle, C12 ProtectedStore | Sole authorized serialized SQLite mutation/restore, expected versions/exact confirmations, encrypted plan/snapshot paths, current non-rollback deletion ledger, purge/rewrite/maintenance restore | Kelly; Ananya reviews encryption/deletion trust boundaries | Save receipt separates commit from backup success; stale revisions denied; delete/reset and restore cannot resurrect removed plans; interrupted unsafe state fails closed |
| M06 Browser experience and accessibility | C01 BrowserUI | Mode/form/window controls, job progress/cancel, day/budget/provenance cards, partial-plan questions, confirmed revision diff, local save/delete/reset and status view | Sarah; all members review journeys | Both modes complete without irrelevant fields; unknowns/partial/fallback/history readable; keyboard/screen-reader-oriented flows, narrow viewport and confirmations usable |
| M07 Protected observability and collector integration | C13 ReadinessMonitor, C15 ProtectedLogCollector | Independently OS-owned encrypted append/tamper-evident collector, ≥90-day security retention, safe event allowlist/aggregate queries/alerts; local dependency/backup/job health | Ananya; Kelly reviews permissions/data minimization | App may submit safe events/read aggregates but cannot rewrite/delete/raw-read collector logs; no secrets/prompts/private plan contents; loss of required controls marks security-unready |

No ownership assignment claims that the work has already occurred. Ananya and Kelly jointly review identity/encryption/deletion mechanisms; all four members continue major AI-DLC decisions. Lead assignments do not grant system permissions or identify who operates the current conversation.

## Greenfield code organization strategy

Use the installed single-unit pattern `src/`, `tests/`, `config/` at the repository root. Proposed paths below are documentation only; none are created by this Inception artifact.

| Root-relative path | Intended contents / ownership |
|---|---|
| `src/frontend/` | React/TypeScript UI, M06; local bundled assets only |
| `src/backend/` | Modular Python/FastAPI app, M01–M05 and M07's safe readiness adapter |
| `src/backend/contracts/` | Typed domain/API/guard schemas, M01; no SQLite/model imports |
| `src/backend/api/`, `src/backend/identity/`, `src/backend/runtime/` | M01 boundaries/adapters |
| `src/backend/sources/` | M02 reviewed catalog/TCAT ports and importer |
| `src/backend/domain/` | M03 pure deterministic submodules |
| `src/backend/jobs/`, `src/backend/orchestration/`, `src/backend/model/`, `src/backend/tools/` | M04; only declared ports to other modules |
| `src/backend/lifecycle/`, `src/backend/storage/` | M05; sole plan mutation boundary/repository implementation |
| `src/backend/readiness/` | M07 aggregate status adapter; no raw collector log access |
| `src/collector/` | M07 separately OS-owned collector implementation; neutral event/schema dependency only |
| `tests/frontend/`, `tests/backend/`, `tests/collector/` | Mirror code boundaries; example-based and PBT suites clearly distinguished |
| `tests/fixtures/` | Clearly labeled synthetic GTFS/city/model/error/temporal examples; never imported as actual traveler schedules |
| `config/contracts/` | Neutral versioned safe-event schema shared by producer/collector; no private key/owner/session data |
| `config/` | Non-secret local default configuration/templates; explicit validation required at startup |
| `scripts/` | Existing installer plus later local setup/import/restore/build verification entry points; privileged changes require actual execution authorization at that time |
| `docs/`, `examples/` | Existing input/reference documents and illustrative examples; examples are not served as product endpoints |
| `aidlc-docs/` | Generated workflow documentation only; never implementation, runtime data or test code |

Exact Python/TypeScript manifests and working dependency pins are established during Construction. Runtime archives, plaintext/secret config, SQLite/WAL/journals, ledger, backups, local certificates/private keys, session/bootstrap material and collector logs belong in approved protected OS paths, not the repository or a public artifact. Shared types/schema versions and round-trip tests must prevent producer/collector drift without cross-importing business implementation.

## U01 acceptance and completion criteria for the final project

- Both General/DC and Cornell/NYC journeys work, with reviewed catalogs and honest provider/source/date/unknown semantics. No confirmed TCAT departure without genuine applicable source/path.
- Window/transfer/budget/pace/provenance validators and targeted-revision confirmation guard every returned/saved plan; incomplete plans ask which constraints to change.
- Local Qwen3/tool behavior is bounded and benchmarked, structured fallback is labeled, transient jobs do not become raw-chat storage, and cancellation/restart/deletion prevents late state resurrection.
- Local identity/session/object authorization, HTTPS/headers, encrypted stores/backups, independent protected logs/retention/alerts and fail-closed readiness are actually verified, not assumed from approved documents.
- Latest-state snapshot/restore is tested; ledger/current owner state cannot be rolled back; delete/reset protects every app-managed recovery copy. Save/backup failures are truthful.
- Accessibility scenarios and all 72 story criteria are covered by meaningful checks. Pure planner/validator coverage target ≥80%; full applicable PBT plus example scenarios with generators/shrinking/seeds/CI, not implementation-mirroring tests alone.
- All approved FR/NFRs, extension rules and later permitted process decisions are resolved/verified in their applicable stages, with actual team approvals. Component/work-package checkpoints do not replace per-unit AI-DLC gates.

These are future Construction completion criteria. At this milestone only unit documentation is generated and reviewed. After unit artifact approval, mark Inception complete and STOP before Construction.

## Related artifacts

- [Dependency/order map](unit-of-work-dependency.md)
- [Story and requirement map](unit-of-work-story-map.md)
- [Approved application design](application-design.md)
