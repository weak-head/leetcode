# flake8: noqa: F403, F405
import pytest
from leetcode.p0224_basic_calculator import *

solutions = [
    calculate,
]

test_cases = [
    ("7 + (3 - 4) + 5-(12-11)", 10),
    ("-6 + (1-12)", -17),
    ("((((-4+3)+7)-1)-1)+12-(4-4)+(-7+7)", 16),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
