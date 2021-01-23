import pytest
from leetcode.p0616_add_bold_tag_in_string import addBoldTag


@pytest.mark.parametrize(
    ("a", "expectation"),
    (
        (("abcxyz123", ["abc", "123"]), ("<b>abc</b>xyz<b>123</b>")),
        (("aaaa", ["a"]), ("<b>aaaa</b>")),
    ),
)
def test_solve(a, expectation):
    assert addBoldTag(a[0], a[1]) == expectation
