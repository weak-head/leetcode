
def clumsy(N: int) -> int:
    n_clumsy, ix = 0, N
    while ix >= 1:
        n1 = ix if ix > 0 else 0
        n2 = ix - 1 if ix - 1 > 0 else 1
        n3 = ix - 2 if ix - 2 > 0 else 1
        n4 = ix - 3 if ix - 3 > 0 else 0
        if ix == N:
            n_clumsy = n1 * n2 // n3 + n4
        else:
            n_clumsy = n_clumsy - (n1 * n2 // n3) + n4
        ix = ix - 4
    return n_clumsy