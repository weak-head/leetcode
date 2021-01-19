from typing import List


def isAlienSorted(words: List[str], order: str) -> bool:
    """
    Time: O(c)
    c - total number of all characters in all words combined
    """
    m = {k: v for v, k in enumerate(order)}
    for w1, w2 in zip(words, words[1:]):
        for c1, c2 in zip(w1, w2):
            if m[c2] == m[c1]:
                continue
            elif m[c2] > m[c1]:
                break
            else:
                return False
        else:
            if len(w2) < len(w1):
                return False
    return True
