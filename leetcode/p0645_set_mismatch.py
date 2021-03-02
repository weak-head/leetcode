from typing import List
from collections import Counter


def findErrorNums_map(nums: List[int]) -> List[int]:
    """
    Hashtable

    Time: O(n)
    Space: O(n)
    """
    m = Counter(nums)
    dup, missing = None, 1

    for i in range(1, len(nums) + 1):
        if i not in m:
            missing = i
        elif m[i] == 2:
            dup = i

    return dup, missing


def findErrorNums_optimized(nums: List[int]) -> List[int]:
    """
    Optimized for space

    Time: O(n)
    Space: O(1)
    """
    dup, missing = None, 1

    for n in nums:
        if nums[abs(n) - 1] < 0:
            dup = abs(n)
        else:
            nums[abs(n) - 1] *= -1

    for i in range(1, len(nums)):
        if nums[i] > 0:
            missing = i + 1

    return dup, missing
