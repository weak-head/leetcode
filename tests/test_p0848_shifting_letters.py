# flake8: noqa: F403, F405
import pytest
from leetcode.p0848_shifting_letters import *

solutions = [
    shiftingLetters,
]

test_cases = [
    (["abc", [3, 5, 9]], "rpl"),
    (["aaa", [1, 2, 3]], "gfd"),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(*args) == expectation
