import pytest
from leetcode.p0594_longest_harmonious_subsequence import findLHS


@pytest.mark.parametrize(
    ("a", "expectation"),
    (
        (([1, 3, 2, 2, 5, 2, 3, 7]), (5)),
        (([1, 2, 3, 4]), (2)),
        (([1, 1, 1, 1]), (0)),
    ),
)
def test_solve(a, expectation):
    assert findLHS(a) == expectation
