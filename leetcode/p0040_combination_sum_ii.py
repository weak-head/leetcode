from typing import List


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    result = []
    backtrack([], target, candidates, result)

    ur = set()
    for r in result:
        ur.add(tuple(sorted(r)))
    return list(ur)


def backtrack(seq, target, candidates, result):
    if target < 0:
        return

    if target == 0:
        result.append(seq)
        return

    cnd = list(candidates)
    while cnd:
        c = cnd[0]
        cnd = cnd[1:]
        if c <= target:
            backtrack(seq + [c], target - c, cnd, result)
