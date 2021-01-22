from typing import List
from collections import defaultdict


class WordDistance:
    def __init__(self, words: List[str]):
        """
        Time: O(n)
        Space: O(n)
        """
        self.m = defaultdict(list)
        for ix, w in enumerate(words):
            self.m[w].append(ix)

    def shortest(self, word1: str, word2: str) -> int:
        """
        Time: O(n)
        Space: O(1)
        """
        loc1, loc2 = self.m[word1], self.m[word2]
        ix1, ix2 = 0, 0
        min_dist = float("inf")
        while ix1 < len(loc1) and ix2 < len(loc2):
            min_dist = min(min_dist, abs(loc1[ix1] - loc2[ix2]))
            if loc1[ix1] < loc2[ix2]:
                ix1 += 1
            else:
                ix2 += 1
        return min_dist
