import pytest
from leetcode.p0015_3sum import threeSum

@pytest.mark.parametrize(('nums', 'sums'), (
    ( [-1, 0, 1, 2, -1, -4], [[-1, 0, 1], [-1, -1, 2]] ),
    ( [0, 0, 0], [[0, 0, 0]])
))
def test_threeSum(nums, sums):
    res = threeSum(nums)
    assert len(res) == len(sums)

    res = [tuple(sorted(el)) for el in res]
    sums = [tuple(sorted(s)) for s in sums]
    for s in sums:
        assert s in res