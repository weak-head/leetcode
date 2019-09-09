import pytest
from leetcode.p0343_integer_break import integer_break


@pytest.mark.parametrize(("input", "expectation"), ((2, 1), (10, 36)))
def test_integer_break(input, expectation):
    assert integer_break(input) == expectation
