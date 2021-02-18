# flake8: noqa: F403, F405
import pytest
from leetcode.p0413_arithmetic_slices import *

solutions = [
    numberOfArithmeticSlices,
]

test_cases = [
    ([1, 2, 3, 4], 3),
    ([1, 2], 0),
    ([1, 2, 3], 1),
    ([1, 2, 3, 4, 6, 8, 10, 12, 10, 8, 10, 12], 11),
    ([1, 2, 5, 6, 3, 9, 10], 0),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
