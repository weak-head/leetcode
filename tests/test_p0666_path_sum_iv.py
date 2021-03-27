# flake8: noqa: F403, F405
import pytest
from leetcode.p0666_path_sum_iv import *

solutions = [
    pathSum,
]

test_cases = [
    ([113, 215, 221], 12),
    ([113, 221], 4),
    ([111, 217, 221, 315, 415], 20),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
