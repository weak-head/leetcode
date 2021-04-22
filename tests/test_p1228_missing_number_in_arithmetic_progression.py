# flake8: noqa: F403, F405
import pytest
from leetcode.p1228_missing_number_in_arithmetic_progression import *

solutions = [
    missingNumber,
]

test_cases = [
    ([5, 7, 11, 13], 9),
    ([15, 13, 12], 14),
    ([1, 2, 3, 5, 6, 7], 4),
    ([5, 4, 2, 1], 3),
    ([1, 2, 4], 3),
    ([1, 3, 4], 2),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
