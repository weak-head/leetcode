from collections import defaultdict
from typing import List


def sumSubarrayMins_ms(A):
    """
    Monotonic stack
    Maintain stack of minimums.

    Notable links:
        https://leetcode.com/problems/sum-of-subarray-minimums/discuss/170750/C++JavaPython-Stack-Solution
        https://leetcode.com/problems/sum-of-subarray-minimums/discuss/178876/stack-solution-with-very-detailed-explanation-step-by-step
        https://leetcode.com/problems/sum-of-subarray-minimums/discuss/214611/O(N)-Stack-solution-with-example-and-detailed-explanation


    Similar:
        828. Unique Letter String
        891. Sum of Subsequence Widths
        1130. Minimum Cost Tree From Leaf Values
        907. Sum of Subarray Minimums
        901. Online Stock Span
        856. Score of Parentheses
        503. Next Greater Element II
        496. Next Greater Element I
        84. Largest Rectangle in Histogram
        42. Trapping Rain Water

    Time: O(n)
    Space: O(n)
        n - length of the array
    """
    res = 0
    s = []
    A = [0] + A + [0]

    for i, x in enumerate(A):
        while s and A[s[-1]] > x:
            j = s.pop()
            k = s[-1]
            res += A[j] * (i - j) * (j - k)

        s.append(i)

    return res % (10 ** 9 + 7)


def sumSubarrayMins_dp(arr: List[int]) -> int:
    """
    Dynamic Programming, following the optimal structure

    Time: O(n^2)
    Space: O(n^2)
        n - length of the array

    Leetcode: TLE
    """

    mins = defaultdict(lambda: {})

    def get_min(start, end):
        if start > end:
            return float("inf")
        return mins[start][end]

    for width in range(1, len(arr) + 1):
        for start in range(0, len(arr) - width + 1):
            end = start + width - 1
            min_value = min(arr[start], get_min(start + 1, end))
            mins[start][end] = min_value

    min_sum = 0
    for v in mins.values():
        for min_v in v.values():
            min_sum += min_v

    return min_sum % (10 ** 9 + 7)
