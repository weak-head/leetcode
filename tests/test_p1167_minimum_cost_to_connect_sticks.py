# flake8: noqa: F403, F405
import pytest
from leetcode.p1167_minimum_cost_to_connect_sticks import *

solutions = [
    connectSticks,
]

#   ([args], expectation),
test_cases = [
    ([2, 4, 3], 14),
    ([1, 8, 3, 5], 30),
    ([5], 0),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
