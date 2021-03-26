from typing import List
import random


class Solution:
    def __init__(self, nums: List[int]):
        self.orig = nums
        self.shu = list(nums)

    def reset(self) -> List[int]:
        return self.orig

    def shuffle(self) -> List[int]:
        n = len(self.shu)

        for i in range(n):
            rix = random.randint(i, n - 1)
            self.shu[i], self.shu[rix] = self.shu[rix], self.shu[i]

        return self.shu
