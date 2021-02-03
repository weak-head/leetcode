from typing import List


def fourSum(nums: List[int], target: int) -> List[List[int]]:
    """
    Time: O(n^3)
    Space: O(n^3)
        n - number of elements in array
    """
    return nSum(nums, target, 4)


def nSum(nums: List[int], target: int, n: int) -> List[List[int]]:
    """
    Generalization of n-sum

    Time: O(k ^ (n - 1))
    Space: O(k ^ (n - 1))
        k - number of elements in the array
        n - number of elements to sum to get the target
    """
    nums.sort()
    result = []

    def get_sum(l, r, n, target, current_sum):
        """
        Reduce the n-sum problem to 2-sum problem
        """
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
                    while l < r and nums[l] == nums[l - 1]:
                        l = l + 1
                else:
                    r = r - 1
                    while l < r and nums[r] == nums[r + 1]:
                        r = r - 1
        # reduce
        else:
            for ix in range(l, r + 1):
                if ix == l or (ix > l and nums[ix] != nums[ix - 1]):
                    get_sum(
                        ix + 1, r, n - 1, target - nums[ix], current_sum + [nums[ix]]
                    )

    get_sum(0, len(nums) - 1, n, target, [])
    return result
