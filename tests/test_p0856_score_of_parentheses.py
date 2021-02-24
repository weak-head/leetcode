# flake8: noqa: F403, F405
import pytest
from leetcode.p0856_score_of_parentheses import *

solutions = [
    scoreOfParentheses,
]

test_cases = [
    ("", 0),
    ("()", 1),
    ("()()", 2),
    ("(()())", 4),
    ("((()))", 4),
    ("((()()))", 8),
    ("(((())))", 8),
    ("()(())()((()()((()))))", 28),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
