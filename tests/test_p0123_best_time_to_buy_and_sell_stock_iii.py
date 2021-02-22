# flake8: noqa: F403, F405
import pytest
from leetcode.p0123_best_time_to_buy_and_sell_stock_iii import *

solutions = [
    maxProfit,
    maxProfit_optimized,
]

test_cases = [
    ([3, 3, 5, 0, 0, 3, 1, 4], 6),
    ([1, 3, 2, 9, 1, 3, 3, 9, 1, 9], 16),
    ([1, 9], 8),
    ([9, 1], 0),
    ([1, 9, 1, 9, 1, 9], 16),
    ([1, 1, 1, 1, 1, 3, 1], 2),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
