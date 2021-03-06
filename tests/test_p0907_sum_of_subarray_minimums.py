# flake8: noqa: F403, F405
import pytest
from leetcode.p0907_sum_of_subarray_minimums import *

solutions = [
    sumSubarrayMins_dp,
    sumSubarrayMins_ms,
]

test_cases = [
    ([3, 1, 2, 4], 17),
    ([11, 81, 94, 43, 3], 444),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
