from typing import List
from collections import defaultdict

"""
This is NP-Complete problem, as shown here:

    http://www.mathmeth.com/tom/files/settling-debts.pdf

This problem could be tranformed to 3-partition problem:
    https://en.wikipedia.org/wiki/3-partition_problem

The two solutions below have complexity of O(n!) and O(n * 2^n)
"""


def minTransfers1(transactions: List[List[int]]) -> int:
    """
    DFS with backtracking

    Time: O(n!)
    Space: O(n)

    There two optimizations, though it's still O(n!):
        - skip same sign
        - skip already tested (if the same as previously tested)

    """

    balance = defaultdict(int)
    for t in transactions:
        balance[t[0]] -= t[2]
        balance[t[1]] += t[2]

    balance = [val for val in balance.values() if val != 0]

    def dfs(ix: int) -> int:
        # skip the next empty debt
        while ix < len(balance) and balance[ix] == 0:
            ix += 1

        min_transfers = float("inf")
        prev = 0
        for jx in range(ix + 1, len(balance)):
            # skip already tested or same sign
            if (balance[jx] != prev) and (balance[ix] * balance[jx] < 0):

                # track the transfer, balance[ix] is completely cleared
                balance[jx] += balance[ix]

                min_transfers = min(min_transfers, 1 + dfs(ix + 1))

                # recover/backtrack
                balance[jx] -= balance[ix]

                # keep track of the previous check
                # to optimize the time
                prev = balance[jx]

        return min_transfers if min_transfers != float("inf") else 0

    return dfs(0)


def minTransfers2(transactions: List[List[int]]) -> int:
    """
    Dynamic Programming, find max number of min subsets that sums to 0

    Time: O(N * 2^N)
    Space: O(2^N)
    """
    persons = defaultdict(int)
    for sender, receiver, amount in transactions:
        persons[sender] -= amount
        persons[receiver] += amount

    amounts = [amount for amount in persons.values() if amount != 0]

    N = len(amounts)
    dp = [0] * (2 ** N)  # dp[mask] = number of sets whose sum = 0
    sums = [0] * (2 ** N)  # sums[mask] = sum of numbers in mask

    # Find the maximum number of min-subsets,
    # such as each subset has a sum of 0.
    #
    # Example:
    #   The following set (N=5):
    #       [-2,2,-7,4,3]
    #   Has two min-subsets (M=2):
    #       {-2,2} & {-7,4,3}
    #   To settle the debt (get sum of 0) number of transactions required:
    #       len({-2,2}) - 1   = 1
    #       len({-7,4,3}) - 1 = 2
    #   The total transactions required:
    #       (len({-2, -2}) - 1) + (len({-7,4,3}) - 1) = 3
    #   That is same as (N-M)
    #
    # The optimal substructure:
    #   {set}[mask] => subset of elements, whose position is '1' in the mask
    #       {-2,2,-7,4,3}[01010] = {2,3}
    #   dp[mask] => maximum number of min sets, that can be formed by elements in {set}[mask]
    #   sum[mask] => sum of elements in {set}[mask]
    #   sub_mask => has one less bits set to '1' than mask
    #   Then we have:
    #       if sum[mask] == 0:
    #           dp[mask] = max(dp[sub_mask] + 1) for all possible sub_mask
    #       else:
    #           dp[mask] = max(dp[sub_mask]) for all possible sub_mask
    #
    #
    # There are 2^N subsets of a set with N elements,
    # each subset represented by the 'mask'
    for mask in range(2 ** N):

        # Starting from the first element
        current_element = 1
        # try all the elements in the array
        for b in range(N):

            # We want to check only elements that are not in the current mask
            if mask & current_element == 0:

                # 'nxt' is the subset that is formed when we include
                # the 'current_element' to the 'mask' subset
                nxt = mask | current_element

                # The sum for this 'nxt' subset
                sums[nxt] = sums[mask] + amounts[b]

                if sums[nxt] == 0:
                    dp[nxt] = max(dp[nxt], dp[mask] + 1)
                else:
                    dp[nxt] = max(dp[nxt], dp[mask])

            # Move to the next element
            current_element <<= 1

    return N - dp[-1]  # N - M
