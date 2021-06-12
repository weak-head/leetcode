import heapq
from typing import List


def minRefuelStops(target: int, startFuel: int, stations: List[List[int]]) -> int:
    stations.sort()
    passed = []
    at = startFuel
    fills = 0

    while True:

        if at >= target:
            return fills

        while stations and stations[0][0] <= at:
            heapq.heappush(passed, -stations[0][1])
            stations.pop(0)

        if not passed:
            return -1

        gas = heapq.heappop(passed)
        at += -gas
        fills += 1
