from typing import List
from collections import deque
import heapq
import itertools


def kWeakestRows_heap_bs(mat: List[List[int]], k: int) -> List[int]:
    """
    Max heap + binary search

    Time: O(r * log k + r * log c) = O( r * log (k * c) )
    Space: O(k)
        r - number of rows
        c - number of columns
        k - number of weakest rows to find
    """

    # binary search to find the right boundary of '1'
    def num(row):
        l, r = 0, len(mat[row])
        while l < r:
            m = (l + r) >> 1
            if mat[row][m] == 1:
                l = m + 1
            else:
                r = m
        return l

    # get k weakest using max heap
    q = []
    for r in range(len(mat)):
        if len(q) < k:
            heapq.heappush(q, (-num(r), -r))
        else:
            heapq.heappushpop(q, (-num(r), -r))

    # reverse index order
    r = deque()
    while q:
        r.appendleft(-heapq.heappop(q)[1])

    return r


def kWeakestRows_vertical(mat: List[List[int]], k: int) -> List[int]:
    """
    Time: O(r * c)
    Space: O(1)
        r - number of rows
        c - number of columns
    """
    m = len(mat)
    n = len(mat[0])

    indexes = []
    for c, r in itertools.product(range(n), range(m)):
        if len(indexes) == k:
            break
        # If this is the first 0 in the current row.
        if mat[r][c] == 0 and (c == 0 or mat[r][c - 1] == 1):
            indexes.append(r)

    # If there aren't enough, it's because some of the first k weakest rows
    # are entirely 1's. We need to include the ones with the lowest indexes
    # until we have at least k.
    i = 0
    while len(indexes) < k:
        # If index i in the last column is 1, this was a full row and therefore
        # couldn't have been included in the output yet.
        if mat[i][-1] == 1:
            indexes.append(i)
        i += 1

    return indexes
