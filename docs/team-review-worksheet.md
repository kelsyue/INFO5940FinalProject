# BigRedRoutes — Team Review Worksheet

**Purpose:** Prepare for a genuine joint AI-DLC Inception session. **This is not a fabricated meeting log or a replacement for `aidlc-docs/audit.md`.** Fill the 'actual decision' cells only after your team really meets.

## Suggested 60-minute agenda

1. **10 min — Problem and audience:** Why Cornell origin planning is distinct from normal city itineraries; why support non-Cornell travelers too.
2. **15 min — Scope:** Two modes; NYC primary transport corridor; DC as general city; 1–5 days; 3–4 demo scenarios.
3. **15 min — Source realities:** Public Cornell calendar; TCAT GTFS date validity; OurBus/C2C/ITH links without unsupported live booking claims.
4. **10 min — Architecture:** React, FastAPI, SQLite, Ollama Qwen3 local, tool boundaries, graceful offline fallback and tests.
5. **10 min — Roles and gates:** Assign operator, names/NetIDs, meeting cadence, reviewer at each AI-DLC gate, repository rights.

## Review decisions

| Question | Proposed direction | Team's actual decision/reason |
|---|---|---|
| Product positioning | BigRedRoutes: Travel Planning for Cornell and Beyond | [TO BE DISCUSSED] |
| Distinct modes | General and Cornell | [TO BE DISCUSSED] |
| General itinerary cities | NYC and DC | [TO BE DISCUSSED] |
| Full Cornell travel corridor | Ithaca/Cornell → NYC; return if grounded | [TO BE DISCUSSED] |
| Campus origin | North, West, Central Campus | [TO BE DISCUSSED] |
| Cornell academic events | Public Registrar snapshot only, not private student schedule | [TO BE DISCUSSED] |
| TCAT | Static GTFS when source covers date, otherwise unavailable | [TO BE DISCUSSED] |
| OurBus | Official provider link + stop metadata; no live prices/tickets API | [TO BE DISCUSSED] |
| C2C | Official timetable/booking link; timetable import as stretch | [TO BE DISCUSSED] |
| ITH Airport | Information/status link only; no live flights API | [TO BE DISCUSSED] |
| Local model | Qwen3 4B/Ollama, fallback if not supported | [TO BE DISCUSSED] |
| Coding agent | Codex + AWS AI-DLC v1.0.1 | [TO BE DISCUSSED] |
| Budget | USD/person/day food+activities; separate unknown transportation | [TO BE DISCUSSED] |
| Dates | 1–5 days, aware America/New_York times | [TO BE DISCUSSED] |
| Live booking? | Explicitly no | [TO BE DISCUSSED] |
| Data license/attribution | Review TCAT feed permissions before any redistribution | [TO BE DISCUSSED] |
| Scheduling tests | No overlaps, date-valid source, transfer buffer, unknown != zero | [TO BE DISCUSSED] |
| Team operator and reviewer | Named people for every gate | [TO BE DISCUSSED] |
| Meeting cadence | Two 45-min meetings/week as proposed in README | [TO BE DISCUSSED] |

## High-value questions when reviewing actual agent output

- "Is the Cornell integration a visible UX difference or just extra links below a generic chatbot?"
- "Are we comparing real provider schedules or only telling students where to check? Please label this honestly."
- "Does every TCAT departure come from a feed that actually covers the requested service date and specific stops?"
- "What user action fills in an unverified intercity time so we can check a first-mile transfer?"
- "Does the general DC flow avoid asking about Cornell completely?"
- "How does the model handle a conflict between an academic break and the user's own availability?"
- "Do we accurately separate activity/food estimates from unknown transportation fares?"
- "What happens if the user insists the AI book a ticket?"
- "Are requirements, acceptance tests, architecture units and source data traceable to one another?"
- "How does the proposed algorithm behave when GTFS service crosses midnight or daylight saving boundaries?"

**How to record real engagement:** In each AI-DLC stage, ask the coding agent to show draft artifacts, review them as a group, answer its genuine questions, request any justified changes, and approve only when satisfied. Explicitly ask the agent to update its own `audit.md`/`aidlc-state.md` if a real conversation/decision was missed. Do not directly hand-edit agent-generated Inception output or invent answers.

## Signoff areas (fill only after real review)

- Team members present: [ACTUAL NAMES]
- Date of team scope approval: [ACTUAL DATE]
- Named repository operator: [ACTUAL NAME]
- Chosen coding agent/version check: [ACTUAL RESULT]
- Chosen local demo machine/model: [ACTUAL RESULT]
- Remaining unresolved risks: [ACTUAL DISCUSSION]
