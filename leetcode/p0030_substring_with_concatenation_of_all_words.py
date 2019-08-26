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


# -------------------------------------------------------------------


def findSubstring2(s, words):
    """
    Using sliding window.

    We need to consider the cases when words,
    are having some offset in the original string.
    As an example the words: ['cat', 'dog'] are shifted
    by two characters 'ab' in the string 'abcatdogbat',
    and that's the valid scenario were the result is [2].
    """
    if not s or not words:
        return []

    sl, wn, wl = len(s), len(words[0]), len(words)
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

        if isMatch(offsets[ix]):
            res.append(ix)

    # Using the sliding window we update the state
    # of the each particular offset, tracking if
    # it is the match that we are looking for.
    for si in range(wn, sl):
        offset = si % wn
        prev_word = s[si - wn : si]
        next_word = s[si + (wn * wl) - wn : si + (wn * wl)]

        if prev_word in wset:
            offsets[offset][prev_word] += 1

        if next_word in wset:
            offsets[offset][next_word] -= 1

        if isMatch(offsets[offset]):
            res.append(si)

    return res


def isMatch(counter_state):
    for val in counter_state.values():
        if val != 0:
            return False
    return True
