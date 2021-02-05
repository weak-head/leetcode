def countAndSay(n: int) -> str:
    """
    Time: (2^n)
    Space: (2^n)
    """

    r = "1"
    for _ in range(n - 1):

        t, c, k = [], r[0], 0
        for v in r:
            if v == c:
                k += 1
            else:
                t.extend([k, c])
                c, k = v, 1

        t.extend([k, c])
        r = "".join(map(str, t))

    return r
