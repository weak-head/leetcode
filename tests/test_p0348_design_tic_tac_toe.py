import pytest
from leetcode.p0348_design_tic_tac_toe import TicTacToe


@pytest.mark.parametrize(
    ("a", "expectation"),
    (
        (
            (
                [
                    3,
                    [
                        [0, 0, 1],
                        [0, 2, 2],
                        [2, 2, 1],
                        [1, 1, 2],
                        [2, 0, 1],
                        [1, 0, 2],
                        [2, 1, 1],
                    ],
                ]
            ),
            ([0, 0, 0, 0, 0, 0, 1]),
        ),
        (([2, [[0, 1, 1], [1, 1, 2], [1, 0, 1]]]), ([0, 0, 1])),
    ),
)
def test_ticTacToe(a, expectation):
    n, moves = a
    t = TicTacToe(n)
    for ix, move in enumerate(moves):
        assert t.move(move[0], move[1], move[2]) == expectation[ix]
