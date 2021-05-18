from functools import lru_cache


def minKnightMoves_dfs_dp(x: int, y: int) -> int:
    """
    DFS, DP

    Move from abs(x, y) to (0, 0)

    Time: O(log(max(|x|, |y|)))
    Space: O(log(max(|x|, |y|)))
        x - x coord
        y - y coord
    """

    @lru_cache(None)
    def move(x, y):
        # x == 0 and y == 0
        if x + y == 0:
            return 0

        # (x == 0 and y == 2) or (x == 1 and y == 1) or (x == 2 and y == 0)
        elif x + y == 2:
            return 2

        else:
            a = move(abs(x - 1), abs(y - 2))
            b = move(abs(x - 2), abs(y - 1))
            return 1 + min(a, b)

    return move(abs(x), abs(y))


def minKnightMoves_math(x: int, y: int) -> int:
    """
    Math formula
    O(1)
    """
    x, y = abs(x), abs(y)

    if x < y:
        x, y = y, x

    if x == 1 and y == 0:
        return 3

    if x == 2 and y == 2:
        return 4

    delta = x - y

    if y > delta:
        return delta - 2 * int((delta - y) // 3)
    else:
        return delta - 2 * int((delta - y) // 4)
