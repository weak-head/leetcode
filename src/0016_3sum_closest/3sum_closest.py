from typing import List
import sys

# O(n^2)
def threeSumClosest(nums: List[int], target: int) -> int:
    nums.sort()
    closest_sum, nums_len = sys.maxsize, len(nums)
    for l_base in range(0, nums_len):
        l_ix, r_ix = l_base + 1, nums_len - 1
        while l_ix < r_ix:
            value = nums[l_base] + nums[l_ix] + nums[r_ix]
            if abs((target - value)) < abs((target - closest_sum)):
                closest_sum = value
            l_value = nums[l_base] + nums[l_ix + 1] + nums[r_ix]
            r_value = nums[l_base] + nums[l_ix] + nums[r_ix - 1]
            if abs(target - l_value) < abs(target - r_value):
                l_ix = l_ix + 1
                while l_ix < r_ix and nums[l_ix - 1] == nums[l_ix]:
                    l_ix = l_ix + 1
            else:
                r_ix = r_ix - 1
                while r_ix > l_ix and nums[r_ix + 1] == nums[r_ix]:
                    r_ix = r_ix - 1
    return closest_sum

if __name__ == '__main__':
    assert threeSumClosest([-1,2,1,-4], 1) == 2

    print('done')