from typing import List


def increasingTriplet(nums: List[int]) -> bool:
    """
    Time: O(n)
    Space: O(1)
        n - length of the array
    """
    if not nums:
        return False

    first = second = float("inf")
    for i, v in enumerate(nums):
        if v <= first:
            first = v
        elif v <= second:
            second = v
        else:
            return True

    return False
