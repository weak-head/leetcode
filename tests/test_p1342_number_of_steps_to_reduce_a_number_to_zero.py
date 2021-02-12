# flake8: noqa: F403, F405
import pytest
from leetcode.p1342_number_of_steps_to_reduce_a_number_to_zero import *

solutions = [
    numberOfSteps,
]

#   ([args], expectation),
test_cases = [
    (0, 0),
    (14, 6),
    (2, 2),
    (1, 1),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
