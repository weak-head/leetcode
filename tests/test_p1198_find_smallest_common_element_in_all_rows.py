# flake8: noqa: F403, F405
import pytest
from leetcode.p1198_find_smallest_common_element_in_all_rows import *

solutions = [
    smallestCommonElement,
]

test_cases = [
    ([[1, 2, 3, 4, 5], [2, 4, 5, 8, 10], [3, 5, 7, 9, 11], [1, 3, 5, 7, 9]], 5),
    ([[1, 2, 3], [3, 4, 5], [6, 7, 8]], -1),
    ([[1], [1], [1]], 1),
    ([[]], -1),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
