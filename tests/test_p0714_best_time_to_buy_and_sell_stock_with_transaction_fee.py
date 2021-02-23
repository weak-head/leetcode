# flake8: noqa: F403, F405
import pytest
from leetcode.p0714_best_time_to_buy_and_sell_stock_with_transaction_fee import *

solutions = [
    maxProfit,
    maxProfit_optimized,
]

test_cases = [
    ([[1, 3, 2, 8, 4, 9], 2], 8),
    ([[1, 3, 2, 8, 4, 9], 200], 0),
    ([[1, 3, 2, 8, 4, 9], 7], 1),
    ([[1, 30, 2, 8, 40, 9], 20], 27),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(*args) == expectation
