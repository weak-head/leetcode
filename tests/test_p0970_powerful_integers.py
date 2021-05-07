# flake8: noqa: F403, F405
import pytest
from leetcode.p0970_powerful_integers import *

solutions = [
    powerfulIntegers,
]

test_cases = [
    ([2, 3, 10], set([2, 3, 4, 5, 7, 9, 10])),
    ([3, 5, 15], set([2, 4, 6, 8, 10, 14])),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert set(solution(*args)) == expectation
