import pytest
from leetcode.p0006_zigzag_conversion import convert, convert2


@pytest.mark.parametrize(
    ("s", "numRows", "expectation"),
    (
        ("", 10, ""),
        ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
        ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
        ("PAYPALISHIRING", 99, "PAYPALISHIRING"),
        ("PAYPALISHIRING", 1, "PAYPALISHIRING"),
        ("PAYPALISHIRING", 2, "PYAIHRNAPLSIIG"),
    ),
)
def test_convert(s, numRows, expectation):
    assert convert(s, numRows) == expectation
    assert convert2(s, numRows) == expectation
