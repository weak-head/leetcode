# flake8: noqa: F403, F405
import pytest
from leetcode.p0076_minimum_window_substring import *

solutions = [minWindow]

test_cases = [
    ("", "b", ""),
    ("a", "a", "a"),
    ("ADOBECODEBANC", "ABC", "BANC"),
    ("ABBBABACCBAD", "DEF", ""),
    ("1234567890", "36", "3456"),
]


@pytest.mark.parametrize(("s", "t", "r"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_minWindow(s, t, r, solution):
    assert solution(s, t) == r
