# flake8: noqa: F403, F405
import pytest
from leetcode.p0560_subarray_sum_equals_k import *

solutions = [
    subarraySum,
]

test_cases = [
    ([[1, 2, 3], 3], 2),
    ([[1, 1, 1, 1, 1], 2], 4),
    ([[-2, 7, 3, -6, 1, 3, -2, 5, 2, 1, 3, -2, -1, 4], 5], 6),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(*args) == expectation
