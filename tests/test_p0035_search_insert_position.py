import pytest
from leetcode.p0035_search_insert_position import searchInsert


@pytest.mark.parametrize(('nums', 'target', 'index'), (
    ([1, 3, 5, 6], 5, 2),
    ([1, 3, 5, 6], 2, 1),
    ([1, 3, 5, 6], 7, 4),
    ([1, 3, 5, 6], 0, 0),
))
def test_search(nums, target, index):
    assert searchInsert(nums, target) == index
