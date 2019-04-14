import pytest
from leetcode.p1007_minimum_domino_rotations_for_equal_row import minDominoRotations


@pytest.mark.parametrize(('a', 'b', 'rotations'), (
    ([2,1,2,4,2,2], [5,2,6,2,3,2], 2),
    ([3,5,1,2,3], [3,6,3,3,4], -1),
    ([3,3,3,3,3], [0,0,0,2,0], 0),
    ([1,2,1,1,1,2,2,2], [2,1,2,2,2,2,2,2], 1)
))
def test_rotations(a, b, rotations):
    minDominoRotations(a, b) == rotations