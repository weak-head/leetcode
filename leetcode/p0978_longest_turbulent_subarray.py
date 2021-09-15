from typing import List


def maxTurbulenceSize(arr: List[int]) -> int:
    """
    Time: O(n)
    Space: O(1)
        n - length of the array
    """
    current = max_size = 0

    for i in range(len(arr)):
        if i >= 2 and (
            (arr[i - 2] < arr[i - 1] > arr[i]) or (arr[i - 2] > arr[i - 1] < arr[i])
        ):
            current += 1
        elif i >= 1 and (arr[i - 1] != arr[i]):
            current = 2
        else:
            current = 1
        max_size = max(max_size, current)

    return max_size
