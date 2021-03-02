# flake8: noqa: F403, F405
import pytest
from leetcode.p0645_set_mismatch import *

solutions = [
    findErrorNums_map,
    findErrorNums_optimized,
]

test_cases = [
    ([1, 1], [1, 2]),
    ([2, 2], [2, 1]),
    ([2, 3, 2, 4], [2, 1]),
    ([1, 2, 3, 2], [2, 4]),
    ([1, 1, 2, 3], [1, 4]),
    ([4, 2, 2, 1], [2, 3]),
    ([3, 1, 1, 4], [1, 2]),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert tuple(solution(args)) == tuple(expectation)
