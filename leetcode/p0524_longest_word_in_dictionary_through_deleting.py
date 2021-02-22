from typing import List


def findLongestWord(s: str, d: List[str]) -> str:
    """
    Time: O(s * n * log(n) + n * m)
    Space: O(1)
        s - length of 's'
        n - length of 'd'
        m - max length of the word in 'd'
    """
    # by length, then by lexicographical
    d.sort(key=lambda x: (-len(x), x))

    def subseq(s, t):
        si = ti = 0
        while si < len(s) and ti < len(t):
            if s[si] == t[ti]:
                ti += 1
            si += 1
        return ti == len(t)

    for t in d:
        if subseq(s, t):
            return t

    return ""
