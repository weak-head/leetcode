from typing import List
from collections import defaultdict


def longestStrChain_sort(words: List[str]) -> int:
    """
    Sort, go from small to big.
    Extart subword from big, and check if it's in small.

    Time: O(n * l)
    Space: O(n)
        n - number of words
        l - max length of the word
    """
    ht = {}

    words.sort(key=lambda x: len(x))

    for word in words:
        max_chain = 1

        for i in range(len(word)):
            # drop char at 'i'
            small_word = word[:i] + word[i + 1 :]

            if small_word in ht:
                max_chain = max(max_chain, ht[small_word] + 1)

        ht[word] = max_chain

    return max(ht.values())


def longestStrChain_group(words: List[str]) -> int:
    """
    Group by length,
    go from big to small.
    If small is predecessor of big, update length.

    Time: O(l * n * n)
    Space: O(n)
        n - number of words
        l - max length of the word
    """
    wl = defaultdict(list)  # [len] -> word list
    cl = defaultdict(int)  # word -> max chain len
    mlen = 0
    for word in words:
        mlen = max(mlen, len(word))
        wl[len(word)].append(word)
        cl[word] = 1

    def is_pred(small, big):
        """
        Returns true if big is pred of small
        """
        i = j = 0
        while i < len(small) and j < len(big):
            if small[i] != big[j]:
                j += 1
                if j > i + 1:
                    return False
            else:
                i += 1
                j += 1
        return True

    mlen -= 1
    while mlen > 0:
        for word in wl[mlen]:
            for pred in wl[mlen + 1]:
                if is_pred(word, pred):
                    cl[word] = max(cl[word], cl[pred] + 1)
        mlen -= 1

    return max(cl.values())
