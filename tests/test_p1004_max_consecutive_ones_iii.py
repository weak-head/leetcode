# flake8: noqa: F403, F405
import pytest
from leetcode.p1004_max_consecutive_ones_iii import *

solutions = [
    longestOnes,
]

test_cases = [
    ([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 0], 0),
    ([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 1], 1),
    ([[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 0], 1),
    ([[0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0], 0], 3),
    ([[0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0], 0], 3),
    ([[0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0], 0], 3),
    ([[0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0], 1], 6),
    ([[0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0], 2], 7),
    ([[0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0], 2], 8),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(*args) == expectation
