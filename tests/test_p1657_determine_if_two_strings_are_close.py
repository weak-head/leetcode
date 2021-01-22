import pytest
from leetcode.p1657_determine_if_two_strings_are_close import closeStrings


@pytest.mark.parametrize(
    ("a", "expectation"),
    (
        (("abc", "bca"), (True)),
        (("abcbcc", "aabcbb"), (True)),
        (("abc", "def"), (False)),
        (("aa", "a"), (False)),
    ),
)
def test_solve(a, expectation):
    assert closeStrings(a[0], a[1]) == expectation
