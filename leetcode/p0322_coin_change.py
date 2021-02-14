from functools import lru_cache
from typing import List


def coinChange_dp_td(coins: List[int], amount: int) -> int:
    """
    Dynamic programming, top-down

    Time: O(a * c)
    Space: O(a)
        a - amount
        c - number of coins
    """

    @lru_cache(None)
    def min_coins(n):
        if n == 0:
            return 0

        if n < 0:
            return float("inf")

        m = float("inf")
        for coin in coins:
            m = min(m, 1 + min_coins(n - coin))
        return m

    v = min_coins(amount)
    return v if v != float("inf") else -1


def coinChange_dp_bu(coins: List[int], amount: int) -> int:
    """
    Dynamic programming, bottom-up

    Time: O(a * c)
    Space: O(a)
        a - amount
        c - number of coins
    """
    min_coins = [float("inf")] * (amount + 1)
    min_coins[0] = 0

    for a in range(amount + 1):
        for coin in coins:
            if coin > a:
                continue

            min_coins[a] = min(
                min_coins[a],
                1 + min_coins[a - coin],
            )

    v = min_coins[amount]
    return v if v != float("inf") else -1
