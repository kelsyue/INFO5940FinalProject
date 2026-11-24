"""Illustrative deterministic functions for technical input—not a built travel app.

Actual TCAT times must come from a feed with date-valid service, stop, and trip checks.
These helpers do not themselves fetch GTFS, schedules, fares, or LLM output.
"""
from dataclasses import dataclass
from datetime import date, datetime, timedelta


@dataclass(frozen=True)
class FeedCoverage:
    start_date: date
    end_date: date
    source_url: str

    def covers(self, travel_date: date) -> bool:
        return self.start_date <= travel_date <= self.end_date


def connection_is_feasible(
    feeder_arrival: datetime | None,
    intercity_departure: datetime | None,
    boarding_margin_minutes: int = 15,
) -> bool | None:
    """Return True/False for an aware, confirmed schedule; None for unknown.

    Inputs must already have valid provenance and GTFS service-date coverage.
    A boarding margin is a planning rule, not a provider's guaranteed policy.
    """
    if boarding_margin_minutes < 0 or boarding_margin_minutes > 180:
        raise ValueError("Boarding margin must be between 0 and 180 minutes")
    if feeder_arrival is None or intercity_departure is None:
        return None  # Never convert unknown feeder or intercity time into 'feasible'.
    for timestamp in (feeder_arrival, intercity_departure):
        if timestamp.tzinfo is None or timestamp.utcoffset() is None:
            raise ValueError("All connection times must be timezone-aware")
    return feeder_arrival + timedelta(minutes=boarding_margin_minutes) <= intercity_departure


@dataclass(frozen=True)
class Activity:
    attraction_id: str
    start: datetime
    end: datetime
    admission_usd: int | None


def validate_day(activities: list[Activity]) -> None:
    """Reject duplicate IDs, nonpositive durations, naive times, or overlaps."""
    seen: set[str] = set()
    last_end: datetime | None = None
    for item in sorted(activities, key=lambda activity: activity.start):
        if item.attraction_id in seen:
            raise ValueError("Duplicate attraction")
        if item.start.tzinfo is None or item.end.tzinfo is None:
            raise ValueError("Naive activity time")
        if item.end <= item.start:
            raise ValueError("Nonpositive activity duration")
        if last_end is not None and item.start < last_end:
            raise ValueError("Overlapping activities")
        if item.admission_usd is not None and item.admission_usd < 0:
            raise ValueError("Invalid admission fee")
        seen.add(item.attraction_id)
        last_end = item.end


def estimated_activity_cost_usd(activities: list[Activity], food_allowance_usd: int) -> int | None:
    """Never treat an unknown admission fee as a free attraction."""
    if food_allowance_usd < 0:
        raise ValueError("Food allowance must be nonnegative")
    if any(a.admission_usd is None for a in activities):
        return None
    return sum(a.admission_usd for a in activities if a.admission_usd is not None) + food_allowance_usd
