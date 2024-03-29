from typing import List


def updateMatrix(matrix: List[List[int]]) -> List[List[int]]:
    """
    Dynamic programming

    Time: O(r * c)
    Space: O(r * c)
        r - rows
        c - columns
    """
    m = len(matrix)
    n = len(matrix and matrix[0])

    # first pass 0 -> n
    for i in range(m):
        for j in range(n):
            if matrix[i][j] != 0:
                matrix[i][j] = float("inf")

                # up
                if i > 0 and matrix[i - 1][j] + 1 < matrix[i][j]:
                    matrix[i][j] = matrix[i - 1][j] + 1

                # left
                if j > 0 and matrix[i][j - 1] + 1 < matrix[i][j]:
                    matrix[i][j] = matrix[i][j - 1] + 1

    # second pass n -> 0
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if matrix[i][j] != 0:

                # down
                if i + 1 < m and matrix[i + 1][j] + 1 < matrix[i][j]:
                    matrix[i][j] = matrix[i + 1][j] + 1

                # right
                if j + 1 < n and matrix[i][j + 1] + 1 < matrix[i][j]:
                    matrix[i][j] = matrix[i][j + 1] + 1

    return matrix
