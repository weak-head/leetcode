# flake8: noqa: F403, F405
import pytest
from leetcode.p1151_minimum_swaps_to_group_all_1s_together import *

solutions = [
    minSwaps,
]

test_cases = [
    ([1, 0, 1, 0, 1], 1),
    ([0, 0, 0, 1, 0], 0),
    ([1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1], 3),
    (
        [
            1,
            0,
            1,
            0,
            1,
            0,
            1,
            1,
            1,
            0,
            1,
            0,
            0,
            1,
            1,
            1,
            0,
            0,
            1,
            1,
            1,
            0,
            1,
            0,
            1,
            1,
            0,
            0,
            0,
            1,
            1,
            1,
            1,
            0,
            0,
            1,
        ],
        8,
    ),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
