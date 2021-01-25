from typing import List


def kLengthApart(nums: List[int], k: int) -> bool:
    if not nums:
        return True
    d = 0 if nums[0] else float("inf")
    for i in range(1, len(nums)):
        if nums[i] and d < k:
            return False

        d += 1

        if nums[i]:
            d = 0

    return True
