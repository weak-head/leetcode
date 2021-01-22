import pytest
from leetcode.p0244_shortest_word_distance_ii import WordDistance


@pytest.mark.parametrize(
    ("a", "expectation"),
    (
        (
            (
                ["practice", "makes", "perfect", "coding", "makes"],
                ["coding", "practice"],
            ),
            (3),
        ),
        (
            (["practice", "makes", "perfect", "coding", "makes"], ["coding", "makes"]),
            (1),
        ),
    ),
)
def test_solve(a, expectation):
    w = WordDistance(a[0])
    assert w.shortest(a[1][0], a[1][1]) == expectation
