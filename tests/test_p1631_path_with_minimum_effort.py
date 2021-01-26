import pytest
from leetcode.p1631_path_with_minimum_effort import (
    minimumEffortPath_bf,
    minimumEffortPath_dijkstra,
    minimumEffortPath_binary_bfs,
)


@pytest.mark.parametrize(
    ("a", "expectation"),
    (
        (([[1, 2, 2], [3, 8, 2], [5, 3, 5]], False), (2)),
        (
            (
                [
                    [8, 3, 2, 5, 2, 10, 7, 1, 8, 9],
                    [1, 4, 9, 1, 10, 2, 4, 10, 3, 5],
                    [4, 10, 10, 3, 6, 1, 3, 9, 8, 8],
                    [4, 4, 6, 10, 10, 10, 2, 10, 8, 8],
                    [9, 10, 2, 4, 1, 2, 2, 6, 5, 7],
                    [2, 9, 2, 6, 1, 4, 7, 6, 10, 9],
                    [8, 8, 2, 10, 8, 2, 3, 9, 5, 3],
                    [2, 10, 9, 3, 5, 1, 7, 4, 5, 6],
                    [2, 3, 9, 2, 5, 10, 2, 7, 1, 8],
                    [9, 10, 4, 10, 7, 4, 9, 3, 1, 6],
                ],
                False,
            ),
            (5),
        ),
        (([[1, 10, 6, 7, 9, 10, 4, 9]], False), (9)),
        (([[1], [10], [6], [7], [9], [10], [4], [9]], False), (9)),
    ),
)
def test_solve(a, expectation):
    heights, is_long = a[0], a[1]
    for f, skip_long in [
        (minimumEffortPath_bf, True),
        (minimumEffortPath_dijkstra, False),
        (minimumEffortPath_binary_bfs, False),
    ]:
        if is_long and skip_long:
            continue
        assert f(heights) == expectation
