# flake8: noqa: F403, F405
import pytest
from leetcode.p0554_brick_wall import *

solutions = [
    leastBricks,
]

test_cases = [
    ([[1, 2, 2, 1], [3, 1, 2], [1, 3, 2], [2, 4], [3, 1, 2], [1, 3, 1, 1]], 2),
    ([[1, 2], [1, 2], [1, 1, 1], [1, 1, 1]], 0),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
