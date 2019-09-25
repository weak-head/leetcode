import pytest
from leetcode.p0312_burst_balloons import solve


@pytest.mark.parametrize(("a", "expectation"), (((), ()),))
def test_(a, expectation):
    assert solve(a) == expectation
