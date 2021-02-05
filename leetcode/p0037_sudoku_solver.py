from typing import List


def solveSudoku(board: List[List[str]]) -> None:
    """
    Time: O(9! ^ 9) = O(1)
    Space: O(9 * 9) = O(1)
    """

    def candidates(row, col):
        ca = set("123456789")
        for i in range(9):
            if board[i][col] in ca:
                ca.remove(board[i][col])
            if board[row][i] in ca:
                ca.remove(board[row][i])

        br, bc = (row // 3) * 3, (col // 3) * 3
        for r in range(br, br + 3):
            for c in range(bc, bc + 3):
                if board[r][c] in ca:
                    ca.remove(board[r][c])
        return ca

    def backtrack(row, col):
        if row > 8:
            return True

        if col > 8:
            return backtrack(row + 1, 0)

        if board[row][col] != ".":
            return backtrack(row, col + 1)
        else:
            v = board[row][col]
            for candidate in candidates(row, col):
                board[row][col] = candidate
                if backtrack(row, col + 1):
                    return True
            board[row][col] = v

        return False

    return backtrack(0, 0)
