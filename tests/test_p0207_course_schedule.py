# flake8: noqa: F403, F405
import pytest
from leetcode.p0207_course_schedule import *

solutions = [
    canFinish,
]

test_cases = [
    ([2, [[1, 0]]], True),
    ([20, []], True),
    ([2, [[1, 0], [0, 1]]], False),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(*args) == expectation
