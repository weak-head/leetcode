# flake8: noqa: F403, F405
import pytest
from leetcode.p0784_letter_case_permutation import *

solutions = [
    letterCasePermutation,
]

test_cases = [
    ("a1b2", ["a1b2", "A1b2", "a1B2", "A1B2"]),
    ("a1b23", ["a1b23", "A1b23", "a1B23", "A1B23"]),
    ("12a34", ["12a34", "12A34"]),
    ("123", ["123"]),
    ("", [""]),
    ("ab", ["ab", "aB", "Ab", "AB"]),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    want = expectation
    got = solution(args)
    assert len(want) == len(got)
    assert set(got) == set(want)
