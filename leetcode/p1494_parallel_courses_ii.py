from typing import List
from itertools import permutations


def minNumberOfSemesters(n: int, dependencies: List[List[int]], k: int) -> int:
    """
    Dynamic programming, binary masks

    TBD:
    https://leetcode.com/problems/parallel-courses-ii/discuss/710229/Python-Short-DP-with-Binary-Masks-O(n2*2n)-explained

    Time: O(n^2 * 2^n)
    Space: O(2^n * n)
    """
    dp = [[(100, 0, 0)] * n for _ in range(1 << n)]

    bm_dep = [0] * (n)
    for i, j in dependencies:
        bm_dep[j - 1] ^= 1 << (i - 1)

    for i in range(n):
        if bm_dep[i] == 0:
            dp[1 << i][i] = (1, 1, 1 << i)

    for i in range(1 << n):
        n_z_bits = [len(bin(i)) - p - 1 for p, c in enumerate(bin(i)) if c == "1"]

        for t, j in permutations(n_z_bits, 2):
            if bm_dep[j] & i == bm_dep[j]:
                cand, bits, mask = dp[i ^ (1 << j)][t]
                if bm_dep[j] & mask == 0 and bits < k:
                    dp[i][j] = min(dp[i][j], (cand, bits + 1, mask + (1 << j)))
                else:
                    dp[i][j] = min(dp[i][j], (cand + 1, 1, 1 << j))

    return min([i for i, j, k in dp[-1]])
