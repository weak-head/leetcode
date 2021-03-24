from typing import List
from collections import deque


def advantageCount(a: List[int], b: List[int]) -> List[int]:
    """
    Greedy

    Time: O(n * log n)
    Space: O(n)
        n - length of the array
    """

    ao = sorted([(v, i) for i, v in enumerate(a)])
    bo = sorted([(v, i) for i, v in enumerate(b)])

    rest = []
    res = [None] * len(ao)

    ai = bi = 0
    while ai < len(ao):
        if ao[ai][0] > bo[bi][0]:
            res[bo[bi][1]] = ao[ai][0]
            ai += 1
            bi += 1
        else:
            rest.append(ao[ai][0])
            ai += 1

    for i in range(len(res)):
        if res[i] is None:
            res[i] = rest.pop()

    return res


def advantageCount_2(A: List[int], B: List[int]) -> List[int]:
    """
    Greedy
    Similar idea, but different perspective.

    Time: O(n * log n)
    Space: O(n)
        n - length of the array
    """

    res = [None] * len(A)
    bo = deque(sorted([(b, i) for i, b in enumerate(B)]))

    for a in sorted(A):
        if a > bo[0][0]:
            _, idx = bo.popleft()
        else:
            _, idx = bo.pop()
        res[idx] = a

    return res
