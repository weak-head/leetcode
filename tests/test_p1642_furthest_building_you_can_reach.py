# flake8: noqa: F403, F405
import pytest
from leetcode.p1642_furthest_building_you_can_reach import *

solutions = [
    furthestBuilding,
]

test_cases = [
    ([[4, 2, 7, 6, 9, 14, 12], 5, 1], 4),
    ([[4, 12, 2, 7, 3, 18, 20, 3, 19], 10, 2], 7),
    ([[14, 3, 19, 3], 17, 0], 3),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(*args) == expectation
