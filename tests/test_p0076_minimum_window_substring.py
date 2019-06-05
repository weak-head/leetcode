import pytest
from leetcode.p0076_minimum_window_substring import minWindow


@pytest.mark.parametrize(
    ("s", "t", "r"),
    (
        ("a", "a", "a"),
        ("ADOBECODEBANC", "ABC", "BANC"),
        ("", "b", ""),
        ("ABBBABACCBAD", "DEF", ""),
    ),
)
def test_minWindow(s, t, r):
    assert minWindow(s, t) == r
