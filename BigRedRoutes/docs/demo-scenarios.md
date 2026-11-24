# Demonstration Scenarios & Acceptance Walkthroughs

**These are proposed final-project tests, not claim of existing functionality.** A team member should review them in Inception.

## Scenario 1 — Cornell NYC February Break (flag unknown TCAT)

- **Input:** Cornell mode, North Campus, NYC, February 13–15, 2027, 1 adult, relaxed pace, art/food, $80/person/day activities; requests OurBus/C2C options.
- **Expected:** Registrar context identifies Feb 13–16 2027 as university February Break/No Classes and asks the student to verify personal commitments. Official OurBus/C2C links are shown; no invented seat or fare. **TCAT 2026 feed is out of range**, so no confirmed 2027 TCAT departure is displayed. Destination schedule stays within valid activity hours/assumptions and separate daily activity budget. First-day activities start after confirmed arrival or clearly disclosed user assumption.
- **Failure:** The app says "TCAT bus at 8:15 AM Feb 13 2027" or "OurBus costs $42" without valid data, or claims the student definitely has no classes.

## Scenario 2 — Transfer boundary test (test-only fixture)

- **Input:** Clearly labeled synthetic schedule fixture within a known feed service-date range, feeder bus arrives 09:10, user-confirmed intercity departure 09:25, boarding margin 15 min.
- **Expected:** Transfer passes exactly at boundary. Change feeder arrival to 09:11; transfer fails as one minute too late. All timestamps timezone-aware and same service/local date.
- **Failure:** Transfer is accepted because 09:11 is before 09:25 without allowing boarding time, or uses next-day GTFS time incorrectly.

## Scenario 3 — General DC itinerary

- **Input:** General mode, Washington DC, three days, history/art/food, $70/person/day, balanced pace, no campus field.
- **Expected:** The app asks nothing about Cornell. It retrieves a curated DC catalog and shows budget/status/rationale with city-specific entries; never fabricates a trip from Ithaca.
- **Failure:** The app requires a campus origin or displays TCAT/C2C options without selecting Cornell mode.

## Scenario 4 — Revise a NYC itinerary

- **Input:** Existing 3-day NYC plan. "Make day two more relaxed and keep admission costs under $50".
- **Expected:** Reinterpret target date, replace or remove activities with IDs from catalog, re-run day constraint/budget validation, show a change summary, preserve days 1 and 3 unless a dependency forces changes (then disclose).
- **Failure:** The LLM returns only prose, schedules overlapping visits, hides unknown prices or silently changes other days.

## Scenario 5 — Unsupported booking request

- **Input:** "Book my C2C seat for 10 AM tomorrow" or "Tell me the cheapest ITH flight right now."
- **Expected:** Clear statement no booking/real-time fare API is connected; official provider link; user retains control of the transaction.
- **Failure:** Confirms purchase, price or seat without provider-backed data.

## Scenario 6 — Academic calendar nuance

- **Input:** "Since Cornell has February Break, am I guaranteed to be free all four days?"
- **Expected:** App differentiates university no-classes event from individual exams/work/research; prompts user to check their own calendar.
- **Failure:** Impersonates access to user's Cornell schedule or claims guaranteed availability.

## Suggested demo artifacts (only in final project)

A screen recording showing both modes, source freshness labels, a valid and invalid transfer, an initial plan, one agent revision, and a transparent unsupported-data response. Midterm deliverable is **Inception artifacts**, not a recorded working app.
