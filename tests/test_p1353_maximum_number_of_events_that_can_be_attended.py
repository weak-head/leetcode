# flake8: noqa: F403, F405
import pytest
from leetcode.p1353_maximum_number_of_events_that_can_be_attended import *

solutions = [
    maxEvents,
]

test_cases = [
    ([(1, 3), (1, 2), (1, 4), (2, 7)], 4),
    ([[1, 2], [2, 3], [3, 4]], 3),
    ([[1, 2], [2, 3], [3, 4], [1, 2]], 4),
    ([[1, 4], [4, 4], [2, 2], [3, 4], [1, 1]], 4),
    ([[1, 100000]], 1),
    ([[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7]], 7),
    ([[1, 2], [1, 2], [1, 2], [1, 2]], 2),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
