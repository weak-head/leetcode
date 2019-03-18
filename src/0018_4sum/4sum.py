from typing import List

def fourSum(nums: List[int], target: int) -> List[List[int]]:
    nums.sort()
    result = []
    nums_len = len(nums)
    a = 0
    while a < nums_len - 2:
        b = a + 1
        while b < nums_len - 1:
            l, r = b + 1, nums_len - 1
            while l < r:
                ab_sum = nums[a] + nums[b]
                lr_sum = nums[l] + nums[r]

                # exact match
                if ab_sum + lr_sum == target:
                    result.append([nums[a], nums[b], nums[l], nums[r]])

                # we need to increase l_r sum
                if lr_sum < (target - ab_sum):
                    l = l + 1
                    while nums[l - 1] == nums[l] and l < r:
                        l = l + 1
                # we need to reduce l_r sum
                else:
                    r = r - 1
                    while nums[r + 1] == nums[r] and l < r:
                        r = r - 1
            b = b + 1
            while nums[b] == nums[b - 1] and b < nums_len - 1:
                b = b + 1

        a = a + 1
        while nums[a] == nums[a - 1] and a < nums_len - 2:
            a = a + 1

    return result


if __name__ == '__main__':
    assert fourSum([1, 0, -1, 0, -2, 2], 0) == [
        [-1,  0, 0, 1],
        [-2, -1, 1, 2],
        [-2,  0, 0, 2]
    ]

    print('passed')
