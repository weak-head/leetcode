# flake8: noqa: F403, F405
import pytest
from leetcode.p0882_reachable_nodes_in_subdivided_graph import *

solutions = [
    reachableNodes,
]

test_cases = [
    ([[[0, 1, 10], [0, 2, 1], [1, 2, 2]], 6, 3], 13),
    ([[[0, 1, 4], [1, 2, 6], [0, 2, 8], [1, 3, 1]], 10, 4], 23),
    ([[[1, 2, 4], [1, 4, 5], [1, 3, 1], [2, 3, 4], [3, 4, 5]], 17, 5], 1),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(*args) == expectation
