# flake8: noqa: F403, F405
import pytest
from leetcode.p0647_palindromic_substrings import *

solutions = [
    countSubstrings,
]

test_cases = [
    ("", 0),
    ("aba", 4),
    ("abc", 3),
    ("aaa", 6),
    ("a", 1),
    ("aa", 3),
    ("aaaaaaaaaa", 55),
    ("aaaaaaaaaaaaaaa", 120),
    ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", 703),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
