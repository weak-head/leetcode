from typing import List


def maximumSum(arr: List[int]) -> int:
    """
    Kadane's algorithm

    Similar to:
        LC 53
        LC 978
        LC 1191
    """
    ignore = not_ignore = max_sum = float("-inf")

    for x in arr:
        ignore = max(ignore + x, not_ignore)
        not_ignore = max(x, not_ignore + x)
        max_sum = max(max_sum, ignore, not_ignore)

    return max_sum
