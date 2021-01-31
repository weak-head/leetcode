from typing import List
import heapq


def assignBikes(workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
    """
    Optimization of the approach with one heap
    for tuples of (distance, worker, bike).
    We use heap of heaps to reduce the time complexity
    of searching the next best fit.

    Time: O(w * b)
    Space: O(w * b)
        w - number of workers
        b - number of bikes
    """

    dist = []
    for w_ix, (w_x, w_y) in enumerate(workers):
        dist.append([])
        for b_ix, (b_x, b_y) in enumerate(bikes):
            d = abs(w_x - b_x) + abs(w_y - b_y)
            dist[-1].append((d, w_ix, b_ix))
        heapq.heapify(dist[-1])

    # heap of heaps
    q = [heapq.heappop(worker_dist) for worker_dist in dist]
    heapq.heapify(q)

    res = [None] * len(workers)  # worker_id => bike_id
    taken = set()
    workers_left = len(workers)
    while workers_left > 0:
        d, w, b = heapq.heappop(q)
        if res[w] is None:
            if b not in taken:
                res[w] = b
                taken.add(b)
                workers_left -= 1
            else:
                if dist[w]:
                    heapq.heappush(q, heapq.heappop(dist[w]))
    return res
