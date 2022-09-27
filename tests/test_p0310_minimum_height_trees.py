# flake8: noqa: F403, F405
import pytest
from leetcode.p0310_minimum_height_trees import *

solutions = [
    findMinHeightTrees_ts,
    findMinHeightTrees_brute_force,
]

test_cases = [
    ([4, [[1, 0], [1, 2], [1, 3]]], [1]),
    ([6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]], [3, 4]),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert set(solution(*args)) == set(expectation)
