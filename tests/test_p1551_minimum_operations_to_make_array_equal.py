# flake8: noqa: F403, F405
import pytest
from leetcode.p1551_minimum_operations_to_make_array_equal import *

solutions = [
    minOperations,
]

test_cases = [
    (3, 2),
    (6, 9),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
