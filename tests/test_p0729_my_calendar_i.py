# flake8: noqa: F403, F405
import pytest
from leetcode.p0729_my_calendar_i import *

solutions = [
    Calendar,
]

test_cases = [
    [
        [10, 20, True],
        [15, 25, False],
        [20, 30, True],
    ],
    [
        [1, 100, True],
        [10, 20, False],
        [30, 150, False],
        [100, 250, True],
        [260, 300, True],
        [120, 320, False],
        [250, 270, False],
    ],
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize("args", test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, solution):
    c = solution()
    for start, end, outcome in args:
        assert c.book(start, end) == outcome
