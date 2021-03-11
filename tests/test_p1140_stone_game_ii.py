# flake8: noqa: F403, F405
import pytest
from leetcode.p1140_stone_game_ii import *

solutions = [
    stoneGameII,
]

test_cases = [
    ([2, 7, 9, 4, 4], 10),
    ([1, 2, 3, 4, 5, 100], 104),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
