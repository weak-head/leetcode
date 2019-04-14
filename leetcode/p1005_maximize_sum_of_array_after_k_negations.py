from typing import List
import heapq

def largestSumAfterKNegations(A: List[int], K: int) -> int:
    heapq.heapify(A)
    for _k in range(0, K):
        el = heapq.heappop(A)
        heapq.heappush(A, el * -1)
    return sum(A)