from bisect import bisect_left
from typing import List


def maxEnvelopes(a: List[List[int]]) -> int:
    """
    Dynamic Programming

    Sort the numbers by width asc, and height desc.
    Find LIS of heights.

    Similar to the Longest Increasing Sequence (LC300)

    Time: O(n * log(n))
    Space: O(n)
        n - number of envelopes
    """
    env = sorted(a, key=lambda x: (x[0], -x[1]))
    env = [x[1] for x in env]

    r = []
    for height in env:
        ix = bisect_left(r, height)
        if ix == len(r):
            r.append(height)
        else:
            r[ix] = height

    return len(r)
