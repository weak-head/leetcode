# flake8: noqa: F403, F405
import pytest
from leetcode.p0474_ones_and_zeroes import *

solutions = [
    findMaxForm,
]

test_cases = [
    ([["10", "0001", "111001", "1", "0"], 5, 3], 4),
    ([["10", "0", "1"], 1, 1], 2),
    ([["1", "1", "1", "111", "0", "01", "000", "0"], 3, 4], 6),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(*args) == expectation
