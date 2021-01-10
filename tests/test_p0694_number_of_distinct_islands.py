import pytest
from leetcode.p0694_number_of_distinct_islands import numDistinctIslands


@pytest.mark.parametrize(
    ("a", "expectation"),
    (
        (([[1, 1, 0], [0, 1, 1], [0, 0, 0], [1, 1, 1], [0, 1, 0]]), (2)),
        (([[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]), (1)),
    ),
)
def test_island(a, expectation):
    assert numDistinctIslands(a) == expectation
