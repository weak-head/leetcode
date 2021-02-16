# flake8: noqa: W605
import math
from functools import lru_cache


@lru_cache(None)
def egg_drop_dp(K: int, N: int) -> int:
    """
    The overall best strategy is binary search,
    but we cannot use it because we have a limited number
    of eggs and we have to guarantee that we can find
    the optimal solution.

    That said, the best strategy is binary search until we have
    more than 1 egg and when we have 1 egg - linear search.

    Using this strategy we need to simulate the problem space of
    multiple choices that we would make for the every combination of
    floors and eggs.

    We don't need to check if egg is going to break or not,
    we are checking the full space of possibilities at once,
    and the results of our choice when the egg breaks and when it's not.

    When we have K eggs and N floors left, we can pick any of N floors
    and drop an egg. Lets say we pick a floor F that is 1 <= F <= N.
    The egg could break or it could survive the drop from the floor F.
    If the egg breaks - it means that we have K-1 eggs left and
    we need to check the floors below the floor F.
    If the egg survives - it means that we still have K eggs and
    we need to check the floors above the floor F.

    Here comes the tricky part, because we don't know if egg will break or not,
    we work with all sets of possibilities and variants of our actions and their
    consequences. Effectively it means that we have to check every possible combination
    of every possible decision for K eggs and N floors that we could make,
    and find the optimal choices that would results in minimal amount of drops.

    Based on this the state transition equation is following:
        (k, n) = min{ [.forall i in 1..n] max{ (k-1,i-1) , (k,n-i) } + 1 }

    Conter-intuitive thing about this problem, is that all floors are equal...
    Basically if we need to check the floor range [7..10],
    it is the same as checking the floor ranges [0..3].
    We only need to know that we have 3 more floors to check,
    and where those floors are located will make no impact on us.

    Time: O(n * n * k)
    Space: O(n * k)
        k - number of eggs
        n - number of floors

    Leetcode: TLE
    """

    # If we have no floors left
    # we don't need to do any more attempts
    if N == 0:
        return 0

    # If we have only one egg left
    # we have to try all N floors one-by-one
    if K == 1:
        return N

    min_tries = math.inf
    for choice in range(1, N + 1):
        # This is the case when the egg breaks on this floor.
        # It means that we have one less egg and we have to try
        # [0 .. choice - 1] floors.
        if_breaks = egg_drop_dp(K - 1, choice - 1)

        # This is the case when the egg doesn't break on this floor.
        # It means that we have not lost the egg and we still have 'K' eggs.
        # But the number of floors we need to check is
        # [0 .. (N - choice)]
        if_not_breaks = egg_drop_dp(K, N - choice)

        max_tries_this_choice = max(if_breaks, if_not_breaks)
        min_tries = min(min_tries, max_tries_this_choice + 1)

    return min_tries


@lru_cache(None)
def egg_drop_dp_bs(K: int, N: int) -> int:
    """
    Optimization of the previous solution.

    By looking at dp(K-1, F-1) and dp(K, N-F), where 1 <= F <= N
    we can notice that with increase of F:
        - dp(K-1, F-1) is monotonically increasing  (#2)
        - dp(K, N-F) is monotonically decreasing    (#1)

    Because of this finding maximum value of these two functions
    and then finding minimum, is actually search of their intersection.

     #1       #2
        \   /      #
         \ /       #
         / \       #
        /   \      #
    ################

    The intersection is the result of min(max(..)).
    Knowing this we can use binary search to avoid computing
    results of all possible values choice F could have (1 <= F <= N)
    and narrow down the search space by checking if we are
    from the right or left side of the intersection.

    Time: (k * n * log n)
    Space: (k * n)

    Leetcode: slow
    """

    if K == 1:
        return N

    if N == 0:
        return 0

    res = math.inf
    lo, hi = 1, N
    while lo <= hi:
        mid = (lo + hi) // 2
        if_broken = egg_drop_dp_bs(K - 1, mid - 1)  # 2 incresing
        if_not_broken = egg_drop_dp_bs(K, N - mid)  # 1 decreasing

        # here we are checking if we are
        # from the left or right side
        # of the intersection
        if if_broken > if_not_broken:
            hi = mid - 1
            res = min(res, if_broken + 1)
        else:
            lo = mid + 1
            res = min(res, if_not_broken + 1)

    return res
