import pytest
from leetcode.p0042_trapping_rain_water import trap, trap2

solutions = [
    trap,
    trap2,
]


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
        ([0, 1, 2, 3, 4, 5, 0, 5, 4, 3, 2, 1], 5),
        ([0, 1, 2, 3, 4, 5, 0, 0, 0, 0], 0),
    ),
)
@pytest.mark.parametrize(("solution"), solutions)
def test_trap(a, expectation, solution):
    assert solution(a) == expectation
