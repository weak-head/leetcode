# flake8: noqa: F403, F405
import pytest
from leetcode.p0698_partition_to_k_equal_sum_subsets import *

solutions = [
    canPartitionKSubsets,
]

test_cases = [
    ([[4, 4, 6, 2, 3, 8, 10, 2, 10, 7], 4], True),
    ([[4, 3, 2, 3, 5, 2, 1], 4], True),
    ([[1, 2, 3, 4], 3], False),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(*args) == expectation
