class HitCounterBuckets:
    def __init__(self, seconds):
        self._seconds = seconds
        self.buckets = [(0, 0)] * self._seconds

    def hit(self, timestamp: int) -> None:
        """
        O(1)
        """
        index = timestamp % self._seconds
        time, hit = self.buckets[index]
        if time == timestamp:
            self.buckets[index] = time, hit + 1
        else:
            self.buckets[index] = timestamp, 1

    def getHits(self, timestamp: int) -> int:
        """
        O(s)
        s - seconds
        """
        hits = 0
        for index in range(0, self._seconds):
            time, hit = self.buckets[index]
            if timestamp - time < self._seconds:
                hits += hit
        return hits
