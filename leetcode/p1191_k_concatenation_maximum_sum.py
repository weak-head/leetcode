from typing import List


def kConcatenationMaxSum(arr: List[int], k: int) -> int:
    """
    # TODO
    """
    mod = 10 ** 9 + 7

    def kadane(arr):
        current = max_sum = 0
        for i in range(len(arr)):
            current = max(current + arr[i], arr[i])
            max_sum = max(max_sum, current)
        return max_sum

    if k > 1:
        ksum = kadane(arr * 2)
        csum = (k - 2) * max(sum(arr), 0)
        return (ksum + csum) % mod
    else:
        return kadane(arr) % mod
