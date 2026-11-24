# BigRedRoutes — Technical Environment & Engineering Constraints

**AWS AI-DLC v1.0.1 input document; team review reported November 24, 2026. Requirements Q&A reconciliation below does not imply approval of the generated requirements or a completed implementation.**  
**Chosen concept:** Two-mode, locally demonstrable Cornell-aware + general travel itinerary planner.  
**Important:** This document specifies a design; it is not proof that the full application has been coded or external APIs are integrated.

## 1. Runtime, frameworks and packages

| Layer | Technology / version | Package manager / reason |
|---|---|---|
| Web UI | TypeScript **5.x**, React **19.x** | npm + pinned `package-lock.json`; accessible typed components |
| Frontend build | Vite **6.x or 7.x**, Node.js **22 LTS** | Pin a compatible minor version when implementation begins |
| API/service | Python **3.11.x**, FastAPI `>=0.115,<1` | `python -m venv`, `pip`, pinned requirements once tested |
| Schema validation | Pydantic `>=2,<3` | Request validation, LLM tool calls, provider metadata schema |
| HTTP client | httpx `>=0.27,<1` | Timeouts, bounded LLM requests; no uncontrolled provider scraping |
| ASGI server | Uvicorn `>=0.30,<1` | Local FastAPI development service |
| LLM runtime | Ollama localhost, proposed `qwen3:4b` | No paid key; tool calls + JSON schema validation, fallback for incompatible output |
| Storage | SQLite via Python `sqlite3` | Draft plans, versioned source metadata; no account needed |
| Dates/time | Python `datetime`, `zoneinfo` | IANA timezone `America/New_York`, DST-safe aware time checks |
| Transit feed | Python standard `zipfile` + `csv` GTFS static parser | Offline, explicit `calendar.txt` + `calendar_dates.txt` service applicability |
| Backend tests | pytest `>=8,<10`, pytest-cov | Deterministic algorithm, schema, GTFS and API tests |
| Frontend tests | Vitest + React Testing Library | Form, mode, provenance/status and accessibility regression |
| Formatting | Ruff + Prettier (later) | Repeatable project style; not a prerequisite to Inception |

Choose and pin exact working minors in Construction after running the environment check; do not assert all version combinations have been exercised.

## 2. Deployment and dependencies

Local-only demo: **Browser** `localhost:5173` → **FastAPI** `localhost:8000` → **SQLite/curated JSON, GTFS fixture** and optional **Ollama** `localhost:11434`. No cloud account, Cornell login, API key or payment platform is required. The app must offer a read-only deterministic fallback/warning when local model inference fails, rather than fabricate a result. Demo data must be bundled or downloaded under permitted licenses and accurately attributed; fake *transport times* may be used only inside clearly labeled unit-test fixtures, never surfaced as real provider schedules.

**Model availability gate:** Kelly Yue’s laptop is reported as macOS Tahoe 26.5.2 with 16 GB RAM; the team reports Qwen3 4B works. Ollama version, structured tool behavior and measured latency remain to be checked during Construction. The code should isolate the LLM behind `LLMClient` so a model change can be made without changing planning logic. The coding agent (Codex/Cursor/etc.) is **distinct** from the product LLM. AI-DLC workflow uses official **v1.0.1** rules.

## 3. Logical architecture

```text
React UI
  ├─ ModeSelector (General / Cornell)
  ├─ TripForm + CornellOriginFields
  ├─ AcademicBreakContext
  ├─ TransportOptions (source, as-of, status, official link)
  ├─ DayTimeline / BudgetSummary / Warnings
  └─ RevisionPanel
         │ POST typed payload / GET saved plan
FastAPI REST API
  ├─ InputSchema + StatePersistence
  ├─ IntentInterpreter → Local Ollama (bounded tools/JSON)
  ├─ ToolRegistry
  │    ├─ AcademicCalendarSnapshot
  │    ├─ ProviderDirectory (OurBus, C2C, ITH links)
  │    ├─ TCAT_GTFS_Adapter (service dates, stops, trips, exceptions)
  │    └─ AttractionCatalog (NYC, DC)
  ├─ ItineraryPlanner (deterministic slotting + city zones)
  ├─ ConnectionValidator (local time + buffers + coverage)
  ├─ CostValidator (USD known/unknown separated)
  └─ ProvenanceValidator / WarningAssembler
        └─ SQLite (local draft) + vetted data snapshots
```

