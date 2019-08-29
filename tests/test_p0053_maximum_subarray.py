import pytest
from leetcode.p0053_maximum_subarray import (
    max_subarray,
    max_subarray_3,
    max_subarray_4,
    max_subarray_5,
)


@pytest.mark.parametrize(
    ("nums", "expectation"), (([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),)
)
def test_max_subarray(nums, expectation):
    assert max_subarray(nums) == expectation
    assert max_subarray_3(nums) == expectation
    assert max_subarray_4(nums) == expectation
    assert max_subarray_5(nums) == expectation
