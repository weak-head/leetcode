import pytest
from leetcode.p0573_squirrel_simulation import minDistance


@pytest.mark.parametrize(
    ("a", "expectation"),
    (
        (
            (
                [2, 2],
                [4, 4],
                [[3, 0], [2, 5]],
            ),
            (12),
        ),
        (
            (
                [3, 2],
                [0, 1],
                [
                    [2, 0],
                    [4, 1],
                    [0, 4],
                    [1, 3],
                    [1, 0],
                    [3, 4],
                    [3, 0],
                    [2, 3],
                    [0, 2],
                    [0, 0],
                    [2, 2],
                    [4, 2],
                    [3, 3],
                    [4, 4],
                    [4, 0],
                    [4, 3],
                    [3, 1],
                    [2, 1],
                    [1, 4],
                    [2, 4],
                ],
            ),
            (100),
        ),
        (
            (
                [0, 1],
                [0, 0],
                [[0, 2]],
            ),
            (3),
        ),
    ),
)
def test_solve(a, expectation):
    assert minDistance(0, 0, a[0], a[1], a[2]) == expectation