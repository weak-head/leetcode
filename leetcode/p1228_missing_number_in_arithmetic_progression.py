from typing import List


def missingNumber(arr: List[int]) -> int:
    """
    Binary search over the array

    Because first and last are fixed,
    and cannot be dropped, we can get the difference in O(1).

    With binary search we can probe elements,
    to see if they are shifted or not.

    Time: O(log n)
    Space: O(1)
        n - size of the array
    """
    difference = (arr[-1] - arr[0]) // len(arr)
    l, r = 0, len(arr) - 1

    while l < r:
        m = (l + r) // 2

        if arr[m] == (arr[0] + (m * difference)):
            l = m + 1
        else:
            r = m

    return arr[0] + (l * difference)
