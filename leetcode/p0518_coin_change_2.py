from typing import List


def change(amount: int, coins: List[int]) -> int:
    """
    Dynamic programming

    Similar to:
        LC377 - Combination Sum 4

    Time: O(t * n)
    Space: O(t)
        t - amount
        n - length of coins
    """
    m = [0] * (amount + 1)
    m[0] = 1

    for coin in coins:
        for x in range(coin, amount + 1):
            m[x] += m[x - coin]

    return m[amount]
