import pytest
from leetcode.p1013_partition_array_into_three_parts_with_equal_sum import (
    canThreePartsEqualSum,
)


@pytest.mark.parametrize(
    ("a", "expectation"),
    (
        ([0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1], True),
        ([0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1], False),
        ([3, 3, 6, 5, -2, 2, 5, 1, -9, 4], True),
        ([0, 0, 0, 0, 0, 0], True),
        ([0, 0, 0], True),
        ([0, 0], False),
        ([-1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1], True),
        ([-1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, 1, 1, 1], True),
        ([-1, 1, 1, 1, -1, 1, -1, 1, -1, 1, -1, 1, 1, -1, 1], True),
        ([1, 1, 1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, -1, 1], False),
    ),
)
def test_(a, expectation):
    assert canThreePartsEqualSum(a) == expectation
