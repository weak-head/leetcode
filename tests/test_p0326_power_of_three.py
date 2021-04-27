# flake8: noqa: F403, F405
import pytest
from leetcode.p0326_power_of_three import *

solutions = [
    isPowerOfThree,
]

test_cases = [
    (3 ** 11, True),
    (2 ** 12, False),
    (88, False),
    (3 ** 19, True),
    (3 ** 18, True),
    (3 ** 7, True),
    (99, False),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
