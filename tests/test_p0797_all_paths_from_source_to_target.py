# flake8: noqa: F403, F405
import pytest
from leetcode.p0797_all_paths_from_source_to_target import *

solutions = [
    allPathsSourceTarget,
]

test_cases = [
    ([[1, 2], [3], [3], []], [[0, 1, 3], [0, 2, 3]]),
    (
        [[4, 3, 1], [3, 2, 4], [3], [4], []],
        [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]],
    ),
    ([[1], []], [[0, 1]]),
    ([[1, 2, 3], [2], [3], []], [[0, 1, 2, 3], [0, 2, 3], [0, 3]]),
    ([[1, 3], [2], [3], []], [[0, 1, 2, 3], [0, 3]]),
    ([[1, 2], [3], [3], []], [[0, 1, 3], [0, 2, 3]]),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert set(solution(args)) == set(map(tuple, expectation))
