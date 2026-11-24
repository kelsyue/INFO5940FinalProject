"""Focused example pytest checks for Cornell transfer and itinerary invariants."""
from datetime import date, datetime
from zoneinfo import ZoneInfo

import pytest

from planner_rule_example import (
    Activity,
    FeedCoverage,
    connection_is_feasible,
    estimated_activity_cost_usd,
    validate_day,
)

ET = ZoneInfo("America/New_York")


def t(hour: int, minute: int) -> datetime:
    return datetime(2026, 11, 27, hour, minute, tzinfo=ET)


def test_tcat_feed_february_2027_not_covered():
    feed = FeedCoverage(date(2026, 9, 22), date(2026, 12, 19), "https://www.transit.land/")
    assert feed.covers(date(2026, 11, 27))
    assert not feed.covers(date(2027, 2, 13))


def test_transfer_exact_boarding_buffer_boundary_passes():
    assert connection_is_feasible(t(9, 10), t(9, 25), 15) is True


def test_transfer_one_minute_short_of_buffer_fails():
    assert connection_is_feasible(t(9, 11), t(9, 25), 15) is False


def test_unverified_transfer_time_is_unknown():
    assert connection_is_feasible(None, t(9, 25), 15) is None


def test_naive_datetime_is_rejected():
    with pytest.raises(ValueError, match="timezone-aware"):
        connection_is_feasible(datetime(2026, 11, 27, 9, 10), t(9, 25), 15)


def test_valid_day_and_cost():
    activities = [Activity("museum-1", t(10, 0), t(11, 0), 20), Activity("food-1", t(12, 0), t(13, 0), 0)]
    validate_day(activities)
    assert estimated_activity_cost_usd(activities, food_allowance_usd=25) == 45


def test_activities_cannot_overlap():
    with pytest.raises(ValueError, match="Overlapping"):
        validate_day([Activity("a", t(10, 0), t(11, 30), 0), Activity("b", t(11, 0), t(12, 0), 0)])


def test_unknown_admission_not_treated_as_free():
    assert estimated_activity_cost_usd([Activity("x", t(10, 0), t(11, 0), None)], 25) is None
