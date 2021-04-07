# flake8: noqa: F403, F405
import pytest
from leetcode.p1471_the_k_strongest_values_in_an_array import *

solutions = [
    getStrongest_quickselect,
    getStrongest_sort,
]

test_cases = [
    ([[-7, 22, 17, 3], 2], {22, 17}),
    ([[1, 2, 3, 4, 5], 2], {5, 1}),
    ([[1, 1, 3, 5, 5], 2], {5}),
    ([[6, 7, 11, 7, 6, 8], 5], {11, 8, 6, 7}),
    ([[6, -3, 7, 2, 11], 3], {-3, 11, 2}),
    ([[-7, 22, 17, 3], 2], {22, 17}),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    r = solution(*args)
    assert len(r) == args[1]
    assert set(r) == expectation
