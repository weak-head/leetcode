# flake8: noqa: F403, F405
import pytest
from leetcode.p0630_course_schedule_iii import *

solutions = [
    scheduleCourse,
]

test_cases = [
    ([[100, 200], [200, 1300], [1000, 1250], [2000, 3200]], 3),
    ([[1, 2]], 1),
    ([[3, 2], [4, 3]], 0),
    ([[3000, 3000], [2500, 3500], [2000, 4000], [1500, 4500]], 2),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
