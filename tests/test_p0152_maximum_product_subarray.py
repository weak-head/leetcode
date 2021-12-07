# flake8: noqa: F403, F405
import pytest
from leetcode.p0152_maximum_product_subarray import *

solutions = [
    maxProduct,
]

test_cases = [
    ([2, 3, -2, 4], 6),
    ([-2, 0, -1], 0),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
