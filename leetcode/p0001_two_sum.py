from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    diffs = {}
    for idx, val in enumerate(nums):
        # we've got the match
        if val in diffs:
            return [diffs[val], idx]
        else:
            match = target - val
            diffs[match] = idx
    return None
