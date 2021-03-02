# flake8: noqa: F403, F405
import pytest
from leetcode.p0739_daily_temperatures import *

solutions = [
    dailyTemperatures,
]

test_cases = [
    ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
    ([1, 2, 3, 4, 5], [1, 1, 1, 1, 0]),
    ([1, 10, 20, 21, 30, 22], [1, 1, 1, 1, 0, 0]),
    ([5, 4, 3, 2, 1], [0, 0, 0, 0, 0]),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert list(solution(args)) == expectation
