# flake8: noqa: F403, F405
import pytest
from leetcode.p0692_top_k_frequent_words import *

solutions = [
    topKFrequent,
]

test_cases = [
    ([["i", "love", "leetcode", "i", "love", "coding"], 2], ["i", "love"]),
    (
        [["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4],
        ["the", "is", "sunny", "day"],
    ),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(*args) == expectation
