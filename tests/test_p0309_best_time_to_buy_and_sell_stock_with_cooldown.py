# flake8: noqa: F403, F405
import pytest
from leetcode.p0309_best_time_to_buy_and_sell_stock_with_cooldown import *

solutions = [
    maxProfit,
]

test_cases = [
    ([1, 2, 3, 0, 2], 3),
    ([1, 7, 6, 2, 9], 13),
    ([1, 2, 1, 2, 1, 2, 1, 2, 1, 2], 3),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
