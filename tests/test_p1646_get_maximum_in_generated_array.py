import pytest
from leetcode.p1646_get_maximum_in_generated_array import getMaximumGenerated


@pytest.mark.parametrize(
    ("a", "expectation"),
    (
        ((7), (3)),
        ((3), (2)),
        ((30), (8)),
        ((0), (0)),
        ((1), (1)),
        ((2), (1)),
    ),
)
def test_solve(a, expectation):
    assert getMaximumGenerated(a) == expectation
