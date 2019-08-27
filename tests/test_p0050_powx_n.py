import pytest
from leetcode.p0050_powx_n import power, power2


@pytest.mark.parametrize(
    ("x", "n", "expectation"), ((0, 1, 0), (2.1, 3, 9.261000000000001), (2, -2, 0.25))
)
def test_power(x, n, expectation):
    assert power(x, n) == expectation
    assert power2(x, n) == expectation
