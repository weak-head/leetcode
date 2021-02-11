from typing import List


def maximalSquare_dp_optimized(matrix: List[List[str]]) -> int:
    """
    Dynamic Programming, optimized for space

    Time: O(r * c)
    Space: O(r)
        r - number of rows
        c - number of columns
    """
    r = [0 for _ in range(len(matrix[0]) + 1)]

    # for r[i]:
    #  - r[i-1]   -> left
    #  - r[i]     -> up
    #  - diagonal -> diagonal
    diagonal = 0
    max_side = 0
    for row in range(1, len(matrix) + 1):
        for col in range(1, len(matrix[0]) + 1):
            temp = r[col]

            if matrix[row - 1][col - 1] == "0":
                r[col] = 0
            else:
                r[col] = min(r[col - 1], r[col], diagonal) + 1
                max_side = max(max_side, r[col])

            diagonal = temp

    return max_side * max_side


def maximalSquare_dp(matrix: List[List[str]]) -> int:
    """
    Dynamic Programming

    Optimal substructure:
        a b
        c d
            > d = min(a, b, c) + 1

    Time: O(r * c)
    Space: O(r * c)
        r - number of rows
        c - number of columns
    """
    m = [[0 for _ in range(len(matrix[0]) + 1)] for _ in range(len(matrix) + 1)]

    max_side = 0
    for row in range(1, len(m)):
        for col in range(1, len(m[0])):
            if matrix[row - 1][col - 1] == "0":
                continue

            m[row][col] = min(m[row - 1][col], m[row][col - 1], m[row - 1][col - 1]) + 1
            max_side = max(max_side, m[row][col])

    return max_side * max_side
