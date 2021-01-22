import pytest
from leetcode.p1010_pairs_of_songs_with_total_durations_divisible_by_60 import (
    numPairsDivisibleBy60,
    numPairsDivisibleBy60_2,
)


@pytest.mark.parametrize(
    ("a", "expectation"),
    (
        ([], 0),
        ([20, 40], 1),
        ([60, 60, 60], 3),
        ([30, 20, 150, 100, 40], 3),
        ([15, 63, 451, 213, 37, 209, 343, 319], 1),
    ),
)
def test_pairs(a, expectation):
    assert numPairsDivisibleBy60(a) == expectation
    assert numPairsDivisibleBy60_2(a) == expectation
