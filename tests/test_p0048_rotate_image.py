import pytest
from leetcode.p0048_rotate_image import rotate


@pytest.mark.parametrize(("a", "expectation"), (((), ()),))
def test_rotate(a, expectation):
    assert rotate is not None
    pass
    # assert solve(a) == expectation
