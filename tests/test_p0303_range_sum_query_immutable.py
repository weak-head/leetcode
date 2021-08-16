# flake8: noqa: F403, F405
import pytest
from leetcode.p0303_range_sum_query_immutable import *

solutions = [
    NumArray,
]

test_cases = [
    [
        [1, 2, 3, 4, 5, 6],
        (0, 2, 6),
        (0, 4, 15),
        (1, 2, 5),
    ],
    [
        [0, 0, 0, 0, 1, 0, 0, 1, 0],
        (0, 3, 0),
        (0, 8, 2),
        (1, 6, 1),
    ],
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize("args", test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, solution):
    na = solution(args[0])
    for l, r, e in args[1:]:
        assert na.sumRange(l, r) == e
