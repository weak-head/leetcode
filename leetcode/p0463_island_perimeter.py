from typing import List


def islandPerimeter_better_counting(grid: List[List[int]]) -> int:
    """
    More advanced and improved counting

    Time: (r * c)
    Space: O(1)
        r - number of rows
        c - number of cols
    """
    rows = len(grid)
    cols = len(grid[0])

    result = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                result += 4

                if r > 0 and grid[r - 1][c] == 1:
                    result -= 2

                if c > 0 and grid[r][c - 1] == 1:
                    result -= 2

    return result


def islandPerimeter_counting(grid: List[List[int]]) -> int:
    """
    Naive counting

    Time: (r * c)
    Space: O(1)
        r - number of rows
        c - number of cols
    """

    perimeter = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1:
                if r == 0:
                    up = 0
                else:
                    up = grid[r - 1][c]

                if c == 0:
                    left = 0
                else:
                    left = grid[r][c - 1]

                if r == len(grid) - 1:
                    down = 0
                else:
                    down = grid[r + 1][c]

                if c == len(grid[0]) - 1:
                    right = 0
                else:
                    right = grid[r][c + 1]

                perimeter += 4 - (up + down + left + right)

    return perimeter


def islandPerimeter_dfs(grid: List[List[int]]) -> int:
    """
    DFS, slow and not efficient

    Time: O(r * c)
    Space: O(r * c)
        r - number of rows
        c - number of columns
    """
    seen = set()
    perim = 0

    def is_water(r, c):
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
            return True
        return grid[r][c] == 0

    def dfs(r, c):
        nonlocal perim
        for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            nr, nc = r + dr, c + dc
            if is_water(nr, nc):
                perim += 1
            elif not is_water(nr, nc) and (nr, nc) not in seen:
                seen.add((nr, nc))
                dfs(nr, nc)

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1:
                seen.add((r, c))
                dfs(r, c)
                return perim

    return 0
