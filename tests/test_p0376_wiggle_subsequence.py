# flake8: noqa: F403, F405
import pytest
from leetcode.p0376_wiggle_subsequence import *

solutions = [
    wiggleMaxLength_dp,
    wiggleMaxLength_dp_optimized,
    wiggleMaxLength_dp_optimized_space_time,
]

test_cases = [
    ([1, 7, 4, 9, 2, 5], 6),
    ([1, 17, 5, 10, 13, 15, 10, 5, 16, 8], 7),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 2),
    ([1, 1, 1, 1, 1, 1], 1),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
