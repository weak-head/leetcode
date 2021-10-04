# flake8: noqa: F403, F405
import pytest
from leetcode.p0463_island_perimeter import *

solutions = [
    islandPerimeter_dfs,
    islandPerimeter_counting,
    islandPerimeter_better_counting,
]

test_cases = [
    ([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]], 16),
    ([[1]], 4),
    ([[1, 0]], 4),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
