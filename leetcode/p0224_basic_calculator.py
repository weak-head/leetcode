from collections import deque


def calculate(s: str) -> int:
    """
    Time: O(n)
    Space: O(n)
    """

    def calc(s):

        num = 0
        sign = "+"
        stack = []

        while s:
            c = s.popleft()

            if c.isdigit():
                num = num * 10 + (ord(c) - ord("0"))

            if c == "(":
                num = calc(s)

            if (not c.isdigit() and c != " ") or not s:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                num = 0
                sign = c

            if c == ")":
                break

        return sum(stack)

    return calc(deque(s))
