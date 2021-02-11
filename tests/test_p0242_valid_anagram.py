# flake8: noqa: F403, F405
import pytest
from leetcode.p0242_valid_anagram import *

solutions = [
    isAnagram,
]

#   ([args], expectation),
test_cases = [
    (["cat", "tac"], True),
    (["dog", "dog"], True),
    (["fog", "dog"], False),
    (["fog", "fogg"], False),
    (["anagram", "nagaram"], True),
    (["anagram", "pagaram"], False),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(*args) == expectation
