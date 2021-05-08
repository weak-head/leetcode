def minDistance(a: str, b: str) -> int:
    """
    Dynamic programming,
    Longest common subsequence

    Optimized for space

    Same as:
        # 1143 - Longest Common Subsequence

    Time: O(m * n)
    Space: O(min(m, n))
        n - length of a
        m - length of b
    """
    if a < b:
        a, b = b, a

    pre = [0] * (len(b) + 1)
    cur = [0] * (len(b) + 1)

    for r in range(1, len(a) + 1):
        for c in range(1, len(b) + 1):
            if a[r - 1] == b[c - 1]:
                cur[c] = pre[c - 1] + 1
            else:
                cur[c] = max(pre[c], cur[c - 1])
        pre, cur = cur, pre

    change_a = len(a) - pre[-1]
    change_b = len(b) - pre[-1]
    return change_a + change_b
