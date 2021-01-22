import pytest
from leetcode.p0161_one_edit_distance import isOneEditDistance


@pytest.mark.parametrize(
    ("a", "expectation"),
    (
        (
            ("abc", "aabc"),
            (True),
        ),
        (
            ("abc", "abc"),
            (False),
        ),
    ),
)
def test_solve(a, expectation):
    assert isOneEditDistance(a[0], a[1]) == expectation
