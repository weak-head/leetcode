from typing import List


def evalRPN(tokens: List[str]) -> int:
    """
    Stack-based RPN evaluation

    Time: O(n)
    Space: O(n)
        n - number of elements
    """

    s = []
    for c in tokens:
        if c not in {"+", "-", "/", "*"}:
            s.append(int(c))
            continue

        v1 = s.pop()
        v2 = s.pop()

        if c == "+":
            s.append(v2 + v1)
        elif c == "-":
            s.append(v2 - v1)
        elif c == "*":
            s.append(v2 * v1)
        elif c == "/":
            s.append(int(v2 / v1))

    return s[0]
