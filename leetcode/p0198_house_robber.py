from typing import List


def rob(nums: List[int]) -> int:
    """
    Dynamic Programming

    At each house robber has two options, rob or skip.
    It gives us two states for each house, that is very similar to
    the buy/sell stocks problem.

    Time: O(n)
    Space: O(n)
        n - number of houses
    """
    n = len(nums)
    s = [(0, 0)] * (n + 2)  # (skip, rob)

    for house in range(2, n + 2):

        # best of skip or rob previous
        if_skip = max(s[house - 1][0], s[house - 1][1])

        # best of skip previous or rob one before
        if_rob = max(
            s[house - 2][1] + nums[house - 2], s[house - 1][0] + nums[house - 2]
        )

        s[house] = (if_skip, if_rob)

    return max(s[-1])
