import pytest
from leetcode.p1057_campus_bikes import assignBikes


@pytest.mark.parametrize(
    ("a", "expectation"),
    (
        (([[0, 0], [2, 1]], [[1, 2], [3, 3]]), ([1, 0])),
        (([[0, 0], [1, 1], [2, 0]], [[1, 0], [2, 2], [2, 1]]), ([0, 2, 1])),
        (
            (
                [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0]],
                [
                    [0, 999],
                    [1, 999],
                    [2, 999],
                    [3, 999],
                    [4, 999],
                    [5, 999],
                    [6, 999],
                    [7, 999],
                ],
            ),
            [0, 1, 2, 3, 4, 5, 6, 7],
        ),
    ),
)
def test_solve(a, expectation):
    assert assignBikes(a[0], a[1]) == expectation
