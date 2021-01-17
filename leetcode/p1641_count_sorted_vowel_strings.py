def countVowelStrings(n: int) -> int:
    """
    Dynamic Programming

    O(n)
    """
    rlen, clen = 5, n
    count = [[0 for _ in range(clen)] for _ in range(rlen)]

    for c in range(clen):
        count[0][c] = 1

    for r in range(rlen):
        count[r][0] = r + 1

    for c in range(1, clen):
        for r in range(1, rlen):
            count[r][c] = count[r - 1][c] + count[r][c - 1]

    return count[rlen - 1][clen - 1]
