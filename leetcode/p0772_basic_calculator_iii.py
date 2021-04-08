from collections import deque


def calculate(s: str) -> int:
    """
    Time: O(n)
    Space: O(n)
        n - length of the string
    """

    def calc(s):

        num = 0
        sign = "+"
        stack = []

        while s:
            c = s.popleft()

            if c.isdigit():
                num = num * 10 + int(c)

            if c == "(":
                num = calc(s)

            if (not c.isdigit() and c != " ") or not s:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    pre = stack.pop()
                    stack.append(pre * num)
                elif sign == "/":
                    pre = stack.pop()
                    stack.append(int(pre / num))
                num = 0
                sign = c

            if c == ")":
                break

        return sum(stack)

    return calc(deque(s))
