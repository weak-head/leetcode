# flake8: noqa: F403, F405
import pytest
from leetcode.p0322_coin_change import *

solutions = [
    coinChange_dp_td,
    coinChange_dp_bu,
]

#   ([args], expectation),
test_cases = [
    ([[1, 2, 5], 11], 3),
    ([[2], 3], -1),
    ([[1], 0], 0),
    ([[1], 1], 1),
    ([[1], 2], 2),
    ([[1], 200], 200),
    ([[1, 2], 200], 100),
    ([[1, 2147483647], 2], 2),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(*args) == expectation
