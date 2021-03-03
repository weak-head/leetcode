from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    """
    Backtracking

    Time: O(r * c * (3 ** l))
    Space: O(l)
        r - number of rows
        c - number of cols
        l - length of the word
    """

    def track(r, c, path, ix):
        if board[r][c] != word[ix]:
            return False

        if ix == len(word) - 1:
            return True

        for (
            dr,
            dc,
        ) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nr, nc = r + dr, c + dc
            if (
                0 <= nr < len(board)
                and 0 <= nc < len(board[0])
                and (nr, nc) not in path
                and board[nr][nc] == word[ix + 1]
            ):
                path.add((nr, nc))
                if track(nr, nc, path, ix + 1):
                    return True
                path.remove((nr, nc))

        return False

    for r in range(len(board)):
        for c in range(len(board[0])):
            if track(r, c, set([(r, c)]), 0):
                return True

    return False
