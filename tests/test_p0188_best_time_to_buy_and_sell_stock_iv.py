# flake8: noqa: F403, F405
import pytest
from leetcode.p0188_best_time_to_buy_and_sell_stock_iv import *

solutions = [
    maxProfit,
    maxProfit_optimized,
]

test_cases = [
    ([2, [2, 4, 1]], 2),
    ([2, [2, 4]], 2),
    ([1, [2, 4]], 2),
    ([1, [4, 2]], 0),
    ([2, [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]], 2),
    ([4, [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]], 4),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(*args) == expectation
