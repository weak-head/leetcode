from typing import List


def minimumTotal(triangle: List[List[int]]) -> int:
    """
    Compute paths using dynamic programming

    Time: O(n)
    Space: O(r)
        n - number of elements in the triangle
        r - number of rows in the triangle
    """
    prev = triangle[0]
    for row in range(1, len(triangle)):
        this = list(triangle[row])
        this[0] += prev[0]
        this[-1] += prev[-1]
        for i in range(1, len(this) - 1):
            this[i] += min(prev[i], prev[i - 1])
        prev = this
    return min(prev)
