# flake8: noqa: F403, F405
import pytest
from leetcode.p0906_super_palindromes import *

solutions = [
    superpalindromesInRange,
]

test_cases = [
    ([1, 2], 1),
    ([4, 1000], 4),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(*args) == expectation
