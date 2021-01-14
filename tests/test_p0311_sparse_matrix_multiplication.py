import pytest
from leetcode.p0311_sparse_matrix_multiplication import multiplySparse


@pytest.mark.parametrize(
    ("a", "expectation"),
    (
        (
            (
                [[1, 0, 0], [-1, 0, 3]],
                [[7, 0, 0], [0, 0, 0], [0, 0, 1]],
            ),
            ([[7, 0, 0], [-7, 0, 3]]),
        ),
    ),
)
def test_mul(a, expectation):
    assert multiplySparse(a[0], a[1]) == expectation
