# flake8: noqa: F403, F405
import pytest
from leetcode.p0518_coin_change_2 import *

solutions = [
    change,
]

test_cases = [
    ([5, [1, 2, 5]], 4),
    ([3, [2]], 0),
    ([10, [10]], 1),
    ([20, [10]], 1),
    ([90, [10]], 1),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(*args) == expectation
