from typing import List

def removeElement(nums: List[int], val: int) -> int:
    if nums == []:
        return 0
    current_ix = 0
    for ix in range(len(nums)):
        if nums[ix] != val:
            nums[current_ix] = nums[ix]
            current_ix = current_ix + 1
    return current_ix
