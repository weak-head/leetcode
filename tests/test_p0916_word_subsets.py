# flake8: noqa: F403, F405
import pytest
from leetcode.p0916_word_subsets import *

solutions = [
    wordSubsets,
]

test_cases = [
    (
        [["amazon", "apple", "facebook", "google", "leetcode"], ["e", "o"]],
        ["facebook", "google", "leetcode"],
    ),
    (
        [["amazon", "apple", "facebook", "google", "leetcode"], ["l", "e"]],
        ["apple", "google", "leetcode"],
    ),
    (
        [["amazon", "apple", "facebook", "google", "leetcode"], ["e", "oo"]],
        ["facebook", "google"],
    ),
    (
        [["amazon", "apple", "facebook", "google", "leetcode"], ["lo", "eo"]],
        ["google", "leetcode"],
    ),
    (
        [["amazon", "apple", "facebook", "google", "leetcode"], ["ec", "oc", "ceo"]],
        ["facebook", "leetcode"],
    ),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(*args) == expectation
