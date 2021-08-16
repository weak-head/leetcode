# flake8: noqa: F403, F405
import pytest
from leetcode.p0265_paint_house_ii import *

solutions = [
    minCostII_dp,
    minCostII_two_mins,
]

test_cases = [
    ([[8]], 8),
    ([[1, 5, 3], [2, 9, 4]], 5),
    ([[1, 3], [2, 4]], 5),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
