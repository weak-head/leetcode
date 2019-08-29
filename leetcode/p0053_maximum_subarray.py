def max_subarray(nums):
    """
    Dynamic programming, O(n)
    """
    nums_len = len(nums)
    max_sums = [0] * nums_len
    max_sums[0] = nums[0]

    for i in range(1, nums_len):
        max_sums[i] = max(max_sums[i - 1] + nums[i], nums[i])

    return max(max_sums)


# --------------------------------------------------------------------


def max_subarray_2(nums):
    """
    Divide and conquer, O(n * log n)
    """

    def max_cross_sum(nums, lix, mix, rix):
        current_sum, left_sum = 0, float("-inf")

        for ix in range(mix, lix - 1, -1):
            current_sum += nums[ix]
            if current_sum > left_sum:
                left_sum = current_sum

        current_sum, right_sum = 0, float("-inf")
        for ix in range(mix + 1, rix + 1):
            current_sum += nums[ix]
            if current_sum > right_sum:
                right_sum = current_sum

        return left_sum + right_sum

    def max_sum(nums, lix, rix):
        if lix == rix:
            return nums[lix]

        m = (lix + rix) >> 1
        return max(
            max_sum(nums, lix, m),
            max_sum(nums, m + 1, rix),
            max_cross_sum(nums, lix, m, rix),
        )

    return max_sum(nums, 0, len(nums) - 1)


# --------------------------------------------------------------------


def max_subarray_3(nums):
    """
    Sliding window, O(n)
    """
    maxSum = windowSum = 0
    maxNum = float("-inf")

    for end in range(len(nums)):
        windowSum += nums[end]
        if nums[end] >= maxNum:
            maxNum = nums[end]

        if windowSum <= 0:
            windowSum = 0

        maxSum = max(windowSum, maxSum)

    if maxSum == 0:
        maxSum = maxNum

    return maxSum


# --------------------------------------------------------------------


def max_subarray_4(nums):
    max_sum, curr_sum = nums[0], 0

    for num in nums:
        curr_sum += num

        if curr_sum > max_sum:
            max_sum = curr_sum

        if curr_sum < 0:
            curr_sum = 0

    return max_sum


# --------------------------------------------------------------------


def max_subarray_5(nums):
    curr_sum = max_sum = nums[0]

    for i in range(1, len(nums)):
        curr_sum = max(nums[i], curr_sum + nums[i])
        max_sum = max(curr_sum, max_sum)

    return max_sum
