def constructArray(n, k):
    """
    Time: O(n)
    Space: O(n)
    """
    ans = list(range(1, n - k))

    for i in range(k + 1):
        if i % 2 == 0:
            ans.append(n - k + i // 2)
        else:
            ans.append(n - i // 2)

    return ans
