from typing import List


def solve_dfs(board: List[List[str]]) -> None:
    """
    DFS from each border cell
    Replace all connected O => #
    Replace all other O => X
    Replace all # to O

    Time: O(r * c)
    Space: O(r * c) -> stack
        r - number of rows
        c - number of cols
    """

    def dfs(x, y):
        if board[x][y] != "O":
            return

        board[x][y] = "#"

        for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
                dfs(nx, ny)

    for x in range(len(board)):
        dfs(x, 0)
        dfs(x, len(board[0]) - 1)

    for y in range(len(board[0])):
        dfs(0, y)
        dfs(len(board) - 1, y)

    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y] == "O":
                board[x][y] = "X"

    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y] == "#":
                board[x][y] = "O"


def solve_union_find(board: List[List[str]]) -> None:
    """
    Union-find

    Not as efficient as BSF or DFC,
    but very interesting and beautiful

    Time: O(r * c)
    Space: O(r * c) # parent & rank
        r - number of rows
        c - number of columns
    """
    xc = len(board)
    yc = len(board[0])
    parent = [i for i in range((xc * yc) + 1)]
    rank = [0] * ((xc * yc) + 1)
    dummy = xc * yc

    def ix(x, y):
        return x * yc + y

    def find(a):
        if a != parent[a]:
            parent[a] = find(parent[a])
        return parent[a]

    def union(a, b):
        ap, bp = find(a), find(b)
        if rank[ap] < rank[bp]:
            parent[ap] = bp
        else:
            parent[bp] = ap
            if rank[bp] == rank[ap]:
                rank[ap] += 1

    def connected(a, b):
        return find(a) == find(b)

    for x in range(xc):
        if board[x][0] == "O":
            union(dummy, ix(x, 0))
        if board[x][yc - 1] == "O":
            union(dummy, ix(x, yc - 1))

    for y in range(yc):
        if board[0][y] == "O":
            union(dummy, ix(0, y))
        if board[xc - 1][y] == "O":
            union(dummy, ix(xc - 1, y))

    for x in range(1, xc - 1):
        for y in range(1, yc - 1):
            if board[x][y] == "O":
                for xd, yd in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    if board[x + xd][y + yd] == "O":
                        union(ix(x, y), ix(x + xd, y + yd))

    for x in range(1, xc - 1):
        for y in range(1, yc - 1):
            if not connected(ix(x, y), dummy):
                board[x][y] = "X"
