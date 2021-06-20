# flake8: noqa: F403, F405
import pytest
from leetcode.p0778_swim_in_rising_water import *

solutions = [
    swimInWater,
]

test_cases = [
    (
        [
            [0, 1, 2, 3, 4],
            [24, 23, 22, 21, 5],
            [12, 13, 14, 15, 16],
            [11, 17, 18, 19, 20],
            [10, 9, 8, 7, 6],
        ],
        16,
    ),
    ([[0, 2], [1, 3]], 3),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
