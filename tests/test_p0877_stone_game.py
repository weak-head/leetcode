# flake8: noqa: F403, F405
import pytest
from leetcode.p0877_stone_game import *

solutions = [
    stone_game,
    stone_game_optimized,
]

test_cases = [
    ([5, 3, 4, 5], True),
    ([5, 4, 5, 5], True),
    ([1, 5, 4, 2], True),
    ([1, 5, 1, 5, 1], False),
    ([5, 3, 4, 5, 1], True),
    ([1, 5, 7, 3, 5, 1], True),
    ([10, 1, 10, 2, 10], False),
    ([2, 20, 2], False),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
