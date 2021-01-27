import pytest
from leetcode.p1680_concatenation_of_consecutive_binary_numbers import (
    concatenatedBinary_fast,
    concatenatedBinary_slow,
)


@pytest.mark.parametrize(("a", "expectation"), (((3), (27)), ((1), (1))))
def test_solve(a, expectation):
    assert concatenatedBinary_slow(a) == expectation
    assert concatenatedBinary_fast(a) == expectation
