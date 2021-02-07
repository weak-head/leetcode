# flake8: noqa: F403, F405
import pytest
from leetcode.p0821_shortest_distance_to_a_character import *

solutions = [
    shortestToChar,
    shortestToChar2,
]

#   ([args], expectation),
test_cases = [
    (["aaba", "b"], [2, 1, 0, 1]),
    (["baabab", "b"], [0, 1, 1, 0, 1, 0]),
    (["abaa", "b"], [1, 0, 1, 2]),
    (["loveleetcode", "e"], [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solve(args, expectation, solution):
    assert solution(*args) == expectation
