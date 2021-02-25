# flake8: noqa: F403, F405
import pytest
from leetcode.p0046_permutations import *

solutions = [
    permute,
]

test_cases = [
    ([0], [[0]]),
    ([0, 1], [[0, 1], [1, 0]]),
    ([0, 1, 2], [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
