# flake8: noqa: F403, F405
import pytest
from leetcode.p1136_parallel_courses import *

solutions = [
    minimumSemesters,
]

test_cases = [
    ([3, [[1, 3], [2, 3]]], 2),
    ([3, [[1, 2], [2, 3], [3, 1]]], -1),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(*args) == expectation
