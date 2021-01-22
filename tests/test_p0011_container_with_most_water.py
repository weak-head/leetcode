import pytest
from leetcode.p0011_container_with_most_water import maxArea, maxArea2, maxArea3


@pytest.mark.parametrize(
    ("container", "area"),
    (
        ([1, 4], 1),
        ([4, 1], 1),
        ([1, 1, 1, 1, 1, 1, 1, 1], 7),
        ([1, 1, 1, 1, 100, 1, 1, 1], 7),
        ([1, 5, 1, 1, 1, 1, 1, 1], 7),
        ([1, 5, 1, 1, 1, 1, 1, 8], 30),
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([6, 14, 2, 11, 2, 7, 0, 9, 12, 7], 84),
    ),
)
def test_maxArea(container, area):
    assert maxArea(container) == area
    assert maxArea2(container) == area
    assert maxArea3(container) == area
