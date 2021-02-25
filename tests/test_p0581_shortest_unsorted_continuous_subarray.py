# flake8: noqa: F403, F405
import pytest
from leetcode.p0581_shortest_unsorted_continuous_subarray import *

solutions = [
    findUnsortedSubarray,
]

test_cases = [
    ([1, 2, 3, 4, 5], 0),
    ([2, 3, 4, 5, 1], 5),
    ([5, 1, 2, 3, 4], 5),
    ([3, 4, 5, 2, 6, 9, 1, 3, 6, 7, 10, 11, 12], 10),
    ([3, 4, 5, 2, 6, 1, 9], 6),
    ([5, 6, 4, 3, 2, 1, 7, 8, 9], 6),
    ([1, 2, 3, 9, 8, 7, 6, 4, 5, 6], 7),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
