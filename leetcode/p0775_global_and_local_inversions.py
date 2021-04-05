from typing import List


def isIdealPermutation_scan(A):
    """
    In ideal permutation the absolute difference
    between value and index should be less or equal to one.

    Time: O(n)
    Space: O(1)
    """
    for i, v in enumerate(A):
        if abs(i - v) > 1:
            return False

    return True


def isIdealPermutation_minv(A: List[int]) -> bool:
    """
    Moving from right to left, memorize the minimum value.
    All values with [index-2] should be decreasing, related to minimum.

    Time: O(n)
    Space: O(1)
    """
    if not A:
        return True

    min_v = float("inf")
    for i in range(len(A) - 1, 1, -1):
        min_v = min(min_v, A[i])
        if A[i - 2] > min_v:
            return False

    return True
