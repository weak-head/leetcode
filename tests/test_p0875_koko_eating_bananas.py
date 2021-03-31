# flake8: noqa: F403, F405
import pytest
from leetcode.p0875_koko_eating_bananas import *

solutions = [
    minEatingSpeed,
]

test_cases = [
    ([[3, 6, 7, 11], 8], 4),
    ([[30, 11, 23, 4, 20], 5], 30),
    ([[30, 11, 23, 4, 20], 6], 23),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(*args) == expectation
