from typing import List


def numDistinctIslands(grid: List[List[int]]) -> int:
    """
    For the same islands we get the same path.

    Time: O(r * c)
    Space: O(r * c)
        r - number of rows
        c - number of cols
    """
    moves = {"D": (1, 0), "L": (0, -1), "U": (-1, 0), "R": (0, 1)}

    def walk(r, c, path, visited):
        """
        DFS walk from the top left corner
        of the two identical islands would be the same
        """
        visited.add((r, c))

        for move, (rx, cx) in moves.items():
            nr, nc = r + rx, c + cx
            if (
                0 <= nr < len(grid)
                and 0 <= nc < len(grid[nr])
                and (nr, nc) not in visited
                and grid[nr][nc]
            ):
                path.append(move)
                walk(nr, nc, path, visited)

                # We need to track cases like this:
                #   110
                #   011
                #   000
                #   111
                #   010
                #
                # With backward movement we have:
                #   R -> D -> R
                #   R -> D -> B -> R
                #
                # Without tracking the backward movement
                #   R -> D -> R
                #   R -> D -> R
                #
                path.append("B")  # back

    visited = set()  # cells
    islands = set()
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] and (r, c) not in visited:
                path = []
                walk(r, c, path, visited)
                islands.add("".join(path))

    return len(islands)
