from typing import List

# O(n^2)
def maxArea3(heights: List[int]) -> int:
    greatest_volume = 0
    for l_ix in range(0, len(heights)):
        for r_ix in range(l_ix, len(heights)):
            current_height = min(heights[l_ix], heights[r_ix])
            current_volume = (r_ix - l_ix) * current_height
            # if the current volume is greater than the current maximum
            if (current_volume > greatest_volume):
                greatest_volume = current_volume
    return greatest_volume

# O(n)
# greedy with overhead
def maxArea2(heights: List[int]) -> int:
    max_height, h_len = 0, len(heights)
    coverage = [0] * (h_len)
    for ix in range(0, h_len):
        max_height = max(max_height, heights[ix])
        coverage[ix] = max_height

    max_height = 0
    for ix in range(h_len - 1, -1, -1):
        max_height = max(max_height, heights[ix])
        coverage[ix] = min(coverage[ix], max_height)

    for ix in range(0, h_len - 1):
        coverage[ix] = min(coverage[ix], coverage[ix+1])

    max_volume, l_ix, r_ix = 0, 0, h_len - 2
    while l_ix <= r_ix:
        min_height = min(coverage[l_ix], coverage[r_ix])
        volume = min_height * (r_ix - l_ix + 1)
        if volume > max_volume:
            max_volume = volume
        if coverage[l_ix] < coverage[r_ix]:
            l_ix = l_ix + 1
        else:
            r_ix = r_ix - 1

    return max_volume

# O(n)
# greedy without overhead
def maxArea(heights: List[int]) -> int:
    l_ix, r_ix = 0, len(heights) - 1
    max_volume = 0
    while l_ix < r_ix:
        current_volume = min(heights[l_ix], heights[r_ix]) * (r_ix - l_ix)
        max_volume = max(max_volume, current_volume)
        if heights[l_ix] < heights[r_ix]:
            l_ix = l_ix + 1
        else:
            r_ix = r_ix - 1
    return max_volume

if __name__ == '__main__':
    assert maxArea([1,4]) == 1
    assert maxArea([4,1]) == 1
    assert maxArea([1,1,1,1,1,1,1,1]) == 7
    assert maxArea([1,1,1,1,100,1,1,1]) == 7
    assert maxArea([1,5,1,1,1,1,1,1]) == 7
    assert maxArea([1,5,1,1,1,1,1,8]) == 30
    assert maxArea([1,8,6,2,5,4,8,3,7]) == 49
    assert maxArea([6,14,2,11,2,7,0,9,12,7]) == 84

    print('passed')