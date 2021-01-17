from typing import List


def minCost(costs: List[List[int]]) -> int:
    """
    Typical Dynamic Programming problem.
    Very similar to Fibonacci numbers.

    Time: O(n)
    """

    for ix in reversed(range(len(costs) - 1)):
        costs[ix][0] += min(costs[ix + 1][1], costs[ix + 1][2])
        costs[ix][1] += min(costs[ix + 1][0], costs[ix + 1][2])
        costs[ix][2] += min(costs[ix + 1][0], costs[ix + 1][1])

    return min(costs[0])
