import pytest
from leetcode.p0045_submissions import jump


@pytest.mark.parametrize(
    ("input", "res"),
    (([2, 3, 1, 1, 4], 2), ([], 0), ([1, 2, 1, 3, 1, 1, 2, 1, 1, 7], 5)),
)
def test_jump(input, res):
    assert jump(input) == res
