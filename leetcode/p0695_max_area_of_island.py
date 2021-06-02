from typing import List


def maxAreaOfIsland(grid: List[List[int]]) -> int:
    """
    DFS

    Time: O(r * c)
    Space: O(r * c) # call stack
        r - number of rows
        c - number of columns
    """

    max_area = 0

    def area(r, c):
        if grid[r][c] != 1:
            return 0

        grid[r][c] = "#"

        m = 1
        for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + x, c + y
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                m += area(nr, nc)

        return m

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1:
                max_area = max(max_area, area(r, c))

    return max_area
