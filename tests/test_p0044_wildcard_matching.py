import pytest
from leetcode.p0044_wildcard_matching import isMatch


@pytest.mark.parametrize(
    ("s", "p", "expectation"),
    (
        ("", "", True),
        ("a", "", False),
        ("", "b", False),
        ("abc", "a?c", True),
        ("abc", "a*", True),
        ("abc", "*", True),
        ("abc", "*d", False),
        ("abcd", "*a*d", True),
        ("abc", "abc****d*", False),
        ("abcd", "abc****d*", True),
        ("aaaaaa", "?*?*?**?**a***?", True),
        ("aaaaaa", "?*?*?**?**a***???***", False),
    ),
)
def test_match(s, p, expectation):
    assert isMatch(s, p) == expectation
