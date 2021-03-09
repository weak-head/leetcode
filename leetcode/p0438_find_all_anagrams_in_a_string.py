from typing import List
from collections import Counter


def findAnagrams(s: str, p: str) -> List[int]:
    """
    Sliding window, with optimization

    Similar to:
        - LC76

    Time: O(s + p)
    Space: O(p)
        s - length of 's'
        p - length of 'p'
    """
    if not s or not p:
        return []

    state = Counter(p)
    state_num = len(state)
    li = ri = 0
    res = []
    while li < len(s):
        anagram = state_num == 0

        if anagram:
            res.append(li)

        if anagram or ri == len(s) or (ri - li == len(p)):
            ch = s[li]
            if ch in state:
                state[ch] += 1
                if state[ch] == 1:
                    state_num += 1
            li += 1

        else:
            ch = s[ri]
            if ch in state:
                state[ch] -= 1
                if state[ch] == 0:
                    state_num -= 1
            ri += 1

    return res
