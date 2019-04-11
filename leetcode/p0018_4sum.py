from typing import List

def fourSum2(nums: List[int], target: int) -> List[List[int]]:
    '''O(n^3)'''
    nums.sort()
    result = []
    nums_len = len(nums)
    a = 0
    while a < nums_len - 2:
        b = a + 1
        while b < nums_len - 1:
            l, r = b + 1, nums_len - 1
            ab_sum = nums[a] + nums[b]
            while l < r:
                if (nums[l] * 2 > (target - ab_sum)) or (nums[r] * 2 < (target - ab_sum)):
                    break

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

def fourSum(nums: List[int], target: int) -> List[List[int]]:
    '''Generalization to N-sum'''
    nums.sort()
    result = []

    # Reduce sum to two-sum
    def get_sum(l, r, n, target, current_sum):
        # any combination of the elements will not yield the target
        if (r - l + 1 < n) or (nums[l] * n > target) or (nums[r] * n < target):
            return

        # two sum
        if n == 2:
            while l < r:
                lr_sum = nums[l] + nums[r]
                if lr_sum == target:
                    result.append(current_sum + [nums[l], nums[r]])

                if lr_sum < target:
                    l = l + 1
                    while l < r and nums[l] == nums[l-1]:
                        l = l + 1
                else:
                    r = r - 1
                    while l < r and nums[r] == nums[r+1]:
                        r = r - 1
        # reduce
        else:
            for ix in range(l, r + 1):
                if ix == l or (ix > l and nums[ix] != nums[ix-1]):
                    get_sum(ix + 1, r, n - 1, target - nums[ix], current_sum + [nums[ix]])

    get_sum(0, len(nums) - 1, 4, target, [])
    return result


if __name__ == '__main__':

    nsum = fourSum([1, 0, -1, 0, -2, 2], 0)
    assert [-1,  0, 0, 1] in nsum
    assert [-2, -1, 1, 2] in nsum
    assert [-2,  0, 0, 2] in nsum
    assert len(nsum) == 3

    print('passed')
