from typing import List


def sortArrayByParityII(nums: List[int]) -> List[int]:
    """
    Time: O(n)
    Space: O(1)
        n - length of the array
    """

    n = len(nums)
    if n < 2:
        return nums

    o, e = 1, 0

    while e < n:
        if nums[e] % 2 != 0:
            while o < n:
                if nums[o] % 2 != 1:
                    nums[e], nums[o] = nums[o], nums[e]
                    break
                o += 2
        e += 2

    return nums
