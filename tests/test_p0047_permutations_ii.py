# flake8: noqa: F403, F405
import pytest
from leetcode.p0047_permutations_ii import *

solutions = [
    permuteUnique,
]

test_cases = [
    ([1, 1, 2], [[1, 1, 2], [1, 2, 1], [2, 1, 1]]),
    ([1, 2, 2], [[1, 2, 2], [2, 1, 2], [2, 2, 1]]),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == set(map(tuple, expectation))
