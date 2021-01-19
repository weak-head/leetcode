"""Without using linear Manacher's algorithm"""


def longestPalindrome(s: str) -> str:
    """
    Time: O(n^2)
    Space: O(1)
    """

    def expand(s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1 : r]

    p = ""
    for center in range(len(s)):
        p = max(p, expand(s, center, center), key=len)
        p = max(p, expand(s, center, center + 1), key=len)
    return p
