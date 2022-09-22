# flake8: noqa: F403, F405
import pytest
from leetcode.p1584_min_cost_to_connect_all_points import *

solutions = [
    minCostConnectPoints1,
    minCostConnectPoints2,
    minCostConnectPoints3,
]

test_cases = [
    ([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]], 20),
    ([[3, 12], [-2, 5], [-4, 1]], 18),
    ([[0, 0], [1, 1]], 2),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
