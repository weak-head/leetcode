from typing import List
from collections import defaultdict, deque


def shortestDistance(grid: List[List[int]]) -> int:
    """
    pass
    """
    LAND, BUILDING = 0, 1

    def dfs(building, land):
        """
        Run DFS from cell that is 'building', to
        track distance to all pieces of reachable land.
        """

        # left, up, right, down
        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        seen = set()
        q = deque([(building[0], building[1], 0)])

        while q:
            row, col, d = q.popleft()

            for move in directions:
                new_row = row + move[0]
                new_col = col + move[1]

                # if cell is not visited yet and
                # not outside the grid
                if (
                    (0 <= new_row < len(grid))
                    and (0 <= new_col < len(grid[0]))
                    and (new_row, new_col) not in seen
                    and grid[new_row][new_col] == LAND
                ):
                    seen.add((new_row, new_col))
                    q.append((new_row, new_col, d + 1))
                    land[(new_row, new_col)].append(d + 1)

    # Map of buildings and land
    buildings = []
    land = defaultdict(list)

    # Track distance to each reachable cell of land
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == BUILDING:
                buildings.append((row, col))
                dfs((row, col), land)

    # Get the shortest distance
    shortest = float("inf")
    for distances in land.values():
        # The land should be reachable from every building
        if len(distances) == len(buildings):
            shortest = min(shortest, sum(distances))

    return shortest if shortest != float("inf") else -1
