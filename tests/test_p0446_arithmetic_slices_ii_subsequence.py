# flake8: noqa: F403, F405
import pytest
from leetcode.p0446_arithmetic_slices_ii_subsequence import *

solutions = [
    numberOfArithmeticSlices,
]

test_cases = [
    ([2, 4, 6, 8, 10], 7),
    ([7, 7, 7, 7, 7], 16),
    ([7, 7, 7, 7, 7, 7], 42),
    ([7, 7, 7, 7, 7, 7, 7], 99),
    ([7, 7, 7, 7, 7, 7, 7, 7], 219),
    ([1, 3, 4, 2, 5, 3, 2, 1, 5, 3, 2, 1, 4, 2, 1], 64),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
