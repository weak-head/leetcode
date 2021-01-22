from typing import List


def shortestDistance(words: List[str], word1: str, word2: str) -> int:
    """
    O(n * l)
    n - total number of words
    l - total length of all words combined
    """
    shortest, w1ix, w2ix = float("inf"), float("inf"), float("inf")
    for ix, word in enumerate(words):
        w1ix = ix if word == word1 else w1ix
        w2ix = ix if word == word2 else w2ix
        shortest = min(shortest, abs(w1ix - w2ix))
    return shortest
