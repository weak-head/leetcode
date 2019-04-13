import pytest
from leetcode.p0013_roman_to_integer import romanToInt

@pytest.mark.parametrize(('roman', 'integer'), (
    ('I', 1),
    ('IV', 4),
    ('VII', 7),
    ('IIX', 8),
    ('XVII', 17),
    ('IVIV', 8)
))
def test_romanToInt(roman, integer):
    assert romanToInt(roman) == integer