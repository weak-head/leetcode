from typing import List


def trap(height: List[int]) -> int:
    """
    Two pointers, greedy

    As long as right_max[i] > left_max[i]
    water trapped depends on left_max.
    And similar in case if left_max[i] > right_max[i]
    watter trapped depends on right_max.

    Time: O(n)
    Space: O(1)
        n - number of elements in the array
    """
    if not height:
        return 0

    l, r = 0, len(height) - 1
    l_max, r_max = height[0], height[-1]
    volume = 0

    while l <= r:
        l_max = max(l_max, height[l])
        r_max = max(r_max, height[r])

        if l_max < r_max:
            volume += l_max - height[l]
            l += 1
        else:
            volume += r_max - height[r]
            r -= 1

    return volume


def trap2(height: List[int]) -> int:
    """
    Time: O(n)
    Space: O(n)
        n - number of elements in the array
    """
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
