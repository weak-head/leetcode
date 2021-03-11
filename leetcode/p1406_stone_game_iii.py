from typing import List
from functools import lru_cache


def stoneGameIII_bu(piles: List[int]) -> str:
    """
    Dynamic Programming, bottom up
    Not optimized for space

    Time: O(n)
    Space: O(n)
    """
    n = len(piles)
    m = [(0, 0)] * (n + 3)

    for i in range(n - 1, -1, -1):
        best = (float("-inf"), 0)
        this_sum = 0
        for take in range(i, min(i + 3, n)):
            this_sum += piles[take]
            rest = m[take + 1]
            if this_sum + rest[1] > best[0]:
                best = (this_sum + rest[1], rest[0])
        m[i] = best

    a, b = m[0]
    if a == b:
        return "Tie"
    return "Alice" if a > b else "Bob"


def stoneGameIII_td(piles: List[int]) -> str:
    """
    Dynamic Programming, top down
    Not optimized

    Time: O(n)
    Space: O(n)
    """

    @lru_cache(None)
    def take(i):
        if i >= len(piles):
            return (0, 0)

        best = (float("-inf"), 0)
        for o in range(i, min(i + 3, len(piles))):
            s = sum(piles[i : o + 1])
            rest = take(o + 1)
            if s + rest[1] > best[0]:
                best = (s + rest[1], rest[0])

        return best

    a, b = take(0)
    if a == b:
        return "Tie"
    return "Alice" if a > b else "Bob"
