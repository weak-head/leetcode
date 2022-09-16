from typing import List


def singleNumber(nums: List[int]) -> int:
    x = 0
    for n in nums:
        x = x ^ n
    return x
