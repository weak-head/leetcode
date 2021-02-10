# flake8: noqa: F403, F405
import pytest
from leetcode.p0238_product_of_array_except_self import *

solutions = [
    productExceptSelf,
]

#   ([args], expectation),
test_cases = [
    ([1, 2, 3, 4], [24, 12, 8, 6]),
    ([0, 2, 0, 4], [0, 0, 0, 0]),
    ([1, 2, 1, 2], [4, 2, 4, 2]),
    ([1, 1, 1, 1], [1, 1, 1, 1]),
    ([1, 0, 1, 1], [0, 1, 0, 0]),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
