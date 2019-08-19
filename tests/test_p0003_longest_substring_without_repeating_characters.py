import pytest
from leetcode.p0003_longest_substring_without_repeating_characters import (
    lengthOfLongestSubstring,
    lengthOfLongestSubstring2,
)


@pytest.mark.parametrize(
    ("s", "expectation"),
    (
        ("abcd", 4),
        ("aaaaa", 1),
        ("a", 1),
        ("", 0),
        ("abcabcdabcdeabc", 5),
        ("ababbbbaaabba", 2),
        ("ababbbbaaacbbbaabaaac", 3),
        ("tmmzuxt", 5),
    ),
)
def test_lengthOfSubstring(s, expectation):
    assert lengthOfLongestSubstring(s) == expectation
    assert lengthOfLongestSubstring2(s) == expectation
