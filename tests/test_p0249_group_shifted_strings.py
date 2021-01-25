import pytest
from leetcode.p0249_group_shifted_strings import groupStrings


@pytest.mark.parametrize(
    ("a", "expectation"),
    (
        (
            (["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]),
            ([["abc", "bcd", "xyz"], ["az", "ba"], ["acef"], ["a", "z"]]),
        ),
    ),
)
def test_solve(a, expectation):
    assert sorted(groupStrings(a), key=len) == sorted(expectation, key=len)
