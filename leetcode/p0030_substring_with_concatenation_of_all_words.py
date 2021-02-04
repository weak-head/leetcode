from typing import List
from collections import Counter, defaultdict


def findSubstring(s: str, words: List[str]) -> List[int]:
    """
    Sliding window, with state for each possible offset.

    The substring we are searching could be shifted,
    and could start from any location in the string.
    Because of this we need to maintain the state for each
    possible offset of the substring.

    For the word of length 'm' we need to maintain 'm' states.

    Time: O(n * k * m)
    Space: O(k * m * m)
        n - length of the input string
        k - length of the 'words' array
        m - length of the word in 'words' array
    """
    if not s or not words:
        return []

    wl, wn = len(words[0]), len(words)
    if wl * wn > len(s):
        return []

    c = Counter(words)
    state = defaultdict(lambda: defaultdict(int))  # char offset -> {state}
    for i in range(wl * wn):
        offset = i % wl
        word = s[i : i + wl]
        state[offset][word] += 1

    r = []
    for i in range(len(s) - wl * wn + wl):
        offset = i % wl
        if state[offset] == c:
            r.append(i)

        last_word = s[i : i + wl]
        state[offset][last_word] -= 1
        if state[offset][last_word] == 0:
            del state[offset][last_word]

        next_word = s[(wl * wn) + i : (wl * wn) + i + wl]
        state[offset][next_word] += 1

    return r
