import pytest

from leetcode.p0981_time_based_key_value_store import (
    TimeMapListTE,
    TimeMapAvl,
    TimeMapBisect,
    TimeMapOD,
)


@pytest.mark.parametrize(("cls"), (TimeMapListTE, TimeMapAvl, TimeMapBisect, TimeMapOD))
def test_timemap(cls):
    tm = cls()
    assert tm.set("foo", "bar", 1) is None
    assert tm.get("foo", 1) == "bar"
    assert tm.get("foo", 3) == "bar"

    assert tm.set("foo", "bar2", 4) is None
    assert tm.get("foo", 4) == "bar2"
    assert tm.get("foo", 5) == "bar2"
