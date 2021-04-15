# flake8: noqa: F403, F405
import pytest
from leetcode.p0509_fibonacci_number import *

solutions = [
    fib,
]

test_cases = [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (10, 55),
    (15, 610),
    (150, 9969216677189303386214405760200),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
