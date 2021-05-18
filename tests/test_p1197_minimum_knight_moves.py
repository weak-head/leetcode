# flake8: noqa: F403, F405
import pytest
from leetcode.p1197_minimum_knight_moves import *

solutions = [
    minKnightMoves_dfs_dp,
    minKnightMoves_math,
]

test_cases = [
    ((2, 1), 1),
    ((1, 2), 1),
    ((5, 5), 4),
    ((50, 50), 34),
    ((170, 120), 98),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(*args) == expectation
