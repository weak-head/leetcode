from functools import lru_cache


def mergeStones(stones, K):
    """
    Dynamic programming

    We keep merging K piles of stones until there is only one pile.
    For the last step, stones[i .. j] are divided into K piles,
    and we merge them into one pile, which costs
        | sum(nums[i .. j]) + cost to make stones[i .. j] form K piles.

    The problem get the minimum cost to make stones[i .. j] form 1 pile equals to
        | the minimum cost to make stones[i .. j] form K piles
        | + sum(nums[i .. j])

    The subproblem the minimum cost to make stones[i .. j] form K piles equals to
        | the minimum cost to make stones[i .. k] form K - 1 piles
        | + the minimum cost to make stones[(k + 1) .. j] form 1 pile
        | + sum(nums[i .. j])


    Time: O(n^3 / k)
    Space: O(n^2)
        n - number of piles
        k - K
    """
    n = len(stones)

    # Every merge will make [k-1] piles to dissapear
    if (n - 1) % (K - 1) != 0:
        return -1

    # Partial sums helps us to quickly run partial sum queries:
    #   prefix[10] - prefix[5]
    # Gives us sum from 6 to 10
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + stones[i]

    @lru_cache(None)
    def dp(i, j):
        if j - i + 1 < K:
            return 0

        res = float("inf")
        # We should move with step 'K-1' in order
        # to create sub-sequences that we can merge into one
        for mid in range(i, j, K - 1):
            # the price of merging [i .. j] into K piles
            # with subroblems [i .. mid] and [mid + 1 .. j]
            k_piles = dp(i, mid) + dp(mid + 1, j)
            res = min(res, k_piles)

        # Merge of the K piles [i .. j] into 1 pile
        if (j - i) % (K - 1) == 0:
            res += prefix[j + 1] - prefix[i]

        return res

    return dp(0, n - 1)
