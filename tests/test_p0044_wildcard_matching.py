# flake8: noqa: F403, F405
import pytest
from leetcode.p0044_wildcard_matching import *

solutions = [
    isMatch_dp,
    isMatch_backtrack,
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize("solution", solutions)
@pytest.mark.parametrize(
    ("s", "p", "expectation"),
    (
        ("", "", True),
        ("a", "", False),
        ("", "b", False),
        ("abc", "a?c", True),
        ("abc", "a*", True),
        ("abc", "*", True),
        ("abc", "*?*", True),
        ("b", "*?*", True),
        ("b", "***b***", True),
        ("acbcd", "***b***", True),
        ("bbcbb", "*?*", True),
        ("abc", "*d", False),
        ("abcd", "*a*d", True),
        ("abc", "abc****d*", False),
        ("abcd", "abc****d*", True),
        ("aaaaaa", "?*?*?**?**a***?", True),
        ("aaaaaa", "?*?*?**?**a***???***", False),
    ),
)
def test_match(s, p, expectation, solution):
    assert solution(s, p) == expectation
