import pytest
from leetcode.p1153_string_transforms_into_another_string import canConvert


@pytest.mark.parametrize(
    ("a", "expectation"),
    (
        (
            ("aabcc", "bbadd"),
            (True),
        ),
        (
            ("ccbbb", "bfbee"),
            (False),
        ),
    ),
)
def test_canConvert(a, expectation):
    assert canConvert(a[0], a[1]) == expectation
