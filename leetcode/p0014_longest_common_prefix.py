from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    """
    Time: O(n * l)
    Space: O(1)
        n - number of strings in array
        l - min length of the string in array
    """
    if not strs:
        return ""

    base = strs[0]
    for i, c in enumerate(base):
        for s in strs:
            if len(s) <= i:
                return s

            if s[i] != c:
                return base[:i]

    return base
