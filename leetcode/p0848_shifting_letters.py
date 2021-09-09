from typing import List


def shiftingLetters(s: str, shifts: List[int]) -> str:
    """
    Prefix sum

    Time: O(n)
    Space: O(n)
    """

    for i in range(len(shifts) - 2, -1, -1):
        shifts[i] += shifts[i + 1]

    r = []
    for i, c in enumerate(s):
        val = (ord(c) - ord("a") + shifts[i]) % 26
        nc = chr(val + ord("a"))
        r.append(nc)

    return "".join(r)
