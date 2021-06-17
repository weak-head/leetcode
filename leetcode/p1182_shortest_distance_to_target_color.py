from bisect import bisect_left
from typing import List


def shortestDistanceColor(colors: List[int], queries: List[List[int]]) -> List[int]:
    """
    Time: O( max(n, q * log n) )
    Space: O(n)
        n - number of colors
        q - number of queries
    """
    one = []
    two = []
    three = []

    for ix, c in enumerate(colors):
        if c == 1:
            one.append(ix)
        elif c == 2:
            two.append(ix)
        else:
            three.append(ix)

    res = []
    for ix, color in queries:
        arr = None
        if color == 1:
            arr = one
        elif color == 2:
            arr = two
        else:
            arr = three

        if not arr:
            res.append(-1)
            continue

        lix = bisect_left(arr, ix)

        lix = max(0, lix - 1)
        rix = min(len(arr) - 1, lix + 1)

        distance = min(abs(ix - arr[lix]), abs(ix - arr[rix]))
        res.append(distance)

    return res
