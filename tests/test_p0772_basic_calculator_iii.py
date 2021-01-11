import pytest
from leetcode.p0772_basic_calculator_iii import calculate1, calculate2


@pytest.mark.parametrize(
    ("a", "expectation"),
    (
        ("7+3", 10),
        ("-7+3", -4),
        ("(-7)+3", -4),
        ("(-7 + 3) * (-2)", 8),
        ("(-7 + 3) * (-2 + 4)", -8),
        ("(-7 + 3) / (-2 + 4)", -2),
        ("(2+6*3+5-(3*14/7+2)*5)+3", -12),
        ("((2+((6*3))+5)-(3*14/7+2)*5)+3", -12),
    ),
)
def test_calculate(a, expectation):
    assert calculate1(a) == expectation
    assert calculate2(a) == expectation
