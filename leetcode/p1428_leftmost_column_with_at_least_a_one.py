from typing import List


class BinaryMatrix(object):
    def __init__(self, mx):
        self._mx = mx

    def get(self, row: int, col: int) -> int:
        return self._mx[row][col]

    def dimensions(self) -> List[str]:
        return [len(self._mx[0]), len(self._mx)]


def leftMostColumnWithOne(binaryMatrix: "BinaryMatrix") -> int:
    rows, cols = binaryMatrix.dimensions()
    current_row, current_col = 0, cols - 1

    while current_row < rows and current_col >= 0:
        if binaryMatrix.get(current_row, current_col) == 0:
            current_row += 1
        else:
            current_col -= 1

    return current_col + 1 if current_col != cols - 1 else -1
