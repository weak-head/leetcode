import pytest
from leetcode.p0004_median_of_two_sorted_arrays import findMedianSortedArrays


@pytest.mark.parametrize(
    ("a", "b", "exp"),
    (
        ([], [1], 1),
        ([], [2, 3, 4, 5, 6, 7, 8, 9, 10], 6),
        ([], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5.5),
        ([1], [], 1),
        ([2, 3, 4, 5, 6, 7, 8, 9, 10], [], 6),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [], 5.5),
        ([1], [2], 1.5),
        ([1, 2], [3, 4], 2.5),
        ([1, 2, 3], [4, 5, 6], 3.5),
        ([1, 3], [2], 2),
        ([1, 3, 5, 8, 9, 10], [2, 4, 6, 7, 11], 6),
        ([1, 3, 5], [2, 4, 6], 3.5),
        ([1], [2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 6),
        ([1], [2, 3, 4, 5, 6, 7, 8, 9, 10], 5.5),
        ([2, 3, 4, 5, 6, 7, 8, 9, 10], [1], 5.5),
        ([2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [1], 6),
        ([3, 4, 5, 6, 7], [1, 2], 4),
        ([6, 7, 8], [9, 10, 11], 8.5),
    ),
)
def test_findMedian(a, b, exp):
    assert findMedianSortedArrays(a, b) == exp
