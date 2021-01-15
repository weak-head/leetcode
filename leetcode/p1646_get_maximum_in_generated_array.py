def getMaximumGenerated(n: int) -> int:
    nums = {0: 0, 1: 1}
    if n in nums:
        return nums[n]

    max_val = 1
    for i in range(2, n + 1):
        if (i % 2) == 0:
            nums[i] = nums[i // 2]
        else:
            nums[i] = nums[(i - 1) // 2] + nums[((i - 1) // 2) + 1]
        max_val = max(max_val, nums[i])

    return max_val
