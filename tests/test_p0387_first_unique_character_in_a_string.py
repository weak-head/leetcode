import pytest
from leetcode.p0387_first_unique_character_in_a_string import firstUniqChar


@pytest.mark.parametrize(
    ("s", "ix"),
    (
        ("leetcode", 0),
        ("loveleetcode", 2),
        ("ll", -1),
        ("", -1),
        ("abcdefgh", 0),
        ("asdfasdfasdf", -1),
        ("aaaaabbbbbaaaabbbbc", 18),
    ),
)
def test_fistUniqueChar(s, ix):
    assert firstUniqChar(s) == ix
