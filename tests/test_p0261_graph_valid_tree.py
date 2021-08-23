# flake8: noqa: F403, F405
import pytest
from leetcode.p0261_graph_valid_tree import *

solutions = [
    validTree_bfs,
    validTree_uf,
]

test_cases = [
    ([5, [[0, 1], [0, 2], [0, 3], [1, 4]]], True),
    ([5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]], False),
    ([6, [(0, 5), (4, 0), (1, 2), (4, 5), (3, 2)]], False),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(*args) == expectation
