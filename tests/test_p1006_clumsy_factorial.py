import pytest
from leetcode.p1006_clumsy_factorial import clumsy


@pytest.mark.parametrize(('n', 'res'), (
    (10, 12),
    (4, 7)
))
def test_clumsy(n, res):
    assert clumsy(n) == res