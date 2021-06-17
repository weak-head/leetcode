# flake8: noqa: F403, F405
import pytest
from leetcode.p0795_number_of_subarrays_with_bounded_maximum import *

solutions = [
    numSubarrayBoundedMax,
]

test_cases = [
    ([[2, 1, 4, 3], 2, 3], 3),
    ([[2, 1, 1, 1, 1, 1, 5], 2, 3], 6),
    ([[2, 1, 4, 2, 3], 2, 3], 5),
    ([[2, 3, 4, 5, 6, 7, 10, 2, 3], 2, 9], 21 + 3),
    ([[2, 3, 4, 5, 6, 7, 10, 2, 3], 2, 90], 45),
    ([[2, 4, 2, 6, 2, 7], 2, 3], 3),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(*args) == expectation
