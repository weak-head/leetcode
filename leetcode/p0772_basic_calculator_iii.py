def calculate(s: str) -> int:
    """
    Time: O(n)
    Space: O(n)
    """
    if not s:
        return 0

    def precedence(c):
        if c in "+-":
            return 1
        if c in "*/":
            return 2
        return 0

    def operation(c, n2, n1):
        if c == "+":
            return n1 + n2
        if c == "-":
            return n1 - n2
        if c == "*":
            return n1 * n2
        if c == "/":
            return int(n1 // n2)

    ops, data, index, prev = [], [], 0, False
    while index < len(s):
        if s[index] == " ":
            index += 1
            continue

        # 0-9
        if s[index].isdigit():
            end = index + 1
            while end < len(s) and s[end].isdigit():
                end += 1

            data.append(int(s[index:end]))
            index = end
            prev = True

        # + - * /
        elif s[index] in "+-*/":
            # handle negative values, e.g. '-1'
            if not prev:
                data.append(0)

            while ops and precedence(ops[-1]) >= precedence(s[index]):
                data.append(operation(ops.pop(), data.pop(), data.pop()))
            ops.append(s[index])
            index += 1

        # (
        elif s[index] == "(":
            ops.append(s[index])
            index += 1
            prev = False

        # )
        else:
            while ops[-1] != "(":
                data.append(operation(ops.pop(), data.pop(), data.pop()))
            ops.pop()
            index += 1

    while ops:
        data.append(operation(ops.pop(), data.pop(), data.pop()))

    return data[-1]
