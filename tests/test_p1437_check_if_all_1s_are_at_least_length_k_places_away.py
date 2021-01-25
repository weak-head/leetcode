import pytest
from leetcode.p1437_check_if_all_1s_are_at_least_length_k_places_away import (
    kLengthApart,
)


@pytest.mark.parametrize(
    ("a", "expectation"),
    (
        (([], 17), (True)),
        (([0], 1), (True)),
        (([1, 0, 0, 1], 2), (True)),
        (([1, 0, 0, 1], 3), (False)),
        (([1, 1, 1, 1], 0), (True)),
        (([1, 1, 1, 1], 1), (False)),
    ),
)
def test_solve(a, expectation):
    assert kLengthApart(a[0], a[1]) == expectation
