# flake8: noqa: F403, F405
import pytest
from leetcode.p0435_non_overlapping_intervals import *

solutions = [
    eraseOverlapIntervals,
]

test_cases = [
    ([], 0),
    ([[1, 2], [2, 3], [3, 4], [1, 3]], 1),
    ([[1, 2], [1, 2], [1, 2]], 2),
    ([[1, 2], [2, 3]], 0),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
