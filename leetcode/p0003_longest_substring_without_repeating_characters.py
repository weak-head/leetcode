def lengthOfLongestSubstring(s: str) -> int:
    """
    Keep position of the last seen character.
    Adjust left border based on max possible range.

    Time: O(n)
    Space: O(n)
        n - length of the string
    """
    seen = {}
    left, longest = 0, 0
    for right, c in enumerate(s):
        if c in seen:
            left = max(left, seen[c] + 1)

        longest = max(longest, right - left + 1)
        seen[c] = right
    return longest
