# flake8: noqa: F403, F405
import pytest
from leetcode.p0899_orderly_queue import *

solutions = [
    orderlyQueue,
]

test_cases = [
    (["cba", 1], "acb"),
    (["baaca", 3], "aaabc"),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(*args) == expectation
