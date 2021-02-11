from collections import Counter


def isAnagram(s: str, t: str) -> bool:
    """
    Time: O(n)
    Space: O(n)
        n - length of the string
    """
    if len(s) != len(t):
        return False

    return Counter(s) == Counter(t)
