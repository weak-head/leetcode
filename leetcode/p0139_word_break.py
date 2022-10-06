from typing import List


def wordBreak(s: str, words: List[str]) -> bool:
    """
    Dynamic programming

    Time:
    Space:
    """

    words_set = set(words)
    can_segment = [False] * (len(s) + 1)
    can_segment[0] = True

    for i in range(1, len(s) + 1):
        for j in range(i):
            word = s[j:i]
            can_segment[i] |= can_segment[j] and word in words_set

    return can_segment[-1]
