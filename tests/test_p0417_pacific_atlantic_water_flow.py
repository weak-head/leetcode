# flake8: noqa: F403, F405
import pytest
from leetcode.p0417_pacific_atlantic_water_flow import *

solutions = [
    pacificAtlantic,
]

test_cases = [
    (
        [
            [1, 2, 2, 3, 5],
            [3, 2, 3, 4, 4],
            [2, 4, 5, 3, 1],
            [6, 7, 1, 4, 5],
            [5, 1, 1, 2, 4],
        ],
        [[4, 0], [0, 4], [3, 1], [1, 4], [3, 0], [2, 2], [1, 3]],
    )
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == set(map(tuple, expectation))
