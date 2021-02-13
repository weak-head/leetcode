import heapq
from typing import List


def shortestPathBinaryMatrix_a_star(grid: List[List[int]]) -> int:
    """
    A* with heuristic that yields better results
    than plain Dijkstra shortest path.

    Time: O(n * log n)
    Space: O(n)
        n - number of cells in the matrix
    """
    if grid[0][0] == 1:
        return -1

    max_x, max_y = len(grid) - 1, len(grid[0]) - 1

    def estimate(x, y, d):
        """
        A* heuristic
        """
        return max(max_x - x, max_y - y) + d

    visited = set()
    q = [(estimate(0, 0, 0), 1, 0, 0)]  # wight, distance, x, y
    while q:
        _, d, x, y = heapq.heappop(q)

        if x == max_x and y == max_y:
            return d

        if (x, y) in visited:
            continue

        visited.add((x, y))

        for cx, cy in [
            (0, 1),
            (1, 1),
            (1, 0),
            (1, -1),
            (0, -1),
            (-1, -1),
            (-1, 0),
            (-1, 1),
        ]:
            cx, cy = cx + x, cy + y
            if (
                0 <= cx <= max_x
                and 0 <= cy <= max_y
                and grid[cx][cy] == 0
                and (cx, cy) not in visited
            ):
                heapq.heappush(q, (estimate(cx, cy, d + 1), d + 1, cx, cy))

    return -1
