import pytest
from leetcode.p1658_minimum_operations_to_reduce_x_to_zero import minOperations


@pytest.mark.parametrize(
    ("a", "expectation"),
    (
        (([1, 1, 4, 2, 3], 5), (2)),
        (([3, 2, 20, 1, 1, 3], 10), (5)),
    ),
)
def test_minOps(a, expectation):
    assert minOperations(a[0], a[1]) == expectation
