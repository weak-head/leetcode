# flake8: noqa: F403, F405
import pytest
from leetcode.p0377_combination_sum_iv import *

solutions = [
    combinationSum_bu,
    combinationSum_td,
]

test_cases = [
    ([[1, 2, 3], 4], 7),
    ([[9], 3], 0),
    ([[1, 2], 4], 5),
    ([[1, 2, 3, 4, 5], 122], 351978576042669895764118928906140786),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(*args) == expectation
