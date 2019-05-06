from typing import List

def isValidSudoku(board: List[List[str]]) -> bool:
    return False

def backtrack(board, row, column):
    if row >= 9:
        return True
    