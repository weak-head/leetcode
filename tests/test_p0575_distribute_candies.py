# flake8: noqa: F403, F405
import pytest
from leetcode.p0575_distribute_candies import *

solutions = [
    distributeCandies,
]

test_cases = [
    ([1, 1, 2, 2, 3, 3], 3),
    ([1, 1, 2, 2, 3], 2),
    ([1, 1, 1, 1, 1, 1, 1], 1),
    ([1], 0),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
