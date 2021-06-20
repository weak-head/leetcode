from typing import List
import heapq


def swimInWater(grid: List[List[int]]) -> int:
    """
    Dijkstra shortest path.

    Time: O(n * log n)
    Space: O(n)
        n - number of cells in the grid
    """
    if not grid:
        return 0

    max_x, max_y = len(grid) - 1, len(grid[0]) - 1
    visited = set()
    q = [(grid[0][0], 0, 0)]

    while q:
        h, x, y = heapq.heappop(q)

        if x == max_x and y == max_y:
            return h

        if (x, y) in visited:
            continue

        visited.add((x, y))

        for cx, cy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = cx + x, cy + y
            if 0 <= nx <= max_x and 0 <= ny <= max_y and (nx, ny) not in visited:
                heapq.heappush(q, (max(h, grid[nx][ny]), nx, ny))

    return -1
