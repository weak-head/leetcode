# flake8: noqa: F403, F405
import pytest
from leetcode.p0210_course_schedule_ii import *

solutions = [
    findOrder,
]

test_cases = [
    ([4, [[1, 0], [2, 0], [3, 1], [3, 2]]], [0, 2, 1, 3]),
    ([2, [[1, 0]]], [0, 1]),
    ([1, []], [0]),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert list(solution(*args)) == expectation
