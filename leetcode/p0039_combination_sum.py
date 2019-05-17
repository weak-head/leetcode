from typing import List


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    """
    This approach uses dynamic programming to
    generate all possible combinations for all numbers
    up to the 'target'. It's pretty slow in compare to
    the other solutions.
    """
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


# ----------------------


def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    """Backtracking that uses set to store
    unique combinations. Pretty slow."""
    result = set()
    backtrack(target, (), candidates, result)
    return list(result)


def backtrack(target, comb, candidates, result):
    if target == 0:
        result.add(comb)

    if target < 0:
        return

    for c in candidates:
        backtrack(target - c, tuple(sorted((comb + (c,)))), candidates, result)


# -------------------------


def combinationSum3(candidates: List[int], target: int) -> List[List[int]]:
    """Optimized backtracking that excludes each
    processed item and doesn't require to maintain
    set of unique combinations
    """
    result = []
    backtrack3(target, [], candidates, result)
    return result


def backtrack3(target, comb, candidates, result):
    if target == 0:
        result.append(comb)

    if target < 0:
        return

    cnd = list(candidates)
    while cnd:
        c = cnd[0]
        if c <= target:
            backtrack3(target - c, comb + [c], cnd, result)
        cnd.pop(0)
