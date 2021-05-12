# flake8: noqa: F403, F405
import pytest
from leetcode.p0304_range_sum_query_2d_immutable import *

solutions = [
    NumMatrix,
    NumMatrixBF,
]

test_cases = [
    [
        [
            [3, 0, 1, 4, 2],
            [5, 6, 3, 2, 1],
            [1, 2, 0, 1, 5],
            [4, 1, 0, 1, 7],
            [1, 0, 3, 0, 5],
        ],
        ([2, 1, 4, 3], 8),
        ([1, 1, 2, 2], 11),
        ([1, 2, 2, 4], 12),
    ],
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize("args", test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, solution):
    m = solution(args[0])
    for r, e in args[1:]:
        assert m.sumRegion(*r) == e
