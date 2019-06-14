from typing import List


def jump(nums: List[int]) -> int:
    """
    O(n^2)
    """
    if not nums:
        return 0
    jumps = [10000000] * len(nums)
    jumps[0] = 0
    for ix, n in enumerate(nums):
        for jumpix in range(ix, ix + n + 1):
            if jumpix == len(nums):
                return jumps[-1]
            jumps[jumpix] = min(jumps[jumpix], jumps[ix] + 1)
    return jumps[-1]


# ------------


def max_val(nums, l, r):
    m_ix, m_val = l, nums[l]
    for ix in range(l, r + 1):
        if ix + nums[ix] >= m_ix + m_val:
            m_ix, m_val = ix, nums[ix]
    return m_ix, m_val


def jump2(nums):
    """
    O(n)
    """
    nums_max_ix = len(nums) - 1
    if nums == [] or nums[0] == 0 or nums_max_ix == 0:
        return 0

    m_ix, m_val = 0, nums[0]
    jumps = 0
    while True:
        jumps += 1
        if m_ix + m_val >= nums_max_ix:
            break

        m_ix, m_val = max_val(nums, m_ix + 1, m_ix + m_val)

    return jumps
