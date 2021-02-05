from typing import List


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    """
    Backtracking.

    Time: O(n^(t/m))
    Space: O(t/m)
        n - total number of candidates
        t - target value
        m - minimal value among the candidates

    Similar problems:
        https://leetcode.com/problems/subsets
        https://leetcode.com/problems/subsets-ii
        https://leetcode.com/problems/permutations/
        https://leetcode.com/problems/permutations-ii/
        https://leetcode.com/problems/combinations/
        https://leetcode.com/problems/combination-sum-ii/
        https://leetcode.com/problems/combination-sum-iii/
        https://leetcode.com/problems/palindrome-partitioning/
    """

    def backtrack(target, comb, candidates, result):
        if target == 0:
            result.append(comb)

        if target < 0:
            return

        cnd = list(candidates)
        while cnd:
            c = cnd[0]
            if c <= target:
                backtrack(target - c, comb + [c], cnd, result)
            cnd.pop(0)

    result = []
    backtrack(target, [], candidates, result)
    return result
