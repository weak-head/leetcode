import pytest
from leetcode.p0005_longest_palindromic_substring import longestPalindrome

@pytest.mark.parametrize(('input', 'expectation'), (
    ('', ''),
    ('abcd', 'a'),
    ('aba', 'aba'),
    ('abacaba', 'abacaba'),
    ('abacabad', 'abacaba'),
    ('dabacaba', 'abacaba'),
    ('abaccaba', 'abaccaba'),
    ('dabaccaba', 'abaccaba'),
    ('abaccabad', 'abaccaba')
))
def test_longest(input, expectation):
    assert longestPalindrome(input) ==  expectation