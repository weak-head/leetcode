def can_jump(nums):
    """
    Track mack distance from start to end.
    O(n)
    """
    if not nums:
        return True

    target = len(nums) - 1
    max_distance = ix = 0

    while ix <= max_distance:
        max_distance = max(max_distance, ix + nums[ix])

        if max_distance >= target:
            return True

        ix += 1

    return False


def can_jump2(nums):
    """
    Track max distance from end to start.
    O(n)
    """
    last_valid = len(nums) - 1
    for ix in range(len(nums) - 1, -1, -1):
        if ix + nums[ix] >= last_valid:
            last_valid = ix
    return last_valid == 0
