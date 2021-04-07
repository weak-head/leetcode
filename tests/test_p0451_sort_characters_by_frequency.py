# flake8: noqa: F403, F405
import pytest
from leetcode.p0451_sort_characters_by_frequency import *

solutions = [
    frequencySort_bucket,
    frequencySort_pq,
]

test_cases = [
    ("tree", {"eert", "eetr"}),
    ("cccaaa", {"aaaccc", "cccaaa"}),
    ("Aabb", {"bbAa", "bbaA"}),
    ("abccddda", {"dddccaab", "dddaaccb"}),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) in expectation
