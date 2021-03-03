from typing import List


def missingNumber(nums: List[int]) -> int:
    """
    Time: O(n)
    Space: O(1)
        n - number of elements in the array
    """
    s = sum(nums)
    n = len(nums)
    return ((n * (n + 1)) // 2) - s
