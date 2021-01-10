from typing import List


def numDistinctIslands(grid: List[List[int]]) -> int:
    """
    For the same islands we get the same path.
    O(r * c)
    """

    seen = set()
    paths = set()

    def dfs(path: [], r: int, c: int, d: int):
        """
        DFS walk from top left corner of a two identical
        islands would be the same
        """
        if (
            ((r, c) in seen)
            or not (0 <= r < len(grid))
            or not (0 <= c < len(grid[0]))
            or not grid[r][c]
        ):
            return

        seen.add((r, c))

        # forward
        path.append(d)

        dfs(path, r + 1, c, 1)  # down
        dfs(path, r - 1, c, 2)  # up
        dfs(path, r, c + 1, 3)  # right
        dfs(path, r, c - 1, 4)  # left

        # We need to track cases like this:
        #   110
        #   011
        #   000
        #   111
        #   010
        #
        # With backward movement we have:
        #   o -> right -> down -> right
        #   o -> right -> down -> back -> right
        #
        # Without tracking the backward movement
        #   o -> right -> down -> right
        #   o -> right -> down -> right
        #

        # back
        path.append(5)

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            path = []
            dfs(path, r, c, 0)
            if path:
                paths.add(tuple(path))

    return len(paths)
