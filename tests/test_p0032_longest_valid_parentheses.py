import pytest
from leetcode.p0032_longest_valid_parentheses import (
    longestValidParentheses,
    longestValidParentheses2,
)


@pytest.mark.parametrize(
    ("s", "length"),
    (
        ("", 0),
        ("(()", 2),
        (")))(((", 0),
        ("()()()", 6),
        ("(()()())", 8),
        ("()())()()()", 6),
        (")((()))())(())", 8),
        (")((()))())((((()))))", 10),
        ("()(()", 2),
        ("()((())", 4),
        ("(()(((()", 2),
    ),
)
def test_longestValidPar(s, length):
    assert longestValidParentheses(s) == length
    assert longestValidParentheses2(s) == length
