# flake8: noqa: F403, F405
import pytest
from leetcode.p1704_determine_if_string_halves_are_alike import *

solutions = [
    halvesAreAlike,
]

test_cases = [
    ("tool", True),
    ("meme", True),
    ("abbb", False),
    ("bbab", False),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
