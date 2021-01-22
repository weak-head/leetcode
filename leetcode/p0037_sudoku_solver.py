from typing import List


def solveSudoku(board: List[List[str]]):
    return backtrack(board, 0, 0)


def backtrack(board, row, column):
    if row >= 9:
        return True

    if column >= 9:
        return backtrack(board, row + 1, 0)

    if board[row][column] == ".":
        for num in possible_nums(board, row, column):
            board[row][column] = num
            if backtrack(board, row, column + 1):
                return True
            else:
                board[row][column] = "."
    else:
        return backtrack(board, row, column + 1)

    return False


def possible_nums(board, row, column):
    all = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
    filled = set(board[row])

    for r in range(9):
        filled.add(board[r][column])

    r_rect, c_rect = (row // 3) * 3, (column // 3) * 3
    for rix in range(r_rect, r_rect + 3):
        for cix in range(c_rect, c_rect + 3):
            filled.add(board[rix][cix])

    return list(all - filled)
