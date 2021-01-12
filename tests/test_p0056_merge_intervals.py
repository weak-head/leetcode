import pytest
from leetcode.p0056_merge_intervals import merge


@pytest.mark.parametrize(
    ("a", "expectation"),
    (
        (
            ([[1, 3], [2, 6], [8, 10], [15, 18]]),
            ([[1, 6], [8, 10], [15, 18]]),
        ),
        (
            ([[1, 3], [4, 5]]),
            ([[1, 3], [4, 5]]),
        ),
    ),
)
def test_(a, expectation):
    assert merge(a) == expectation
