import heapq


class MedianFinder:
    """
    The 'median' is the middle value in an ordered integer list.
    We achieve the 'ordered' stream by using two heaps.

    Use two heaps:
        - min-heap with 'right part' of the stream
        - max-heap with 'left part' of the stream

    | * * * * * * | <- max-heap _ min-heap -> | * * * * * * |
    """

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        """
        Time: O(log n)
        """
        min_value = heapq.heappushpop(self.min_heap, num)
        heapq.heappush(self.max_heap, -min_value)

        if len(self.min_heap) < len(self.max_heap):
            max_value = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -max_value)

    def findMedian(self) -> float:
        """
        Time: O(1)
        """
        if len(self.min_heap) > len(self.max_heap):
            return float(self.min_heap[0])

        return (self.min_heap[0] - self.max_heap[0]) / 2.0
