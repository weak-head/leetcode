from typing import List


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    """
    Time: O(2^n) # all subsets of candidates set
    Space: O(n)  # all candidates used
        n - number of candidates
    """

    def backtrack(candidates, combinations, combination, index, target):
        if target < 0:
            return

        if target == 0:
            combinations.append(combination)
            return

        for i in range(index, len(candidates)):
            num = candidates[i]

            # would yeld the same combination as before
            if i > index and candidates[i - 1] == num:
                continue

            if num > target:
                break

            backtrack(
                candidates, combinations, combination + [num], i + 1, target - num
            )

    combinations = []
    backtrack(sorted(candidates), combinations, [], 0, target)
    return combinations
