import heapq
from typing import List


def connectSticks(sticks: List[int]) -> int:
    """
    Greedy + heap

    Time: O(n * log n)
    Space: O(n)
        n - number of sticks
    """
    heapq.heapify(sticks)

    p = 0
    while len(sticks) > 1:
        a = heapq.heappop(sticks)
        b = heapq.heappop(sticks)

        s = a + b
        p += s

        heapq.heappush(sticks, s)

    return p
