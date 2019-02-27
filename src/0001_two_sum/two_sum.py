from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = {}
        for idx, val in enumerate(nums):
            # we've got the match
            if val in diffs:
                return [diffs[val], idx]
            else:
                match = target - val
                diffs[match] = idx
        return None

if __name__ == '__main__':
    assert Solution.twoSum(None, [2, 7, 11, 15], 9) == [0, 1]
    assert Solution.twoSum(None, [2, 7, 11, 15, 17, 4, 21, 9], 20) == [2, 7]
    assert Solution.twoSum(None, [], 12) == None
    assert Solution.twoSum(None, [1, 3, 7, 15, 18, 22, 29], 9) == None

    print('passed')
