import pytest
from leetcode.p0007_reverse_integer import reverse


@pytest.mark.parametrize(
    ("x", "exp"),
    ((123, 321), (0, 0), (9, 9), (-123, -321), (-(2 ** 31) - 1, 0), (2 ** 31, 0)),
)
def test_reverse(x, exp):
    assert reverse(x) == exp
