# flake8: noqa: F403, F405
import pytest
from leetcode.p0334_increasing_triplet_subsequence import *

solutions = [
    increasingTriplet,
]

test_cases = [
    ([], False),
    ([1, 2, 3], True),
    ([2, 2, 3], False),
    ([3, 2, 1], False),
    ([6, 5, 4, 5, 5, 4, 4, 2], False),
    ([1, 1, 1], False),
    ([1, 2], False),
    ([6, 5, 4, 4, 7, 3, 6, 5, 2, 9], True),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
