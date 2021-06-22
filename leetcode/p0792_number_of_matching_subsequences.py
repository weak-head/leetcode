from typing import List
from collections import defaultdict


def numMatchingSubseq(s: str, words: List[str]) -> int:
    """
    Time: O(n + m)
        n - length of 's'
        m - number of words
    """
    heads = defaultdict(list)
    for w in words:
        heads[w[0]].append(w)

    result = 0
    for c in s:
        if c not in heads:
            continue

        head_words = heads[c]
        heads[c] = []

        for wrd in head_words:
            rest = wrd[1:]
            if not rest:
                result += 1
            else:
                heads[rest[0]].append(rest)

    return result
