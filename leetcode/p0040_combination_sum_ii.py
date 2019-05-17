from typing import List


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    result = []
    backtrack([], target, 0, sorted(candidates), result)
    return result


def backtrack(seq, target, index, candidates, result):
    if target < 0:
        return

    if target == 0:
        result.append(seq)
        return

    for i in range(index, len(candidates)):
        num = candidates[i]

        if i > index and candidates[i - 1] == candidates[i]:
            continue

        if num > target:
            break

        backtrack(seq + [num], target - num, i + 1, candidates, result)
