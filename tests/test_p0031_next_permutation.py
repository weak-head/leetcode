import pytest
from leetcode.p0031_next_permutation import nextPermutation


@pytest.mark.parametrize(
    ("a", "expectation"),
    (
        (([3, 2, 1]), ([1, 2, 3])),
        (([1, 1, 1]), ([1, 1, 1])),
        (([1, 1, 2]), ([1, 2, 1])),
        (([1, 2, 1]), ([2, 1, 1])),
        (([2, 1, 1]), ([1, 1, 2])),
        (([1, 1, 1, 1, 1, 3]), ([1, 1, 1, 1, 3, 1])),
        (([1, 1, 1, 3, 1, 1]), ([1, 1, 3, 1, 1, 1])),
        (([1, 2, 1, 1, 1, 1, 0]), ([2, 0, 1, 1, 1, 1, 1])),
    ),
)
def test_solve(a, expectation):
    nextPermutation(a)
    assert a == expectation
