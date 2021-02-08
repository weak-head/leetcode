import pytest
from leetcode.p0045_jump_game_ii import jump


@pytest.mark.parametrize(
    ("input", "res"),
    (
        ([2, 3, 1, 1, 4], 2),
        ([], 0),
        ([1, 2, 1, 3, 1, 1, 2, 1, 1, 7], 5),
        ([3, 2, 1], 1),
        ([1, 2], 1),
        ([2, 3, 1], 1),
        ([5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0], 3),
        ([1], 0),
        ([1, 2, 3], 2),
    ),
)
def test_jump(input, res):
    assert jump(input) == res
