from collections import Counter
from typing import List
import heapq


def topKFrequent(words: List[str], k: int) -> List[str]:
    """
    Time: O(n * log k)
    Space: O(n)
        n - number of words
        k - top k most frequent to get
    """
    h = [(-value, key) for key, value in Counter(words).items()]
    heapq.heapify(h)

    r = []
    while k > 0:
        r.append(heapq.heappop(h)[1])
        k -= 1

    return r
