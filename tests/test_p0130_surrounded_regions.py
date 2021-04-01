# flake8: noqa: F403, F405
import pytest
from leetcode.p0130_surrounded_regions import *

solutions = [
    solve_dfs,
    solve_union_find,
]

test_cases = [
    (
        [
            ["X", "X", "X", "X"],
            ["X", "O", "O", "X"],
            ["X", "X", "O", "X"],
            ["X", "O", "X", "X"],
        ],
        [
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "O", "X", "X"],
        ],
    ),
    (
        [
            ["X", "X", "X", "X"],
            ["O", "O", "O", "X"],
            ["X", "O", "O", "X"],
            ["X", "O", "X", "X"],
        ],
        [
            ["X", "X", "X", "X"],
            ["O", "O", "O", "X"],
            ["X", "O", "O", "X"],
            ["X", "O", "X", "X"],
        ],
    ),
    (
        [
            ["X", "O", "X", "X"],
            ["O", "X", "O", "X"],
            ["X", "O", "X", "O"],
            ["O", "X", "O", "X"],
            ["X", "O", "X", "O"],
            ["O", "X", "O", "X"],
        ],
        [
            ["X", "O", "X", "X"],
            ["O", "X", "X", "X"],
            ["X", "X", "X", "O"],
            ["O", "X", "X", "X"],
            ["X", "X", "X", "O"],
            ["O", "X", "O", "X"],
        ],
    ),
    (
        [
            ["X", "O", "X", "X"],
            ["O", "O", "O", "X"],
            ["X", "O", "X", "O"],
            ["O", "O", "O", "X"],
            ["X", "O", "X", "O"],
            ["O", "O", "O", "X"],
        ],
        [
            ["X", "O", "X", "X"],
            ["O", "O", "O", "X"],
            ["X", "O", "X", "O"],
            ["O", "O", "O", "X"],
            ["X", "O", "X", "O"],
            ["O", "O", "O", "X"],
        ],
    ),
    (
        [
            ["O", "O", "O", "O"],
            ["O", "X", "O", "X"],
            ["X", "O", "X", "O"],
            ["O", "X", "O", "X"],
            ["X", "O", "X", "O"],
            ["O", "X", "O", "X"],
        ],
        [
            ["O", "O", "O", "O"],
            ["O", "X", "O", "X"],
            ["X", "X", "X", "O"],
            ["O", "X", "X", "X"],
            ["X", "X", "X", "O"],
            ["O", "X", "O", "X"],
        ],
    ),
    ([["X"]], [["X"]]),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    copy = [[args[x][y] for y in range(len(args[0]))] for x in range(len(args))]
    solution(copy)
    assert copy == expectation
