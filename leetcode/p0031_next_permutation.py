from typing import List


def nextPermutation(nums: List[int]) -> None:
    """

    ======= From Leetcode Solution ==============================

    First, we observe that for any given sequence
    that is in descending order, no next larger permutation is possible.
    For example, no next permutation is possible for the following array:

        [9, 5, 4, 3, 1]

    We need to find the first pair of two successive numbers
    a[i] and a[i−1], from the right, which satisfy a[i] > a[i-1].

    Now, no rearrangements to the right of a[i−1] can create
    a larger permutation since that subarray consists of numbers
    in descending order. Thus, we need to rearrange the numbers
    to the right of a[i−1] including itself.

    Now, what kind of rearrangement will produce the next larger number?
    We want to create the permutation just larger than the current one.
    Therefore, we need to replace the number a[i−1] with the number
    which is just larger than itself among the numbers lying to its
    right section, say a[j].

    We swap the numbers a[i−1] and a[j].

    We now have the correct number at index i−1.
    But still the current permutation isn't the permutation that
    we are looking for. We need the smallest permutation that can be
    formed by using the numbers only to the right of a[i−1].
    Therefore, we need to place those numbers in ascending order
    to get their smallest permutation.

    But, recall that while scanning the numbers from the right,
    we simply kept decrementing the index until we found the pair
    a[i] and a[i−1] where, a[i] > a[i−1].
    Thus, all numbers to the right of a[i−1] were already sorted
    in descending order. Furthermore, swapping a[i−1] and a[j]
    didn't change that order.

    Therefore, we simply need to reverse the numbers following
    a[i−1] to get the next smallest lexicographic permutation.

    ==========================================================

    Time: O(n)
    Space: O(1)
        n - length of the array
    """

    i = len(nums) - 1
    while i > 0 and nums[i - 1] >= nums[i]:
        i -= 1

    # all numbers are in descending order,
    # we can simply reverse the array
    if i == 0:
        nums.reverse()
        return

    # first index of the value we need to swap
    k = i - 1

    # find the second index of the value we need to swap
    j = len(nums) - 1
    while nums[j] <= nums[k]:
        j -= 1

    # swap 'k' with 'j'
    nums[j], nums[k] = nums[k], nums[j]

    # reverse subarray [i : len(nums)]
    l, r = i, len(nums) - 1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1
