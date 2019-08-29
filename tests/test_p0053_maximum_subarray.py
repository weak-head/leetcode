import pytest
from leetcode.p0053_maximum_subarray import (
    max_subarray,
    max_subarray_2,
    max_subarray_3,
    max_subarray_4,
    max_subarray_5,
)

test_cases = (
    ([4], 4),
    ([-1, -3, -7], -1),
    ([-1, 1, -2, -7], 1),
    ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
)


@pytest.mark.parametrize(("nums", "expectation"), test_cases)
def test_max_subarray_1(nums, expectation):
    assert max_subarray(nums) == expectation


@pytest.mark.parametrize(("nums", "expectation"), test_cases)
def test_max_subarray_2(nums, expectation):
    assert max_subarray_2(nums) == expectation


@pytest.mark.parametrize(("nums", "expectation"), test_cases)
def test_max_subarray_3(nums, expectation):
    assert max_subarray_3(nums) == expectation


@pytest.mark.parametrize(("nums", "expectation"), test_cases)
def test_max_subarray_4(nums, expectation):
    assert max_subarray_4(nums) == expectation


@pytest.mark.parametrize(("nums", "expectation"), test_cases)
def test_max_subarray_5(nums, expectation):
    assert max_subarray_5(nums) == expectation
