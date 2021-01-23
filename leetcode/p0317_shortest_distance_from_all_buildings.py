from typing import List
from collections import defaultdict, deque


def shortestDistance(grid: List[List[int]]) -> int:
    """
    BFS from each building, one by one, tracking land to each land

    Time: O(n * l)
    Space: O(n * l)
        n - number of buildings
        l - number of land cells
    """
    LAND, BUILDING = 0, 1

    def bfs(building, land):
        """
        Run BFS from the cell that is 'building', to
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
    land = defaultdict(list)  # cell: [distance]

    # Track distance to each reachable cell of the land
    # from each building
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == BUILDING:
                buildings.append((row, col))
                bfs((row, col), land)

    # Get the shortest distance
    shortest = float("inf")
    for distances in land.values():
        # The land should be reachable from every building
        if len(distances) == len(buildings):
            shortest = min(shortest, sum(distances))

    return shortest if shortest != float("inf") else -1
