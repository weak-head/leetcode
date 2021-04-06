def minOperations(n: int) -> int:
    """
    Time: O(1)
    Space: O(1)
    """
    t = n // 2
    return t * (n - t)
