# flake8: noqa: F403, F405
import pytest
from leetcode.p1165_single_row_keyboard import *

solutions = [
    calculateTime,
]

test_cases = [
    (["abcdefghijklmnopqrstuvwxyz", "cba"], 4),
    (["pqrstuvwxyzabcdefghijklmno", "leetcode"], 73),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(*args) == expectation
