# flake8: noqa: F403, F405
import pytest
from leetcode.p0792_number_of_matching_subsequences import *

solutions = [
    numMatchingSubseq,
]

test_cases = [
    (["abcde", ["a", "bb", "acd", "ace"]], 3),
    (["dsahjpjauf", ["ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"]], 2),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(*args) == expectation
