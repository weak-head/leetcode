import pytest
from leetcode.p0340_longest_substring_with_at_most_k_distinct_characters import (
    lengthOfLongestSubstringKDistinct1,
    lengthOfLongestSubstringKDistinct2,
)


@pytest.mark.parametrize(
    ("a", "expectation"),
    (
        (("eceba", 2), (3)),
        (("aa", 1), (2)),
        (("aabb", 2), (4)),
        (("abccad", 3), (5)),
        (("fabccadd", 4), (7)),
    ),
)
def test_solve(a, expectation):
    assert lengthOfLongestSubstringKDistinct1(a[0], a[1]) == expectation
    assert lengthOfLongestSubstringKDistinct2(a[0], a[1]) == expectation
