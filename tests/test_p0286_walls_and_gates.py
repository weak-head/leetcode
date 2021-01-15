import pytest
from leetcode.p0286_walls_and_gates import wallsAndGates


@pytest.mark.parametrize(
    ("a", "expectation"),
    (
        (
            (
                [
                    [2147483647, -1, 0, 2147483647],
                    [2147483647, 2147483647, 2147483647, -1],
                    [2147483647, -1, 2147483647, -1],
                    [0, -1, 2147483647, 2147483647],
                ]
            ),
            ([[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4]]),
        ),
        (
            ([[2147483647]]),
            ([[2147483647]]),
        ),
    ),
)
def test_solve(a, expectation):
    wallsAndGates(a)
    assert a == expectation
