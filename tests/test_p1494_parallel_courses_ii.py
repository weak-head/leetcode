# flake8: noqa: F403, F405
import pytest
from leetcode.p1494_parallel_courses_ii import *

solutions = [
    minNumberOfSemesters,
]

test_cases = [
    (
        [
            13,
            [
                [12, 8],
                [2, 4],
                [3, 7],
                [6, 8],
                [11, 8],
                [9, 4],
                [9, 7],
                [12, 4],
                [11, 4],
                [6, 4],
                [1, 4],
                [10, 7],
                [10, 4],
                [1, 7],
                [1, 8],
                [2, 7],
                [8, 4],
                [10, 8],
                [12, 7],
                [5, 4],
                [3, 4],
                [11, 7],
                [7, 4],
                [13, 4],
                [9, 8],
                [13, 8],
            ],
            9,
        ],
        3,
    ),
    ([4, [[2, 1], [3, 1], [1, 4]], 2], 3),
    ([5, [[2, 1], [3, 1], [4, 1], [1, 5]], 2], 4),
    ([11, [], 2], 6),
    ([11, [], 1], 11),
    ([11, [], 3], 4),
    ([11, [], 6], 2),
    ([11, [], 8], 2),
    ([11, [], 10], 2),
    ([11, [], 11], 1),
    ([11, [], 12], 1),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(*args) == expectation
