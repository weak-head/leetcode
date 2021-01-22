from typing import List


def removeDuplicates(nums: List[int]) -> int:
    if nums == []:
        return 0
    u_ix = 0
    for c_ix in range(len(nums)):
        if nums[u_ix] != nums[c_ix]:
            u_ix = u_ix + 1
            nums[u_ix] = nums[c_ix]
    return u_ix + 1
