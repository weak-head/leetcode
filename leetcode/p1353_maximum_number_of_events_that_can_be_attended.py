import heapq
from collections import deque


def maxEvents(events):
    """
    Sweep line with priority queue and restrictions

    Time: O(n * log n)
    Space: O(n)
        n - number of events
    """
    ev = deque(sorted(events))  # sort by start day
    pq = []  # min heap
    res = 0
    event_start = None

    while ev or pq:
        if not pq:
            event_start = ev[0][0]

        # the next event is earlier or same
        # as the current one
        while ev and ev[0][0] <= event_start:
            event_end = ev.popleft()[1]
            heapq.heappush(pq, event_end)

        heapq.heappop(pq)
        res += 1
        event_start += 1  # we consumed one day

        # clean-up all finished events
        while pq and pq[0] < event_start:
            heapq.heappop(pq)

    return res
