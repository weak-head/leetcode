import pytest
from leetcode.p0064_minimum_path_sum import minPathSum


@pytest.mark.parametrize(
    ("a", "expectation"), ((([[1, 3, 1], [1, 5, 1], [4, 2, 1]]), (7)),)
)
def test_solve(a, expectation):
    assert minPathSum(a) == expectation
