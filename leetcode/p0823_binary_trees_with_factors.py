from typing import List


def numFactoredBinaryTrees(a: List[int]) -> int:
    """
    Dynamic programming

    Each node should be equal to the product of its both children.

    Time: O(n^2)
    Space: O(n)
        n - length of the array
    """
    mod = 10 ** 9 + 7
    a.sort()
    index = {v: i for i, v in enumerate(a)}  # val -> ix
    m = [1] * len(a)

    for root in range(len(a)):  # ascending order
        for first_child in range(root):
            if a[root] % a[first_child] != 0:
                continue

            second_child = a[root] / a[first_child]
            if second_child in index:
                m[root] += m[first_child] * m[index[second_child]]
                m[root] %= mod

    return sum(m) % mod
