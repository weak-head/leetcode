from typing import List
from collections import deque


def dailyTemperatures(t: List[int]) -> List[int]:
    """
    Monotonic stack

    Time: O(n)
    Space: O(n)
        n - length of the array
    """
    r = deque()
    s = []
    for i in range(len(t) - 1, -1, -1):

        while s and t[s[-1]] <= t[i]:
            s.pop()

        next_warm = 0 if not s else s[-1] - i
        r.appendleft(next_warm)
        s.append(i)

    return r
