from typing import List
from collections import Counter


def findSubstring(s: str, words: List[str]) -> List[int]:
    """
    Extremely slow and unusable for long inputs.
    """
    if not s or not words:
        return []

    wnum, wlen, slen = len(words), len(words[0]), len(s)
    wset = Counter(words)
    si, res = 0, {}

    while si < slen:
        word = s[si : si + wlen]
        res[si] = wset.copy()

        for ri in range(si, si - (wlen * wnum), -wlen):
            if ri < 0 or not res[ri]:
                break

            if word in res[ri]:
                res[ri][word] -= 1
                if res[ri][word] == 0:
                    del res[ri][word]
            else:
                break

        si += 1

    matches = []
    for ix, v in res.items():
        if v == {}:
            matches.append(ix)

    return matches


def findSubstring2(s, words):
    """
    Using sliding window.
    """
    if not s or not words:
        return []

    sn, wn, wl = len(s), len(words[0]), len(words)
    wset = Counter(words)
    res = []

    # For every possible offset,
    # we are building offset map with the
    # current state of the word match.
    # In case if all values in the particular
    # offset are zeroes it means that we have
    # the combination match.
    offsets = {}
    for ix in range(wn):
        offsets[ix] = wset.copy()
        for wi in range(wl):
            word = s[ix + (wi * wn) : ix + (wi * wn) + wn]
            if word in wset:
                offsets[ix][word] -= 1

        if isMatch(ix, offsets):
            res.append(ix)

    # Using the sliding window we update the state
    # of the each particular offset, tracking if
    # it is the match that we are looking for.
    si = wn
    while si < sn:
        offset = si % wn
        prev_word = s[si - wn : si]
        next_word = s[si + (wn * wl) - wn : si + (wn * wl)]

        if prev_word in wset:
            offsets[offset][prev_word] += 1

        if next_word in wset:
            offsets[offset][next_word] -= 1

        if isMatch(offset, offsets):
            res.append(si)

        si += 1

    return res


def isMatch(ix, d):
    for val in d[ix].values():
        if val != 0:
            return False
    return True
