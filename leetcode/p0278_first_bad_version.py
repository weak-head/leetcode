def firstBadVersion(n, isBadVersion):
    """
    Typical binary search

    Time: O(log n)
    Space: O(1)
    """
    l, r = 0, n
    while l <= r:
        m = (l + r) // 2
        if isBadVersion(m):
            r = m - 1
        else:
            l = m + 1
    return l
