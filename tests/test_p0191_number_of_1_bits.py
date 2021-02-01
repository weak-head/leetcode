import pytest
from leetcode.p0191_number_of_1_bits import hammingWeight, hammingWeight2


@pytest.mark.parametrize(("a", "expectation"), (((4), (1)), ((9), (2))))
def test_solve(a, expectation):
    assert hammingWeight(a) == expectation
    assert hammingWeight2(a) == expectation
