# flake8: noqa: F403, F405
import pytest
from leetcode.p0871_minimum_number_of_refueling_stops import *

solutions = [
    minRefuelStops,
]

test_cases = [
    ([1, 1, []], 0),
    ([100, 1, [[10, 100]]], -1),
    ([100, 10, [[10, 60], [20, 30], [30, 30], [60, 40]]], 2),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(*args) == expectation
