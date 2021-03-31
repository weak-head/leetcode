# flake8: noqa: F403, F405
import pytest
from leetcode.p0204_count_primes import *

solutions = [
    countPrimes,
]

test_cases = [
    (10, 4),
    (101, 25),
    (1010, 169),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
