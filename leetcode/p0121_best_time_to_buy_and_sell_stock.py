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
