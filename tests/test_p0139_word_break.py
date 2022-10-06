# flake8: noqa: F403, F405
import pytest
from leetcode.p0139_word_break import *

solutions = [
    wordBreak,
]

test_cases = [
    (["leetcode", ["leet", "code"]], True),
    (["applepenapple", ["apple", "pen"]], True),
    (["catsandog", ["cats", "dog", "sand", "and", "cat"]], False),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(*args) == expectation
