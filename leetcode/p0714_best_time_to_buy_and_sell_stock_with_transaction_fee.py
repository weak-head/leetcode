from typing import List


def maxProfit(prices: List[int], fee: int) -> int:
    """
    Dynamic Programming

    Time: O(n)
    Space: O(n)
        n - number of elements in the array

    Similar to all other buy/sell stock problems
    """

    n = len(prices)
    s = [None] * (n + 1)
    s[0] = (0, float("-inf"))

    # days are shifted related to the prices
    for day in range(1, n + 1):

        # didn't hold yesterday, or sold today
        dont_hold = max(s[day - 1][0], s[day - 1][1] + prices[day - 1] - fee)

        # held yesterday or bought today
        do_hold = max(s[day - 1][1], s[day - 1][0] - prices[day - 1])

        s[day] = (dont_hold, do_hold)

    return s[-1][0]


def maxProfit_optimized(prices: List[int], fee: int) -> int:
    """
    Dynamic Programming
    Same as before, but optimized for space

    Time: O(n)
    Space: O(1)
        n - number of elements in the array
    """

    prev_dont, prev_do = 0, float("-inf")
    for day in range(len(prices)):

        dont_hold = max(prev_dont, prev_do + prices[day] - fee)
        do_hold = max(prev_do, prev_dont - prices[day])

        prev_dont, prev_do = dont_hold, do_hold

    return prev_dont
