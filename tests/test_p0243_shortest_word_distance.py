import pytest
from leetcode.p0243_shortest_word_distance import shortestDistance


@pytest.mark.parametrize(
    ("a", "expectation"),
    (
        (
            (
                ["practice", "makes", "perfect", "coding", "makes"],
                "coding",
                "practice",
            ),
            (3),
        ),
        (
            (
                ["practice", "makes", "perfect", "coding", "makes"],
                "coding",
                "coding",
            ),
            (0),
        ),
    ),
)
def test_solve(a, expectation):
    assert shortestDistance(a[0], a[1], a[2]) == expectation
