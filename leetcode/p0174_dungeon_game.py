from typing import List


def calculateMinimumHP(dungeon: List[List[int]]) -> int:
    """
    Time: O(r * c)
    Space: O(r * c)
        r - number of rows
        c - number of collumns
    """

    rows = len(dungeon)
    cols = len(dungeon[0])
    m = [[float("inf")] * cols for _ in range(rows)]

    def health(this_cell, next_row, next_col):
        if next_row >= rows or next_col >= cols:
            return float("inf")
        next_cell = m[next_row][next_col]
        return max(1, next_cell - this_cell)

    for row in reversed(range(rows)):
        for col in reversed(range(cols)):
            this_cell = dungeon[row][col]

            down = health(this_cell, row + 1, col)
            right = health(this_cell, row, col + 1)
            min_health = min(down, right)

            if min_health == float("inf"):
                min_health = 1 if this_cell >= 0 else (1 - this_cell)

            m[row][col] = min_health

    return m[0][0]
