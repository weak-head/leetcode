from typing import List


def minPathSum(grid: List[List[int]]) -> int:
    """
    Dynamic Programming

    Time: O(r * c)
        r - number of rows
        c - number of columns

    Space: O(1)
    """

    for row in range(1, len(grid)):
        grid[row][0] += grid[row - 1][0]

    for col in range(1, len(grid[0])):
        grid[0][col] += grid[0][col - 1]

    for col in range(1, len(grid[0])):
        for row in range(1, len(grid)):
            grid[row][col] += min(grid[row - 1][col], grid[row][col - 1])

    return grid[-1][-1]
