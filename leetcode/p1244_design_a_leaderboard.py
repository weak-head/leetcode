from collections import defaultdict
import heapq


class Leaderboard:
    """
    Heap for top-K
    """

    def __init__(self):
        self.scores = defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        """
        O(1)
        """
        self.scores[playerId] += score

    def top(self, K: int) -> int:
        """
        O(n * log(k))
        n - total number of players
        k - number of top players to get
        """
        heap = []
        for x in self.scores.values():
            heapq.heappush(heap, x)
            if len(heap) > K:
                heapq.heappop(heap)
        return sum(heap)

    def reset(self, playerId: int) -> None:
        """
        O(1)
        """
        self.scores[playerId] = 0
