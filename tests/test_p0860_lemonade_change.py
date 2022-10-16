# flake8: noqa: F403, F405
import pytest
from leetcode.p0860_lemonade_change import *

solutions = [
    lemonadeChange,
]

test_cases = [
    ([5, 5, 5, 10, 20], True),
    ([5, 5, 10, 10, 20], False),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
