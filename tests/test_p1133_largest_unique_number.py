# flake8: noqa: F403, F405
import pytest
from leetcode.p1133_largest_unique_number import *

solutions = [
    largestUniqueNumber,
]

test_cases = [
    ([5, 7, 3, 9, 4, 9, 8, 3, 1], 8),
    ([9, 9, 8, 8], -1),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
