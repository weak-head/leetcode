from typing import List
from collections import Counter


def largestUniqueNumber(A: List[int]) -> int:
    """
    Time: O(n)
    Space: O(n)
    """
    c = Counter(A)
    max_v = -1
    for k, v in c.items():
        if v == 1:
            max_v = max(max_v, k)
    return max_v
