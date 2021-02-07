from typing import List


def shortestToChar(s, c):
    """
    Two passes:
        - Left to Right
        - Right to Left

    Time: O(n)
    Space: O(n)
    """
    v = [float("-inf")] * len(s)
    p = float("-inf")
    for i in range(len(s)):
        if s[i] == c:
            p = i
        v[i] = i - p

    p = float("inf")
    for i in range(len(s) - 1, -1, -1):
        if s[i] == c:
            p = i
        v[i] = min(v[i], p - i)

    return v


def shortestToChar2(s: str, c: str) -> List[int]:
    """
    Single pass, with adjusting left side

    Time: O(n)
    Space: O(n)
    """

    def adjust(l, r, s, v, c):
        for j in range(l + 1, r):
            if l > -1 and s[l] == c:
                v[j] = min(v[j], j - l)
            if r < len(s) and s[r] == c:
                v[j] = min(v[j], r - j)

    p = -1
    v = [float("inf")] * len(s)
    for i in range(len(s)):
        if s[i] == c:
            v[i] = 0
            adjust(p, i, s, v, c)
            p = i

    if s[-1] != c:
        adjust(p, len(s), s, v, c)

    return v
