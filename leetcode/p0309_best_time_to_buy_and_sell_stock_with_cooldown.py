from typing import List


def maxProfit(prices: List[int]) -> int:
    """
    Dynamic Programming

    Time: O(n)
    Space: O(n)
        n - length of the array

    Similar to other buy/sell stock problems
    """
    n = len(prices)
    s = [(0, float("-inf"))] * (n + 2)

    # days are shifted related to prices by 2
    for day in range(2, n + 2):

        # didn't have it yesterday or sold today
        dont_hold = max(s[day - 1][0], s[day - 1][1] + prices[day - 2])

        # had it yesterday, or bought it today after one day cooldown
        do_hold = max(s[day - 1][1], s[day - 2][0] - prices[day - 2])

        s[day] = (dont_hold, do_hold)

    # don't hold on the last day
    return s[-1][0]
