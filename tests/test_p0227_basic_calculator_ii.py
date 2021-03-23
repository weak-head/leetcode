# flake8: noqa: F403, F405
import pytest
from leetcode.p0227_basic_calculator_ii import *

solutions = [
    calculate,
]

test_cases = [
    ("5+3/2", 6),
    ("1+2+4", 7),
    ("2+4/2+2*3", 10),
    ("14-3/2", 13),
    ("3/2", 1),
    ("-3/2", -1),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
