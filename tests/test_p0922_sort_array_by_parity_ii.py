# flake8: noqa: F403, F405
import pytest
from leetcode.p0922_sort_array_by_parity_ii import *

solutions = [
    sortArrayByParityII,
]

test_cases = [
    [4, 2, 5, 7],
    [2, 3],
    [0, 2, 1, 2, 3, 5],
    [3, 2],
    [7, 7, 7, 2, 2, 2],
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize("args", test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, solution):
    arr = solution(args)
    for i in range(len(args)):
        assert arr[i] % 2 == i % 2
