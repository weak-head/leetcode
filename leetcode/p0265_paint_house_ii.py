from typing import List


def minCostII_two_mins(costs):
    """
    Interesting solution that avoids using double cycle
    by taking advantage of two minimal values of the previous
    paint cycle.

    Time: O(n * k)
    Space: O(1)
        n - number of houses
        k - number of paint types
    """

    colors = len(costs[0])
    prev_min1 = prev_min2 = 0
    prev_color = None

    for house in range(len(costs)):
        this_min1 = this_min2 = this_color = None

        for color in range(colors):
            cost = costs[house][color]

            if prev_color == color:
                cost += prev_min2
            else:
                cost += prev_min1

            if this_min1 is None or this_min1 > cost:
                this_min2 = this_min1
                this_min1 = cost
                this_color = color
            elif this_min2 is None or this_min2 > cost:
                this_min2 = cost

        prev_min1 = this_min1
        prev_min2 = this_min2
        prev_color = this_color

    return prev_min1


def minCostII_dp(costs: List[List[int]]) -> int:
    """
    DP with optimization

    Time: O(n * k * k)
    Space: O(k)
        n - number of houses
        k - number of paint types
    """
    if not costs:
        return 0

    if len(costs) == 1:
        return min(costs[0])

    ncolors = len(costs[0])
    m = [0] * ncolors

    for house in range(len(costs)):
        nc = [0] * ncolors

        for ci in range(ncolors):
            min_v = float("inf")
            for cp in range(ncolors):
                if ci == cp:
                    continue
                min_v = min(min_v, m[cp] + costs[house][ci])
            nc[ci] = min_v

        m = nc

    return min(m)
