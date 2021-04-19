from functools import lru_cache
from typing import List


def combinationSum_bu(nums: List[int], target: int) -> int:
    """
    Dynamic Programming, bottom-up

    Simlar to:
        LC518 - Coin Change 2

    Time: O(t * n)
    Space: O(t)
        t - target
        n - length of nums
    """
    nums.sort()

    m = [0] * (target + 1)
    m[0] = 1

    for comb_sum in range(target + 1):
        for num in nums:
            if num <= comb_sum:
                m[comb_sum] += m[comb_sum - num]
            else:
                break

    return m[target]


def combinationSum_td(nums: List[int], target: int) -> int:
    """
    Dynamic programming, top-down

    Time: O(t * n)
    Space: O(t)
        t - target
        n - length of nums
    """
    nums.sort()

    @lru_cache(maxsize=None)
    def combs(remain):
        if remain == 0:
            return 1

        result = 0
        for num in nums:
            if num <= remain:
                result += combs(remain - num)
            else:
                break

        return result

    return combs(target)
