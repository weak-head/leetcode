import pytest
from leetcode.p0042_trapping_rain_water import trap


@pytest.mark.parametrize(
    ("a", "expectation"),
    (
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        ([0, 0, 0, 0, 0], 0),
        ([0, 0], 0),
        ([8, 0, 0, 0, 4], 12),
        ([100, 0, 0, 0, 0, 0], 0),
        ([0, 0, 0, 0, 0, 100], 0),
        ([1, 0, 0, 0, 0, 0, 100], 5),
    ),
)
def test_trap(a, expectation):
    assert trap(a) == expectation
