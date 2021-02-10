from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    """
    We use several tricks here:
        - keep partial left product in 'res'
        - evaluate partial right product

    Time: O(n)
    Space: O(1)
        n - number of elements in the array
    """
    res = [1] * len(nums)

    # res[i] contains partial product of nums[0 .. i-1]
    for i in range(1, len(nums)):
        res[i] = res[i - 1] * nums[i - 1]  # nums[0 .. i-2] * nums[i-1]

    r_prod = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] = res[i] * r_prod  # nums[0 .. i-1] * nums[i+1 .. ]
        r_prod = r_prod * nums[i]

    return res
