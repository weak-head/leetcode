from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    """
    Binary search

    Time: O(log (r * c))
    Space: O(1)
        r - number of rows
        c - number of columns
    """

    def n(rc):
        r, c = rc
        k = len(matrix[0])
        return (r * k) + c

    def rc(n):
        k = len(matrix[0])
        return (n // k, n % k)

    l = (0, 0)
    r = (len(matrix) - 1, len(matrix[0]) - 1)
    ln, rn = n(l), n(r)

    while ln <= rn:
        mn = (ln + rn) >> 1
        m = rc(mn)

        if matrix[m[0]][m[1]] == target:
            return True
        elif matrix[m[0]][m[1]] < target:
            ln = mn + 1
        else:
            rn = mn - 1

    return False
