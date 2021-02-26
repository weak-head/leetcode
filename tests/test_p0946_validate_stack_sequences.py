# flake8: noqa: F403, F405
import pytest
from leetcode.p0946_validate_stack_sequences import *

solutions = [
    validateStackSequences,
]

test_cases = [
    ([[1, 2, 3], [3, 2, 1]], True),
    ([[1, 2, 3], [1, 2, 3]], True),
    ([[1, 2, 3], [2, 3, 1]], True),
    ([[1, 2, 3, 4, 5], [4, 5, 3, 2, 1]], True),
    ([[1, 2, 3, 4, 5], [4, 3, 5, 1, 2]], False),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(*args) == expectation
