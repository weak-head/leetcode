# flake8: noqa: F403, F405
import pytest
from leetcode.p0733_flood_fill import *

solutions = [
    floodFill,
]

test_cases = [
    ([[[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2], [[2, 2, 2], [2, 2, 0], [2, 0, 1]]),
    (
        [
            [[0, 0, 0], [0, 1, 1]],
            1,
            1,
            1,
        ],
        [[0, 0, 0], [0, 1, 1]],
    ),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(*args) == expectation
