import pytest
from leetcode.p0829_consecutive_numbers_sum import consecutiveNumbersSum


@pytest.mark.parametrize(
    ("a", "expectation"),
    (
        ((9548114), (4)),
        ((15), (4)),
    ),
)
def test_solve(a, expectation):
    assert consecutiveNumbersSum(a) == expectation
