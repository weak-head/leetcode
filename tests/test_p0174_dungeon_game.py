# flake8: noqa: F403, F405
import pytest
from leetcode.p0174_dungeon_game import *

solutions = [
    calculateMinimumHP,
]

test_cases = [
    ([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]], 7),
    ([[0]], 1),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
