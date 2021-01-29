import pytest
from leetcode.p0075_sort_colors import sortColors


@pytest.mark.parametrize(
    ("a", "expectation"),
    (
        (([2, 2, 2, 1, 2, 1, 0, 0, 2]), ([0, 0, 1, 1, 2, 2, 2, 2, 2])),
        (([2, 1, 0]), ([0, 1, 2])),
    ),
)
def test_solve(a, expectation):
    sortColors(a)
    assert a == expectation
