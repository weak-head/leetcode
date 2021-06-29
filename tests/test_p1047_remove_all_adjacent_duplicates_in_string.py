# flake8: noqa: F403, F405
import pytest
from leetcode.p1047_remove_all_adjacent_duplicates_in_string import *

solutions = [
    removeDuplicates_stack,
    removeDuplicates_quadratic,
]

test_cases = [
    ("abbaca", "ca"),
    ("azxxzy", "ay"),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
