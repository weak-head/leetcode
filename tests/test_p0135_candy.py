# flake8: noqa: F403, F405
import pytest
from leetcode.p0135_candy import *

solutions = [
    candy,
]

test_cases = [
    ([1, 0, 2], 5),
    ([1, 2, 2], 4),
    ([1, 2, 1, 1, 1, 1, 2, 1], 10),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
