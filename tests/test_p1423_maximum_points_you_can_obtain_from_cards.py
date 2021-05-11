# flake8: noqa: F403, F405
import pytest
from leetcode.p1423_maximum_points_you_can_obtain_from_cards import *

solutions = [
    maxScore_sliding_window,
]

test_cases = [
    ([[1, 2, 3, 4, 5, 6, 1], 3], 12),
    ([[2, 2, 2], 2], 4),
    ([[9, 7, 7, 9, 7, 7, 9], 7], 55),
    ([[1, 1000, 1], 1], 1),
    ([[1, 79, 80, 1, 1, 1, 200, 1], 3], 202),
    ([[100, 40, 17, 9, 73, 75], 3], 248),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(*args) == expectation
