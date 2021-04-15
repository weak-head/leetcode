from typing import List


def minSwaps(data: List[int]) -> int:
    """
    Sliding window

    Window size is the number of '1'.
    Swaps required for the window are the number of '0'.

    Time: O(n)
    Space: O(1)
    """

    # window size is the number of '1' in the array
    window_size = sum((1 for v in data if v == 1))

    # expand to the window size and calculate the number of zeros
    zeros_count = sum((1 for v in data[:window_size] if v == 0))
    min_swaps = zeros_count
    l, r = 0, window_size - 1

    while r < len(data) - 1:
        if data[l] == 0:
            zeros_count -= 1
        if data[r + 1] == 0:
            zeros_count += 1
        r += 1
        l += 1
        min_swaps = min(min_swaps, zeros_count)

    return min_swaps
