# flake8: noqa: F403, F405
import pytest
from leetcode.p0452_minimum_number_of_arrows_to_burst_balloons import *

solutions = [
    findMinArrowShots,
]

test_cases = [
    ([[10, 16], [2, 8], [1, 6], [7, 12]], 2),
    ([[1, 2], [3, 4], [5, 6], [7, 8]], 4),
    ([[1, 2], [2, 3], [3, 4], [4, 5]], 2),
    ([[1, 2]], 1),
    ([[2, 3], [2, 3]], 1),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
