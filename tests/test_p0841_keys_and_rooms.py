# flake8: noqa: F403, F405
import pytest
from leetcode.p0841_keys_and_rooms import *

solutions = [
    canVisitAllRooms,
]

test_cases = [
    ([[1], [2], [3], []], True),
    ([[1, 3], [3, 0, 1], [2], [0]], False),
    ([[1], [1], [1]], False),
    ([[1, 2, 3], [], [], []], True),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
