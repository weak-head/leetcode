import pytest
from leetcode.p0014_longest_common_prefix import (
    longestCommonPrefix,
)


@pytest.mark.parametrize(
    ("items", "prefix"),
    (
        ([], ""),
        (["abc", "abcd", "abcdef", "abb"], "ab"),
        (["abc", "fde", "fek"], ""),
        (["flower", "flow", "flight"], "fl"),
        (["aca", "bca"], ""),
        (["aa", "a"], "a"),
    ),
)
def test_lcp(items, prefix):
    assert longestCommonPrefix(items) == prefix
