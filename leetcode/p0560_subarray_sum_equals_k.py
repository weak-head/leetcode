from collections import defaultdict


def subarraySum(nums, k):
    """
    Frequency map of sub-array sums.

    Time: O(n)
    Space: O(n)
    """

    freq = defaultdict(int)
    freq[0] = 1
    subsum = 0
    res = 0

    for i in range(len(nums)):
        # prefix sum from 0 to i
        subsum += nums[i]

        # the other prefix sum from 0 to j,
        # (where 0 <= j < i)
        # to receive the subarray sum of 'k'
        other_sum = subsum - k
        if other_sum in freq:
            res += freq[other_sum]

        freq[subsum] += 1

    return res
