from typing import List

def maxArea(heights: List[int]) -> int:
    greatest_volume = 0
    for l_ix in range(0, len(heights)):
        for r_ix in range(l_ix, len(heights)):
            current_height = min(heights[l_ix], heights[r_ix])
            current_volume = (r_ix - l_ix) * current_height
            # if the current volume is greater than the current maximum
            if (current_volume > greatest_volume):
                greatest_volume = current_volume
    return greatest_volume

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