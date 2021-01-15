import pytest
from leetcode.p0353_design_snake_game import SnakeGame


@pytest.mark.parametrize(
    ("a", "expectation"),
    (
        (
            (
                (3, 3),
                [[0, 1], [0, 2], [1, 2], [2, 2], [2, 1], [2, 0], [1, 0]],
                "RRDDLLUURRDDLLURULD",
            ),
            ([1, 2, 3, 4, 5, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, -1]),
        ),
    ),
)
def test_snake(a, expectation):
    width, height = a[0]
    s = SnakeGame(width, height, a[1])
    for direction, score in zip(a[2], expectation):
        assert s.move(direction) == score
