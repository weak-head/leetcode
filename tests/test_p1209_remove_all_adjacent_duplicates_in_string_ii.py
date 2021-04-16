# flake8: noqa: F403, F405
import pytest
from leetcode.p1209_remove_all_adjacent_duplicates_in_string_ii import *

solutions = [
    removeDuplicates_stack,
    removeDuplicates_naive,
]

test_cases = [
    (["deeedbbcccbdaa", 3], "aa"),
    (["deeedbbcccbdaa", 2], "dedcbd"),
    (["pbbcggttciiippooaais", 2], "ps"),
    (["abcd", 2], "abcd"),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(*args) == expectation
