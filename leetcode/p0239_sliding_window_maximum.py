from typing import List
from collections import deque


def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    """
    Monotonic Queue with sliding window

    Time: O(n)
    Space: O(k)
        n - number of elements in the list
        k - k
    """

    class MonotonicQueue:
        """Monotonically decreasing queue"""

        def __init__(self):
            self.q = deque()

        def put(self, val):
            """
            Time: O(n) # worst case time
            Time: O(1) # amortized time
            """
            while self.q and self.q[-1] < val:
                self.q.pop()
            self.q.append(val)

        def extract(self, val):
            """
            Time: O(1)
            """
            if self.q and self.q[0] == val:
                self.q.popleft()

        def max(self):
            """
            Time: O(1)
            """
            return self.q[0]

    r = []
    q = MonotonicQueue()
    for i in range(len(nums)):
        if i < k - 1:
            q.put(nums[i])
        else:
            q.extract(nums[i - k])
            q.put(nums[i])
            r.append(q.max())

    if k == len(nums):
        return [q.max()]
    else:
        return r
