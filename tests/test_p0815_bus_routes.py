# flake8: noqa: F403, F405
import pytest
from leetcode.p0815_bus_routes import *

solutions = [
    numBusesToDestination,
]

test_cases = [
    ([[[1, 2, 7], [3, 6, 7]], 1, 1], 0),
    ([[[1, 2, 7], [3, 6, 7]], 1, 6], 2),
    ([[[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]], 15, 12], -1),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(*args) == expectation
