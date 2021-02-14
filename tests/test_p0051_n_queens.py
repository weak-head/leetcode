# flake8: noqa: F403, F405
import pytest
from leetcode.p0051_n_queens import *

solutions = [solveNQueens]

test_cases = [
    (1, set([("Q",)])),
    (2, set()),
    (3, set()),
    (4, {("..Q.", "Q...", "...Q", ".Q.."), (".Q..", "...Q", "Q...", "..Q.")}),
    (
        5,
        {
            (
                "....Q",
                "..Q..",
                "Q....",
                "...Q.",
                ".Q...",
            ),
            (
                "....Q",
                ".Q...",
                "...Q.",
                "Q....",
                "..Q..",
            ),
            (
                "...Q.",
                ".Q...",
                "....Q",
                "..Q..",
                "Q....",
            ),
            (
                "...Q.",
                "Q....",
                "..Q..",
                "....Q",
                ".Q...",
            ),
            (
                "..Q..",
                "....Q",
                ".Q...",
                "...Q.",
                "Q....",
            ),
            (
                "..Q..",
                "Q....",
                "...Q.",
                ".Q...",
                "....Q",
            ),
            (
                ".Q...",
                "....Q",
                "..Q..",
                "Q....",
                "...Q.",
            ),
            (
                ".Q...",
                "...Q.",
                "Q....",
                "..Q..",
                "....Q",
            ),
            (
                "Q....",
                "...Q.",
                ".Q...",
                "....Q",
                "..Q..",
            ),
            (
                "Q....",
                "..Q..",
                "....Q",
                ".Q...",
                "...Q.",
            ),
        },
    ),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert set(map(tuple, solution(args))) == expectation
