# flake8: noqa: F403, F405
import pytest
from leetcode.p0820_short_encoding_of_words import *

solutions = [
    minimumLengthEncoding_trie,
    minimumLengthEncoding_substr,
    minimumLengthEncoding_set,
]

test_cases = [
    (["t"], 2),
    (["a", "b"], 4),
    (["time", "me", "bell"], 10),
    (["atime", "btime", "time"], 12),
    (["abcde", "bcde", "cde", "de"], 6),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
