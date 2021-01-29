from typing import List


def sortColors(nums: List[int]) -> None:
    """
    Time: O(n)
    Space: O(1)
        n - number of elements in the array

    0 -> l             = 0
    l -> r             = 1
    r -> len(nums) - 1 = 2
    """
    c, l, r = 0, 0, len(nums) - 1
    while c <= r:
        if nums[c] == 0:
            nums[c], nums[l] = nums[l], nums[c]
            l += 1
            c += 1
        elif nums[c] == 2:
            nums[c], nums[r] = nums[r], nums[c]
            r -= 1
        else:
            c += 1
