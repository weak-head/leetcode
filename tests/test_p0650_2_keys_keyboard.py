# flake8: noqa: F403, F405
import pytest
from leetcode.p0650_2_keys_keyboard import *

solutions = [
    minSteps_dp,
    minSteps_prime,
]

test_cases = [
    (3, 3),
    (10, 7),
    (237, 82),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
