# flake8: noqa: F403, F405
import pytest
from leetcode.p0785_is_graph_bipartite import *

solutions = [
    isBipartite,
]

#   ([args], expectation),
test_cases = [
    ([[1, 3], [0, 2], [1, 3], [0, 2]], True),
    ([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]], False),
    (
        [
            [],
            [2, 4, 6],
            [1, 4, 8, 9],
            [7, 8],
            [1, 2, 8, 9],
            [6, 9],
            [1, 5, 7, 8, 9],
            [3, 6, 9],
            [2, 3, 4, 6, 9],
            [2, 4, 5, 6, 7, 8],
        ],
        False,
    ),
    ([[], [], [], []], True),
    ([[1, 2, 3], [0], [0], [0]], True),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
