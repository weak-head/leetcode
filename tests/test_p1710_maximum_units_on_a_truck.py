# flake8: noqa: F403, F405
import pytest
from leetcode.p1710_maximum_units_on_a_truck import *

solutions = [
    maximumUnits,
]

test_cases = [
    ([[[1, 3], [2, 2], [3, 1]], 4], 8),
    ([[[5, 10], [2, 5], [4, 7], [3, 9]], 10], 91),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(*args) == expectation
