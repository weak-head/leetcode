# flake8: noqa: F403, F405
import pytest
from leetcode.p1191_k_concatenation_maximum_sum import *

solutions = [
    kConcatenationMaxSum,
]

test_cases = [
    ([[1, 2], 3], 9),
    ([[1, -2, 1], 5], 2),
    ([[-1, -2], 7], 0),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(*args) == expectation
