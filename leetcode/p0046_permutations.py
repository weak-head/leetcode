from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    """
    Backtracking
    Because numbers are unique, we can use set

    Time: O(n!)
    Space: O(n!)
    """

    result = []

    def backtrack(ns, permutation):
        if not ns:
            result.append(list(permutation))

        for number in list(ns):
            ns.remove(number)
            backtrack(ns, permutation + [number])
            ns.add(number)

    backtrack(set(nums), [])
    return result
