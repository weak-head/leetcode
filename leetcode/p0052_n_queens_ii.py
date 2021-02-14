def totalNQueens(n: int) -> int:
    """
    Backtracking

    Time: O(n!)
    Space: O(n)
        n - number of queens / grid side size
    """

    col = set()
    diag_1 = set()
    diag_2 = set()

    count = 0

    def can_place(r, c):
        return not (c in col or r - c in diag_1 or r + c in diag_2)

    def place_queen(r, c):
        nonlocal count
        col.add(c)
        diag_1.add(r - c)
        diag_2.add(r + c)
        if r == n - 1:
            count += 1

    def remove_queen(r, c):
        col.remove(c)
        diag_1.remove(r - c)
        diag_2.remove(r + c)

    def track(r):
        for c in range(n):
            if can_place(r, c):
                place_queen(r, c)
                track(r + 1)
                remove_queen(r, c)

    track(0)
    return count
