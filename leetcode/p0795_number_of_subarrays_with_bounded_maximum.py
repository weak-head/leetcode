def numSubarrayBoundedMax(A, L, R):
    """
    Dynamic programming

    We have 3 cases that define optimal substructure:

        if A[i] < L:
            dp[i] = dp[i-1]

        if A[i] > R:
            dp[i] = 0
            prev = i

        if L <= A[i] <= R:
            dp[i] = i - prev

    Time: O(n)
    Space: O(1)
        n - length of the array
    """
    res, dp, prev = 0, 0, -1

    for i, n in enumerate(A):
        if n > R:
            dp = 0
            prev = i
        elif n >= L:
            dp = i - prev

        res += dp
    return res
