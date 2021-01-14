from typing import List


def minOperations(nums: List[int], x: int) -> int:
    """
    O(n)
    """
    target_subarr_sum = sum(nums) - x

    partial_sums = {0: 0}
    max_subarr_len = -1
    current_sum = 0

    for right in range(len(nums)):
        current_sum += nums[right]
        partial_sums[current_sum] = right

        # from 0 to 'right'
        if current_sum == target_subarr_sum:
            max_subarr_len = max(max_subarr_len, right + 1)

        elif current_sum - target_subarr_sum in partial_sums:
            left = partial_sums[current_sum - target_subarr_sum]
            max_subarr_len = max(max_subarr_len, right - left)

    if max_subarr_len == -1:
        return -1
    else:
        return len(nums) - max_subarr_len
