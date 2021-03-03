# flake8: noqa: F403, F405
import pytest
from leetcode.p0556_next_greater_element_iii import *

solutions = [
    nextGreaterElement,
]

test_cases = [
    (12, 21),
    (123, 132),
    (213, 231),
    (112, 121),
    (111222333, 111223233),
    (21, -1),
    (321, -1),
    (2 ** 33 - 1, -1),
    (2 ** 35 - 2 ** 9 - 1, -1),
    (123654, 124356),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(args) == expectation
