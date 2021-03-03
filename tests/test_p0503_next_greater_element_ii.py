# flake8: noqa: F403, F405
import pytest
from leetcode.p0503_next_greater_element_ii import *

solutions = [
    nextGreaterElements,
]

test_cases = [
    ([1, 2, 1], [2, -1, 2]),
    ([1], [-1]),
    ([1, 1], [-1, -1]),
    ([3, 2, 1], [-1, 3, 3]),
    ([3, 1, 3], [-1, 3, -1]),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
