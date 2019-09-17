import pytest
from leetcode.p0054_spiral_matrix import spiral_order


@pytest.mark.parametrize(
    ("a", "expectation"),
    (
        ([], []),
        ([[]], []),
        ([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
        (
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
            [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
        ),
    ),
)
def test_spiral(a, expectation):
    assert spiral_order(a) == expectation