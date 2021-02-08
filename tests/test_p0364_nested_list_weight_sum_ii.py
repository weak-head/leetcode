# flake8: noqa: F403, F405
import pytest
from leetcode.p0364_nested_list_weight_sum_ii import *

solutions = [
    depthSumInverse,
]

#   ([args], expectation),
test_cases = [
    ([[[1, 1]], 2, [[[[1, 1]]]]], 18),
    ([[[1, 1]], [2], [[[[1, 1]]]]], 16),
    ([1, 2, 3, 4, 5], 15),
    ([[list(range(30))], [[list(range(10))]]], 915),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    ni = to_nlist(args)
    assert solution(ni.getList()) == expectation


def to_nlist(arr):
    ni = NestedInteger()
    if isinstance(arr, list):
        for a in arr:
            ni.add(to_nlist(a))
    else:
        ni.setInteger(arr)
    return ni
