import pytest
from leetcode.p0016_3sum_closest import threeSumClosest


@pytest.mark.parametrize(('input', 'target', 'result'), (
    ([-1, 2, 1, -4], 1, 2),
))
def test_threeSumCloses(input, target, result):
    assert threeSumClosest(input, target) == result