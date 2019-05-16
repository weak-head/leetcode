from typing import List


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    sc = sorted(filter(lambda x: x <= target, candidates))
    combs = {}

    for n in sc:
        add_new(n, target, {(n,)}, combs)

    return list(combs.get(target, set()))


def add_new(n, target, combination, combs):
    if n > target:
        return

    if n not in combs:
        combs[n] = combination
    else:
        combs[n] |= combination

    for key, value in list(combs.items()):
        if key + n <= target:
            all_combs = set((tuple(sorted(a + b)) for a in value for b in combs[n]))
            add_new(key + n, target, all_combs, combs)
