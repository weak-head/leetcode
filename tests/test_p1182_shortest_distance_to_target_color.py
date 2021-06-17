# flake8: noqa: F403, F405
import pytest
from leetcode.p1182_shortest_distance_to_target_color import *

solutions = [
    shortestDistanceColor,
]

test_cases = [
    ([[1, 1, 2, 1, 3, 2, 2, 3, 3], [[1, 3], [2, 2], [6, 1]]], [3, 0, 3]),
    ([[1, 2], [[0, 3]]], [-1]),
    ([[2, 1, 2, 2, 1], [[1, 1], [4, 3], [1, 3], [4, 2], [2, 1]]], [0, -1, -1, 1, 1]),
    (
        [
            [3, 2, 2, 1, 3, 1, 1, 1, 3, 1],
            [
                [4, 1],
                [9, 2],
                [4, 2],
                [8, 1],
                [0, 3],
                [2, 1],
                [2, 3],
                [6, 3],
                [4, 1],
                [1, 2],
            ],
        ],
        [1, 7, 2, 1, 0, 1, 2, 2, 1, 0],
    ),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(*args) == expectation
