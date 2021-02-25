from typing import List
from collections import Counter


def permuteUnique(nums: List[int]) -> List[List[int]]:
    """
    Backtracking
    Counter instead of set to track number of items we can use

    Time: O(n!)
    Space: O(n!)
    """

    result = set()

    def backtrack(ns, permutation):
        if len(permutation) == len(nums):
            result.add(tuple(permutation))

        for number, count in ns.items():
            if count > 0:
                ns[number] -= 1
                backtrack(ns, permutation + [number])
                ns[number] += 1

    backtrack(Counter(nums), [])
    return result
