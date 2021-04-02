from typing import List


def findMaxForm(strs: List[str], m: int, n: int) -> int:
    """
    Dynamic programming,
    with rolling array optimization

    Typical knapsack problem
    https://en.wikipedia.org/wiki/Knapsack_problem

    Time: O(l * m * n)
    Space: O(m * n)
        l - number of strings
        m - max zeroes
        n - max ones
    """
    # m - max zeroes
    # n - max ones
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for s in strs:
        zeros = s.count("0")
        ones = s.count("1")

        for z in range(m, zeros - 1, -1):
            for o in range(n, ones - 1, -1):
                dp[z][o] = max(dp[z][o], dp[z - zeros][o - ones] + 1)

    return dp[m][n]
