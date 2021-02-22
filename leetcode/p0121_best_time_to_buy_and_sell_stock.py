from typing import List


def maxProfit(prices: List[int]) -> int:
    """
    Kadane's algorithm
    https://en.wikipedia.org/wiki/Maximum_subarray_problem#Kadane's_algorithm

    Time: O(n)
    Space: O(1)
    """
    min_price = float("inf")
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit


def maxProfit_dp(prices: List[int]) -> int:
    """
    Dynamic Programming

    Each day has the two possible states:
        - we hold stock
        - we don't hold the stock

    If we hold the stock, it means that we either had it yesterday,
    or we bought it today.

    If we dont hold the stock, we either didn't have it yesterday,
    or we sold it today.

    Time: O(n)
    Space: O(n)
    """
    n = len(prices)
    dp = [None] * (n + 1)
    dp[0] = (0, float("-inf"))  # (don't have stock, have stock)

    # days are shifted related to prices
    # so we refer 'prices[day - 1]'
    for day in range(1, n + 1):
        # today we dont hold the stock if we had no stock yesterday,
        # of we have sold the stock today
        dont_hold = max(dp[day - 1][0], dp[day - 1][1] + prices[day - 1])

        # today we hold the stock if we had stock yesterday,
        # of we have bought the stock today
        hold = max(dp[day - 1][1], -prices[day - 1])

        dp[day] = (dont_hold, hold)

    return dp[n][0]


def maxProfit_dp_optimized(prices: List[int]) -> int:
    """
    Dynamic Programming

    Similar to the previous solution,
    but optimized for memory.

    And with this optimization it looks exactly like
    Kadene's algorithm.

    Time: O(n)
    Space: O(1)
    """
    n = len(prices)
    prev_dont, prev_do = 0, float("-inf")

    for day in range(n):
        # today we dont hold the stock if we had no stock yesterday,
        # of we have sold the stock today
        dont_hold_today = max(prev_dont, prev_do + prices[day])

        # today we hold the stock if we had stock yesterday,
        # of we have bought the stock today
        hold_today = max(prev_do, -prices[day])

        prev_dont, prev_do = dont_hold_today, hold_today

    return prev_dont
