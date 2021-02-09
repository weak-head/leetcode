from typing import List


def numIslands(grid: List[List[str]]) -> int:
    """
    DFS to cover the new island

    Time: O(r * c)
    Space: O(r * c)
        r - number of rows
        c - number of columns
    """
    islands = 0
    seen = set()

    def walk(r, c):
        seen.add((r, c))

        for rx, cx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = r + rx, c + cx
            if (
                0 <= nr < len(grid)
                and 0 <= nc < len(grid[0])
                and (nr, nc) not in seen
                and grid[nr][nc] == "1"
            ):
                walk(nr, nc)

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if (r, c) not in seen and grid[r][c] == "1":
                islands += 1
                walk(r, c)

    return islands


def numIslands2(grid: List[List[str]]) -> int:
    """
    DFS to cover the new island
    and change "1" to "0"

    Time: O(r * c)
    Space: O(max(r, c))  # call stack
        r - number of rows
        c - number of columns
    """
    islands = 0

    def walk(r, c):
        grid[r][c] = "0"

        for rx, cx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = r + rx, c + cx
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == "1":
                walk(nr, nc)

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "1":
                islands += 1
                walk(r, c)

    return islands
