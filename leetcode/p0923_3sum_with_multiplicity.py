from typing import List
from collections import Counter
from itertools import combinations_with_replacement


def threeSumMulti(arr: List[int], target: int) -> int:
    """
    Count the occurrence of each number.

    Loop i on all numbers,
    Loop j on all numbers,
    Check if k = target - i - j is valid.

    Add the number of this combination to result.
    3 cases covers all possible combination:
        i == j == k
        i == j != k
        i < k && j < k

    Time: O(n * m * m)
    Space: O(n)
        n - length of the array
        m - max value in the array
    """
    c = Counter(arr)
    res = 0

    for i, j in combinations_with_replacement(c, 2):
        k = target - i - j
        if i == j == k:
            res += c[i] * (c[i] - 1) * (c[i] - 2) / 6
        elif i == j != k:
            res += c[i] * (c[i] - 1) / 2 * c[k]
        elif k > i and k > j:
            res += c[i] * c[j] * c[k]

    return int(res % (10 ** 9 + 7))
