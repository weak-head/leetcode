def scoreOfParentheses(s: str) -> int:
    """
    Only "()" creates a value,
    all other parentheses around it
    defines the depth of the "()".

    The depth increases the value by power of two.
      "()"     => 1 * (2^0) == 1 << 0
      "(())"   => 1 * (2^1) == 1 << 1
      "((()))" => 1 * (2^2) == 1 << 2
      "(()())" => 1 * (2^1) + 1 * (2^1) == (1 << 1) + (1 << 1)

    So we have to track the current depth,
    and when we face closed pair "()",
    we have to accumulate the shifted value.

    Time: O(n)
    Space: O(1)
        n - length of the string
    """
    score = depth = 0
    for i in range(len(s)):
        if s[i] == "(":
            depth += 1
        else:
            depth -= 1
            if s[i - 1] == "(":  # "()" case
                score += 1 << depth

    return score
