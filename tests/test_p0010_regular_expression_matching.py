import pytest
from leetcode.p0010_regular_expression_matching import isMatch

@pytest.mark.timeout(10)
@pytest.mark.parametrize(('string', 'pattern', 'match'), (
    ('aaa', 'aaa', True),
    ('aaa', 'a*', True),

    ('aaa', 'aaaa', False),
    ('aaaa', 'aaa', False),

    ('', '.*', True),
    ('', 'a*', True),

    ('abc', 'c*d*abb*cc*', True),
    ('abc', 'c*d*a.b*cc*', True),
    ('abcde', 'c*d*a.c.*', True),
    ('abcde', 'c*d*a.b.*', False),
    ('abc', '.*', True),

    ('', '', True),
    ('abc', '', False),
    ('', 'abc', False),
    ('', 'a*b*c*', True),

    ('abcde', '.....', True),
    ('abcdef', '.....', False),
    ('abcd', '.....', False),

    ('bbbbba', '.*a*a', True),

    #("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c", False)
))
def test_isMatch(string, pattern, match):
    assert isMatch(string, pattern) == match