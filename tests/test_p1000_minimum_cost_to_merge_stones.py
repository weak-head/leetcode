# flake8: noqa: F403, F405
import pytest
from leetcode.p1000_minimum_cost_to_merge_stones import *

solutions = [
    mergeStones,
]

#   ([args], expectation),
test_cases = [
    ([[3, 5, 1, 2, 6], 3], 25),
    ([[9, 6, 1, 1, 1, 7, 8], 3], 52),
    ([[3, 3, 3, 1, 1, 1, 1, 2, 2, 2], 4], 32),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(*args) == expectation
