# flake8: noqa: F403, F405
import pytest
from leetcode.p0127_word_ladder import *

solutions = [
    ladderLength,
]

test_cases = [
    (["hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]], 5),
    (["hit", "cog", ["hot", "dot", "dog", "lot", "log"]], 0),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(*args) == expectation
