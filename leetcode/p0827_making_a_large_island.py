from typing import List


def largestIsland(grid: List[List[int]]) -> int:
    """
    Time: O(n^2)
    Space: O(n^2)
        n - number of cells in the grid
    """

    groups = {}
    groups[0] = 0

    def neighbors(r, c):
        for xr, xc in ([0, 1], [0, -1], [1, 0], [-1, 0]):
            nr, nc = r + xr, c + xc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                yield nr, nc

    def dfs(r, c, group_id):
        area = 1
        grid[r][c] = group_id
        for nr, nc in neighbors(r, c):
            if grid[nr][nc] == 1:
                area += dfs(nr, nc, group_id)
        return area

    group_id = 2
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] != 0 and grid[r][c] not in groups:
                area = dfs(r, c, group_id)
                groups[group_id] = area
                group_id += 1

    max_area = max(groups.values() or [0])
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] != 0:
                continue
            adjacent = {grid[nr][nc] for nr, nc in neighbors(r, c)}
            max_area = max(max_area, 1 + sum(groups[gid] for gid in adjacent))

    return max_area
