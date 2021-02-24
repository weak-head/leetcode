# flake8: noqa: F403, F405
import pytest
from leetcode.p0198_house_robber import *

solutions = [
    rob,
]

test_cases = [
    ([1, 2, 3, 1], 4),
    ([2, 7, 9, 3, 1], 12),
    ([1, 2, 1, 3, 1, 1, 7], 12),
    ([1, 1, 1, 1, 1, 1], 3),
    ([1, 1, 1, 1, 1, 1, 1], 4),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
