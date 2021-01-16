import pytest
from leetcode.p0215_kth_largest_element_in_an_array import (
    findKthLargest,
    findKthLargest2,
)


@pytest.mark.parametrize(
    ("a", "expectation"),
    (
        (([3, 2, 1, 5, 6, 4], 2), (5)),
        (([3, 2, 1, 5, 6, 4], 1), (6)),
        (([3, 2, 1, 5, 6, 4], 6), (1)),
    ),
)
def test_solve(a, expectation):
    assert findKthLargest(a[0], a[1]) == expectation
    assert findKthLargest2(a[0], a[1]) == expectation
