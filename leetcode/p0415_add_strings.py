from collections import deque


def addStrings(num1: str, num2: str) -> str:
    """
    Time: O(n)
    Space: O(n)
        n - max length of the string
    """
    if len(num2) > len(num1):
        num1, num2 = num2, num1

    r = deque()
    zord = ord("0")
    c, ix = 0, 1
    while ix <= len(num1):
        n1 = ord(num1[-ix]) - zord
        n2 = ord(num2[-ix]) - zord if ix <= len(num2) else 0
        v = (n1 + n2 + c) % 10
        c = (n1 + n2 + c) // 10
        r.appendleft(chr(v + zord))
        ix += 1

    if c:
        r.appendleft(chr(c + zord))

    return "".join(r)
