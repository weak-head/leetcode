# flake8: noqa: F403, F405
import pytest
from leetcode.p0150_evaluate_reverse_polish_notation import *

solutions = [
    evalRPN,
]

test_cases = [
    (["2", "1", "+", "3", "*"], 9),
    (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22),
    (["4", "13", "5", "/", "+"], 6),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
