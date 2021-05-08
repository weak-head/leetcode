from math import sqrt


def superpalindromesInRange(L, R):
    """
    Math magic
    """
    L, R = int(L), int(R)

    left = len(str(int(sqrt(L))))
    right = len(str(int(sqrt(R))))

    n1 = (left - 1) // 2 + 1
    n2 = (right - 1) // 2 + 1

    l = 10 ** (n1 - 1)
    r = 10 ** n2

    res = 0
    for i in range(l, r):
        x = str(i)
        even = int(x + x[::-1])
        odd = int(x + x[-2::-1])

        for n in (even, odd):
            sq = n * n
            ss = str(sq)
            if ss == ss[::-1] and L <= sq <= R:
                res += 1

    return res
