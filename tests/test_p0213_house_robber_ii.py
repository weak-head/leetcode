# flake8: noqa: F403, F405
import pytest
from leetcode.p0213_house_robber_ii import *

solutions = [
    rob,
    rob_optimized,
]

test_cases = [
    ([2, 3, 2], 3),
    ([1, 2, 3, 1], 4),
    ([0], 0),
    ([7], 7),
    ([1, 2], 2),
    ([2, 1], 2),
    ([2, 1, 2], 2),
    ([7, 3, 2, 7], 10),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
