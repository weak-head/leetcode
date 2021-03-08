def removePalindromeSub(s: str) -> int:
    """
    String contains only 'a' and 'b'.
    So the max effort is '2', because
    we can remove the subsequence of 'a's
    and then subsequence of 'b's.

    Time: O(n)
    Space: O(1)
        n - length of the sting
    """

    def is_palindrome(s):
        left, right = 0, len(s) - 1
        while left <= right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    if not s:
        return 0
    elif is_palindrome(s):
        return 1
    else:
        return 2
