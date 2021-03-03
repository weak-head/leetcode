# flake8: noqa: F403, F405
import pytest
from leetcode.p0496_next_greater_element_i import *

solutions = [
    nextGreaterElement,
]

test_cases = [
    ([[4, 1, 2], [1, 3, 4, 2]], [-1, 3, -1]),
    ([[2, 4], [1, 2, 3, 4]], [3, -1]),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(*args) == expectation
