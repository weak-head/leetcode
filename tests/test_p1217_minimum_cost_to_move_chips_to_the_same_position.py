# flake8: noqa: F403, F405
import pytest
from leetcode.p1217_minimum_cost_to_move_chips_to_the_same_position import *

solutions = [
    minCostToMoveChips,
]

test_cases = [
    ([1, 2, 3], 1),
    ([2, 2, 2, 3, 3], 2),
    ([1, 1000000000], 1),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
