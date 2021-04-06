# flake8: noqa: F403, F405
import pytest
from leetcode.p0947_most_stones_removed_with_same_row_or_column import *

solutions = [
    removeStones,
]

test_cases = [
    ([[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]], 5),
    ([[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]], 3),
    ([[0, 0]], 0),
    ([[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]], 0),
    ([[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [4, 3]], 2),
    ([[0, 0], [0, 1], [0, 2], [0, 3]], 3),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
