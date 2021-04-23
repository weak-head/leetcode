# flake8: noqa: F403, F405
import pytest
from leetcode.p0696_count_binary_substrings import *

solutions = [
    countBinarySubstrings,
]

test_cases = [
    ("00110011", 6),
    ("000011", 2),
    ("001111", 2),
    ("010101", 5),
    ("000111111111100", 5),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
