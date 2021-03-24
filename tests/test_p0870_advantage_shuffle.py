# flake8: noqa: F403, F405
import pytest
from leetcode.p0870_advantage_shuffle import *

solutions = [
    advantageCount,
    advantageCount_2,
]

test_cases = [
    ([[2, 7, 11, 15], [1, 10, 4, 11]], [2, 11, 7, 15]),
    ([[12, 24, 8, 32], [13, 25, 32, 11]], [24, 32, 8, 12]),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(*args) == expectation
