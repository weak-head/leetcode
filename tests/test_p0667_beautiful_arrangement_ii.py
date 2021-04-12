# flake8: noqa: F403, F405
import pytest
from leetcode.p0667_beautiful_arrangement_ii import *

solutions = [
    constructArray,
]

test_cases = [
    ([3, 1], [1, 2, 3]),
    ([3, 2], [1, 3, 2]),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(*args) == expectation
