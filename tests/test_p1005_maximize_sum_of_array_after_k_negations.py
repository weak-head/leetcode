import pytest
from leetcode.p1005_maximize_sum_of_array_after_k_negations import (
    largestSumAfterKNegations,
)


@pytest.mark.parametrize(
    ("array", "k", "resulting_sum"),
    (([4, 2, 3], 1, 5), ([3, -1, 0, 2], 3, 6), ([2, -3, -1, 5, -4], 2, 13)),
)
def test_largest_sum(array, k, resulting_sum):
    largestSumAfterKNegations(array, k) == resulting_sum
