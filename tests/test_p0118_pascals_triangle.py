# flake8: noqa: F403, F405
import pytest
from leetcode.p0118_pascals_triangle import *

solutions = [
    generate,
]

test_cases = [
    (1, [[1]]),
    (5, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
