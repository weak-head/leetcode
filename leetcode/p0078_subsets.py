from typing import List


def subsets_backtracking(nums):
    """
    Backtracking

    Time: O(n * 2^n)
    Space: O(n)
        n - length of the array
    """

    res = []

    def track(start, subset):
        res.append(list(subset))

        for i in range(start, len(nums)):
            subset.append(nums[i])
            track(i + 1, subset)
            subset.pop()

    track(0, [])
    return res


def subsets_induction(nums: List[int]) -> List[List[int]]:
    """
    Math induction

    Time: O(n * 2^n)
    Space: O(n)  # stack
        n - length of the array
    """
    if not nums:
        return [[]]

    n = nums.pop()
    subs = subsets_induction(nums)

    res = []
    for sub in subs:
        res.append([n] + sub)

    return res + subs
