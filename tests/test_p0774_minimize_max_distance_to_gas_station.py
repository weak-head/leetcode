# flake8: noqa: F403, F405
import pytest
from leetcode.p0774_minimize_max_distance_to_gas_station import *

solutions = [
    minmaxGasDist_heap,
    minmaxGasDist_binary_search,
]

test_cases = [
    ([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9], 0.5),
    ([[[23, 24, 36, 39, 46, 56, 57, 65, 84, 98], 1], 14]),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    r = solution(*args)
    assert abs(r - expectation) <= 1e-6
