# flake8: noqa: F403, F405
import pytest
from leetcode.p0347_top_k_frequent_elements import *

solutions = [
    topKFrequent,
]

test_cases = [
    ([[1, 1, 1, 2, 2, 3], 2], [1, 2]),
    ([[1], 1], [1]),
    ([[1, 2, 3, 4, 5, 6, 3, 2, 3], 1], [3]),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert set(solution(*args)) == set(expectation)
