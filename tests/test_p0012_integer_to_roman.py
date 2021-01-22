import pytest
from leetcode.p0012_integer_to_roman import intToRoman


@pytest.mark.parametrize(
    ("integer", "roman"),
    ((4, "IV"), (123, "CXXIII"), (1994, "MCMXCIV"), (999, "CMXCIX"), (2019, "MMXIX")),
)
def test_intToRoman(integer, roman):
    assert intToRoman(integer) == roman
