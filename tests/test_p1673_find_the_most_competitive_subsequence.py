import pytest
from leetcode.p1673_find_the_most_competitive_subsequence import mostCompetitive


@pytest.mark.parametrize(
    ("a", "expectation"),
    (
        (([3, 5, 2, 6], 2), ([2, 6])),
        (([2, 4, 3, 3, 5, 4, 9, 6], 4), ([2, 3, 3, 4])),
    ),
)
def test_solve(a, expectation):
    assert mostCompetitive(a[0], a[1]) == expectation
