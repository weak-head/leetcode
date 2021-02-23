from typing import List


def maxProfit(k: int, prices: List[int]) -> int:
    """
    Dynamic Programming

    The most generic version of the problem:
        - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
        - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
        - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
        - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
        - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
        - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

    All these problems are same and have the same optimal structure
    and state transition equation.

    Time: O(n * k)
    Space: O(n * k)
        n - number of prices
        k - number of transactions
    """
    n = len(prices)
    s = [[(0, float("-inf"))] * (k + 1) for _ in range(n + 1)]

    for day in range(1, n + 1):
        for transaction in range(1, k + 1):

            # didn't hold yesterday or sold today
            dont_hold = max(
                s[day - 1][transaction][0], s[day - 1][transaction][1] + prices[day - 1]
            )

            # held yesterday or bought today
            do_hold = max(
                s[day - 1][transaction][1],
                s[day - 1][transaction - 1][0] - prices[day - 1],
            )

            s[day][transaction] = (dont_hold, do_hold)

    return s[-1][-1][0]


def maxProfit_optimized(k: int, prices: List[int]) -> int:
    """
    Dynamic Programming
    Same as above, but optimized for space

    Time: O(n * k)
    Space: O(k)
        n - number of days
        k - number of transactions
    """
    n = len(prices)
    yesterday = [(0, float("-inf"))] * (k + 1)
    today = [(0, float("-inf"))] * (k + 1)

    for day in range(1, n + 1):
        for transaction in range(1, k + 1):

            # didn't hold yesterday or sold today
            dont_hold = max(
                yesterday[transaction][0], yesterday[transaction][1] + prices[day - 1]
            )

            # held yesterday or bought today
            do_hold = max(
                yesterday[transaction][1],
                yesterday[transaction - 1][0] - prices[day - 1],
            )

            today[transaction] = (dont_hold, do_hold)

        today, yesterday = yesterday, today

    return yesterday[-1][0]
