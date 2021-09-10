from collections import Counter
from typing import List


def numberOfArithmeticSlices(A: List[int]) -> int:
    """
    Dynamicall Programming

    Time: O(n^2)
    Space: O(n^2)
    """

    total = 0
    n = len(A)
    m = [Counter() for _ in A]

    for i in range(n):
        for j in range(i):
            diff = A[i] - A[j]
            m[i][diff] += m[j][diff] + 1
            total += m[j][diff]

    return total
