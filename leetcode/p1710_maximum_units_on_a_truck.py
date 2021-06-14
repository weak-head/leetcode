from typing import List
import heapq


def maximumUnits(boxTypes: List[List[int]], truckSize: int) -> int:
    """
    Time: O(n)
    Space: O(n)
        n - number of boxes
    """
    q = [(-v[1], v[0]) for v in boxTypes]
    heapq.heapify(q)

    max_units = 0
    left_space = truckSize
    while left_space > 0 and q:
        units, cnt = heapq.heappop(q)
        max_units += -units * min(cnt, left_space)
        left_space -= cnt

    return max_units
