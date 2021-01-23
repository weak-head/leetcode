import pytest
from leetcode.p1329_sort_the_matrix_diagonally import diagonalSort1, diagonalSort2


@pytest.mark.parametrize(
    ("a", "expectation"),
    (
        (
            ([[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]]),
            ([[1, 1, 1, 1], [1, 2, 2, 2], [1, 2, 3, 3]]),
        ),
        (
            ([[3, 3, 1, 1], [2, 2, 1, 2], [8, 1, 6, 2], [7, 1, 3, 2]]),
            ([[2, 1, 1, 1], [1, 2, 2, 2], [1, 2, 3, 3], [7, 8, 3, 6]]),
        ),
    ),
)
def test_solve(a, expectation):
    assert diagonalSort1(a) == expectation
    assert diagonalSort2(a) == expectation
