# flake8: noqa: F403, F405
import pytest
from leetcode.p0278_first_bad_version import *

solutions = [
    firstBadVersion,
]

test_cases = [
    (500, 5),
    (50, 4),
    (20, 1),
    (20, 20),
    (501, 1),
    (501, 501),
    (501, 50),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    isBad = lambda x: x >= expectation
    assert solution(args, isBad) == expectation
