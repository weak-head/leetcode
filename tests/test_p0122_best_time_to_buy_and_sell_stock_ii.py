# flake8: noqa: F403, F405
import pytest
from leetcode.p0122_best_time_to_buy_and_sell_stock_ii import *

solutions = [
    maxProfit,
    maxProfit_optimized,
]

test_cases = [
    ([7, 1, 5, 3, 6, 4], 7),
    ([1, 2, 1, 2, 1, 2, 1, 2], 4),
    ([1, 2, 3, 4, 5], 4),
    ([1, 1], 0),
    ([1, 1, 1, 1, 1, 1, 1], 0),
    ([4, 3, 2, 1], 0),
    ([2, 7, 3, 8, 4, 9], 15),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
