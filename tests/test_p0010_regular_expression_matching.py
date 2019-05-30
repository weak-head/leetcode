import pytest
from leetcode.p0010_regular_expression_matching import isMatch, isMatch2


@pytest.mark.timeout(10)
@pytest.mark.parametrize(
    ("string", "pattern", "match", "both"),
    (
        ("aaa", "aaa", True, True),
        ("aaa", "a*", True, True),
        ("aaa", "aaaa", False, True),
        ("aaaa", "aaa", False, True),
        ("", ".*", True, True),
        ("", "a*", True, True),
        ("abc", "c*d*abb*cc*", True, True),
        ("abc", "c*d*a.b*cc*", True, True),
        ("abcde", "c*d*a.c.*", True, True),
        ("abcde", "c*d*a.b.*", False, True),
        ("abc", ".*", True, True),
        ("", "", True, True),
        ("abc", "", False, True),
        ("", "abc", False, True),
        ("", "a*b*c*", True, True),
        ("abcde", ".....", True, True),
        ("abcdef", ".....", False, True),
        ("abcd", ".....", False, True),
        ("bbbbba", ".*a*a", True, True),
        ("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c", False, False),
    ),
)
def test_isMatch(string, pattern, match, both):
    if both:
        assert isMatch(string, pattern) == match
    assert isMatch2(string, pattern) == match
