# flake8: noqa: F403, F405
import pytest
from leetcode.p0969_pancake_sorting import *

solutions = [
    pancakeSort,
]

test_cases = [
    ([], []),
    ([2, 7, 3, 1, 0, 4], [0, 1, 2, 3, 4, 7]),
    ([1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7]),
    ([7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7]),
    ([5, 5, 5, 5, 1], [1, 5, 5, 5, 5]),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    solution(args)
    assert args == expectation
