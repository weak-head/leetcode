from typing import List


def removeDuplicates(nums: List[int]) -> int:
    """
    Time: O(n)
    Space: O(1)
    """
    if not nums:
        return 0

    l = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[l] = nums[i]
            l += 1

    return l
