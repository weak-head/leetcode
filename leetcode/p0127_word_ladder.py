from collections import defaultdict, deque
from typing import List


def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
    """
    Time: O(l * l * n)
    Space: O(l * l * n)
        l - length of the word
        n - number of words
    """

    if not beginWord or not endWord or not wordList:
        return 0

    if endWord not in wordList:
        return 0

    n = len(beginWord)

    # all possible words combinations
    combs = defaultdict(list)
    for word in wordList:
        for i in range(n):
            comb = word[:i] + "*" + word[i + 1 :]
            combs[comb].append(word)

    q = deque([(beginWord, 1)])
    seen = set([beginWord])

    while q:
        word, level = q.popleft()

        for i in range(n):
            comb = word[:i] + "*" + word[i + 1 :]

            for next_word in combs[comb]:

                if next_word == endWord:
                    return level + 1

                if next_word not in seen:
                    seen.add(next_word)
                    q.append((next_word, level + 1))

            combs[comb] = []

    return 0
