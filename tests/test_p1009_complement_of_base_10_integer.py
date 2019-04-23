import pytest
from leetcode.p1009_complement_of_base_10_integer import bitwiseComplement


@pytest.mark.parametrize(('a', 'expectation'), (
    (5, 2),
    (11, 4),
    (7, 0),
    (2, 1),
    (0, 1),
    (32, 31),
    (33, 30)
))
def test_bitwiseComplement(a, expectation):
    assert bitwiseComplement(a) == expectation
