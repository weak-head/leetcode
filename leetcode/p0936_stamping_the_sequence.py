from typing import List
from collections import deque


def movesToStamp(stamp: str, target: str) -> List[int]:
    """
    Greedy,
    Work backwards to convert target into (['?'] * n)

    Time: O(n * (n - m))
    Space: O(n)
    """
    tl = len(target)
    sl = len(stamp)
    t = list(target)
    s = list(stamp)
    res = deque()

    def check(i):
        """
        Check target starting at 'i' position,
        against stamp.
        If target at 'i' matches (ignoring '?') to
        stamp, we can substitute it with '?'
        """
        changed = False
        for j in range(sl):
            # ignore '?'
            if t[i + j] == "?":
                continue

            # target starting at 'i' doesn't match the stamp
            if t[i + j] != s[j]:
                return False

            changed = True

        # substitute entire substring with '?'
        if changed:
            t[i : i + sl] = ["?"] * sl
            res.appendleft(i)

        return changed

    # Keep substituting the characters in
    # target until we can change it
    changed = True
    while changed:
        changed = False
        for i in range(tl - sl + 1):
            changed |= check(i)

    if t != ["?"] * tl:
        return []

    return res
