import heapq
from collections import Counter
from typing import List


def topKFrequent(nums: List[int], k: int) -> List[int]:
    """
    Time: O(n * log k)
    Space: O(n)
        n - length of the array
    """
    c = Counter(nums)
    h = []

    for key, val in c.items():
        heapq.heappush(h, (val, key))
        if len(h) > k:
            heapq.heappop(h)

    return [v for _, v in h]
