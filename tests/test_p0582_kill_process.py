# flake8: noqa: F403, F405
import pytest
from leetcode.p0582_kill_process import *

solutions = [
    killProcess,
]

test_cases = [
    ([[1, 3, 10, 5], [3, 0, 5, 3], 5], [5, 10]),
    ([[1, 3, 10, 5], [3, 0, 5, 3], 1], [1]),
    ([[1, 3, 10, 5], [3, 0, 5, 3], 10], [10]),
    ([[1, 3, 10, 5], [3, 0, 5, 3], 3], [3, 1, 5, 10]),
    ([[1, 2, 3, 4, 5, 6], [0, 1, 2, 3, 4, 5], 0], [0, 1, 2, 3, 4, 5, 6]),
    ([[1, 2, 3, 4, 5, 6], [0, 1, 2, 3, 4, 5], 1], [1, 2, 3, 4, 5, 6]),
    ([[1, 2, 3, 4, 5, 6], [0, 1, 2, 3, 4, 5], 4], [4, 5, 6]),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(*args) == expectation
