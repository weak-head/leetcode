from collections import Counter
from typing import List


def findLHS(nums: List[int]) -> int:
    """
    Time: O(n)
    Space: O(n)
        n - number of elements in the list
    """
    c, l = Counter(nums), 0
    for k, v in c.items():
        if k - 1 in c:
            l = max(l, v + c[k - 1])
        if k + 1 in c:
            l = max(l, v + c[k + 1])
    return l
