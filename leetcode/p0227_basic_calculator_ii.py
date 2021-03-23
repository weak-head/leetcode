def calculate(s: str) -> int:

    stack = []
    num = 0
    sign = "+"

    for i in range(len(s)):

        if s[i].isdigit():
            num = num * 10 + int(s[i])

        if (not s[i].isdigit() and s[i] != " ") or i == len(s) - 1:
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
            sign = s[i]

    return sum(stack)
