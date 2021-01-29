import pytest
from leetcode.p0277_find_the_celebrity import findCelebrity


@pytest.mark.parametrize(
    ("a", "expectation"),
    (
        ((3, [[1, 1, 0], [0, 1, 0], [1, 1, 1]]), (1)),
        ((4, [[1, 1, 0, 1], [0, 1, 0, 1], [1, 1, 1, 1], [1, 0, 0, 1]]), (-1)),
        ((3, [[1, 0, 1], [1, 1, 0], [0, 1, 1]]), (-1)),
    ),
)
def test_solve(a, expectation):
    assert findCelebrity(a[0], get_knows(a[1])) == expectation


def get_knows(arr):
    return lambda a, b: arr[a][b]
