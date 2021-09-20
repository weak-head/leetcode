from typing import List


def tictactoe(moves: List[List[int]]) -> str:
    """
    Time: O(1)
    Space: O(1)
    """

    r = [0, 0, 0]
    c = [0, 0, 0]
    d1 = d2 = 0
    p = 1

    for x, y in moves:
        r[x] += p
        c[y] += p

        if x == y:
            d1 += p

        if x == 2 - y:
            d2 += p

        if 3 in {abs(r[x]), abs(c[y]), abs(d1), abs(d2)}:
            return "A" if p > 0 else "B"

        p = -p

    if len(moves) < 9:
        return "Pending"

    return "Draw"
