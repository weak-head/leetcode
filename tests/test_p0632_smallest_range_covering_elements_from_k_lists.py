# flake8: noqa: F403, F405
from cgitb import small
import pytest
from leetcode.p0632_smallest_range_covering_elements_from_k_lists import *

solutions = [
    smallestRange,
]

test_cases = [
    ([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]], (20, 24)),
    ([[1, 2, 3], [1, 2, 3], [1, 2, 3]], (1, 1)),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
