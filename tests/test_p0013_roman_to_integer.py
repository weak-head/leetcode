import pytest
from leetcode.p0013_roman_to_integer import romanToInt

@pytest.mark.parametrize(('roman', 'integer'), (
    ('I', 1),
    ('IV', 4),
    ('VII', 7),
    ('IIX', 8),
    ('XVII', 17),
    ('IVIV', 8),
    ('XC', 90),
    ('MD', 1500),
    ('MC', 1100),
    ('CM', 900),
    ('MDCLXVI', 1666)
))
def test_romanToInt(roman, integer):
    assert romanToInt(roman) == integer


@pytest.mark.parametrize('roman', (
    'ABC',
    '!@#',
    'QWE'
))
def test_romanToInt_invalid(roman):
    with pytest.raises(Exception) as ex:
        romanToInt(roman)
