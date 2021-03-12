# flake8: noqa: F403, F405
import pytest
from leetcode.p1461_check_if_a_string_contains_all_binary_codes_of_size_k import *

solutions = [
    hasAllCodes,
]

test_cases = [
    (["00110", 2], True),
    (["00110110", 2], True),
    (["0110", 1], True),
    (["0001110110100", 3], True),
    (["000111011010", 3], False),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(*args) == expectation
