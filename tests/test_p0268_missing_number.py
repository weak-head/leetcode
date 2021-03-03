# flake8: noqa: F403, F405
import pytest
from leetcode.p0268_missing_number import *

solutions = [
    missingNumber,
]

test_cases = [
    ([1, 2], 0),
    ([1, 2, 0], 3),
    ([0, 4, 2, 1], 3),
    ([1, 2, 3, 4, 5], 0),
    ([0, 1, 2, 3, 4], 5),
    ([0, 1, 2, 3, 5], 4),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
