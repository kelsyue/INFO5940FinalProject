# Technical-environment examples — not the built product

- `planner_rule_example.py` — deterministic static-feed coverage, timezone-aware transfer check, activity validation and unknown price handling.
- `api_example.py` — illustrative FastAPI endpoint showing type validation and transparent `unknown` response; **not** a real TCAT integration.
- `test_planner_rule_example.py` — test suite covering Feb 2027 TCAT feed expiration, exact transfer buffer boundaries, unknown times, naive datetimes, schedule overlap and unknown cost.

Run from within `examples/` (only Python and pytest are required for pure-function tests):

```bash
python -m pip install -r requirements.txt
python -m pytest -q
```

Example times are **synthetic test data**. No use of a real transport timetable is implied. The full app is **not implemented** for the Inception milestone.
