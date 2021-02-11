# flake8: noqa: F403, F405
import pytest
from leetcode.p1335_minimum_difficulty_of_a_job_schedule import *

solutions = [
    minDifficulty_dp,
    minDifficulty_dp_space_saving,
    minDifficulty_dp_space_saving_optimized_stack,
]

#   ([args], expectation),
test_cases = [
    ([[9, 9, 9], 4], -1),
    ([[3, 3, 3], 3], 9),
    ([[1, 1, 1], 3], 3),
    ([[1, 1, 2, 1], 3], 4),
    ([[7, 1, 7, 1, 7, 1], 3], 15),
    ([[11, 111, 22, 222, 33, 333, 44, 444], 6], 843),
    ([[], 1], -1),
    ([[1, 2, 3, 4, 1, 1], 3], 6),
    ([[4, 3, 2, 1, 1, 1], 3], 6),
    ([[4, 3, 2, 1, 1, 1], 2], 5),
    ([[4, 3, 2, 1, 1, 1], 1], 4),
    ([[4, 3, 2, 1, 1, 1], 4], 7),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(*args) == expectation
