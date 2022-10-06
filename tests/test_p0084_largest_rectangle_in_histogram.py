# flake8: noqa: F403, F405
import pytest
from leetcode.p0084_largest_rectangle_in_histogram import *

solutions = [
    largestRectangleArea,
]

test_cases = [
    ([2, 1, 5, 6, 2, 3], 10),
    ([2, 4], 4),
    ([3], 3),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
