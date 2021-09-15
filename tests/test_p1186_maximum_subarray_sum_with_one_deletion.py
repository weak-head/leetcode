# flake8: noqa: F403, F405
import pytest
from leetcode.p1186_maximum_subarray_sum_with_one_deletion import *

solutions = [
    maximumSum,
]

test_cases = [
    ([1, -2, 0, 3], 4),
    ([1, -2, -2, 3], 3),
    ([-1, -1, -1, -1], -1),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
