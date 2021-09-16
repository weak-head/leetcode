from typing import List


def spiral_order(matrix: List[List[int]]) -> List[int]:
    """
    Move layer-by-layer, appending the elements to the
    resulting list.

    Time: O(n)
    Space: O(1)
    """

    def path(top_row, left_column, bottom_row, right_column):
        for column in range(left_column, right_column + 1):
            yield top_row, column

        for row in range(top_row + 1, bottom_row + 1):
            yield row, right_column

        if top_row < bottom_row and left_column < right_column:
            for column in range(right_column - 1, left_column, -1):
                yield bottom_row, column

            for row in range(bottom_row, top_row, -1):
                yield row, left_column

    top_row = 0
    left_column = 0
    bottom_row = len(matrix) - 1
    right_column = len(matrix[0]) - 1

    res = []

    while top_row <= bottom_row and left_column <= right_column:
        for x, y in path(top_row, left_column, bottom_row, right_column):
            res.append(matrix[x][y])

        top_row += 1
        bottom_row -= 1
        left_column += 1
        right_column -= 1

    return res
