from typing import List
import sys


def threeSumClosest(nums: List[int], target: int) -> int:
    """
    O(n^2)
    """
    nums.sort()
    closest_sum, diff, nums_len = sys.maxsize, sys.maxsize, len(nums)
    for l_base in range(0, nums_len - 2):
        l_ix, r_ix = l_base + 1, nums_len - 1
        while l_ix < r_ix:
            current_sum = nums[l_base] + nums[l_ix] + nums[r_ix]
            if current_sum == target:
                return current_sum

            if abs(target - current_sum) < diff:
                diff = abs(target - current_sum)
                closest_sum = current_sum

            if current_sum < target:
                l_ix = l_ix + 1
            else:
                r_ix = r_ix - 1
    return closest_sum