**No external source can be considered a live inventory unless a licensed, supported integration is implemented and tested.** OurBus, C2C and ITH are MVP **reference provider links**, not live search APIs.

## 4. Data shapes / contracts

All provider observations carry source provenance and coverage. Proposed Pydantic records:

```python
from datetime import date, datetime
from typing import Literal
from pydantic import BaseModel, Field

class SourceStamp(BaseModel):
    url: str  # approved trusted URL
    observed_at: datetime  # aware timestamp
    status: Literal["published-schedule", "reference-link", "user-provided", "estimate", "unavailable"]
    valid_start: date | None = None
    valid_end: date | None = None

class TripRequest(BaseModel):
    mode: Literal["general", "cornell"]
    destination: Literal["new-york-city", "washington-dc"]
    start_date: date
    end_date: date
    budget_usd_per_person_day: int = Field(ge=25, le=300)
    party_size: int = Field(ge=1, le=4)
    pace: Literal["relaxed", "balanced", "packed"]
    interests: list[str] = Field(min_length=1, max_length=4)
    campus_area: Literal["north", "west", "central"] | None = None
    # Model-level validator: campus_area is required for cornell, absent for general

class TransportOption(BaseModel):
    provider_id: Literal["tcat", "ourbus", "c2c", "ith-airport"]
    label: str
    official_url: str
    source: SourceStamp
    departure_at: datetime | None = None  # only grounded or user supplied
    arrival_at: datetime | None = None
    estimated_fare_usd: float | None = None  # null when unknown; no fake zeros
    boarding_minutes: int | None = None
    notes: list[str] = []
```

