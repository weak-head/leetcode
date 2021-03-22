from typing import List


def smallestCommonElement(mat: List[List[int]]) -> int:
    """
    Time: O(n^2)
    Space: O(n)
    """
    ix = [0] * len(mat)

    minv = float("-inf")
    while True:
        no_change = True
        for row in range(len(mat)):
            if ix[row] >= len(mat[row]):
                return -1

            if mat[row][ix[row]] == minv:
                continue
            elif mat[row][ix[row]] < minv:
                no_change = False
                ix[row] += 1
            else:
                no_change = False
                minv = mat[row][ix[row]]

        if no_change:
            return mat[0][ix[0]]
