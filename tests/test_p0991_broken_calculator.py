# flake8: noqa: F403, F405
import pytest
from leetcode.p0991_broken_calculator import *

solutions = [
    brokenCalc,
]

test_cases = [
    ([1024, 1], 1023),
    ([5, 5], 0),
    ([2, 3], 2),
    ([5, 8], 2),
    ([3, 10], 3),
    ([17, 997], 11),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(*args) == expectation
