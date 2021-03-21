# flake8: noqa: F403, F405
import pytest
from leetcode.p0869_reordered_power_of_2 import *

solutions = [
    reorderedPowerOf2,
]

test_cases = [
    (1, True),
    (2, True),
    (3, False),
    (46, True),
    (812, True),
    (217, False),
    (2014, True),
    (9640, True),
    (9982, False),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
