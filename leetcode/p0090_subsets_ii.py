from typing import List


def subsetsWithDup(nums: List[int]) -> List[List[int]]:
    """
    Backtracking
    Sort number to skip duplicates

    Time: O(n * 2^n)
    Space: O(n)
        n - number of elements
    """
    if not nums:
        return [[]]

    nums.sort()
    r = []

    def track(ix, subset):
        r.append(list(subset))
        for i in range(ix, len(nums)):
            # ignore duplicates
            if i > ix and nums[i] == nums[i - 1]:
                continue
            subset.append(nums[i])
            track(i + 1, subset)
            subset.pop()

    track(0, [])
    return r
