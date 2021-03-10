# flake8: noqa: F403, F405
import pytest
from leetcode.p0072_edit_distance import *

solutions = [
    minDistance,
    minDistance_optimized,
]

test_cases = [
    (["intention", "execution"], 5),
    (["abc", "abc"], 0),
    (["abb", "cbb"], 1),
    (["horse", "ros"], 3),
    (["the book is next to lamp", "the lamp is next to book"], 8),
    (["smart pets", "naughty dogs"], 9),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(*args) == expectation
