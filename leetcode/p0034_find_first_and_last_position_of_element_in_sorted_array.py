from typing import List

def searchRange(nums: List[int], target: int) -> List[int]:
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r) >> 1
        if nums[m] == target:
            return [left(nums, target, l, m), right(nums, target, m, r)]
        elif nums[m] < target:
            l = m + 1
        else:
            r = m - 1
    return [-1, -1]

def left(nums, target, lo, hi):
    while lo <= hi:
        m = (lo + hi) >> 1
        if nums[m] == target:
            hi = m - 1
        else:
            lo = m + 1
    return lo

def right(nums, target, lo, hi):
    while lo <= hi:
        m = (lo + hi) >> 1
        if nums[m] == target:
            lo = m + 1
        else:
            hi = m - 1
    return hi