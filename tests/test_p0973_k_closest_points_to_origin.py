# flake8: noqa: F403, F405
import pytest
from leetcode.p0973_k_closest_points_to_origin import *

solutions = [
    kClosest_k,
    kClosest_n,
]

#   ([args], expectation),
test_cases = [
    ([[[1, 3], [-2, 2]], 1], [(-2, 2)]),
    ([[[1, 3], [-2, 2], [-1, -1]], 1], [(-1, -1)]),
    ([[[1, 3], [-2, 2], [-1, -1]], 2], [(-2, 2), (-1, -1)]),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert set(solution(*args)) == set(expectation)
