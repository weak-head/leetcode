from typing import List


def numberOfArithmeticSlices(A: List[int]) -> int:
    """
    Time: O(n)
    Space: O(1)
    """
    if len(A) < 3:
        return 0

    def num_slices(n):
        """
        Each slice should have at least 3 elements.

        If a sequence has 6 elements (N)
        and the min length of a slice is 3 (L),
        there effective length is [N - (L - 1)].

        For example if N = 6 and L = 5,
        the effective length is [2] and there are
        [2 * (2 + 1) // 2] = [ 6 // 2] = 3
        possible subsequences of length L or more
        that we can create out of N elements.
        """
        L = 3
        if n < L:
            return 0

        n = n - (L - 1)
        return ((n + 1) * n) // 2

    total = 0
    start = 0
    step = A[1] - A[0]

    for end in range(1, len(A)):
        if A[end] - A[end - 1] != step:
            total += num_slices(end - start)
            start = end - 1
            step = A[end] - A[end - 1]

    total += num_slices(len(A) - start)

    return total
