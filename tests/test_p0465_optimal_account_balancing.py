import pytest
from leetcode.p0465_optimal_account_balancing import minTransfers1, minTransfers2


@pytest.mark.parametrize(
    ("a", "expectation"),
    (
        (([[0, 1, 10], [2, 0, 5]]), 2),
        (([[0, 1, 10], [1, 0, 1], [1, 2, 5], [2, 0, 5]]), 1),
    ),
)
def test_transfers(a, expectation):
    assert minTransfers1(a) == expectation
    assert minTransfers2(a) == expectation
