import pytest
from leetcode.p0041_first_missing_positive import firstMissingPositive


@pytest.mark.parametrize(
    ("a", "expectation"),
    (
        ([-1, 4, 2, 1, 9, 10], 3),
        ([-1, 2, 3, 5, 1, 2, 0, 9, 6, 7], 4),
        ([3, 4, -1, 1], 2),
        ([1, 2, 0], 3),
        ([], 1),
        ([3, 5, 4, 2, 1, 6, 9, 7, 8], 10),
    ),
)
def test_firstMissing(a, expectation):
    assert firstMissingPositive(a) == expectation
