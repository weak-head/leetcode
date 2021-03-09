from functools import lru_cache


def lcs_bu_optimized(a, b):
    """
    Dynamic Programming, bottom-up

    Optimized for space

    Time: O(a * b)
    Space: O(min(a, b))
        a - length of 'a'
        b - length of 'b'
    """
    if a < b:
        a, b = b, a

    pre = [0] * (len(b) + 1)
    cur = [0] * (len(b) + 1)

    for r in range(1, len(a) + 1):
        for c in range(1, len(b) + 1):
            if a[r - 1] == b[c - 1]:
                cur[c] = pre[c - 1] + 1
            else:
                cur[c] = max(pre[c], cur[c - 1])
        pre, cur = cur, pre

    return pre[-1]


def lcs_bu(a, b):
    """
    Dynamic Programming, bottom-up

    Could be optimized for space
    Time: (a * b)
    Space: (a * b)
        a - length of 'a'
        b - length of 'b'
    """
    m = [[0 for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]

    for r in range(1, len(a) + 1):
        for c in range(1, len(b) + 1):
            if a[r - 1] == b[c - 1]:
                m[r][c] = m[r - 1][c - 1] + 1
            else:
                m[r][c] = max(m[r][c - 1], m[r - 1][c])

    return m[-1][-1]


def lcs_td(a, b):
    """
    Dynamic programming, top-down

    Time: (a * b)
    Space: (a * b)
        a - length of 'a'
        b - length of 'b'
    """

    @lru_cache(None)
    def lcs(a, b):
        if not a or not b:
            return 0

        if a[-1] == b[-1]:
            return 1 + lcs(a[:-1], b[:-1])
        else:
            return max(lcs(a, b[:-1]), lcs(a[:-1], b))

    return lcs(a, b)
