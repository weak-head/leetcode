import pytest
from leetcode.p0008_string_to_integer_atoi import atoi


@pytest.mark.parametrize(
    ("s", "i"),
    (
        ("", 0),
        ("   37", 37),
        ("   +37", 37),
        ("   -37", -37),
        ("   \t42", 0),
        ("db 44 2", 0),
        ("  -db", 0),
        ("-32db", -32),
        (" -32 db", -32),
        ("-91283472332", -2147483648),
    ),
)
def test_atoi(s, i):
    assert atoi(s) == i
