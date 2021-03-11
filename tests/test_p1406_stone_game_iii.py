# flake8: noqa: F403, F405
import pytest
from leetcode.p1406_stone_game_iii import *

solutions = [
    stoneGameIII_td,
    stoneGameIII_bu,
]

test_cases = [
    ([-1, -2, -3], "Tie"),
    ([1, 2, 3, 6], "Tie"),
    ([1, 2, 3, -1, -2, -3, 7], "Alice"),
    ([1, 2, 3, -9], "Alice"),
    ([1, 2, 3, 7], "Bob"),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
