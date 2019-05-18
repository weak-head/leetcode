from typing import List


def trap(height: List[int]) -> int:
    res, res_len = list(height), len(height)

    max_v = 0
    for i in range(res_len):
        max_v = max(max_v, height[i])
        res[i] = max_v

    max_v = 0
    for i in range(res_len - 1, -1, -1):
        max_v = max(max_v, height[i])
        res[i] = min(res[i], max_v)

    volume = 0
    for i in range(res_len):
        volume = volume + (res[i] - height[i])

    return volume
