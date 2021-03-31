import random
from typing import List


class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        """
        Reservoir sampling
        https://en.wikipedia.org/wiki/Reservoir_sampling

        Time: O(n)
        Space: O(1)
        """
        rix = None
        items = 0
        for i, v in enumerate(self.nums):
            if v == target:
                if random.randint(0, items) == 0:
                    rix = i
                items += 1
        return rix
