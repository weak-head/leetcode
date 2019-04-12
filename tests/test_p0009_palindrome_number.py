import pytest
from leetcode.p0009_palindrome_number import isPalindrome, isPalindrome_2


@pytest.mark.parametrize(('number', 'palindrome'), (
    (0, True),
    (5, True),
    (-5, False),

    (11, True),
    (12, False),

    (121, True),
    (123, False),

    (1221, True),
    (3303, False),
    (3033, False),

    (1234554321, True),
    (1234555321, False),

    (12345654321, True),
    (1234564321, False)
))
def test_isPalindrome(number, palindrome):
    assert isPalindrome(number) == palindrome
    assert isPalindrome_2(number) == palindrome