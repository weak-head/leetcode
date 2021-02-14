from typing import List


def solveNQueens(n: int) -> List[List[str]]:
    """
    Backtracking

    Time: O(n!)
    Space: O(n)
        n - number of queens / grid side size
    """

    # Sets that identify locations of already placed queens
    col = set()
    diag_1 = set()  # left-up -> right-bottom (r - c = const)
    diag_2 = set()  # right-up -> left-bottom (r + c = const)

    res = []
    m = [["." for _ in range(n)] for _ in range(n)]

    def save():
        res.append(["".join(m[i]) for i in range(n)])

    def can_place(r, c):
        return not (c in col or r - c in diag_1 or r + c in diag_2)

    def place_queen(r, c):
        m[r][c] = "Q"
        col.add(c)
        diag_1.add(r - c)
        diag_2.add(r + c)
        if r == n - 1:
            save()

    def remove_queen(r, c):
        col.remove(c)
        diag_1.remove(r - c)
        diag_2.remove(r + c)
        m[r][c] = "."

    def track(r):
        for c in range(n):
            if can_place(r, c):
                place_queen(r, c)
                track(r + 1)
                remove_queen(r, c)

    track(0)
    return res
