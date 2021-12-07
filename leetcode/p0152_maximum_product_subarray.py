from typing import List


def maxProduct(nums: List[int]) -> int:
    """
    Time: O(n)
    Space: O(1)
        n - length of the array
    """
    if len(nums) == 0:
        return 0

    res = vmin = vmax = nums[0]

    for i in range(1, len(nums)):
        curr = nums[i]

        c_vmax = vmax * curr
        c_vmin = vmin * curr

        vmax = max(curr, c_vmax, c_vmin)
        vmin = min(curr, c_vmax, c_vmin)

        res = max(vmax, res)

    return res
