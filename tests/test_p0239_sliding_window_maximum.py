# flake8: noqa: F403, F405
import pytest
from leetcode.p0239_sliding_window_maximum import *

solutions = [
    maxSlidingWindow,
]

test_cases = [
    ([[1, 3, -1, -3, 5, 3, 6, 7], 3], [3, 3, 5, 5, 6, 7]),
    ([[1, 3, -1, -3, 5, 3, 6, 7], 1], [1, 3, -1, -3, 5, 3, 6, 7]),
    ([[1, 2, 3, 4, 5], 5], [5]),
    ([[1, 2, 3, 4, 5], 4], [4, 5]),
    ([[1, 0, 1, 0, 0, 3], 2], [1, 1, 1, 0, 3]),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(*args) == expectation
