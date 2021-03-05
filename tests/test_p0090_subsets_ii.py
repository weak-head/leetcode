# flake8: noqa: F403, F405
import pytest
from leetcode.p0090_subsets_ii import *

solutions = [
    subsetsWithDup,
]

test_cases = [
    ([], [[]]),
    ([1, 2, 2], [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]),
    (
        [1, 2, 2, 2, 2],
        [
            [],
            [1],
            [1, 2],
            [1, 2, 2],
            [1, 2, 2, 2],
            [1, 2, 2, 2, 2],
            [2],
            [2, 2],
            [2, 2, 2],
            [2, 2, 2, 2],
        ],
    ),
    ([1, 2, 3], [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
