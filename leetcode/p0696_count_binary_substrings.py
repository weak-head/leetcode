def countBinarySubstrings(s: str) -> int:
    """
    Time: O(n)
    Space: O(1)
        n - length of the string
    """
    a = b = 0
    cnt, cur = 0, None

    for c in s:
        if cur != c:
            cur = c
            a, b = b, 1
        else:
            b += 1

        if a >= b:
            cnt += 1
    return cnt
