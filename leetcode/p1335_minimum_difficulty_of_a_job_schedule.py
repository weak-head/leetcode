from typing import List
from functools import lru_cache


def minDifficulty_dp(diffs: List[int], d: int) -> int:
    """
    Dynamic programming, top-down

    Quick visualization of the optimal substructure:

                                            [b]#1 + [cdef]#1
                                            [bc]#1 + [def]#1
                    [a]#1 + [bcdef]#2       [bcd]#1 + [ef]#1
                                            [bcde]#1 + [f]#1

                                            [c]#1 + [def]#1
                    [ab]#1 + [cdef]#2       [cd]#1 + [ef]#1
                                            [cde]#1 + [f]#1
    [abcdef]#3

                    [abc]#1 + [def]#2       [d]#1 + [ef]#1
                                            [de]#1 + [f]#1


                    [abcd]#1 + [ef]#2       [e]#1 + [f]#1

    Sub-structure:
        solution(A[0..n], d) = max(A[0..j*]) + solution(A[*j+1..n], d - 1)

    Time: (n * n * d)
    Space: (n * d)
        n - number of jobs
        d - number of days

    Similar to LC1105
    """
    if len(diffs) < d:
        return -1

    @lru_cache(None)
    def min_diff(ix, days):
        if days == 1:
            return max(diffs[ix:])

        total_diff, day_diff = float("inf"), float("-inf")
        for day_end in range(ix, len(diffs) - days + 1):
            day_diff = max(day_diff, diffs[day_end])
            total_diff = min(total_diff, day_diff + min_diff(day_end + 1, days - 1))

        return total_diff

    return min_diff(0, d)


def minDifficulty_dp_space_saving(diffs: List[int], days: int) -> int:
    """
    Dynamic programming, bottom up, with space saving
    Since 'dp(.., day)' depends only on 'dp(.., day-1)'

    Time: (n * n * d)
    Space: (n)
        n - number of jobs
        d - number of days
    """
    ln = len(diffs)
    if ln < days:
        return -1

    dp = [0] * ln  # day 'n'
    dp2 = [float("inf")] * ln  # day 'n+1'

    # day 0
    for j in range(ln - 1, -1, -1):
        if j == ln - 1:
            dp[j] = diffs[j]
        else:
            dp[j] = max(diffs[j], dp[j + 1])

    # day 1 -> d
    for day in range(1, days):

        # all possible endings of this day
        for day_end in range(ln - day - 1, -1, -1):

            # all possible difficulties of this day
            #   dp  -> previous day
            #   dp2 -> this day
            day_diff = 0
            for k in range(day_end, ln - day):
                day_diff = max(day_diff, diffs[k])
                dp2[day_end] = min(dp2[day_end], day_diff + dp[k + 1])

        dp, dp2 = dp2, [float("inf")] * ln

    return dp[0]


def minDifficulty_dp_space_saving_optimized_stack(diffs: List[int], days: int) -> int:
    """
    Dynamic programming, bottom up, with space saving and with monotonic stack optimization

    Time: (n * d)
    Space: (n)
    """
    if len(diffs) < days:
        return -1

    dp1 = [float("inf")] * len(diffs)
    dp2 = [0] * len(diffs)

    for d in range(days):
        stack = []
        for i in range(d, len(diffs)):
            dp2[i] = dp1[i - 1] + diffs[i] if i else diffs[i]

            while stack and diffs[stack[-1]] <= diffs[i]:
                j = stack.pop()
                dp2[i] = min(dp2[i], dp2[j] - diffs[j] + diffs[i])

            if stack:
                dp2[i] = min(dp2[i], dp2[stack[-1]])

            stack.append(i)

        dp1, dp2 = dp2, dp1

    return dp1[-1]
