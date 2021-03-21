from typing import List


def pancakeSort(arr: List[int]) -> List[int]:
    """
    Time: O(n^2)
    Space: O(1)
        n - length of the array
    """
    if not arr:
        return arr

    def reverse(a, n):
        l, r = 0, n
        while l < r:
            a[l], a[r] = a[r], a[l]
            l += 1
            r -= 1

    flips = []
    for n in range(len(arr) - 1, 0, -1):
        max_v, max_i = float("-inf"), 0
        for i in range(n + 1):
            if arr[i] > max_v:
                max_v = arr[i]
                max_i = i
        flips.append(max_i + 1)
        flips.append(n + 1)
        reverse(arr, max_i)  # max moves to head of the list
        reverse(arr, n)  # max moves to 'n'

    return flips
