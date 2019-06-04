import pytest

from leetcode.p0981_time_based_key_value_store import (
    TimeMapListTE,
    TimeMapAvl,
    TimeMapBisect,
    TimeMapOD,
    TimeMap,
)


@pytest.mark.parametrize(
    ("cls", "itms"),
    (
        (TimeMapListTE, 10000),
        (TimeMapAvl, 5000),
        (TimeMapBisect, 10000),
        (TimeMapOD, 1000),
        (TimeMap, 20000),
    ),
)
def test_timemap(cls, itms):
    tm = cls()

    assert tm.set("foo", "bar", 1) is None
    assert tm.get("foo", 1) == "bar"
    assert tm.get("foo", 3) == "bar"
    assert tm.get("foo", 0) == ""

    assert tm.set("foo", "bar2", 4) is None
    assert tm.get("foo", 4) == "bar2"
    assert tm.get("foo", 5) == "bar2"
    assert tm.get("foo", 0) == ""

    assert tm.get("buz", 4) == ""

    for t in range(10, itms):
        tm.set("foo", "bar_" + str(t), t)

    for t in range(10, itms):
        assert "bar_" + str(t) == tm.get("foo", t)
