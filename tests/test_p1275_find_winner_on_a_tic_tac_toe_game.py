# flake8: noqa: F403, F405
import pytest
from leetcode.p1275_find_winner_on_a_tic_tac_toe_game import *

solutions = [
    tictactoe,
]

test_cases = [
    ([[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]], "A"),
    ([[0, 0], [1, 1], [0, 1], [0, 2], [1, 0], [2, 0]], "B"),
    ([[0, 0], [1, 1], [2, 0], [1, 0], [1, 2], [2, 1], [0, 1], [0, 2], [2, 2]], "Draw"),
    ([[0, 0], [1, 1]], "Pending"),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
