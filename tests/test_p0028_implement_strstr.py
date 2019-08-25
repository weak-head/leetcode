import pytest
from leetcode.p0028_implement_strstr import strStr, strStr2


@pytest.mark.parametrize(
    ("haystack", "needle", "index"),
    (("abbba", "bba", 2), ("asb", "", 0), ("kdf", "abc", -1), ("abba", "abbaa", -1)),
)
def test_strStr(haystack, needle, index):
    assert strStr(haystack, needle) == index
    assert strStr2(haystack, needle) == index
