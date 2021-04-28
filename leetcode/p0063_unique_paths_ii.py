from typing import List


def uniquePathsWithObstacles(grid: List[List[int]]) -> int:
    """
    Dynamic programming

    Time: O(r * c)
    Space: O(r * c)
        r - number of rows
        c - number of columns
    """
    if not grid or not grid[0]:
        return 0

    if grid[0][0] == 1:
        return 0

    paths = [[0 for _ in range(len(grid[0]) + 1)] for _ in range(len(grid) + 1)]
    paths[1][1] = 1

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if row == 0 and col == 0:
                continue

            if grid[row][col] == 1:
                paths[row + 1][col + 1] = 0
            else:
                paths[row + 1][col + 1] = paths[row][col + 1] + paths[row + 1][col]

    return paths[-1][-1]
