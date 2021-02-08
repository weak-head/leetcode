from typing import List


def jump(nums: List[int]) -> int:
    """
    Time: O(n)
    Space: O(1)
        n - length of the input array
    """
    if len(nums) < 2:
        return 0

    jump_edge = max_reachable = nums[0]
    jumps = 1

    for i in range(len(nums)):

        # we have reached the edge of the jump,
        # now we can see the next reachable edge
        if i > jump_edge:
            jumps += 1
            jump_edge = max_reachable

        # max
        max_reachable = max(max_reachable, i + nums[i])

    return jumps
