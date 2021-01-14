from typing import List


def maxSubArrayLen(nums: List[int], k: int) -> int:
    partial_sums = {}
    total_sum = 0
    max_len = 0

    for right in range(len(nums)):
        total_sum += nums[right]

        # sum from 0 to right equals to 'total_sum'
        if total_sum not in partial_sums:
            partial_sums[total_sum] = right

        # sum from 0 to right
        if total_sum == k:
            max_len = max(max_len, right + 1)

        # sum from (left to right]
        elif total_sum - k in partial_sums:
            left = partial_sums[total_sum - k]
            max_len = max(max_len, right - left)

    return max_len
