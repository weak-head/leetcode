import pytest
from leetcode.p0750_number_of_corner_rectangles import (
    countCornerRectangles1,
    countCornerRectangles2,
)


@pytest.mark.parametrize(
    ("a", "expectation"),
    (
        (([[1, 0, 0, 1, 0], [0, 0, 1, 0, 1], [0, 0, 0, 1, 0], [1, 0, 1, 0, 1]]), (1)),
        (([[1, 1, 1], [1, 1, 1], [1, 1, 1]]), (9)),
    ),
)
def test_solve(a, expectation):
    assert countCornerRectangles1(a) == expectation
    assert countCornerRectangles2(a) == expectation
