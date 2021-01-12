import pytest
from leetcode.p0986_interval_list_intersections import intervalIntersection


@pytest.mark.parametrize(
    ("a", "expectation"),
    (
        (
            (
                [[0, 2], [5, 10], [13, 23], [24, 25]],
                [[1, 5], [8, 12], [15, 24], [25, 26]],
            ),
            ([[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]),
        ),
    ),
)
def test_(a, expectation):
    assert intervalIntersection(a[0], a[1]) == expectation
