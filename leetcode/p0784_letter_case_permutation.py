from typing import List
from functools import lru_cache


def letterCasePermutation(S: str) -> List[str]:
    """
    Time: O(2^n * n)
    Space: (2^n)
        n - length of the string
    """

    @lru_cache(None)
    def permut(ix):
        if ix == len(S):
            return [[""]]

        r = []
        for p in permut(ix + 1):
            if S[ix].isdigit():
                r.append([S[ix]] + p)
            else:
                r.append([S[ix].upper()] + p)
                r.append([S[ix].lower()] + p)
        return r

    return ["".join(p) for p in permut(0)]
