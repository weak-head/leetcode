from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    """
    Search space reduction

    Time: O(r + c)
    Space: O(1)
        r - number of rows
        c - number of columns
    """

    row = len(matrix) - 1
    col = 0

    while row >= 0 and col < len(matrix[0]):
        val = matrix[row][col]
        if target == val:
            return True
        elif target > val:
            col += 1
        else:
            row -= 1

    return False
