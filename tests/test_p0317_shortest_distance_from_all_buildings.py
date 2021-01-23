import pytest
from leetcode.p0317_shortest_distance_from_all_buildings import shortestDistance


@pytest.mark.parametrize(
    ("a", "expectation"),
    (
        (([[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]), (7)),
        (
            (
                [
                    [1, 1, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 1],
                    [0, 1, 1, 0, 0, 1],
                    [1, 0, 0, 1, 0, 1],
                    [1, 0, 1, 0, 0, 1],
                    [1, 0, 0, 0, 0, 1],
                    [0, 1, 1, 1, 1, 0],
                ]
            ),
            (88),
        ),
    ),
)
def test_solve(a, expectation):
    assert shortestDistance(a) == expectation
