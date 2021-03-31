# flake8: noqa: F403, F405
import pytest
from leetcode.p1011_capacity_to_ship_packages_within_d_days import *

solutions = [
    shipWithinDays,
]

test_cases = [
    ([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5], 15),
    ([[3, 2, 2, 4, 1, 4], 3], 6),
    ([[1, 2, 3, 1, 1], 4], 3),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(*args) == expectation
