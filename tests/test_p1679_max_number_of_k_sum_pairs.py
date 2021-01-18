import pytest
from leetcode.p1679_max_number_of_k_sum_pairs import maxOperations


@pytest.mark.parametrize(
    ("a", "expectation"),
    (
        (([1, 2, 3, 4], 5), (2)),
        (([3, 1, 3, 4, 3], 6), (1)),
        (([2, 5, 4, 4, 1, 3, 4, 4, 1, 4, 4, 1, 2, 1, 2, 2, 3, 2, 4, 2], 3), (4)),
    ),
)
def test_solve(a, expectation):
    assert maxOperations(a[0], a[1]) == expectation
