# flake8: noqa: F403, F405
import pytest
from leetcode.p0438_find_all_anagrams_in_a_string import *

solutions = [
    findAnagrams,
]

test_cases = [
    (["", "a"], []),
    (["a", ""], []),
    (["abab", "ab"], [0, 1, 2]),
    (["cbaebabacd", "abc"], [0, 6]),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(*args) == expectation
