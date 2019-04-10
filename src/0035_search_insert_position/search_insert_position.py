from typing import List

def searchInsert(nums: List[int], target: int) -> int:
    lix, rix = 0, len(nums) - 1
    while lix <= rix:
        mix = (lix + rix) >> 1
        if target == nums[mix]:
            return mix
        elif target > nums[mix]:
            lix = mix + 1
        else:
            rix = mix - 1
    return lix

if __name__ == '__main__':
    assert searchInsert([1,3,5,6], 5) == 2
    assert searchInsert([1,3,5,6], 2) == 1
    assert searchInsert([1,3,5,6], 7) == 4
    assert searchInsert([1,3,5,6], 0) == 0

    print('passed')