# flake8: noqa: F403, F405
import pytest
from leetcode.p0923_3sum_with_multiplicity import *

solutions = [
    threeSumMulti,
]

test_cases = [
    ([[1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 8], 20),
    ([[1, 1, 2, 2, 2, 2], 5], 12),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(*args) == expectation
