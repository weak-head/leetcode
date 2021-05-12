from typing import List


class NumMatrix:
    """
    Pre-compute (0,0)-based sums for all possible rectangles

    ----------------------------
    | O
    |
    |
    |      A --- B
    |      |     |
    |      |     |
    |      C --- D
    |

    Get the sum of (ABCD) in O(1) using the following formula:
        > Sum(ABCD) = Sum(OD) − Sum(OB) − Sum(OC) + Sum(OA)
    """

    def __init__(self, matrix: List[List[int]]):
        """
        Time: O(m * n)
        """
        self.m = matrix
        self.sums = [
            [0 for _ in range(len(matrix[0]) + 1)] for _ in range(len(matrix) + 1)
        ]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                self.sums[row + 1][col + 1] = (
                    self.sums[row + 1][col]
                    + self.sums[row][col + 1]
                    + matrix[row][col]
                    - self.sums[row][col]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        """
        Time: O(1)
        """
        return (
            self.sums[row2 + 1][col2 + 1]
            - self.sums[row1][col2 + 1]
            - self.sums[row2 + 1][col1]
            + self.sums[row1][col1]
        )


class NumMatrixBF:
    """
    Brute-force,

    Time: O(r * c)
    Space: O(1)
        r - number of rows
        c - number of cols
    """

    def __init__(self, matrix: List[List[int]]):
        self.m = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        s = 0
        for r in range(row1, row2 + 1):
            s += sum(self.m[r][col1 : col2 + 1])
        return s
