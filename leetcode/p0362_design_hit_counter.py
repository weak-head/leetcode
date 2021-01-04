from collections import deque


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


class HitCounterQueue:
    def __init__(self, seconds):
        self._seconds = seconds
        self.queue = deque()

    def hit(self, timestamp: int) -> None:
        """
        O(1)
        """
        self.queue.appendleft(timestamp)

    def getHits(self, timestamp: int) -> int:
        """
        O(n)
        """
        while self.queue and timestamp - self.queue[-1] >= self._seconds:
            self.queue.pop()
        return len(self.queue)


class HitCounterQueuePair:
    def __init__(self, seconds):
        self._seconds = seconds
        self.q = deque()  # (time, hits)
        self.total = 0

    def hit(self, timestamp: int) -> None:
        """
        O(1)
        """
        if self.q and self.q[-1][0] == timestamp:
            self.q[-1] = self.q[-1][0], self.q[-1][1] + 1
        else:
            self.q.append((timestamp, 1))
        self.total += 1

    def getHits(self, timestamp: int) -> int:
        """
        O(n) - worst case
        O(1) - amortized, in case of lots of concurrent calls at the same timestamp
        """
        while self.q:
            diff = timestamp - self.q[0][0]
            if diff >= self._seconds:
                _, hit = self.q.popleft()
                self.total -= hit
            else:
                break
        return self.total
