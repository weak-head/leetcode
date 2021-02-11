# flake8: noqa: F403, F405
import pytest
from leetcode.p1105_filling_bookcase_shelves import *

solutions = [
    minHeightShelves_dp_td,
    minHeightShelves_dp_bu,
]

#   ([args], expectation),
test_cases = [
    ([[[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]], 4], 6),
    ([[[3, 1], [4, 1], [5, 1]], 5], 3),
    ([[[1, 3], [1, 4], [7, 1], [3, 5], [1, 1], [3, 1]], 20], 5),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(*args) == expectation
