from collections import defaultdict


class UndergroundSystem:
    """
    Two hashtables, no pessimistic cases

    Time: O(1)
    Space: O(max(n, m))
        n - number of different routes
        m - number of active trips
    """

    def __init__(self):
        self.avg = defaultdict(lambda: (0, 0))
        self.trips = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.trips[id] = (stationName, t)

    def checkOut(self, id: int, endStation: str, t: int) -> None:
        startStation, t0 = self.trips[id]
        del self.trips[id]
        val, cnt = self.avg[(startStation, endStation)]
        self.avg[(startStation, endStation)] = (val + (t - t0), cnt + 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        val, cnt = self.avg[(startStation, endStation)]
        return val / cnt
