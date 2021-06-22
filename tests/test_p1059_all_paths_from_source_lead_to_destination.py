# flake8: noqa: F403, F405
import pytest
from leetcode.p1059_all_paths_from_source_lead_to_destination import *

solutions = [
    leadsToDestination,
]

test_cases = [
    ([[[0, 1], [0, 2]], 0, 2], False),
    ([[[0, 1], [0, 3], [1, 2], [2, 1]], 0, 3], False),
    ([[[0, 1], [0, 2], [1, 3], [2, 3]], 0, 3], True),
    ([[[0, 1], [1, 1], [1, 2]], 0, 2], False),
    ([[[0, 1], [1, 1]], 0, 1], False),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(*args) == expectation
