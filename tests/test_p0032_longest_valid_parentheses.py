import pytest
from leetcode.p0032_longest_valid_parentheses import (
    longestValidParentheses_stack,
    longestValidParentheses_dp,
    longestValidParentheses_two_counters,
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
    assert longestValidParentheses_stack(s) == length
    assert longestValidParentheses_dp(s) == length
    assert longestValidParentheses_two_counters(s) == length
