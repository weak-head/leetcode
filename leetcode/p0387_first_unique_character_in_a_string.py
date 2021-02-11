from collections import Counter


def firstUniqChar(s: str) -> int:
    """
    Time: O(n)
    Space: O(n)
        n - length of the string
    """

    cnt = Counter(s)
    for i, c in enumerate(s):
        if cnt[c] == 1:
            return i

    return -1
