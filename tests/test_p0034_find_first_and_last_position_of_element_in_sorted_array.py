import pytest
from leetcode.p0034_find_first_and_last_position_of_element_in_sorted_array import (
    searchRange,
)


@pytest.mark.parametrize(
    ("a", "target", "expectation"),
    (
        ([5, 7, 7, 8, 8, 10], 8, [3, 4]),
        ([5, 7, 7, 8, 8, 10], 5, [0, 0]),
        ([5, 7, 7, 8, 8, 10], 10, [5, 5]),
        ([5, 7, 7, 8, 8, 10], 7, [1, 2]),
        ([5, 7, 7, 8, 8, 10], 6, [-1, -1]),
        ([2, 2, 2, 2, 2, 2], 2, [0, 5]),
        ([2, 2, 2, 2, 2, 2], 1, [-1, -1]),
        ([2, 2, 2, 2, 2, 2], 3, [-1, -1]),
        ([], 2, [-1, -1]),
    ),
)
def test_search(a, target, expectation):
    assert searchRange(a, target) == expectation
