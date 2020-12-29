import pytest
from leetcode.p1428_leftmost_column_with_at_least_a_one import (
    leftMostColumnWithOne,
    BinaryMatrix,
)


@pytest.mark.parametrize(
    ("a", "expectation"),
    (
        (
            BinaryMatrix(
                [
                    [0, 0, 0],
                    [0, 1, 0],
                    [0, 1, 1],
                ]
            ),
            1,
        ),
        (
            BinaryMatrix(
                [
                    [0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0],
                ]
            ),
            -1,
        ),
        (
            BinaryMatrix(
                [
                    [1, 1, 1],
                    [0, 0, 0],
                    [0, 0, 0],
                ]
            ),
            0,
        ),
        (
            BinaryMatrix(
                [
                    [0, 0, 1],
                    [0, 0, 0],
                    [0, 0, 0],
                ]
            ),
            2,
        ),
    ),
)
def test_leftMost(a, expectation):
    assert leftMostColumnWithOne(a) == expectation
