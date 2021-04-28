# flake8: noqa: F403, F405
import pytest
from leetcode.p0063_unique_paths_ii import *

solutions = [
    uniquePathsWithObstacles,
]

test_cases = [
    ([[0, 0, 0], [0, 1, 0], [0, 0, 0]], 2),
    ([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 6),
    ([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], 10),
    ([[0, 0, 0, 0], [0, 1, 1, 0], [0, 0, 0, 0]], 2),
    ([[0, 1], [0, 0]], 1),
    ([[1]], 0),
    ([[]], 0),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