Additional types: `AcademicEvent` (`name`, dates, provenance, university-wide qualifier), `Attraction` (`id`, `city`, zone, tags, visit_minutes, admission_usd|null, open_windows|null, source_url, verified_at`), `ScheduledVisit` (`attraction_id`, time bounds, buffer), `Itinerary` (`mode`, `days`, `transport_options`, `source_warnings`, `revision_diff`), `TcatServiceLookup` (`service_date`, `feed_validity`, matching_trips, `status`). Unknown is explicitly represented as `null` and a user-facing status.

## 5. Source integration plan: semantics and fallbacks

| Source | Engineering approach | When missing/stale |
|---|---|---|
| Cornell Registrar | Human-verified **versioned 2026–27 event snapshot** with official URL and captured date; only public academic calendar, no personal calendar | Show published date range or `unknown`; offer source link; do not imply student has no assignments |
| TCAT static GTFS | Import/archive a GTFS feed: `agency`, `stops`, `routes`, `trips`, `stop_times`, `calendar`, `calendar_dates`, optional `feed_info`. Query service ID for requested local date, honoring exceptions. Use GTFS 24+:00 times correctly. | If outside validity, missing stops/service or unverified routing, **do not show a confirmed trip**; show official TCAT site and `schedule not verified for date` |
| OurBus | Official Ithaca–NYC URL and known stops directory with verification date; **NO unsupported live API** | Always instruct user to check dates, specific departure, stops, ticket price and availability on OurBus |
| Cornell C2C | Cornell official schedule/stop page + reservation link. Optional reviewed weekly timetable snapshot is stretch | Label schedule 'published timetable' if manually verified and date applicable; **booking availability unverified** |
| ITH Airport | Official flight status and airline pages; optional service overview only | **No date-specific flight guarantee**, airline booking search must be checked at provider |
| NYC/DC attractions | Small versioned seed catalog, curated primary venue links, category tags, durations, approximate fees and last verified date | Unknown price/hours remain null and show verification link; no fabricated opening hours |

**Key real-world constraint observed Nov 19, 2026:** The Transitland-listed TCAT feed is valid **2026-09-22 through 2026-12-19**. Do not assume this feed covers **February 2027** just because an academic break is known. Never hard-code a future bus departure based on a prior schedule.

**TCAT implementation sketch:** Load `feed_info` if present; for target date, also inspect `calendar` base service and `calendar_dates` added/removed exceptions. Require route/stops shape to cover the selected campus stop/terminal in travel direction. Convert `stop_times` including values after midnight to dated aware instances, accounting for local DST; boarding buffer applies to transfer end not the bus timetable's own start. Search network route feasibility only if a valid data path exists; **if not, do not claim campus-to-terminal service**. Realtime GTFS-RT **not in MVP**.

**Service validity types:** `unavailable`, `reference-link`, `published-schedule`, `user-provided`, `estimate`. Never surface `published-schedule` without a timestamp, source, valid range and matched service date. A provider URL is a useful next action, **not** confirmation that a particular seat exists.

## 6. REST endpoints (proposed)

| Method | Path | Contract and behavior |
|---|---|---|
| `GET` | `/api/v1/health` | App readiness + model status (explicit fallback), source snapshot status |
| `GET` | `/api/v1/academic-events?start=...&end=...` | Public events and official sources; no personalized class schedules |
| `GET` | `/api/v1/transport-options?destination=new-york-city&date=...&campus_area=north` | Provider directory, GTFS snapshot viability and provenance; **no booking availability** |
| `GET` | `/api/v1/attractions?city=...&interests=...` | Catalog IDs with fee/hour verification tags |
| `POST` | `/api/v1/itineraries` | Validated `TripRequest` → 1–5 day plan, Cornell context when applicable, warnings |
| `GET` | `/api/v1/itineraries/{id}` | Retrieve locally saved draft; 404 if not found |
| `POST` | `/api/v1/itineraries/{id}/revisions` | Natural-language/typed changes → revalidated plan + structured diff |
| `POST` | `/api/v1/examples/connection-check` | **Example-only** deterministic endpoint shipped in starter package |

**Error codes:** 422 invalid request, 404 missing saved plan, 409 infeasible plan/confirmed connection, 503 model not available when LLM operation strictly needed (or 200 with explicit deterministic fallback status if only planning). All errors return structured machine-readable code and human explanation; do not return stack traces.

### Example HTTP request

```http
POST /api/v1/itineraries
Content-Type: application/json

{
  "mode": "cornell",
  "destination": "new-york-city",
  "start_date": "2027-02-13",
  "end_date": "2027-02-15",
  "campus_area": "north",
  "party_size": 1,
  "budget_usd_per_person_day": 80,
  "pace": "relaxed",
  "interests": ["art", "food"]
}
```

**Expected warning (not an invented schedule):** `"TCAT schedule for February 2027 is not verified by the cached feed; use tcatbus.com for updates."` Transit provider options in response have **unknown time and fare** until dates are confirmed.

## 7. Planning rules and deterministic invariants

- Two mode validation: `cornell` requires campus origin; `general` must clear incompatible fields on mode switch or flag them for correction; General planning must not depend on Cornell data.
- Trip length ≤5 days; no timezone-naive travel anchors; travel anchors explicitly labeled `user-provided` unless sourced from a valid timetable.
- No overlapping destination activity blocks; no duplicate venue within a day; venues must belong to selected city's catalog.
- Every planned activity must fit inside user-selected day window and any **confirmed** arrival/departure constraint, with conservative buffer (proposed 60 minutes after arrival before sightseeing, 90 minutes before travel departure; planning heuristics, **not provider boarding rules**).
- Connection acceptance criterion: `feeder_arrival_at + boarding_margin <= intercity_departure_at` using aware datetimes and consistent service date; otherwise reject or show unverified.
- If the GTFS feed doesn't cover target date or stop path, `feeder_arrival_at` **cannot** become a confirmed transport schedule.
- Group nearby attractions using approximate neighborhood/zone tags, not false 'optimized routing'. Buffers are disclosed estimates, not live traffic duration.
- Cost display `known_estimated_activity_cost` plus `has_unknown_fees`; unknown ticket price is not free. Transportation cost is separate; do not promise a total-trip budget when flight/hotel costs are not available.
- Required attraction omitted only if marked infeasible with reason. A request for a live fare or sold-out state gets link + honest limitation.
- Revisions produce diff and preserve unchanged days unless reallocation is required; any change is explained.
- Source details in the output survive LLM summarization; model cannot upgrade status from estimate/reference into confirmed.

## 8. LLM tool schema and safety

Allowed tools (read-only): `list_academic_breaks`, `list_provider_links`, `search_tcat_static`, `search_attractions`, `get_plan_constraints`, `validate_plan`. No general shell execution, web scraping, arbitrary URLs, email access, booking, payments, or PII access. Backend validates tool arguments against fixed enums and allowed dates, caps tool calls at 6 per request, applies 15-second per-tool deadlines and a 150-second overall deadline (including at most one repair) and handles invalid JSON with one repair attempt followed by transparent fallback. The LLM may narrate *only values present in trusted tool output*, and its text is never treated as proof that a seat/time exists.

Prompt-injection defense: External descriptions, links, attraction metadata and calendar text are **untrusted data**, not instructions; tools can be called only from backend-defined function registry. No model output may write to files or call provider APIs autonomously. For a versioned catalog, store hashes or checked source timestamps to detect unexpected changes.

## 9. Security, privacy, accessibility

- Bind model and API to `127.0.0.1` by default; configure explicit CORS dev origin, no open wildcard in production.
- Validate all incoming strings and dates; use parameterized SQLite queries; limit input sizes; do not render LLM-generated HTML.
- Do not request Cornell credentials, course enrollment data, OAuth tokens, specific residential address, booking IDs or credit-card data.
- No API secrets committed; `.env` ignored if later needed; public repository may contain only non-sensitive demo cases.
- Local itinerary retention configurable; allow delete/reset and avoid logging raw private prompts in GitHub.
- Do not imply affiliation with any university or provider; use link labels and textual warning icons, not warning color alone; keyboard and screen-reader access.
- URL allowlist for provider links; use `https://` where available; no user-supplied redirect endpoints.

## 10. Tests and quality gates

| Layer | Tool | Required checks |
|---|---|---|
| Planning functions | pytest | No overlapping items, attraction IDs from correct city, relaxed/balanced/packed caps, bounded schedule windows |
| Transfer feasibility | pytest | Equal boundary success, one-minute miss rejected, mismatched/naive timezone rejected, in-feed vs out-of-feed status |
| GTFS importer | pytest + fixtures | Calendar exceptions, dates outside feed, after-midnight GTFS times, missing stop path, DST-sensitive fixture |
| Calendar snapshot | pytest | Feb 13–16 2027 break labels, inclusive date matching, source URL and snapshot state |
| Provider integration | pytest with network mocks | No live availability claims, unknown fares stay null, source link present when schedule absent |
| LLM contracts | Stubbed Ollama | Allowed tool calls only, fake stop/venue ID rejected, malformed output safe fallback, provider prompt injection ignored |
| REST API | FastAPI TestClient | Correct mode validation, 422, 404, 409/503, data provenance in JSON |
| UI | Vitest / RTL | Switch modes, show source freshness, show 'verify on provider' links, budgets and warnings readable |
| Demo | 3+ manual scenarios | NYC Cornell, DC general, unsupported 2027 TCAT and targeted revision |
| Coverage target | pytest-cov | **≥80%** on pure planner and validator modules (goal; measure when built) |

**Example endpoint, function and pytest cases included:** `../examples/api_example.py`, `../examples/planner_rule_example.py`, `../examples/test_planner_rule_example.py`. They are technical-document examples only, **not** code generated by AI-DLC or a completed application.

## 11. Prohibited libraries/practices and alternatives

| Prohibited / avoided for MVP | Reason | Approved alternative |
|---|---|---|
| Selenium/Playwright scraping of OurBus, airline or C2C booking pages | Terms, fragility, rate-limits, credential/booking ambiguity | Official provider hyperlinks + clear manual confirmation |
| Unlicensed commercial maps or flight APIs | Payment/API keys, scope and availability | Curated zones and published information with disclaimers |
| LangChain/LlamaIndex as unconditional requirement | Adds dependency surface for a small bounded agent | Ollama structured calls with Pydantic and custom restricted tool router; review later if justified |
| Autonomous web browsing, checkout or ticket purchase | Safety and no verified API/authorization | User opens official provider site |
| Headless access to Cornell authentication or student course calendar | Personal data and integration/consent complexity | Public Registrar calendar only; user types own dates |
| LLM-generated transit timetables or opening hours | Hallucinations and reliability | Source date and official feed + unknown fallback |
| Docker/Kubernetes mandatory for demo | Setup overhead on student laptops | `venv`, npm, Ollama local; Docker optional later |
| Browser-side secrets or uploading itinerary prompts to public logs | Privacy/security | Locally generated credentials/keys stay outside Git and are protected by the OS; no provider secrets required |

## 12. Responsibilities and team decisions

The team should collectively decide exact dependency pins, local laptop environment, GTFS data-licensing strategy, provider source refresh cadence, C2C timetable scope and UI accessibility criteria. Record actual decisions and approvals in the **real AI-DLC** Q&A/audit generated in `aidlc-docs/`. Do not copy this proposal into the audit as though a meeting occurred.

## 13. Data provider references

Read [`data-sources.md`](data-sources.md) for official links and practical integration limits. Key references: [AWS AI-DLC v1.0.1](https://github.com/awslabs/aidlc-workflows/blob/v1.0.1/README.md), [Cornell Registrar](https://registrar.cornell.edu/calendars-exams/academic-calendar/2026-2027), [TCAT GTFS feed](https://www.transit.land/data/feeds/f-dr997-tompkinsconsolidatedareatransit), [OurBus Ithaca to NYC](https://www.ourbus.com/routes/ithaca-to-nyc), [C2C schedule](https://www.fcs.cornell.edu/departments/transportation-delivery-services/campus-campus-bus-service/c2c-departure-schedule-stop-locations), [ITH flight status](https://www.flyithaca.com/flights).


## 14. Reconciliation from actual Requirements Analysis answers

The team's latest scope is **one local laptop; no cloud**. Plain HTTP port examples above describe logical components, not the final secured serving configuration. Full applicable Security enforcement was explicitly retained, including encrypted persistent stores/backups with OS-managed or equivalent keys, protected centralized local logs, local HTTPS/security headers and local session/object authorization for saved plans. No Cornell or external account signup is introduced. Exact mechanisms require Application Design review; current examples do not implement them.

The team accepts at least 12 sourced venues per city; locally import a user-downloaded genuine TCAT archive; never surface synthetic tests as actual service. Dyllan owns source review. Past dates are allowed with historical labeling. First/last-day activity windows must be user-confirmed when travel anchors are missing; intermediate days may default to 09:00–18:00. Unknown hours leave venues unscheduled until confirmed. Unknown fees remain incomplete. Food allowance is inside the $25–$300 per-person/day food-plus-admission budget; transport/lodging excluded.

Partial plans explain unmet constraints and ask which constraints to change before applying changes. Revisions preserve unrelated days/anchors until broader changes are confirmed. Local model failures offer structured deterministic planning while disabling natural-language operations. SQLite retains structured plans/constraints/provenance, not raw chats, and supports delete/reset.

The performance target is 95% of warmed-model requests within 120 seconds, with a 150-second total deadline, six tool calls maximum, 15 seconds per tool call and at most one malformed-output repair within that same budget. Non-LLM lookups target two seconds. These are targets, not measured results.

Security, Resiliency and full PBT remain enabled. Hypothesis and fast-check are proposed PBT tools in the requirements draft, requiring later dependency/configuration verification. No production cloud SLA, multi-zone topology or regional recovery guarantee is required. The requirements draft proposes automated encrypted local latest-state snapshots and a restore check; no numeric RTO/RPO or seven-day/hourly policy was selected by the team. Formal organizational change management is exempt for this course prototype; Git/AI-DLC reviews remain. See `../aidlc-docs/inception/requirements/requirements.md` for the reviewable requirements, local backup proposal and stage-specific extension applicability.


## Inception completion record

All Inception artifacts, including generated units, were subsequently approved through the actual workflow. The final instruction is “Approve units and stop before Construction”. See `../aidlc-docs/aidlc-state.md` and `../aidlc-docs/audit.md`. Reconciliation/proposal language above describes earlier inputs/design discussions; it does not mean implementation, exact package compatibility, OS setup or runtime checks have been completed.
