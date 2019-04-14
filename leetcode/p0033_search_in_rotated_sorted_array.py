from typing import List

def search(nums: List[int], target: int) -> int:
    if nums == []:
        return -1

    nums_len = len(nums)
    lix, rix = 0, nums_len - 1
    while lix <= rix and (lix >= 0 and lix < nums_len) and (rix >= 0 and rix < nums_len):
        mix = (lix + rix) >> 1

        # found match
        if target == nums[lix]:
            return lix

        if target == nums[mix]:
            return mix

        # the pivot is between lix and mix
        if nums[mix] < nums[lix]:

            # target should be between lix and mix
            if target > nums[lix]:
                rix = mix - 1

            # target should be between mix and rix
            elif target > nums[mix]:
                lix = mix + 1

            # target should be between lix and mix
            elif target < nums[mix]:
                rix = mix - 1

        # nums[mix] > nums[lix]:
        else:

            # target should be between mix and rix
            if target > nums[mix]:
                lix = mix + 1

            # target should be between lix and mix
            elif target > nums[lix]:
                rix = mix - 1

            # target should be between mix and rix
            elif target < nums[lix]:
                lix = mix + 1

    return -1