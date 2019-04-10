import pytest
from leetcode.p0001_two_sum import twoSum

@pytest.mark.parametrize(('nums', 'target', 'expectation'), (
    ([2, 7, 11, 15], 9, [0, 1]),
    ([2, 7, 11, 15, 17, 4, 21, 9], 20, [2, 7]),
    ([], 12, None),
    ([1, 3, 7, 15, 18, 22, 29], 9, None)
))
def test_twoSum(nums, target, expectation):
    result = twoSum(nums, target)
    assert result == expectation
