# flake8: noqa: F403, F405
import pytest
from leetcode.p0524_longest_word_in_dictionary_through_deleting import *

solutions = [
    findLongestWord,
]

test_cases = [
    (["abpcplea", ["ale", "apple", "monkey", "plea"]], "apple"),
    (["abpcplea", ["ale", "bpple", "cpple", "monkey", "plea"]], "bpple"),
    (["abpcplea", ["ale", "apple", "bpple", "monkey", "plea"]], "apple"),
    (["abpcplea", ["ale", "apple", "bpple", "pcplea", "monkey", "plea"]], "pcplea"),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(*args) == expectation
