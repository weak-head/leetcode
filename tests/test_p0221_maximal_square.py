# flake8: noqa: F403, F405
import pytest
from leetcode.p0221_maximal_square import *

solutions = [
    maximalSquare_dp,
    maximalSquare_dp_optimized,
]

#   ([args], expectation),
test_cases = [
    (
        [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"],
        ],
        4,
    ),
    ([["0", "1"], ["1", "0"]], 1),
    ([["0"]], 0),
    (
        [
            ["1", "1", "1", "0", "0"],
            ["1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "1", "1", "1"],
        ],
        9,
    ),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
