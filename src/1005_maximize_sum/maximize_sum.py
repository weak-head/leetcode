from typing import List
import heapq

def largestSumAfterKNegations(A: List[int], K: int) -> int:
    heapq.heapify(A)
    for _k in range(0, K):
        el = heapq.heappop(A)
        heapq.heappush(A, el * -1)
    return sum(A)

if __name__ == '__main__':
    assert largestSumAfterKNegations([4,2,3], 1) == 5
    assert largestSumAfterKNegations([3,-1,0,2], 3) == 6
    assert largestSumAfterKNegations([2,-3,-1,5,-4], 2) == 13

    print('done')