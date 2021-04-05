# flake8: noqa: F403, F405
import pytest
from leetcode.p0775_global_and_local_inversions import *

solutions = [
    isIdealPermutation_scan,
    isIdealPermutation_minv,
]

test_cases = [
    ([1, 0, 2], True),
    ([1, 2, 0], False),
    ([1, 2, 3, 4, 5, 6, 7], True),
    ([8, 1, 2, 3, 4, 5, 6, 7], False),
    ([1, 0, 3, 2, 5, 4, 7, 6], True),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
