import pytest
from leetcode.p0055_jump_game import can_jump, can_jump2


@pytest.mark.parametrize(
    ("array", "can"),
    (
        ([0], True),
        ([1], True),
        ([0, 1], False),
        ([2, 3, 1, 1, 4], True),
        ([3, 2, 1, 0, 2], False),
    ),
)
def test_can_jump(array, can):
    assert can_jump(array) == can
    assert can_jump2(array) == can
