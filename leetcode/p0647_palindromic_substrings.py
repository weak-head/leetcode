def countSubstrings(s: str) -> int:
    """
    Time: O(n^2)
    Space: O(1)
        n - size of the string
    """

    def palindrome(l, r):
        c = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
            c += 1
        return c

    cnt = 0
    for i in range(len(s)):
        cnt += palindrome(i, i)
        cnt += palindrome(i, i + 1)

    return cnt
