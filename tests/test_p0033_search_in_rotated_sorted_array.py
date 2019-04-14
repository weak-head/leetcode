import pytest
from leetcode.p0033_search_in_rotated_sorted_array import search


@pytest.mark.parametrize(('nums', 'target', 'index'), (
    ([1], 1, 0),
    ([4,5,6,7,0,1,2], 3, -1),
    ([4,5,6,7,0,1,2], 0, 4),
    ([4,5,6,7,0,1,2], 1, 5)
))
def test_search(nums, target, index):
    assert search(nums, target) == index