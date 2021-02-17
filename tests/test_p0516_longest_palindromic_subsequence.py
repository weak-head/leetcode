# flake8: noqa: F403, F405
import pytest
from leetcode.p0516_longest_palindromic_subsequence import *

solutions = [
    longest_palindrom_subsequence_dp_td,
    longest_palindrom_subsequence_dp_bu,
    longest_palindrom_subsequence_dp_bu_optimized,
]

test_cases = [
    ("aba", 3),
    ("abba", 4),
    ("xacbytaj", 3),
    ("xacbytajxp", 5),
    ("abcppbca", 6),
    ("", 0),
    ("a", 1),
    ("aa", 2),
    ("ab", 1),
    ("aaaaaaaaaaaaaaaaaaaaaaaaa", 25),
    ("aaaaaaaaaaaaaaaaaaaaaaaaaa", 26),
    ("aaaaaaaaaaaaafsebuiopaaaaaaaaaaaaa", 27),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
