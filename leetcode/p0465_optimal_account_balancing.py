from typing import List
from collections import defaultdict


def minTransfers1(transactions: List[List[int]]) -> int:
    """
    http://www.mathmeth.com/tom/files/settling-debts.pdf
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
    there are 2^N subproblems, each subproblem contributes to O(N) larger problems.
    Running Time: O(N * 2^N),
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

    for mask in range(2 ** N):
        set_bit = 1
        for b in range(N):
            if mask & set_bit == 0:
                nxt = mask | set_bit
                sums[nxt] = sums[mask] + amounts[b]
                if sums[nxt] == 0:
                    dp[nxt] = max(dp[nxt], dp[mask] + 1)
                else:
                    dp[nxt] = max(dp[nxt], dp[mask])
            set_bit <<= 1

    return N - dp[-1]
