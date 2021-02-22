import pytest
from leetcode.p0121_best_time_to_buy_and_sell_stock import (
    maxProfit,
    maxProfit_dp,
    maxProfit_dp_optimized,
)

solutions = [maxProfit_dp, maxProfit, maxProfit_dp_optimized]


@pytest.mark.parametrize(
    ("a", "expectation"),
    (
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
        ([3, 1, 1, 1, 7], 6),
        ([5, 4, 3, 2, 1, 2], 1),
        ([2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 2, 3, 3, 2], 1),
    ),
)
@pytest.mark.parametrize("solution", solutions)
def test_solve(a, expectation, solution):
    assert solution(a) == expectation
