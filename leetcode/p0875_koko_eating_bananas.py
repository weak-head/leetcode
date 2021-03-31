import math
from typing import List


def minEatingSpeed(piles: List[int], h: int) -> int:
    """
    Binary search over space of hours needed

    Time: O(n * log n)
    Space: O(1)
    """

    def can_finish(speed):
        return sum(math.ceil(p / speed) for p in piles) <= h

    l, r = 1, max(piles)
    while l < r:
        mid = (l + r) // 2
        if can_finish(mid):
            r = mid
        else:
            l = mid + 1

    return r
