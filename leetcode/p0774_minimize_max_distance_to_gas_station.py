from typing import List
import heapq


def minmaxGasDist_binary_search(stations: List[int], k: int) -> float:
    """
    Binary search the monotone function

    Time: O(n * log w)
    Space: O(1)
        n - number of stations
        w - (10**8 / 10**-6) = 10**14
    """

    def possible(distance):
        total_stops = 0
        for i in range(1, len(stations)):
            stops_to_add = (stations[i] - stations[i - 1]) // distance
            total_stops += stops_to_add
        return total_stops <= k

    lo, hi = 0, 10 ** 8
    while hi - lo > 1e-6:
        mi = (lo + hi) / 2.0
        if possible(mi):
            hi = mi
        else:
            lo = mi
    return lo


def minmaxGasDist_heap(stations: List[int], k: int) -> float:
    """
    Time: O(n + k * log n)
    Space: O(n)
        n - number of stations
        k - number of stations to insert
    """
    h = []
    for i in range(1, len(stations)):
        x = stations[i - 1]
        y = stations[i]
        h.append((x - y, y - x, 1))
    heapq.heapify(h)

    for _ in range(k):
        _, original, parts = heapq.heappop(h)
        parts += 1
        new_dist = original / parts
        heapq.heappush(h, (-new_dist, original, parts))

    max_distance, _, _ = h[0]
    return -max_distance
