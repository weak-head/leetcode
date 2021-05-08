# flake8: noqa: F403, F405
import pytest
from leetcode.p0583_delete_operation_for_two_strings import *

solutions = [
    minDistance,
]

test_cases = [
    (["sea", "eat"], 2),
    (["a", "a"], 0),
    (["sea", "seab"], 1),
    (["sea", "seabb"], 2),
    (["sea", "seabbd"], 3),
    (["seak", "seabbd"], 4),
    (["leetcode", "etco"], 4),
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(("args", "expectation"), test_cases)
@pytest.mark.parametrize("solution", solutions)
def test_solution(args, expectation, solution):
    assert solution(*args) == expectation
