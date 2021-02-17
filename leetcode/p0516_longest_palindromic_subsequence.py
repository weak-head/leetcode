from functools import lru_cache


def longest_palindrom_subsequence_dp_bu_optimized(s: str) -> int:
    """
    Bottom-up DP

    We depend only on [i] and [i-1],
    so no need to store all 'n' states.

    Time: O(n^2)
    Space: O(n)
        n - length of the string
    """
    if not s:
        return 0

    this = [0] * len(s)  # this row
    prev = [0] * len(s)  # previous row
    prev[-1] = 1

    for row in range(len(s) - 2, -1, -1):
        this[row] = 1
        for col in range(row + 1, len(s)):
            if s[row] == s[col]:
                this[col] = prev[col - 1] + 2
            else:
                this[col] = max(this[col - 1], prev[col])

        this, prev = prev, this

    return prev[-1]


def longest_palindrom_subsequence_dp_bu(s: str) -> int:
    """
    Bottom-up DP

    Time: O(n^2)
    Space: O(n^2)
        n - length of the string
    """
    if not s:
        return 0

    m = [[0 for _ in range(len(s))] for _ in range(len(s))]

    for i in range(len(s)):
        m[i][i] = 1

    for row in range(len(s) - 2, -1, -1):
        for col in range(row + 1, len(s)):
            if s[row] == s[col]:
                m[row][col] = m[row + 1][col - 1] + 2
            else:
                m[row][col] = max(m[row + 1][col], m[row][col - 1])

    return m[0][-1]


def longest_palindrom_subsequence_dp_td(s: str) -> int:
    """
    Classical top-down Dynamic Programming

    Time: O(n^2)
    Space: O(n^2)
        n - length of the string
    """

    @lru_cache(None)
    def dp(l, r):
        if l == r:
            return 1

        if l > r:
            return 0

        if s[l] == s[r]:
            return dp(l + 1, r - 1) + 2
        else:
            return max(dp(l + 1, r), dp(l, r - 1))

    return dp(0, len(s) - 1)
