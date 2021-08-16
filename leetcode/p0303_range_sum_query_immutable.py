from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self.m = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.m[i + 1] = self.m[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.m[right + 1] - self.m[left]
