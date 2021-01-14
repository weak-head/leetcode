import pytest
from leetcode.p0325_maximum_size_subarray_sum_equals_k import maxSubArrayLen


@pytest.mark.parametrize(
    ("a", "expectation"),
    (
        (([1, -1, 5, -2, 3], 3), (4)),
        (([-2, -1, 2, 1], 1), (2)),
    ),
)
def test_len(a, expectation):
    assert maxSubArrayLen(a[0], a[1]) == expectation
