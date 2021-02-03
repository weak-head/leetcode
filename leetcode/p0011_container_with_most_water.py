from typing import List


def maxArea(a: List[int]) -> int:
    """
    Greedy, two pointers

    Time: O(n)
    Space: O(1)
        n - length of the list
    """
    l, r = 0, len(a) - 1
    max_area = float("-inf")
    while l < r:
        area = min(a[l], a[r]) * (r - l)
        max_area = max(max_area, area)
        if a[l] < a[r]:
            l += 1
        else:
            r -= 1
    return max_area
