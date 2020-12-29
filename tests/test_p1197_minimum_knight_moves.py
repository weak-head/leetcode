import pytest
from leetcode.p1197_minimum_knight_moves import (
    minKnightMoves_dfs_dp,
    minKnightMoves_bfs_one_dir,
    minKnightMoves_bfs_two_dir,
    minKnightMoves_math,
)


@pytest.mark.parametrize(
    ("a", "expectation"),
    (
        ((2, 1), 1),
        ((1, 2), 1),
        ((5, 5), 4),
        ((50, 50), 34),
    ),
)
def test_(a, expectation):
    x, y = a
    assert minKnightMoves_dfs_dp(x, y) == expectation
    assert minKnightMoves_bfs_one_dir(x, y) == expectation
    assert minKnightMoves_bfs_two_dir(x, y) == expectation
    assert minKnightMoves_math(x, y) == expectation
