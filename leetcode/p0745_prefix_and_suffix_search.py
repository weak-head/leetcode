# flake8: noqa: E731
from typing import List
from collections import defaultdict


class WordFilterTrieSetIntersect:
    """
    Trie + Set intersection

    Leetcode: TLE
    """

    def __init__(self, words: List[str]):
        self.prefix = {}
        self.suffix = {}

        for ix, word in enumerate(words):

            node = self.prefix
            for c in word:
                node = node.setdefault(c, {})
                node.setdefault("#", set()).add(ix)

            node = self.suffix
            for c in word[::-1]:
                node = node.setdefault(c, {})
                node.setdefault("#", set()).add(ix)

    def f(self, prefix: str, suffix: str) -> int:
        node = self.prefix
        for c in prefix:
            if c not in node:
                return -1
            node = node[c]
        prefix_set = node["#"]

        node = self.suffix
        for c in suffix[::-1]:
            if c not in node:
                return -1
            node = node[c]
        suffix_set = node["#"]

        intersect = prefix_set & suffix_set
        return max(intersect) if len(intersect) > 0 else -1


Trie = lambda: defaultdict(Trie)
WEIGHT = False


class WordFilterWrapped:
    """
    Trie of suffix wrapped words

    Leetcode: TLE
    """

    def __init__(self, words):
        self.trie = Trie()

        for weight, word in enumerate(words):
            word += "#"

            for i in range(len(word)):
                cur = self.trie
                cur[WEIGHT] = weight

                for j in range(i, 2 * len(word) - 1):
                    cur = cur[word[j % len(word)]]
                    cur[WEIGHT] = weight

    def f(self, prefix, suffix):
        cur = self.trie

        for letter in suffix + "#" + prefix:
            if letter not in cur:
                return -1

            cur = cur[letter]

        return cur[WEIGHT]
