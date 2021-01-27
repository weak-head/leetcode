import pytest
from leetcode.p0415_add_strings import addStrings


@pytest.mark.parametrize(
    ("a", "expectation"),
    (
        (("99", "99"), ("198")),
        (("0", "0"), ("0")),
        (("10", "0"), ("10")),
        (("110", "0"), ("110")),
        (("110", "1"), ("111")),
        (("999", "1"), ("1000")),
        (("9990", "1"), ("9991")),
    ),
)
def test_solve(a, expectation):
    assert addStrings(a[0], a[1]) == expectation
