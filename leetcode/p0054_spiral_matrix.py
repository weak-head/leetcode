from typing import List


def spiral_order(matrix: List[List[int]]) -> List[int]:
    """
    Move layer-by-layer, appending the elements to the
    resulting list. O(n)
    """
    if not matrix or not matrix[0]:
        return []

    result = []
    top_row, bottom_row = 0, len(matrix) - 1
    left_column, right_column = 0, len(matrix[0]) - 1

    while top_row <= bottom_row and left_column <= right_column:
        for row, column in movement_path(
            top_row, left_column, bottom_row, right_column
        ):
            result.append(matrix[row][column])
        top_row += 1
        bottom_row -= 1
        left_column += 1
        right_column -= 1

    return result


def movement_path(top_row, left_column, bottom_row, right_column):

    # staying on the top row,
    # move from right to left column
    for x in range(left_column, right_column + 1):
        yield top_row, x

    # staying on the right column,
    # move from top to bottom row
    for y in range(top_row + 1, bottom_row + 1):
        yield y, right_column

    # Our path is not a straight line and we can follow
    # the complete rectangle
    if top_row < bottom_row and left_column < right_column:

        # staying on the borrom row,
        # move from left to right column
        for x in range(right_column - 1, left_column, -1):
            yield bottom_row, x

        # staying on the left column,
        # move from bottom to top row
        for y in range(bottom_row, top_row, -1):
            yield y, left_column
