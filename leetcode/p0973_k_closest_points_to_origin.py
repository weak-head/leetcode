import heapq
from typing import List


def kClosest_k(points: List[List[int]], K: int) -> List[List[int]]:
    """
    Maintain max heap of K len, push negated items

    Time: O(n * log(k))
    Space: O(n)
    """
    r = []
    for x, y in points:
        dist = -(x * x + y * y)
        if len(r) == K:
            heapq.heappushpop(r, (dist, (x, y)))
        else:
            heapq.heappush(r, (dist, (x, y)))

    return [(x, y) for _, (x, y) in r]


def kClosest_n(points: List[List[int]], K: int) -> List[List[int]]:
    """
    Build min heap of N len and extract K items

    Time: O(n * log(n))
    Space: O(n)
    """
    pts = [(x * x + y * y, (x, y)) for x, y in points]
    heapq.heapify(pts)

    r = []
    while K > 0:
        r.append(heapq.heappop(pts)[1])
        K -= 1

    return r
