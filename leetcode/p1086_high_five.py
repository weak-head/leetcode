from typing import List
from collections import defaultdict
import heapq


def highFive(items: List[List[int]]) -> List[List[int]]:
    """
    O(n * log(n))
    n - number of unique users
    """

    scores = defaultdict(list)
    for id, score in items:
        heapq.heappush(scores[id], score)

        # we dont need to store more than 5 elements in the heap
        # drop the lowest
        if len(scores[id]) > 5:
            heapq.heappop(scores[id])

    return sorted([(id, sum(score) // len(score)) for id, score in scores.items()])
