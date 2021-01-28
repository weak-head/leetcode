import pytest
from leetcode.p1663_smallest_string_with_a_given_numeric_value import (
    getSmallestString,
    getSmallestString2,
)


@pytest.mark.parametrize(
    ("a", "expectation"), (((3, 27), ("aay")), ((5, 73), ("aaszz")))
)
def test_solve(a, expectation):
    assert getSmallestString(a[0], a[1]) == expectation
    assert getSmallestString2(a[0], a[1]) == expectation
