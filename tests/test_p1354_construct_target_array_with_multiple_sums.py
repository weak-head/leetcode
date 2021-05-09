# flake8: noqa: F403, F405
import pytest
from leetcode.p1354_construct_target_array_with_multiple_sums import *

solutions = [
    isPossible,
]

test_cases = [
    ([1], True),
    ([2], False),
    ([1, 2], True),
    ([1, 1, 2], False),
    ([1, 1000000000], True),
    ([5, 50], False),
    ([9, 3, 5], True),
    ([8, 5], True),
    ([23, 5], True),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
