# flake8: noqa: F403, F405
import pytest
from leetcode.p0077_combinations import *

solutions = [
    combine,
]

test_cases = [
    ([4, 2], [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]),
    ([4, 3], [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]]),
    ([4, 1], [[1], [2], [3], [4]]),
    (
        [6, 3],
        [
            [1, 2, 3],
            [1, 2, 4],
            [1, 2, 5],
            [1, 2, 6],
            [1, 3, 4],
            [1, 3, 5],
            [1, 3, 6],
            [1, 4, 5],
            [1, 4, 6],
            [1, 5, 6],
            [2, 3, 4],
            [2, 3, 5],
            [2, 3, 6],
            [2, 4, 5],
            [2, 4, 6],
            [2, 5, 6],
            [3, 4, 5],
            [3, 4, 6],
            [3, 5, 6],
            [4, 5, 6],
        ],
    ),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(*args) == expectation
