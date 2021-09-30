from typing import List


def canPartitionKSubsets(nums: List[int], k: int) -> bool:
    """
    Combinatorial search

    Time: O(k * 2^n)
    Space: O(k * 2^n)
        k - number of subsets
        n - length of the array
    """
    s = sum(nums)
    if s % k != 0:
        return False

    nums = sorted(nums, reverse=True)

    target_sum = s // k
    target = [target_sum] * k

    def backtrack(ix):
        nonlocal target
        if ix == len(nums):
            return True

        for ti in range(len(target)):
            if target[ti] >= nums[ix]:
                target[ti] -= nums[ix]
                if backtrack(ix + 1):
                    return True
                target[ti] += nums[ix]

        return False

    return backtrack(0)
