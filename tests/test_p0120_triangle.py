# flake8: noqa: F403, F405
import pytest
from leetcode.p0120_triangle import *

solutions = [
    minimumTotal,
]

test_cases = [
    ([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]], 11),
    ([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3], [10, 9, 8, 9, 7]], 19),
    ([[-10]], -10),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
