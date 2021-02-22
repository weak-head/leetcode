from typing import List


def maxProfit(prices: List[int]) -> int:
    """
    Dynamic Programming

    Time: O(n)
    Space: O(n)
        n - number prices

    Similar to all other buy/sell stock problems.
    """
    k = 2
    n = len(prices)
    s = [[(0, float("-inf"))] * (k + 1) for _ in range(n + 1)]

    # days are shifted related to prices
    for day in range(1, n + 1):
        for transaction in range(1, k + 1):

            # didn't hold yesterday or sold today
            dont_hold = max(
                s[day - 1][transaction][0], s[day - 1][transaction][1] + prices[day - 1]
            )

            # hold yesterday or bough today
            do_hold = max(
                s[day - 1][transaction][1],
                s[day - 1][transaction - 1][0] - prices[day - 1],
            )

            s[day][transaction] = (dont_hold, do_hold)

    return s[-1][-1][0]


def maxProfit_optimized(prices: List[int]) -> int:
    """
    Same as above, but optimized for the space.

    Because number of transactions 'k' is fixed and
    limited by 2 we can reduce the space to O(1).
    Though it makes logic hard to follow.

    Time: O(n)
    Space: O(1)
        n - length of the array
    """

    prev_dont_1 = prev_dont_2 = 0
    prev_do_1 = prev_do_2 = float("-inf")

    for day in range(len(prices)):
        # -- k == 1 (first buy) --

        # didn't hold yesterday or sold today
        dont_hold_1 = max(prev_dont_1, prev_do_1 + prices[day])

        # hold yesterday or bought today
        do_hold_1 = max(prev_do_1, 0 - prices[day])

        prev_dont_1, prev_do_1 = dont_hold_1, do_hold_1

        # -- k == 2 (second buy) --

        # didn't hold yesterday or sold today
        dont_hold_2 = max(prev_dont_2, prev_do_2 + prices[day])

        # hold yesterday or bought today
        do_hold_2 = max(prev_do_2, prev_dont_1 - prices[day])

        prev_dont_2, prev_do_2 = dont_hold_2, do_hold_2

    return prev_dont_2
