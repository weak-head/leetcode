from typing import List
from functools import lru_cache


def stoneGameII(piles: List[int]) -> int:
    """
    Dynamic programming, top down

    Time: O(n * n)
    Space: O(n * n)
    """
    n = len(piles)

    # partial sums, from right
    psum = list(piles)
    for i in range(n - 2, -1, -1):
        psum[i] += psum[i + 1]

    @lru_cache(None)
    def take(i, m):
        # all piles till the end
        if m * 2 >= n - i:
            return (psum[i], 0)

        best_pick = (0, 0)
        for t in range(1, (m * 2) + 1):
            took = psum[i] - psum[i + t]
            rest = take(i + t, max(m, t))

            if took + rest[1] > best_pick[0]:
                best_pick = (took + rest[1], rest[0])

        return best_pick

    a, b = take(0, 1)
    return a
