import pytest
from leetcode.p0018_4sum import fourSum, fourSum2


@pytest.mark.parametrize(('nums', 'target', 'expectation'), (
    ([1, 0, -1, 0, -2, 2], 0, [(-1, 0, 0, 1), (-2, -1, 1, 2), (-2, 0, 0, 2)]),
))
def test_fourSum(nums, target, expectation):
    res = fourSum(nums, target)
    assert len(res) == len(expectation)

    res = [tuple(sorted(k)) for k in res]
    exp = [tuple(sorted(k)) for k in expectation]

    for e in exp:
        assert e in res