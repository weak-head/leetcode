# flake8: noqa: F403, F405
import pytest
from leetcode.p0827_making_a_large_island import *

solutions = [
    largestIsland,
]

test_cases = [
    ([[1, 0], [0, 1]], 3),
    ([[1, 1], [1, 0]], 4),
    ([[1, 1], [1, 1]], 4),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
