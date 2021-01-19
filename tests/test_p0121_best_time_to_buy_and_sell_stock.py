import pytest
from leetcode.p0121_best_time_to_buy_and_sell_stock import maxProfit


@pytest.mark.parametrize(
    ("a", "expectation"), ((([7, 1, 5, 3, 6, 4]), (5)), (([7, 6, 4, 3, 1]), (0)))
)
def test_solve(a, expectation):
    assert maxProfit(a) == expectation
