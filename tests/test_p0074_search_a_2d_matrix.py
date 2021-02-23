# flake8: noqa: F403, F405
import pytest
from leetcode.p0074_search_a_2d_matrix import *

solutions = [
    searchMatrix,
]

test_cases = [
    ([[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 21], False),
    ([[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 77], False),
    ([[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 0], False),
    ([[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 5], True),
    ([[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 11], True),
    ([[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 20], True),
    ([[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 23], True),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(*args) == expectation
