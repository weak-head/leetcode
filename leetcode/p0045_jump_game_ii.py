from typing import List


def jump(nums: List[int]) -> int:
    if not nums:
        return 0
    jumps = [10000000] * len(nums)
    jumps[0] = 0
    for ix, n in enumerate(nums):
        for jumpix in range(ix, ix + n + 1):
            if jumpix >= len(nums):
                break
            jumps[jumpix] = min(jumps[jumpix], jumps[ix] + 1)
    return jumps[-1]
