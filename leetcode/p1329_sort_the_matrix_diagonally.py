from typing import List
from collections import defaultdict


def diagonalSort1(mat: List[List[int]]) -> List[List[int]]:
    """
    Accumulate diagonals into separate lists,
    sort them by some type of quick sort,
    and populate back

    Time: O( (r+c) * n * log(n) )
        r - number of rows
        c - number of cols
        n - number of elements in longest diagonal

    Space: O(m)
        m - number of elements in the matrix

    """
    m, n = len(mat), len(mat[0])
    table = defaultdict(list)

    for row in range(m):
        for col in range(n):
            table[col - row].append(mat[row][col])

    for k in table:
        table[k].sort()

    for row in range(m):
        for col in range(n):
            mat[row][col] = table[col - row].pop(0)

    return mat


def diagonalSort2(mat: List[List[int]]) -> List[List[int]]:
    """"""

    def sort(row, col, mat):
        """
        O(n^2)
        n - min between row_num and col_num
        """
        nrow, ncol = len(mat), len(mat[0])
        i = 0
        while True:
            j = i + 1

            while True:
                if row + j >= nrow or col + j >= ncol:
                    break

                if mat[row + i][col + i] > mat[row + j][col + j]:
                    mat[row + i][col + i], mat[row + j][col + j] = (
                        mat[row + j][col + j],
                        mat[row + i][col + i],
                    )

                j += 1

            i += 1
            if row + i >= nrow or col + i >= ncol:
                break

    # O( row_count * O(min(row_count, col_count) ^ 2) )
    for row in range(len(mat)):
        sort(row, 0, mat)

    # O( col_count * O(min(row_count, col_count) ^ 2) )
    for col in range(len(mat[0])):
        sort(0, col, mat)

    return mat
