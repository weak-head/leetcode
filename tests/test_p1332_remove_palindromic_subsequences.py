# flake8: noqa: F403, F405
import pytest
from leetcode.p1332_remove_palindromic_subsequences import *

solutions = [
    removePalindromeSub,
]

test_cases = [
    ("ababa", 1),
    ("aabbbb", 2),
    ("", 0),
    ("abbaaaa", 2),
    ("bbaabbaabb", 1),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
