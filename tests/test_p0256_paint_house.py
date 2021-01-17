import pytest
from leetcode.p0256_paint_house import minCost


@pytest.mark.parametrize(
    ("a", "expectation"),
    (
        (
            ([[5, 8, 6], [19, 14, 13], [7, 5, 12], [14, 15, 17], [3, 20, 10]]),
            (43),
        ),
        (
            ([[17, 2, 17], [16, 16, 5], [14, 3, 19]]),
            (10),
        ),
    ),
)
def test_solve(a, expectation):
    assert minCost(a) == expectation
