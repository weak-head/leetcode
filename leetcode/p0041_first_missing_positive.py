from typing import List


def firstMissingPositive(nums: List[int]) -> int:
    """
    Time: O(n)
    Space: O(n)
    """
    s = set(nums)

    n = 1
    while True:
        if n not in s:
            return n
        n += 1


def firstMissingPositive2(nums: List[int]) -> int:
    """
    Time: O(n)
    Space: O(1)
    """
    n = len(nums)

    # Base case.
    if 1 not in nums:
        return 1

    # nums = [1]
    if n == 1:
        return 2

    # Replace negative numbers, zeros,
    # and numbers larger than n by 1s.
    # After this convertion nums will contain
    # only positive numbers.
    for i in range(n):
        if nums[i] <= 0 or nums[i] > n:
            nums[i] = 1

    # Use index as a hash key and number sign as a presence detector.
    # For example, if nums[1] is negative that means that number `1`
    # is present in the array.
    # If nums[2] is positive - number 2 is missing.
    for i in range(n):
        a = abs(nums[i])
        # If you meet number a in the array - change the sign of a-th element.
        # Be careful with duplicates : do it only once.
        if a == n:
            nums[0] = -abs(nums[0])
        else:
            nums[a] = -abs(nums[a])

    # Now the index of the first positive number
    # is equal to first missing positive.
    for i in range(1, n):
        if nums[i] > 0:
            return i

    if nums[0] > 0:
        return n

    return n + 1


def firstMissingPositive3(nums: List[int]) -> int:
    if not nums:
        return 1

    nums_len = len(nums)

    # We can use indexes of the array to track
    # the existence of each positive element.
    # So our goal is to swap all elements of the array
    # to the appropriate indexes, ignoring elements that are
    # outside the array or less than 1.
    # We are shifting all elements by one index left,
    # to simplify the calculations:
    #  - 1 should have index 0
    #  - 2 should have index 1
    for ix in range(0, nums_len):
        while nums[ix] > 0 and nums[ix] < nums_len and nums[ix] != nums[nums[ix] - 1]:
            nums[nums[ix] - 1], nums[ix] = nums[ix], nums[nums[ix] - 1]

    # Comparing the value with the index
    # we can find the missing element
    for ix in range(nums_len):
        if nums[ix] != ix + 1:
            return ix + 1

    return nums_len + 1
