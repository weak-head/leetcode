from typing import List


def findUnsortedSubarray(nums: List[int]) -> int:
    """
    Time: O(n)
    Space: O(1)
        n - length of the array
    """
    l, r = 0, len(nums) - 1
    while l < r and l < len(nums) - 1 and r > 0:
        if nums[l] <= nums[l + 1]:
            l += 1
        elif nums[r] >= nums[r - 1]:
            r -= 1
        else:
            break

    min_v, max_v = float("inf"), float("-inf")
    for i in range(l, r + 1):
        min_v = min(min_v, nums[i])
        max_v = max(max_v, nums[i])

    # improvement: binary search
    while l >= 0 and nums[l] > min_v:
        l -= 1

    # improvement: binary search
    while r < len(nums) and nums[r] < max_v:
        r += 1

    return r - l - 1 if r != l else 0
