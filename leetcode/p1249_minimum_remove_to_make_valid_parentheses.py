from collections import deque


def minRemoveToMakeValid_three_pass(s: str) -> str:
    """
    Time: O(n)
    Space: O(n)
        n - length of the string
    """

    # Accumulate indexes of parentheses that
    # are out of order and should be deleted
    d = deque()
    for i in range(len(s)):
        if s[i] == "(":
            d.append(("(", i))
        elif s[i] == ")":
            if len(d) == 0 or d[-1][0] != "(":
                d.append((")", i))
            else:
                d.pop()

    r = []
    d = set([i for _, i in d])
    for i, c in enumerate(s):
        if i in d:
            continue
        r.append(c)

    return "".join(r)


def minRemoveToMakeValid_two_pass(s: str) -> str:
    """
    Time: O(n)
    Space: O(n)
        n - length of the string
    """

    # Remove ')'
    first_pass_chars = []
    balance = 0
    open_seen = 0
    for c in s:
        if c == "(":
            balance += 1
            open_seen += 1
        elif c == ")":
            if balance == 0:
                continue  # drop
            balance -= 1
        first_pass_chars.append(c)

    # Remove '('
    result = []
    open_to_keep = open_seen - balance
    for c in first_pass_chars:
        if c == "(":
            open_to_keep -= 1
            if open_to_keep < 0:
                continue  # drop
        result.append(c)

    return "".join(result)
