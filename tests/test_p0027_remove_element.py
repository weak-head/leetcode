import pytest
from leetcode.p0027_remove_element import removeElement


@pytest.mark.parametrize(
    ("nums", "val", "new_nums"),
    (
        ([3, 2, 2, 3], 2, [3, 3]),
        ([3, 2, 2, 3], 3, [2, 2]),
        ([0, 1, 2, 2, 3, 0, 4, 2], 2, [0, 1, 3, 0, 4]),
        ([3, 2, 2, 3], 7, [3, 2, 2, 3]),
        ([], 10, []),
    ),
)
def test_remove(nums, val, new_nums):
    ix = removeElement(nums, val)
    assert ix == len(new_nums)
    for i in range(ix):
        assert nums[i] == new_nums[i]
