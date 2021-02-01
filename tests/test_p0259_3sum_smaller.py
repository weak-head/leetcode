import pytest
from leetcode.p0259_3sum_smaller import threeSumSmaller


@pytest.mark.parametrize(
    ("a", "expectation"),
    ((([-2, 0, 1, 3], 2), (2)), (([0], 0), (0)), (([-1, 1, -1, -1], -1), (1))),
)
def test_solve(a, expectation):
    assert threeSumSmaller(a[0], a[1]) == expectation
