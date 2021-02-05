def longestValidParentheses_two_counters(s: str) -> int:
    """
    Two counters:
        - left brackets
        - right brackets

    Two scans:
        - Left to Right scan
        - Right to Left scan

    Reset both counters:
        - L-R: when right is bigger than left
        - R-L: when left is bigger than right

    Time: O(n)
    Space: O(1)
        n - length of the string
    """
    l = r = max_len = 0
    for i in range(len(s)):
        if s[i] == "(":
            l += 1
        else:
            r += 1

        if l == r:
            max_len = max(max_len, l * 2)
        elif r > l:
            l = r = 0

    l = r = 0
    for i in range(len(s) - 1, -1, -1):
        if s[i] == "(":
            l += 1
        else:
            r += 1

        if l == r:
            max_len = max(max_len, l * 2)
        elif l > r:
            l = r = 0

    return max_len


def longestValidParentheses_stack(s: str) -> int:
    """
    Use stack to keep track of opened parantheses

    Time: O(n)
    Space: O(n)
        n - length of the string
    """
    stack, max_len = [-1], 0

    for ix, c in enumerate(s):
        if c == "(":
            stack.append(ix)
        else:
            stack.pop()
            if len(stack) == 0:
                stack.append(ix)
            else:
                max_len = max(max_len, ix - stack[-1])

    return max_len


def longestValidParentheses_dp(s: str) -> int:
    """
    Dynamic Programming

    Extremely not obvious optimal substructure

    Time: O(n)
    Space: O(n)
        n - length of the string
    """
    max_len, m = 0, [0] * len(s)

    for i in range(1, len(s)):
        if s[i] == ")":
            # previous is "("
            if s[i - 1] == "(":
                m[i] = (m[i - 2] if i >= 2 else 0) + 2
            # previous is ")"
            elif i - m[i - 1] > 0 and s[i - m[i - 1] - 1] == "(":
                v = m[i - m[i - 1] - 2] if i - m[i - 1] >= 2 else 0
                m[i] = m[i - 1] + v + 2
            max_len = max(max_len, m[i])

    return max_len
