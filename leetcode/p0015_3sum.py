from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    negs = [-x for x in nums if x < 0]
    pos = [x for x in nums if x >= 0]
    zeros = [x for x in pos if x == 0]
    negs_set = set(negs)
    pos_set = set(pos)
    negs_len = len(negs)
    pos_len = len(pos)
    result = []

    # zeros edge case
    if len(zeros) >= 3:
        result.append((0, 0, 0))

    # double negative check
    for l1 in range(0, negs_len):
        for l2 in range(l1 + 1, negs_len):
            val = negs[l1] + negs[l2]
            if val in pos_set:
                result.append(tuple(sorted((-negs[l1], -negs[l2], val))))

    # double positive check
    for r1 in range(0, pos_len):
        for r2 in range(r1 + 1, pos_len):
            val = pos[r1] + pos[r2]
            if val in negs_set:
                result.append(tuple(sorted((-val, pos[r1], pos[r2]))))

    return list(set(result))


def threeSum2(nums: List[int]) -> List[List[int]]:
    """
    This solution is easier to follow, but it is slower.
    """
    nums.sort()
    result = set()

    for ix in range(len(nums) - 2):
        left = ix + 1
        right = len(nums) - 1

        while left < right:
            current_sum = nums[ix] + nums[left] + nums[right]
            if current_sum < 0:
                left += 1
            elif current_sum > 0:
                right -= 1
            else:
                result.append((nums[ix], nums[left], nums[right]))
                left += 1
                right -= 1

    return list(result)
