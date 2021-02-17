# flake8: noqa: F403, F405
import pytest
from leetcode.p0300_longest_increasing_subsequence import *

solutions = [
    length_of_lis_dp,
    length_of_lis_dp_bs,
]

test_cases = [
    ([10, 9, 2, 5, 3, 7, 101, 18], 4),
    ([1, 2, 3, 4, 5, 6], 6),
    ([6, 5, 4, 3, 2, 1], 1),
    ([7, 7, 7], 1),
    ([0, 1, 0, 3, 2, 3], 4),
    ([1, 3, 6, 7, 9, 4, 10, 5, 6], 6),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
