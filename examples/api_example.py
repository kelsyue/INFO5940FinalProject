"""Illustrative, independently runnable FastAPI example, NOT the final product."""
from datetime import datetime
from fastapi import FastAPI
from pydantic import BaseModel, Field

from planner_rule_example import connection_is_feasible

app = FastAPI(title="BigRedRoutes Cornell Example Contract")


class ConnectionCheck(BaseModel):
    feeder_arrival: datetime | None = None
    intercity_departure: datetime | None = None
    boarding_margin_minutes: int = Field(default=15, ge=0, le=180)
    # Production must ALSO require verified schedule provenance and feed date.


@app.post("/api/v1/examples/connection-check")
def check_connection(req: ConnectionCheck) -> dict[str, str | bool | None]:
    """Example of deterministic transfer calculation, not a TCAT lookup."""
    try:
        result = connection_is_feasible(
            req.feeder_arrival, req.intercity_departure, req.boarding_margin_minutes
        )
    except ValueError as exc:
        return {"feasible": None, "status": "invalid-input", "message": str(exc)}
    return {
        "feasible": result,
        "status": "unknown" if result is None else "calculated-from-supplied-times",
        "message": "No real provider schedule or seat availability was queried.",
    }
