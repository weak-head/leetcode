from typing import List
from collections import Counter


def findSubstring(s: str, words: List[str]) -> List[int]:
    """
    Slow for long inputs
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


if __name__ == "__main__":
    print(findSubstring("barfoothefoobarman", ["foo", "bar"]))
    print(findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "word"]))
    print(findSubstring("barfoofoobarthefoobarman", ["bar", "foo", "the"]))
    print(
        findSubstring(
            "lingmindraboofooowingdingbarrwingmonkeypoundcake",
            ["fooo", "barr", "wing", "ding", "wing"],
        )
    )
