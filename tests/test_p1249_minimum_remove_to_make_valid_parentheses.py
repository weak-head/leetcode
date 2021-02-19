# flake8: noqa: F403, F405
import pytest
from leetcode.p1249_minimum_remove_to_make_valid_parentheses import *

solutions = [
    minRemoveToMakeValid_three_pass,
    minRemoveToMakeValid_two_pass,
]

test_cases = [
    ("abc", {"abc"}),
    ("a(b)c", {"a(b)c"}),
    ("abc()", {"abc()"}),
    ("abc((((", {"abc"}),
    ("abc)))))((((", {"abc"}),
    ("abc)))))", {"abc"}),
    (")))))abc)))))", {"abc"}),
    (")))))abc", {"abc"}),
    ("(((((abc", {"abc"}),
    ("(((abc))", {"((abc))"}),
    ("()((abc)(()", {"()(abc)()", "()((abc))"}),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) in expectation
