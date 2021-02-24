# flake8: noqa: F403, F405
import pytest
from leetcode.p0651_4_keys_keyboard import *

solutions = [
    maxA,
    maxA_naive_slow,
]

test_cases = [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 9),
    (15, 81),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
