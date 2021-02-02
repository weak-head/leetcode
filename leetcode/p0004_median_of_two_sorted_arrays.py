from typing import List


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    """
    Find median using find k-th element.

    Time: O(log(min(n, m)))
        n - length of first array
        m - length of second array

    Space: O(1)
    """
    n1, n2 = len(nums1), len(nums2)
    k = (n1 + n2) >> 1

    if (n1 + n2) % 2 == 0:
        v1 = kth(nums1, nums2, 0, n1 - 1, 0, n2 - 1, k - 1)
        v2 = kth(nums1, nums2, 0, n1 - 1, 0, n2 - 1, k)
        return (v1 + v2) / 2
    else:
        return kth(nums1, nums2, 0, n1 - 1, 0, n2 - 1, k)


def kth(a, b, al, ar, bl, br, k):
    """
    Find k-th element of two sorted arrays.
    """
    if al > ar:
        return b[k - al]
    if bl > br:
        return a[k - bl]

    am = (al + ar) >> 1
    bm = (bl + br) >> 1
    if am + bm < k:  # need to increase the total index
        if a[am] < b[bm]:
            return kth(a, b, am + 1, ar, bl, br, k)
        else:
            return kth(a, b, al, ar, bm + 1, br, k)
    else:  # need to reduce the total index
        if a[am] > b[bm]:
            return kth(a, b, al, am - 1, bl, br, k)
        else:
            return kth(a, b, al, ar, bl, bm - 1, k)
