from typing import List


def isValidSudoku(board: List[List[str]]) -> bool:

    # all rows are valid
    for row in range(9):
        s = set()
        for col in range(9):
            v = board[row][col]
            if v != ".":
                if v in s:
                    return False
                else:
                    s.add(v)

    # all columns are valid
    for col in range(9):
        s = set()
        for row in range(9):
            v = board[row][col]
            if v != ".":
                if v in s:
                    return False
                else:
                    s.add(v)

    # all rectangles are valid
    for row in range(3):
        for col in range(3):
            s = set()
            for rix in range(3):
                for cix in range(3):
                    v = board[row * 3 + rix][col * 3 + cix]
                    if v != ".":
                        if v in s:
                            return False
                        else:
                            s.add(v)

    return True
