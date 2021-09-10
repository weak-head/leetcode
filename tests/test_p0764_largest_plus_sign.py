# flake8: noqa: F403, F405
import pytest
from leetcode.p0764_largest_plus_sign import *

solutions = [
    orderOfLargestPlusSign,
]

test_cases = [
    ([5, [[4, 2]]], 2),
    ([1, [[0, 0]]], 0),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(*args) == expectation
