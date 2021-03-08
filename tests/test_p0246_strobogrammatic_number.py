# flake8: noqa: F403, F405
import pytest
from leetcode.p0246_strobogrammatic_number import *

solutions = [
    isStrobogrammatic_1,
    isStrobogrammatic_2,
]

test_cases = [
    (181, True),
    (8822, False),
    (1961, True),
    (88588, False),
    (8888, True),
    (1069886901, True),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(str(args)) == expectation
