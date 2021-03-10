def minDistance_optimized(a, b):
    """
    Dynamic Programming, optimized

    Time: (a * b)
    Space: (min(a, b))
        a - len of 'a'
        b - len of 'b'
    """
    if len(a) < len(b):
        a, b = b, a

    pre = list(range(len(b) + 1))
    cur = [0] * (len(b) + 1)

    for r in range(1, len(a) + 1):
        cur[0] = r
        for c in range(1, len(b) + 1):
            if a[r - 1] == b[c - 1]:
                cur[c] = pre[c - 1]
            else:
                cur[c] = 1 + min(cur[c - 1], pre[c - 1], pre[c])
        cur, pre = pre, cur

    return pre[-1]


def minDistance(a: str, b: str) -> int:
    """
    Dynamic Programming, bottom-up

    Not optimized for space

    Time: (a * b)
    Space: (a * b)
        a - length of 'a'
        b - length of 'b'
    """
    m = [[0 for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]

    for i in range(len(a) + 1):
        m[i][0] = i

    for i in range(len(b) + 1):
        m[0][i] = i

    for r in range(1, len(a) + 1):
        for c in range(1, len(b) + 1):
            if a[r - 1] == b[c - 1]:
                m[r][c] = m[r - 1][c - 1]
            else:
                m[r][c] = 1 + min(m[r - 1][c], m[r][c - 1], m[r - 1][c - 1])

    return m[-1][-1]
