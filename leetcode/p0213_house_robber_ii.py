from typing import List


def rob(nums: List[int]) -> int:
    """
    Dynamic Programming
    Similar to LC198

    In case of the circular street,
    we cannot rob both the first and
    the last houses at the same time.
    So we have to find the best between:
        - ignoring first house
        - ignoring second house

    Time: O(n)
    Space: O(n)
        n - number of houses
    """
    if len(nums) == 1:
        return nums[0]

    def rob_sub(ns):
        n = len(ns)
        s = [(0, 0)] * (n + 2)  # skip, rob

        # house is shifted by 2
        for house in range(2, n + 2):

            # best of skip or rob previous house
            if_skip = max(s[house - 1][0], s[house - 1][1])

            # best of skip previous or rob one before
            if_rob = max(s[house - 2][1], s[house - 1][0]) + ns[house - 2]

            s[house] = (if_skip, if_rob)

        return max(s[-1])

    skip_first = rob_sub(nums[1:])
    skip_last = rob_sub(nums[:-1])
    return max(skip_first, skip_last)


def rob_optimized(nums: List[int]) -> int:
    """
    Dynamic Programming
    Same as above, but optimized for space

    Time: O(n)
    Space: O(1)
        n - number of houses
    """
    if len(nums) == 1:
        return nums[0]

    def rob_n(ns):
        n = len(ns)
        prev1 = prev2 = 0

        for house in range(n):
            this = max(prev1, prev2 + ns[house])
            prev2, prev1 = prev1, this
        return prev1

    return max(rob_n(nums[1:]), rob_n(nums[:-1]))
