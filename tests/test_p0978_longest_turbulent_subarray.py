# flake8: noqa: F403, F405
import pytest
from leetcode.p0978_longest_turbulent_subarray import *

solutions = [
    maxTurbulenceSize,
]

test_cases = [
    ([9, 4, 2, 10, 7, 8, 8, 1, 9], 5),
    ([4, 8, 12, 16], 2),
    ([1], 1),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
