# flake8: noqa: F403, F405
import pytest
from leetcode.p1091_shortest_path_in_binary_matrix import *

solutions = [
    shortestPathBinaryMatrix_a_star,
]

#   ([args], expectation),
test_cases = [
    ([[1, 0, 0], [1, 1, 0], [1, 1, 0]], -1),
    ([[0, 1], [1, 0]], 2),
    ([[0, 0, 0], [1, 1, 0], [1, 1, 0]], 4),
    (
        [
            [0, 1, 1, 0, 0, 0],
            [0, 1, 0, 1, 1, 0],
            [1, 0, 1, 1, 0, 0],
            [1, 1, 1, 0, 1, 0],
            [0, 0, 0, 1, 1, 1],
            [0, 0, 0, 0, 0, 0],
        ],
        13,
    ),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
