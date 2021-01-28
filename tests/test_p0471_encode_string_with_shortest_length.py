import pytest
from leetcode.p0471_encode_string_with_shortest_length import encode


@pytest.mark.parametrize(
    ("a", "expectation"),
    (
        (("aaa"), ("aaa")),
        (("aaaaa"), ("5[a]")),
        (("aaaaabbbbb"), ("5[a]5[b]")),
        (("aaaaabbbbbaaaaabbbbb"), ("2[5[a]5[b]]")),
        (("caaaaabbbbbaaaaabbbbbc"), ("c2[5[a]5[b]]c")),
    ),
)
def test_solve(a, expectation):
    assert encode(a) == expectation
